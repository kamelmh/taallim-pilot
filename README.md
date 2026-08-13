# Ta'allim Pilot

AI-powered English language exercise generation and assessment system for Algerian schools.

## What It Does

- **Generates exercises** — Fill-in-blank, MCQ, sentence building, error correction
- **4 proficiency levels** — A1, A2, B1, B2 (aligned to Algerian curriculum 1AM-4AM)
- **6 parallel test forms** — Grammar A/B/C + Vocabulary A/B/C (60 items each)
- **Auto-analysis** — ANCOVA, mixed ANOVA, correlations for pilot data
- **School outreach** — FR/AR email templates for director/teacher recruitment

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Generate exercises (CLI)
python -m src.cli --level B1 --topic "present perfect" --count 10

# Launch web UI
python -m src.app
```

## Project Structure

```
taallim-pilot/
├── src/                    # Core Python modules
│   ├── exercise_generator.py   # Main generator
│   ├── offline_generator.py    # Offline mode (no API)
│   ├── offline_data.py         # Topic database
│   ├── prompts.py              # LLM prompts
│   ├── topics.py               # Topic mapping
│   ├── cli.py                  # Command line interface
│   ├── app.py                  # Streamlit web UI
│   └── topics/                 # Level-specific topics
│       ├── A1.json
│       ├── A2.json
│       ├── B1.json
│       └── B2.json
├── tests/                  # Parallel test forms
│   ├── GRAMMAR_TEST_FORM_A.md
│   ├── GRAMMAR_TEST_FORM_B.md
│   ├── GRAMMAR_TEST_FORM_C.md
│   ├── VOCABULARY_TEST_FORM_A.md
│   ├── VOCABULARY_TEST_FORM_B.md
│   └── VOCABULARY_TEST_FORM_C.md
├── scripts/                # Analysis tools
│   └── taallim_analysis.py    # Auto-generates §4 results tables
├── docs/                   # Protocol & planning
│   ├── TAALLIM_TEST_SPECS.md
│   ├── TAALLIM_PROTOCOL_SUMMARY.md
│   ├── TAALLIM_SCHOOL_OUTREACH.md
│   ├── TAALLIM_6WEEK_PILOT_PLAN.md
│   └── TAALLIM_TEACHER_INSTRUMENTS_RQ3.md
├── data/                   # Sample data
│   ├── sample_pilot_data.csv
│   └── SYNTHETIC_PILOT_DATA.csv
└── requirements.txt
```

## Test Forms

6 parallel forms (A/B/C) for counterbalanced administration:

| Form | Grammar | Vocabulary |
|------|---------|------------|
| A | 55 scored + 5 buffer | 60 distinct words |
| B | Same structure, different items | Same words, different contexts |
| C | Same structure, different items | Same words, different contexts |

## Pilot Plan

- **Site**: Allal (private) + 1 public collège in El Bayadh
- **Duration**: 6 weeks
- **Sample**: 60 students per school (120 total)
- **Design**: Within-school assignment (experimental/control classes)

## License

Private — MAHI Kamel Abdelghani
