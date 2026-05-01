# Football Analytics with Machine Learning

> Applying statistical learning methods to real match data from the **Brazilian Championship Série A 2025**, using the [ISLP book](https://www.statlearning.com/) as a theoretical guide.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-0.14-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)

---

## About the Project

This repository documents a structured study of Machine Learning techniques applied to football analytics. Each notebook corresponds to a lecture from a course based on **ISLP — An Introduction to Statistical Learning with Applications in Python** (James, Witten, Hastie, Tibshirani & Taylor, 2023).

Every concept from the book is adapted to answer real questions about Brazilian football using match-level data from the **Impect API** — one of the most granular tactical datasets available, with 1,400+ metrics per match covering packing, xG, pressure, possession phases, and more.

**Goals:**
- Build a rigorous, reproducible ML portfolio grounded in statistical theory
- Apply each method to a meaningful football analytics question
- Develop intuition about what drives performance in Série A 2025

---

## Dataset

| Field | Details |
|---|---|
| Source | [Impect API](https://www.impect.com/) |
| Competition | Brasileirão Série A 2025 |
| Granularity | Team per match |
| Columns | 1,400+ tactical and possession metrics |
| Key metrics | xG, post-shot xG, packing (bypassed opponents), PPDA, progressive passes, set-piece xG |

> **Note:** The raw data file is not included in this repository (proprietary). To reproduce the analyses, you will need access to the Impect API or a compatible dataset with the same column schema.

---

## Lectures

| # | Notebook | Topic | ISLP Chapter | Status |
|---|---|---|---|---|
| 01 | [lecture01_simple_linear_regression.ipynb](notebooks/lecture01_simple_linear_regression.ipynb) | Simple Linear Regression — inference & prediction | Ch. 3.1 | ✅ Done |

---

## Lecture 01 Highlights — Simple Linear Regression

**Question:** Can the number of shots from inside the box predict post-shot xG in Série A?

**Variable choice rationale:**
- **Target — `POSTSHOT_XG`**: post-shot expected goals, which accounts for actual shot placement and trajectory. More predictive of goals than pre-shot xG.
- **Predictor — `SHOT_AT_GOAL_NUMBER_IN_PITCH_POSITION_OPPONENT_BOX`**: shots taken from inside the penalty area — the primary driver of shot quality, with no leakage from the post-shot model itself.

**Covered:**
- OLS fitting with `statsmodels` — full inference summary (coefficients, SE, t-stats, p-values, R², RSE, F-statistic)
- 95% Confidence Intervals for coefficients
- Point prediction, Confidence Interval (mean response), and Prediction Interval (individual observation)
- Residual diagnostics

---

## Project Structure

```
football-analytics-ml/
├── notebooks/
│   └── lecture01_simple_linear_regression.ipynb
├── utils/
│   └── football_helpers.py   # shared palette, apply_style()
├── data/                     # not versioned — see Dataset section
├── requirements.txt
├── CLAUDE.md                 # project conventions for AI-assisted development
└── README.md
```

---

## Visual Identity

All visualisations share a consistent palette defined in `utils/football_helpers.py`:

| Role | Colour | Hex |
|---|---|---|
| Primary | Dark blue | `#1B4F72` |
| Secondary | Mid blue | `#2E86C1` |
| Tertiary | Light blue | `#85C1E9` |
| Accent | Orange | `#E67E22` |
| Neutral | Light grey | `#BDC3C7` |

---

## Setup

```bash
# Clone the repository
git clone https://github.com/otaviosanluz/football-analytics-ml.git
cd football-analytics-ml

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

Python 3.11+ recommended.

---

## Author

**Otavio Santos** — Football Data Scientist.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin)](https://www.linkedin.com/in/otaviosanluz/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?logo=github)](https://github.com/otaviosanluz)

---

## References

- James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). *An Introduction to Statistical Learning with Applications in Python*. Springer. [Free PDF](https://www.statlearning.com/)
- [Impect API Documentation](https://www.impect.com/)
