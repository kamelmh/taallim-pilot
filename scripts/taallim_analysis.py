#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Taallim pilot — automated §4 analysis  (v3, as-built)
======================================================

Ingests the pilot dataset and produces the Results (§4) tables.

OUTCOMES (as built):
  • GRAMMAR  = PRIMARY   outcome  (raw max 55  -> rescaled to 100)   RQ2 / H1–H3
  • VOCABULARY = SECONDARY / exploratory outcome (raw max 60 -> 100)  H4

RQ / section mapping
  §4.1  Descriptives (0–100) + design check (school × group) + assumption checks
        + baseline equivalence (grammar & vocabulary)
  §4.2  RQ2 / H1 — ANCOVA on the immediate GRAMMAR post-test (covariate = pretest)
        + pretest-adjusted means  + school-robustness ANCOVA (controls for school)
  §4.3  RQ2 / H2 — 2×3 mixed ANOVA (Condition × Time): GRAMMAR retention + simple effects
  §4.4  H3 (exploratory) — usage -> GRAMMAR gain: correlations + standardized regression
  §4.5  H4 (exploratory) — VOCABULARY: ANCOVA (post; covariate = pretest) + adjusted means
  §4.6  RQ3 — TEACHER-questionnaire descriptives

Scores are stored RAW and rescaled to a common 0–100 scale before analysis, so
grammar (/55) and vocabulary (/60) are directly comparable and match the manuscript
(“maximum 55/60, rescaled to 100”). Inferential results are scale-invariant; the
rescaling only fixes the reported descriptive scale.

Outputs: one CSV per table in ./outputs/ plus a combined results_tables.md that
drops straight into the manuscript's §4.

--------------------------------------------------------------------------
EXPECTED INPUT  (wide, one row per student). Use --make-sample to generate a
template you can open in Excel and overwrite with real data.

  student_id            e.g. S001
  group                 "Experimental" | "Control"
  school                e.g. "Allal" | "ElBayadh_Public"   (optional but recommended)
  grammar_pre           0–55   ] GRAMMAR raw totals (primary outcome)
  grammar_post          0–55   ]
  grammar_delayed       0–55   ]
  vocab_pre             0–60   ] VOCABULARY raw totals (secondary/H4) — optional
  vocab_post            0–60   ]
  vocab_delayed         0–60   ]
  cards_reviewed        int       ] usage metrics
  review_regularity     0–1       ] (Experimental group only;
  mcq_accuracy          0–1       ]  leave blank for Control)
  maps_completed        int       ]
  time_on_task_min      minutes   ]
  usability             1–5       ] questionnaire subscale means
  engagement            1–5       ] (Experimental group only)
  usefulness            1–5       ]
  bilingual_design      1–5       ]

Run:
  python3 taallim_analysis.py --make-sample          # write sample_pilot_data.csv
  python3 taallim_analysis.py                         # run on the sample
  python3 taallim_analysis.py --input my_pilot.csv    # run on real data
--------------------------------------------------------------------------
"""

import argparse
import os
import sys
import numpy as np
import pandas as pd

try:
    import pingouin as pg
except ImportError:
    sys.exit("pingouin is required:  pip install pingouin")
import statsmodels.formula.api as smf
import statsmodels.api as sm

GROUPS = ["Experimental", "Control"]

# Raw maxima -> rescaled to 100
GRAMMAR_MAX = 55
VOCAB_MAX = 60

# raw column trios
GRAMMAR_RAW = ["grammar_pre", "grammar_post", "grammar_delayed"]
VOCAB_RAW = ["vocab_pre", "vocab_post", "vocab_delayed"]
# rescaled (0–100) column trios created by prepare()
GRAMMAR = ["g_pre", "g_post", "g_delayed"]
VOCAB = ["v_pre", "v_post", "v_delayed"]
TIME_LABELS = ["pretest", "posttest", "delayed"]

USAGE = ["cards_reviewed", "review_regularity", "mcq_accuracy",
         "maps_completed", "time_on_task_min"]
SUBSCALES = ["usability", "engagement", "usefulness", "bilingual_design"]


# --------------------------------------------------------------------------- #
# Sample-data generator (also documents the required schema)
# --------------------------------------------------------------------------- #
def make_sample(path="sample_pilot_data.csv", n_per_group=60, seed=42):
    """Synthetic but realistic data on the RAW scales (grammar /55, vocab /60),
    with both conditions present in BOTH schools (within-school allocation, per §3.3)."""
    rng = np.random.default_rng(seed)
    n_cell = n_per_group // 2                      # per (school × group) cell
    cells = [("Allal", "Experimental"), ("Allal", "Control"),
             ("ElBayadh_Public", "Experimental"), ("ElBayadh_Public", "Control")]
    rows, idx = [], 1
    for school, grp in cells:
        g_off = 2.0 if school == "Allal" else 0.0  # small private-school baseline edge
        v_off = 2.0 if school == "Allal" else 0.0
        for _ in range(n_cell):
            g_pre = float(np.clip(rng.normal(24 + g_off, 6), 0, GRAMMAR_MAX))
            v_pre = float(np.clip(rng.normal(26 + v_off, 6), 0, VOCAB_MAX))
            if grp == "Experimental":
                uq = rng.uniform(0.3, 1.0)                       # latent engagement
                g_post = np.clip(g_pre + rng.normal(9, 3) + 6 * uq, 0, GRAMMAR_MAX)
                g_del = np.clip(g_post - rng.normal(2.5, 2), 0, GRAMMAR_MAX)
                v_post = np.clip(v_pre + rng.normal(8, 3) + 5 * uq, 0, VOCAB_MAX)
                v_del = np.clip(v_post - rng.normal(2.5, 2), 0, VOCAB_MAX)
                extra = dict(
                    cards_reviewed=int(rng.normal(180, 45) * uq + 40),
                    review_regularity=round(float(np.clip(uq + rng.normal(0, .08), 0, 1)), 3),
                    mcq_accuracy=round(float(np.clip(rng.normal(0.72, 0.1) + 0.1 * uq, 0, 1)), 3),
                    maps_completed=int(np.clip(rng.normal(8, 3) * uq + 1, 0, 30)),
                    time_on_task_min=int(np.clip(rng.normal(320, 80) * uq + 60, 0, 900)),
                    usability=round(float(np.clip(rng.normal(4.1, 0.5), 1, 5)), 2),
                    engagement=round(float(np.clip(rng.normal(4.0, 0.6), 1, 5)), 2),
                    usefulness=round(float(np.clip(rng.normal(4.2, 0.5), 1, 5)), 2),
                    bilingual_design=round(float(np.clip(rng.normal(4.4, 0.5), 1, 5)), 2),
                )
            else:
                g_post = np.clip(g_pre + rng.normal(3.0, 3), 0, GRAMMAR_MAX)
                g_del = np.clip(g_post - rng.normal(4.0, 2.5), 0, GRAMMAR_MAX)
                v_post = np.clip(v_pre + rng.normal(3.0, 3), 0, VOCAB_MAX)
                v_del = np.clip(v_post - rng.normal(4.0, 2.5), 0, VOCAB_MAX)
                extra = {k: np.nan for k in USAGE + SUBSCALES}
            row = dict(student_id=f"S{idx:03d}", group=grp, school=school,
                       grammar_pre=round(g_pre, 1), grammar_post=round(float(g_post), 1),
                       grammar_delayed=round(float(g_del), 1),
                       vocab_pre=round(v_pre, 1), vocab_post=round(float(v_post), 1),
                       vocab_delayed=round(float(v_del), 1))
            row.update(extra)
            rows.append(row)
            idx += 1
    cols = (["student_id", "group", "school"] + GRAMMAR_RAW + VOCAB_RAW
            + USAGE + SUBSCALES)
    df = pd.DataFrame(rows)[cols]
    df.to_csv(path, index=False)
    print(f"[+] wrote sample dataset -> {path}  ({len(df)} rows; scales: grammar/55, vocab/60)")
    return path


# --------------------------------------------------------------------------- #
# Load + prepare (rescale raw -> 0–100)
# --------------------------------------------------------------------------- #
def _round(df, n=3):
    return df.round(n)


def load(path):
    df = pd.read_csv(path)
    missing = [c for c in ["student_id", "group"] + GRAMMAR_RAW if c not in df.columns]
    if missing:
        sys.exit(f"Input is missing required columns: {missing}\n"
                 f"(grammar is the primary outcome and must be present)")
    df["group"] = pd.Categorical(df["group"], categories=GROUPS)
    return df


def prepare(df):
    """Create rescaled 0–100 columns for grammar (always) and vocabulary (if present)."""
    for raw, pct in zip(GRAMMAR_RAW, GRAMMAR):
        df[pct] = df[raw] / GRAMMAR_MAX * 100.0
    has_vocab = all(c in df.columns for c in VOCAB_RAW)
    if has_vocab:
        for raw, pct in zip(VOCAB_RAW, VOCAB):
            df[pct] = df[raw] / VOCAB_MAX * 100.0
    return df, has_vocab


# --------------------------------------------------------------------------- #
# §4.1 Design check, descriptives, assumptions, baseline
# --------------------------------------------------------------------------- #
def design_crosstab(df):
    if "school" not in df.columns:
        return None
    ct = pd.crosstab(df["school"], df["group"]).reset_index()
    return ct


def descriptives(df, times):
    label = dict(zip(times, TIME_LABELS))
    d = (df.melt(id_vars=["group"], value_vars=times, var_name="measure", value_name="score")
           .assign(measure=lambda x: x["measure"].map(label))
           .groupby(["measure", "group"], observed=True)["score"]
           .agg(n="count", M="mean", SD="std").reset_index())
    d["measure"] = pd.Categorical(d["measure"], categories=TIME_LABELS, ordered=True)
    return _round(d.sort_values(["measure", "group"]))


def assumptions(df, pre, post):
    out = []
    norm = pg.normality(df, dv=post, group="group")
    for grp, r in norm.iterrows():
        out.append(dict(check=f"Normality ({post}) – {grp}",
                        stat=round(r["W"], 3), p=round(r["pval"], 3),
                        met=bool(r["normal"])))
    lev = pg.homoscedasticity(df, dv=post, group="group")
    out.append(dict(check="Homogeneity of variance (Levene)",
                    stat=round(float(lev["W"].iloc[0]), 3),
                    p=round(float(lev["pval"].iloc[0]), 3),
                    met=bool(lev["equal_var"].iloc[0])))
    m = smf.ols(f"{post} ~ C(group) * {pre}", data=df).fit()
    at = sm.stats.anova_lm(m, typ=2)
    irow = at.loc[f"C(group):{pre}"]
    inter_p = float(irow["PR(>F)"])
    out.append(dict(check="Homogeneity of regression slopes (group × pretest)",
                    stat=round(float(irow["F"]), 3), p=round(inter_p, 3),
                    met=bool(inter_p > .05)))
    return pd.DataFrame(out)


def baseline(df, pre, label):
    a = df.loc[df.group == "Experimental", pre].dropna()
    b = df.loc[df.group == "Control", pre].dropna()
    t = pg.ttest(a, b, paired=False)
    return dict(outcome=label,
                exp_M=round(float(a.mean()), 2), ctrl_M=round(float(b.mean()), 2),
                t=round(float(t["T"].iloc[0]), 3), dof=int(t["dof"].iloc[0]),
                p=round(float(t["p_val"].iloc[0]), 3),
                d=round(float(t["cohen_d"].iloc[0]), 3),
                equivalent=bool(t["p_val"].iloc[0] > .05))


# --------------------------------------------------------------------------- #
# ANCOVA + adjusted means (reused for grammar and vocabulary)
# --------------------------------------------------------------------------- #
def ancova_table(df, pre, post):
    return _round(pg.ancova(data=df, dv=post, covar=pre, between="group"))


def adjusted_means(df, pre, post):
    m = smf.ols(f"{post} ~ C(group) + {pre}", data=df).fit()
    pred = pd.DataFrame({"group": GROUPS, pre: df[pre].mean()})
    sf = m.get_prediction(pred).summary_frame(alpha=0.05)
    return pd.DataFrame({
        "group": GROUPS,
        "adjusted_M": sf["mean"].round(3),
        "SE": sf["mean_se"].round(3),
        "CI_low": sf["mean_ci_lower"].round(3),
        "CI_high": sf["mean_ci_upper"].round(3),
    })


def school_robustness(df, pre, post):
    """Grammar ANCOVA controlling for school — checks the effect isn't a private/public artefact."""
    if "school" not in df.columns or df["school"].nunique() < 2:
        return None
    m = smf.ols(f"{post} ~ C(group) + C(school) + {pre}", data=df).fit()
    at = sm.stats.anova_lm(m, typ=2)

    def peta2(effect):
        ss = float(at.loc[effect, "sum_sq"]); ssr = float(at.loc["Residual", "sum_sq"])
        return ss / (ss + ssr)
    rows = []
    for eff, nice in [("C(group)", "Condition (adj. for school + pretest)"),
                      ("C(school)", "School (private vs public)")]:
        rows.append(dict(effect=nice, F=round(float(at.loc[eff, "F"]), 3),
                         p=round(float(at.loc[eff, "PR(>F)"]), 4),
                         partial_eta2=round(peta2(eff), 3)))
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- #
# §4.3 Mixed ANOVA + retention simple effects (grammar)
# --------------------------------------------------------------------------- #
def mixed_anova_table(df, times):
    label = dict(zip(times, TIME_LABELS))
    long = df.melt(id_vars=["student_id", "group"], value_vars=times,
                   var_name="time", value_name="score")
    long["time"] = pd.Categorical(long["time"].map(label), categories=TIME_LABELS, ordered=True)
    aov = pg.mixed_anova(data=long, dv="score", within="time",
                         between="group", subject="student_id")
    try:
        sp = pg.sphericity(long, dv="score", subject="student_id", within="time")
        ok = bool(getattr(sp, "spher", sp[0])); W = float(getattr(sp, "W", sp[1]))
        pv = float(getattr(sp, "p_val", sp[4]))
        sph_note = (f"Mauchly W={W:.3f}, p={pv:.3f} — sphericity "
                    f"{'met' if ok else 'violated; Greenhouse–Geisser (p-GG-corr) applies'}")
    except Exception as e:
        sph_note = f"(sphericity check skipped: {e})"
    return _round(aov), sph_note


def retention_simple_effects(df, post, delayed):
    out = []
    for grp in GROUPS:
        sub = df[df.group == grp]
        t = pg.ttest(sub[delayed], sub[post], paired=True)
        out.append(dict(group=grp,
                        post_M=round(sub[post].mean(), 2),
                        delayed_M=round(sub[delayed].mean(), 2),
                        change=round(sub[delayed].mean() - sub[post].mean(), 2),
                        t=round(float(t["T"].iloc[0]), 3),
                        p=round(float(t["p_val"].iloc[0]), 3),
                        d=round(float(t["cohen_d"].iloc[0]), 3)))
    a = df.loc[df.group == "Experimental", delayed]
    b = df.loc[df.group == "Control", delayed]
    bt = pg.ttest(a, b, paired=False)
    out.append(dict(group="Exp vs Control @ delayed", post_M=np.nan, delayed_M=np.nan,
                    change=round(a.mean() - b.mean(), 2),
                    t=round(float(bt["T"].iloc[0]), 3),
                    p=round(float(bt["p_val"].iloc[0]), 3),
                    d=round(float(bt["cohen_d"].iloc[0]), 3)))
    return pd.DataFrame(out)


# --------------------------------------------------------------------------- #
# §4.4 Usage -> grammar gain (experimental group)
# --------------------------------------------------------------------------- #
def usage_analysis(df, pre, post):
    exp = df[df.group == "Experimental"].copy()
    preds = [c for c in USAGE if c in exp.columns and exp[c].notna().any()]
    if not preds:
        return None, None
    exp = exp.dropna(subset=preds + [pre, post])
    exp["gain"] = exp[post] - exp[pre]
    corr_rows = []
    for p in preds:
        c = pg.corr(exp[p], exp["gain"])
        corr_rows.append(dict(predictor=p, r=round(float(c["r"].iloc[0]), 3),
                              p=round(float(c["p_val"].iloc[0]), 3),
                              n=int(c["n"].iloc[0])))
    corr = pd.DataFrame(corr_rows)
    z = exp[preds + ["gain"]].apply(lambda s: (s - s.mean()) / s.std(ddof=1))
    reg = pg.linear_regression(z[preds], z["gain"]).rename(
        columns={"names": "predictor", "coef": "beta"})
    keep = [c for c in ["predictor", "beta", "se", "T", "p_val", "r2", "adj_r2"] if c in reg.columns]
    return corr, _round(reg[keep])


# --------------------------------------------------------------------------- #
# §4.6 Questionnaire
# --------------------------------------------------------------------------- #
def questionnaire(df):
    exp = df[df.group == "Experimental"]
    subs = [c for c in SUBSCALES if c in exp.columns and exp[c].notna().any()]
    if not subs:
        return None
    rows = []
    for s in subs:
        v = exp[s].dropna()
        rows.append(dict(subscale=s, n=int(v.count()), M=round(v.mean(), 2),
                         SD=round(v.std(ddof=1), 2),
                         pct_agree=round(float((v >= 4).mean() * 100), 1)))
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #
def run(df, outdir):
    os.makedirs(outdir, exist_ok=True)
    df, has_vocab = prepare(df)
    md = ["# §4 Results — auto-generated tables",
          "\n*Scores rescaled to 0–100 (grammar raw /55, vocabulary raw /60). "
          "Grammar = primary outcome; vocabulary = secondary/exploratory (H4).*\n"]

    def emit(title, obj, fname=None, note=None):
        print("\n" + "=" * 78 + f"\n{title}\n" + "=" * 78)
        md.append(f"\n## {title}\n")
        if isinstance(obj, pd.DataFrame):
            print(obj.to_string(index=False))
            md.append("\n" + obj.to_markdown(index=False) + "\n")
            if fname:
                obj.to_csv(os.path.join(outdir, fname), index=False)
        else:
            print(obj); md.append(f"\n{obj}\n")
        if note:
            print("  " + note); md.append(f"\n_{note}_\n")

    # ---- §4.1 ------------------------------------------------------------- #
    ct = design_crosstab(df)
    if ct is not None:
        emit("§4.1  Design — participants by school × condition", ct, "t0_design.csv")
    emit("§4.1  Descriptive statistics — GRAMMAR (0–100)", descriptives(df, GRAMMAR), "t1_grammar_desc.csv")
    if has_vocab:
        emit("§4.1  Descriptive statistics — VOCABULARY (0–100)", descriptives(df, VOCAB), "t1b_vocab_desc.csv")
    emit("§4.1  Assumption checks (grammar post-test)", assumptions(df, "g_pre", "g_post"), "t2_assumptions.csv")
    base_rows = [baseline(df, "g_pre", "Grammar")]
    if has_vocab:
        base_rows.append(baseline(df, "v_pre", "Vocabulary"))
    emit("§4.1  Baseline equivalence (pretest t-tests, 0–100)", pd.DataFrame(base_rows), "t2b_baseline.csv")

    # ---- §4.2  RQ2 / H1 — grammar ANCOVA ---------------------------------- #
    emit("§4.2  RQ2/H1 — GRAMMAR ANCOVA (post-test; covariate = pretest)",
         ancova_table(df, "g_pre", "g_post"), "t3_grammar_ancova.csv")
    emit("§4.2  RQ2/H1 — Pretest-adjusted grammar means",
         adjusted_means(df, "g_pre", "g_post"), "t4_grammar_adjusted.csv")
    sr = school_robustness(df, "g_pre", "g_post")
    if sr is not None:
        emit("§4.2  Robustness — grammar effect controlling for school (private vs public)",
             sr, "t4b_school_robustness.csv",
             note="Condition effect should remain significant after adjusting for school, "
                  "confirming the result is not a private/public artefact (per §3.3).")

    # ---- §4.3  RQ2 / H2 — grammar retention ------------------------------- #
    aov, sph = mixed_anova_table(df, GRAMMAR)
    emit("§4.3  RQ2/H2 — GRAMMAR retention: Mixed ANOVA (Condition × Time)", aov, "t5_grammar_mixed.csv", note=sph)
    emit("§4.3  RQ2/H2 — GRAMMAR retention: simple effects",
         retention_simple_effects(df, "g_post", "g_delayed"), "t6_grammar_retention.csv")

    # ---- §4.4  H3 — usage -> grammar gain --------------------------------- #
    corr, reg = usage_analysis(df, "g_pre", "g_post")
    if corr is not None:
        emit("§4.4  H3 (exploratory) — Usage × grammar-gain correlations", corr, "t7_usage_corr.csv")
        emit("§4.4  H3 (exploratory) — Usage regression (standardized betas)", reg, "t8_usage_reg.csv")
    else:
        emit("§4.4  H3 (exploratory) — Usage analysis", "skipped (no usage columns with data)")

    # ---- §4.5  H4 — vocabulary (secondary) -------------------------------- #
    if has_vocab:
        emit("§4.5  H4 (exploratory) — VOCABULARY ANCOVA (post-test; covariate = pretest)",
             ancova_table(df, "v_pre", "v_post"), "t9_vocab_ancova.csv")
        emit("§4.5  H4 (exploratory) — Pretest-adjusted vocabulary means",
             adjusted_means(df, "v_pre", "v_post"), "t10_vocab_adjusted.csv")
    else:
        emit("§4.5  H4 (exploratory) — Vocabulary", "skipped (no vocabulary columns in input)")

    # ---- §4.6  RQ3 — questionnaire ---------------------------------------- #
    q = questionnaire(df)
    if q is not None:
        emit("§4.6  RQ3 — Teacher questionnaire subscales", q, "t11_questionnaire.csv")
    else:
        emit("§4.6  RQ3 — Teacher questionnaire", "skipped (no subscale columns with data)")

    with open(os.path.join(outdir, "results_tables.md"), "w") as f:
        f.write("\n".join(md))
    print("\n" + "-" * 78)
    print(f"[+] CSV tables + results_tables.md written to  {outdir}/")


def main():
    ap = argparse.ArgumentParser(description="Taallim pilot §4 analysis (v3)")
    ap.add_argument("--input", help="path to pilot CSV (wide format)")
    ap.add_argument("--outdir", default="outputs")
    ap.add_argument("--make-sample", action="store_true",
                    help="write sample_pilot_data.csv and exit")
    args = ap.parse_args()

    if args.make_sample:
        make_sample()
        return
    path = args.input
    if not path:
        path = make_sample()
        print("[i] no --input given; running on the generated sample.\n")
    df = load(path)
    run(df, args.outdir)


if __name__ == "__main__":
    main()
