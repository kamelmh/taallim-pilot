# §4 Results — auto-generated tables

*Scores rescaled to 0–100 (grammar raw /55, vocabulary raw /60). Grammar = primary outcome; vocabulary = secondary/exploratory (H4).*


## §4.1  Design — participants by school × condition


| school          |   Experimental |   Control |
|:----------------|---------------:|----------:|
| Allal           |             30 |        30 |
| ElBayadh_Public |             30 |        30 |


## §4.1  Descriptive statistics — GRAMMAR (0–100)


| measure   | group        |   n |      M |     SD |
|:----------|:-------------|----:|-------:|-------:|
| pretest   | Experimental |  60 | 45.458 |  9.258 |
| pretest   | Control      |  60 | 43.594 | 11.92  |
| posttest  | Experimental |  60 | 70.336 | 10.433 |
| posttest  | Control      |  60 | 48.518 | 14.009 |
| delayed   | Experimental |  60 | 65.209 | 11.442 |
| delayed   | Control      |  60 | 41.436 | 13.251 |


## §4.1  Descriptive statistics — VOCABULARY (0–100)


| measure   | group        |   n |      M |     SD |
|:----------|:-------------|----:|-------:|-------:|
| pretest   | Experimental |  60 | 41.311 |  9.191 |
| pretest   | Control      |  60 | 43.025 |  9.853 |
| posttest  | Experimental |  60 | 61.272 | 10.035 |
| posttest  | Control      |  60 | 47.739 |  9.966 |
| delayed   | Experimental |  60 | 57.361 | 10.691 |
| delayed   | Control      |  60 | 40.533 | 10.505 |


## §4.1  Assumption checks (grammar post-test)


| check                                              |   stat |     p | met   |
|:---------------------------------------------------|-------:|------:|:------|
| Normality (g_post) – Experimental                  |  0.983 | 0.564 | True  |
| Normality (g_post) – Control                       |  0.966 | 0.094 | True  |
| Homogeneity of variance (Levene)                   |  5.58  | 0.02  | False |
| Homogeneity of regression slopes (group × pretest) |  0.704 | 0.403 | True  |


## §4.1  Baseline equivalence (pretest t-tests, 0–100)


| outcome    |   exp_M |   ctrl_M |      t |   dof |     p |     d | equivalent   |
|:-----------|--------:|---------:|-------:|------:|------:|------:|:-------------|
| Grammar    |   45.46 |    43.59 |  0.956 |   118 | 0.341 | 0.175 | True         |
| Vocabulary |   41.31 |    43.03 | -0.985 |   118 | 0.326 | 0.18  | True         |


## §4.2  RQ2/H1 — GRAMMAR ANCOVA (post-test; covariate = pretest)


| Source   |      SS |   DF |       F |   p_unc |     np2 |
|:---------|--------:|-----:|--------:|--------:|--------:|
| group    | 11809   |    1 | 344.141 |       0 |   0.746 |
| g_pre    | 13986.3 |    1 | 407.591 |       0 |   0.777 |
| Residual |  4014.8 |  117 | nan     |     nan | nan     |


## §4.2  RQ2/H1 — Pretest-adjusted grammar means


| group        |   adjusted_M |    SE |   CI_low |   CI_high |
|:-------------|-------------:|------:|---------:|----------:|
| Experimental |       69.386 | 0.758 |   67.885 |    70.886 |
| Control      |       49.469 | 0.758 |   47.968 |    50.969 |


## §4.2  Robustness — grammar effect controlling for school (private vs public)


| effect                                |       F |      p |   partial_eta2 |
|:--------------------------------------|--------:|-------:|---------------:|
| Condition (adj. for school + pretest) | 342.99  | 0      |          0.747 |
| School (private vs public)            |   0.628 | 0.4299 |          0.005 |


_Condition effect should remain significant after adjusting for school, confirming the result is not a private/public artefact (per §3.3)._


## §4.3  RQ2/H2 — GRAMMAR retention: Mixed ANOVA (Condition × Time)


| Source      |       SS |   DF1 |   DF2 |       MS |       F |   p_unc |   p_GG_corr |   np2 |     eps |   sphericity |   W_spher |   p_spher |
|:------------|---------:|------:|------:|---------:|--------:|--------:|------------:|------:|--------:|-------------:|----------:|----------:|
| group       | 22519.3  |     1 |   118 | 22519.3  |  58.64  |       0 |         nan | 0.332 | nan     |          nan |   nan     |       nan |
| time        | 13468.3  |     2 |   236 |  6734.15 | 377.628 |       0 |           0 | 0.762 |   0.597 |            0 |     0.325 |         0 |
| Interaction |  8820.12 |     2 |   236 |  4410.06 | 247.301 |       0 |         nan | 0.677 | nan     |          nan |   nan     |       nan |


_Mauchly W=0.325, p=0.000 — sphericity violated; Greenhouse–Geisser (p-GG-corr) applies_


## §4.3  RQ2/H2 — GRAMMAR retention: simple effects


| group                    |   post_M |   delayed_M |   change |       t |   p |     d |
|:-------------------------|---------:|------------:|---------:|--------:|----:|------:|
| Experimental             |    70.34 |       65.21 |    -5.13 |  -9.26  |   0 | 0.468 |
| Control                  |    48.52 |       41.44 |    -7.08 | -11.068 |   0 | 0.519 |
| Exp vs Control @ delayed |   nan    |      nan    |    23.77 |  10.518 |   0 | 1.92  |


## §4.4  H3 (exploratory) — Usage × grammar-gain correlations


| predictor         |     r |     p |   n |
|:------------------|------:|------:|----:|
| cards_reviewed    | 0.372 | 0.003 |  60 |
| review_regularity | 0.433 | 0.001 |  60 |
| mcq_accuracy      | 0.131 | 0.318 |  60 |
| maps_completed    | 0.413 | 0.001 |  60 |
| time_on_task_min  | 0.21  | 0.107 |  60 |


## §4.4  H3 (exploratory) — Usage regression (standardized betas)


| predictor         |   beta |    se |      T |    r2 |   adj_r2 |
|:------------------|-------:|------:|-------:|------:|---------:|
| Intercept         |  0     | 0.117 |  0     | 0.245 |    0.175 |
| cards_reviewed    |  0.073 | 0.173 |  0.425 | 0.245 |    0.175 |
| review_regularity |  0.363 | 0.223 |  1.626 | 0.245 |    0.175 |
| mcq_accuracy      | -0.053 | 0.128 | -0.412 | 0.245 |    0.175 |
| maps_completed    |  0.274 | 0.165 |  1.655 | 0.245 |    0.175 |
| time_on_task_min  | -0.217 | 0.169 | -1.283 | 0.245 |    0.175 |


## §4.5  H4 (exploratory) — VOCABULARY ANCOVA (post-test; covariate = pretest)


| Source   |      SS |   DF |       F |   p_unc |     np2 |
|:---------|--------:|-----:|--------:|--------:|--------:|
| group    | 6797.49 |    1 | 296.107 |       0 |   0.717 |
| v_pre    | 9116.2  |    1 | 397.114 |       0 |   0.772 |
| Residual | 2685.87 |  117 | nan     |     nan | nan     |


## §4.5  H4 (exploratory) — Pretest-adjusted vocabulary means


| group        |   adjusted_M |   SE |   CI_low |   CI_high |
|:-------------|-------------:|-----:|---------:|----------:|
| Experimental |       62.063 | 0.62 |   60.835 |    63.29  |
| Control      |       46.948 | 0.62 |   45.721 |    48.176 |


## §4.6  RQ3 — Teacher questionnaire subscales


| subscale         |   n |    M |   SD |   pct_agree |
|:-----------------|----:|-----:|-----:|------------:|
| usability        |  60 | 4.14 | 0.46 |        61.7 |
| engagement       |  60 | 4.01 | 0.59 |        55   |
| usefulness       |  60 | 4.22 | 0.48 |        68.3 |
| bilingual_design |  60 | 4.33 | 0.42 |        70   |
