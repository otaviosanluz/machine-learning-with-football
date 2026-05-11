# Machine Learning with Football

> Applying statistical learning methods to real match data from **La Liga 2015/16**, using the [ISLP book](https://www.statlearning.com/) as a theoretical guide.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-0.14-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?logo=scikit-learn&logoColor=white)
![StatsBomb](https://img.shields.io/badge/StatsBomb-Open%20Data-red)
![Status](https://img.shields.io/badge/status-in%20progress-yellow)

---

## About the Project

This repository documents a structured study of Machine Learning techniques applied to football analytics. Each notebook corresponds to a lecture from a course based on **ISLP — An Introduction to Statistical Learning with Applications in Python** (James, Witten, Hastie, Tibshirani & Taylor, 2023).

Every concept from the book is adapted to answer real questions about football using match-level data from the **StatsBomb Open Data** — freely available, event-level data with shot-by-shot detail for La Liga 2015/16 (380 matches).

**Goals:**
- Build a rigorous, reproducible ML portfolio grounded in statistical theory
- Apply each method to a meaningful football analytics question

---

## Dataset

| Field | Details |
|---|---|
| Source | [StatsBomb Open Data](https://github.com/statsbomb/open-data) (free, no credentials needed) |
| Competition | La Liga 2015/16 (Spain) |
| Granularity | Team per match |
| Observations | 760 team-match records (380 matches × 2 teams) |
| Key metrics | xG (post-shot model), shots by type and location, freeze frame (defenders near shot) |

> **Reproducibility:** All data is fetched via the `statsbombpy` library at runtime — no raw files needed. Run `pip install -r requirements.txt` and all notebooks will work without any data download.

---

## Lectures

| # | Notebook | Topic | ISLP Chapter | Status |
|---|---|---|---|---|
| 01 | [lecture01_simple_linear_regression.ipynb](notebooks/lecture01_simple_linear_regression.ipynb) | Simple Linear Regression — inference & prediction | Ch. 3.1 | ✅ Done |

---

## Project Structure

```
machine-learning-with-football/
├── notebooks/
│   └── lecture01_simple_linear_regression.ipynb
├── utils/
│   └── football_helpers.py   # shared palette, apply_style()
├── data/                     # not versioned — generated at runtime via statsbombpy
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
git clone https://github.com/otaviosanluz/machine-learning-with-football.git
cd machine-learning-with-football

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
- [StatsBomb Open Data](https://github.com/statsbomb/open-data)
- [statsbombpy documentation](https://github.com/statsbomb/statsbombpy)
