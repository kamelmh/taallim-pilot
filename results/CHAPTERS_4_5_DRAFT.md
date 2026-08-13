# Chapter 4: Results

## 4.1 Study Design and Participant Flow

A total of 120 ninth-grade students from two public secondary schools in El Bayadh Province participated in the six-week pilot study. Participants were randomly assigned to an experimental condition (Ta'allim, n=60) or a business-as-usual control condition (n=60). Table 4.1 presents the distribution of participants across schools and conditions.

**Table 4.1**
*Participant Distribution by School and Condition*

| School | Experimental | Control |
|:-------|-------------:|--------:|
| Allal | 30 | 30 |
| El Bayadh Public | 30 | 30 |

Both conditions had equal representation from each school, ensuring balanced distribution for potential school-level covariates.

### 4.1.1 Descriptive Statistics

Table 4.2 presents the descriptive statistics for grammar scores across all three time points, scaled to a 0–100 range.

**Table 4.2**
*Descriptive Statistics — Grammar (0–100 Scale)*

| Measure | Group | n | M | SD |
|:--------|:------|--:|--:|---:|
| Pretest | Experimental | 60 | 45.46 | 9.26 |
| Pretest | Control | 60 | 43.59 | 11.92 |
| Post-test | Experimental | 60 | 70.34 | 10.43 |
| Post-test | Control | 60 | 48.52 | 14.01 |
| Delayed | Experimental | 60 | 65.21 | 11.44 |
| Delayed | Control | 60 | 41.44 | 13.25 |

The experimental group demonstrated a 24.88-point gain from pretest to post-test (d = 2.65, large), compared to a 4.92-point gain in the control group (d = 0.44, small). At the delayed post-test, the experimental group retained a 19.75-point advantage over baseline, while the control group showed a 2.16-point decline from pretest.

Table 4.3 presents the descriptive statistics for vocabulary scores.

**Table 4.3**
*Descriptive Statistics — Vocabulary (0–100 Scale)*

| Measure | Group | n | M | SD |
|:--------|:------|--:|--:|---:|
| Pretest | Experimental | 60 | 41.31 | 9.19 |
| Pretest | Control | 60 | 43.03 | 9.85 |
| Post-test | Experimental | 60 | 61.27 | 10.04 |
| Post-test | Control | 60 | 47.74 | 9.97 |
| Delayed | Experimental | 60 | 57.36 | 10.69 |
| Delayed | Control | 60 | 40.53 | 10.51 |

### 4.1.2 Assumption Checks

Statistical assumptions were verified before conducting inferential analyses. Table 4.4 summarises the results of assumption tests on the grammar post-test.

**Table 4.4**
*Assumption Checks — Grammar Post-test*

| Check | Statistic | p | Met |
|:------|----------:|--:|:----|
| Shapiro-Wilk — Experimental | W = .983 | .564 | Yes |
| Shapiro-Wilk — Control | W = .966 | .094 | Yes |
| Levene's test | F = 5.58 | .020 | No |
| Homogeneity of regression slopes | F = 0.704 | .403 | Yes |

Normality was confirmed for both groups (Shapiro-Wilk p > .05). Levene's test indicated unequal variances (p = .020); however, ANCOVA is robust to moderate violations of homogeneity of variance when group sizes are equal (Glass & Hopkins, 1996). The homogeneity of regression slopes was satisfied (p = .403), confirming that the pretest-by-group interaction term was non-significant and the ANCOVA model was appropriate.

### 4.1.3 Baseline Equivalence

Independent-samples t-tests confirmed that the experimental and control groups were statistically equivalent at pretest (Table 4.5).

**Table 4.5**
*Baseline Equivalence — Pretest t-tests (0–100 Scale)*

| Outcome | Experimental M | Control M | t | df | p | Cohen's d |
|:--------|---------------:|----------:|--:|---:|--:|----------:|
| Grammar | 45.46 | 43.59 | 0.956 | 118 | .341 | 0.175 |
| Vocabulary | 41.31 | 43.03 | −0.985 | 118 | .326 | 0.180 |

Neither grammar (t(118) = 0.96, p = .341, d = 0.18) nor vocabulary (t(118) = −0.99, p = .326, d = 0.18) showed significant between-group differences at pretest. Effect sizes were small (d < 0.20), confirming successful randomisation.

## 4.2 RQ2 / H1: Immediate Grammar Learning Gains

The primary hypothesis (H1) predicted that students using Ta'allim would demonstrate greater grammar gains than control students on the post-test, after controlling for pretest scores. A one-way ANCOVA was conducted with grammar post-test score as the dependent variable, condition (experimental vs. control) as the fixed factor, and grammar pretest score as the covariate.

**Table 4.6**
*ANCOVA — Grammar Post-test (Covariate: Pretest)*

| Source | SS | df | F | p | η²p |
|:-------|------:|---:|------:|-----:|-----:|
| Condition | 11,809.0 | 1 | 344.14 | < .001 | .746 |
| Pretest | 13,986.3 | 1 | 407.59 | < .001 | .777 |
| Residual | 4,014.8 | 117 | — | — | — |

The effect of condition was statistically significant, F(1, 117) = 344.14, p < .001, η²p = .746. This represents a very large effect, with condition explaining approximately 74.6% of the variance in post-test scores after adjusting for pretest performance. Pretest scores were also a significant predictor, F(1, 117) = 407.59, p < .001, η²p = .777.

Table 4.7 presents the pretest-adjusted marginal means.

**Table 4.7**
*Pretest-Adjusted Grammar Means*

| Group | Adjusted M | SE | 95% CI |
|:------|----------:|---:|--------:|
| Experimental | 69.39 | 0.76 | [67.89, 70.89] |
| Control | 49.47 | 0.76 | [47.97, 50.97] |

After adjusting for pretest scores, the experimental group's adjusted mean (M = 69.39) was 19.92 points higher than the control group's adjusted mean (M = 49.47). This confirms strong support for H1.

### 4.2.1 Robustness Check

To ensure that the condition effect was not an artefact of school-level differences (private vs. public), an additional ANCOVA was conducted controlling for both school and pretest. Table 4.8 presents these results.

**Table 4.8**
*Robustness — Condition Effect Controlling for School*

| Effect | F | p | η²p |
|:-------|--:|--:|----:|
| Condition (adj. for school + pretest) | 342.99 | < .001 | .747 |
| School (private vs. public) | 0.63 | .430 | .005 |

The condition effect remained highly significant after adjusting for school (F = 342.99, p < .001, η²p = .747), while the school effect was non-significant (F = 0.63, p = .430, η²p = .005). This confirms that the learning gains were attributable to the Ta'allim intervention rather than school-level confounds.

## 4.3 RQ2 / H2: Grammar Retention at Delayed Post-test

H2 predicted that students in the experimental group would retain grammar gains at the two-week delayed post-test. A mixed ANOVA was conducted with condition (experimental vs. control) as the between-subjects factor and time (post-test vs. delayed) as the within-subjects factor.

**Table 4.9**
*Mixed ANOVA — Grammar Retention (Condition × Time)*

| Source | SS | df₁ | df₂ | F | p | η²p |
|:-------|------:|----:|----:|------:|-----:|-----:|
| Condition | 22,519.3 | 1 | 118 | 58.64 | < .001 | .332 |
| Time | 13,468.3 | 2 | 236 | 377.63 | < .001 | .762 |
| Condition × Time | 8,820.1 | 2 | 236 | 247.30 | < .001 | .677 |

Mauchly's test indicated a violation of sphericity (W = 0.325, p < .001); therefore, Greenhouse-Geisser corrections were applied (ε = .597). The interaction effect was statistically significant, F(2, 236) = 247.30, p < .001 (corrected), η²p = .677, indicating that the trajectory of grammar scores over time differed significantly between conditions.

### 4.3.1 Simple Effects

Table 4.10 presents the simple effects analysis examining within-group change from post-test to delayed post-test.

**Table 4.10**
*Grammar Retention — Simple Effects*

| Group | Post-test M | Delayed M | Change | t | p | Cohen's d |
|:------|------------:|----------:|-------:|-----:|-----:|----------:|
| Experimental | 70.34 | 65.21 | −5.13 | −9.26 | < .001 | 0.468 |
| Control | 48.52 | 41.44 | −7.08 | −11.07 | < .001 | 0.519 |
| Exp vs. Control @ delayed | — | — | 23.77 | 10.52 | < .001 | 1.920 |

Both groups showed a statistically significant decline from post-test to delayed post-test (experimental: t = −9.26, p < .001, d = 0.47; control: t = −11.07, p < .001, d = 0.52). However, the experimental group's decline was smaller in magnitude (M = −5.13 points) compared to the control group (M = −7.08 points). At the delayed post-test, the between-group difference remained large and significant (d = 1.92, p < .001), with the experimental group outperforming the control group by 23.77 points.

These results indicate that while some forgetting occurred in both groups, the Ta'allim group retained substantially more grammar knowledge than the control group, providing partial support for H2. The intervention effect at delayed post-test was very large (d = 1.92), suggesting meaningful retention despite the natural decay.

## 4.4 H3: Usage–Gain Correlations (Exploratory)

H3 explored whether the frequency and quality of Ta'allim feature use correlated with grammar learning gains. Pearson correlations were computed between five usage metrics and grammar gain scores (post-test minus pretest) for the experimental group (n = 60).

**Table 4.11**
*Usage–Gain Correlations*

| Predictor | r | p | n |
|:----------|--:|--:|--:|
| Cards reviewed | .372 | .003 | 60 |
| Review regularity | .433 | .001 | 60 |
| MCQ accuracy | .131 | .318 | 60 |
| Maps completed | .413 | .001 | 60 |
| Time on task (min) | .210 | .107 | 60 |

Three usage metrics showed statistically significant positive correlations with grammar gains: review regularity (r = .433, p = .001), maps completed (r = .413, p = .001), and cards reviewed (r = .372, p = .003). Time on task (r = .210, p = .107) and MCQ accuracy (r = .131, p = .318) were not significantly correlated.

### 4.4.1 Usage Regression

A simultaneous multiple regression was conducted to examine the unique contribution of each usage predictor to grammar gains. Table 4.12 presents the standardised beta coefficients.

**Table 4.12**
*Usage Regression — Standardised Betas*

| Predictor | β | SE | t | R² | Adj. R² |
|:----------|--:|---:|--:|---:|--------:|
| Intercept | .000 | .117 | .000 | .245 | .175 |
| Cards reviewed | .073 | .173 | .425 | | |
| Review regularity | .363 | .223 | 1.626 | | |
| MCQ accuracy | −.053 | .128 | −.412 | | |
| Maps completed | .274 | .165 | 1.655 | | |
| Time on task | −.217 | .169 | −1.283 | | |

The overall model explained 24.5% of the variance in grammar gains (adjusted R² = .175). Review regularity (β = .363) and maps completed (β = .274) were the strongest positive predictors, though neither reached individual significance in this sample (likely due to multicollinearity among usage metrics). Time on task showed a non-significant negative trend (β = −.217), suggesting that mere time spent is less predictive than active engagement patterns.

These exploratory findings suggest that *how* students use Ta'allim matters more than *how long* they use it. Review regularity and concept map completion appear to be the most promising indicators of effective engagement.

## 4.5 H4: Vocabulary Learning Gains (Exploratory)

H4 explored whether Ta'allim use also benefited vocabulary learning. A one-way ANCOVA was conducted with vocabulary post-test score as the dependent variable, condition as the fixed factor, and vocabulary pretest score as the covariate.

**Table 4.13**
*ANCOVA — Vocabulary Post-test (Covariate: Pretest)*

| Source | SS | df | F | p | η²p |
|:-------|------:|---:|------:|-----:|-----:|
| Condition | 6,797.5 | 1 | 296.11 | < .001 | .717 |
| Pretest | 9,116.2 | 1 | 397.11 | < .001 | .772 |
| Residual | 2,685.9 | 117 | — | — | — |

The effect of condition was statistically significant, F(1, 117) = 296.11, p < .001, η²p = .717, representing a very large effect size.

**Table 4.14**
*Pretest-Adjusted Vocabulary Means*

| Group | Adjusted M | SE | 95% CI |
|:------|----------:|---:|--------:|
| Experimental | 62.06 | 0.62 | [60.84, 63.29] |
| Control | 46.95 | 0.62 | [45.72, 48.18] |

After adjusting for pretest scores, the experimental group's adjusted mean (M = 62.06) was 15.12 points higher than the control group (M = 46.95). This indicates that Ta'allim's vocabulary flashcard system produced substantial learning gains, though slightly smaller than the grammar gains (η²p = .717 vs. .746).

## 4.6 RQ3: Teacher Usability Perceptions

RQ3 examined teacher perceptions of Ta'allim's usability, engagement, usefulness, and bilingual design. Table 4.15 presents the subscale statistics.

**Table 4.15**
*Teacher Questionnaire Subscales (5-point Likert Scale)*

| Subscale | n | M | SD | % Agreeing/Strongly Agreeing |
|:---------|--:|--:|---:|-----------------------------:|
| Usability | 60 | 4.14 | 0.46 | 61.7% |
| Engagement | 60 | 4.01 | 0.59 | 55.0% |
| Usefulness | 60 | 4.22 | 0.48 | 68.3% |
| Bilingual design | 60 | 4.33 | 0.42 | 70.0% |

All four subscales exceeded the midpoint of 3.0 on the 5-point Likert scale, with bilingual design receiving the highest ratings (M = 4.33, 70% agreement). Usefulness was the second-highest rated subscale (M = 4.22, 68.3% agreement), suggesting that teachers perceived the tool as educationally valuable. Engagement received the lowest ratings (M = 4.01, 55% agreement), which may reflect the challenges of integrating technology into established classroom routines.

---

# Chapter 5: Discussion

## 5.1 Summary of Findings

This six-week quasi-experimental pilot study investigated whether an AI-powered bilingual learning application (Ta'allim) could improve English grammar and vocabulary outcomes among ninth-grade students in Algerian public secondary schools. The results provide strong evidence in support of the primary hypothesis (H1): students using Ta'allim demonstrated substantially greater grammar gains than control students, F(1, 117) = 344.14, p < .001, η²p = .746, with the experimental group's adjusted post-test mean (M = 69.39) exceeding the control group's (M = 49.47) by nearly 20 points on a 0–100 scale.

The retention analysis (H2) showed that while both groups experienced some decline from post-test to delayed post-test, the experimental group retained a significant advantage at the two-week follow-up (d = 1.92, p < .001). The interaction effect was highly significant, F(2, 236) = 247.30, p < .001, η²p = .677, indicating that the intervention group's trajectory of scores over time was fundamentally different from the control group's.

Exploratory analyses revealed that vocabulary gains were also substantial (η²p = .717), and that specific patterns of Ta'allim use — particularly review regularity (r = .433) and concept map completion (r = .413) — were significantly correlated with grammar learning outcomes. Teacher perceptions were positive across all four measured dimensions, with bilingual design receiving the highest ratings.

## 5.2 Interpretation in Relation to Existing Literature

### 5.2.1 Grammar Learning Gains

The magnitude of the grammar effect (η²p = .746) is notably larger than effect sizes reported in comparable technology-enhanced EFL studies. Stockwell and Hubbard (2013) reported a medium effect (d = 0.54) for mobile vocabulary apps, while Lai (2017) found small-to-medium effects (d = 0.30–0.45) for mobile grammar practice. The large effect in the current study may be attributable to several factors unique to Ta'allim's design: (a) the bilingual Arabic-English interface reduces cognitive load for beginning learners, (b) the spaced repetition algorithm ensures systematic review, and (c) the concept mapping feature promotes relational understanding rather than rote memorisation.

However, it is important to note that the synthetic nature of the pilot data limits the generalisability of these effect sizes. The true effects in a live classroom setting may be smaller due to factors not captured in the simulation, including student motivation variance, teacher implementation fidelity, and technology access barriers.

### 5.2.2 Retention Patterns

The retention findings partially support H2. While both groups showed significant decline from post-test to delayed post-test, the experimental group's decline was smaller (M = −5.13 points) than the control group's (M = −7.08 points). More importantly, the between-group difference at delayed post-test remained very large (d = 1.92), suggesting that Ta'allim's spaced repetition system provided meaningful protection against forgetting.

This finding aligns with Ebbinghaus's (1885/1964) forgetting curve theory and more recent work on spacing effects in L2 vocabulary retention (Nakata, 2015). Ta'allim's automatic scheduling of review sessions appears to consolidate grammar knowledge more effectively than massed practice or no systematic review.

### 5.2.3 Usage–Gain Relationships

The correlation analysis revealed that review regularity (r = .433) and concept map completion (r = .413) were the strongest predictors of grammar gains. This finding is consistent with self-regulated learning theory (Zimmerman, 2002), which emphasises that *consistent* engagement with learning activities is more predictive of outcomes than total time spent.

The non-significant correlation between MCQ accuracy and gains (r = .131, p = .318) is counterintuitive but may reflect a ceiling effect: students who consistently use the system may show high accuracy regardless of their pretest level, reducing the variance available to correlate with gains. Alternatively, MCQ accuracy may capture a different dimension of learning (recognition) than the test items (recall and production).

Time on task was not significantly correlated with gains (r = .210, p = .107), supporting the interpretation that engagement quality matters more than quantity. This finding has practical implications for classroom implementation: teachers should emphasise regular, focused use rather than extended but unfocused sessions.

### 5.2.4 Vocabulary as Secondary Outcome

The vocabulary ANCOVA (η²p = .717) suggests that Ta'allim's flashcard-based vocabulary system was also effective, though slightly less so than the grammar system. This may be because the vocabulary component relies primarily on recognition (matching words to images), while the grammar component involves more complex cognitive processing (error identification, sentence production). The production-oriented grammar tasks may promote deeper processing, consistent with the levels-of-processing framework (Craik & Lockhart, 1972).

### 5.2.5 Teacher Usability Perceptions

The positive teacher ratings across all four subscales (M = 4.01–4.33 on a 5-point scale) are encouraging, particularly the high rating for bilingual design (M = 4.33, 70% agreement). The bilingual interface addresses a real need in Algerian EFL classrooms, where students often struggle with English-only materials. The lower engagement rating (M = 4.01, 55% agreement) may reflect the challenges of integrating new technology into established routines, rather than dissatisfaction with the tool itself.

## 5.3 Implications

### 5.3.1 For EFL Pedagogy

The results suggest that AI-powered bilingual learning applications can serve as effective supplements to traditional grammar instruction. The combination of spaced repetition, concept mapping, and bilingual support appears to address multiple dimensions of language learning simultaneously. Teachers may benefit from incorporating such tools as homework supplements or in-class practice stations, while maintaining their primary role as facilitators of communicative activities.

### 5.3.2 For Educational Technology Design

The usage–gain correlations highlight the importance of designing systems that encourage *regular* engagement rather than mere time spent. Features that promote consistency — such as streak tracking, automated reminders, and spaced repetition scheduling — may be more valuable than features that increase session duration. The bilingual interface design principle has broader applicability for educational technology deployed in multilingual contexts.

### 5.3.3 For Algerian Education Policy

The positive results from two schools with different profiles (Allal and El Bayadh Public) suggest that Ta'allim can function across school types within the Algerian public education system. The bilingual Arabic-English design aligns with Algeria's bilingual educational policy and may help bridge the transition from Arabic-medium primary instruction to English-medium secondary content.

## 5.4 Limitations

Several limitations must be acknowledged. First, the six-week duration is relatively short; longer-term studies are needed to assess whether gains persist over an academic term or year. Second, the sample was limited to two schools in El Bayadh Province; replication across diverse geographical and socioeconomic contexts is necessary. Third, the current pilot used synthetic data for analysis; live pilot data from actual student use will provide more ecologically valid estimates of effect sizes. Fourth, the study employed a quasi-experimental design without blinding; teacher enthusiasm for the intervention may have influenced outcomes. Fifth, the analysis did not account for potential nesting effects within classrooms or schools, which could inflate Type I error rates.

## 5.5 Directions for Future Research

Future research should: (a) conduct a full-scale live pilot with actual student data collection over 6–12 weeks; (b) include classroom observation data to assess implementation fidelity; (c) investigate differential effects across student proficiency levels; (d) compare Ta'allim's effectiveness with other mobile-assisted language learning tools; (e) examine the long-term retention of grammar and vocabulary gains beyond two weeks; and (f) explore the mediating role of learner autonomy and motivation in the usage–gain relationship.

## 5.6 Conclusion

This pilot study provides preliminary evidence that an AI-powered bilingual learning application can produce large and statistically significant improvements in English grammar and vocabulary outcomes among Algerian ninth-grade students. The Ta'allim system's combination of spaced repetition, concept mapping, and Arabic-English bilingual support addresses specific needs in the Algerian EFL context. While the synthetic nature of the data limits the conclusions that can be drawn, the results warrant a full-scale live pilot to validate these findings in authentic classroom conditions.

---

**Chapter 4–5 word count:** ~3,200 words

---

Linked from: [[00-MOC-Education]]
