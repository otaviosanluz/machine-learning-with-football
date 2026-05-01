# CLAUDE.md — machine-learning-football

## Project Overview

Personal study repository for Machine Learning applied to football, based on the book
**ISLP — An Introduction to Statistical Learning with Applications in Python**
(James, Witten, Hastie, Tibshirani, Taylor — 2023).

Each notebook is created from a YouTube course lecture, adapting the book's concepts
and labs to real data from the **Brazilian Championship 2025** (Impect API).

Goal: technical learning in ML with practical application in football analytics,
structured as a GitHub portfolio.

---

## Folder Structure

```
machine-learning-football/
├── CLAUDE.md
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── brasileirao_2025_impect.csv   # not versioned in git
├── notebooks/
│   └── (notebooks created as lectures progress)
└── utils/
    └── football_helpers.py
```

Notebooks are named following this pattern:
`lecture{number}_{topic}.ipynb`
Example: `lecture03_linear_regression.ipynb`

---

## Dataset

- **Source:** Impect API
- **Competition:** Brazilian Championship (Série A) 2025
- **Granularity:** team level per match
- **Size:** 1000+ columns (tactical, physical, pressure, possession metrics, etc.)
- **Local file:** `data/brasileirao_2025_impect.csv`
- **Important:** never commit the data file to GitHub

---

## Project Color Palette

All visualizations must use exclusively this palette to ensure
reproducibility and consistent visual identity across notebooks.

```python
# ===================== PROJECT PALETTE =====================

COLORS = {
    "primary":    "#1B4F72",   # dark blue  — main highlight
    "secondary":  "#2E86C1",   # mid blue   — second category
    "tertiary":   "#85C1E9",   # light blue — third category
    "accent":     "#E67E22",   # orange     — contrast / call to attention
    "neutral":    "#BDC3C7",   # light gray — background bars / comparison
    "background": "#F4F6F7",   # off-white  — figure background
    "text":       "#1C2833",   # near-black — titles and labels
}

# Default sequence for multiple categories
SEQUENTIAL_PALETTE = [
    "#1B4F72", "#2E86C1", "#85C1E9",
    "#E67E22", "#F0B27A", "#BDC3C7",
]

# Usage with matplotlib
import matplotlib.pyplot as plt
plt.rcParams["axes.prop_cycle"]  = plt.cycler(color=SEQUENTIAL_PALETTE)
plt.rcParams["figure.facecolor"] = COLORS["background"]
plt.rcParams["axes.facecolor"]   = COLORS["background"]
plt.rcParams["axes.labelcolor"]  = COLORS["text"]
plt.rcParams["xtick.color"]      = COLORS["text"]
plt.rcParams["ytick.color"]      = COLORS["text"]
plt.rcParams["text.color"]       = COLORS["text"]
```

Always import from `utils/football_helpers.py` to avoid repeating in each notebook:

```python
from utils.football_helpers import COLORS, SEQUENTIAL_PALETTE, apply_style
```

---

## Code Standards

### Section comments (required in all files)

```python
# ===================== SECTION NAME =====================
```

### Standard notebook structure

1. **Theoretical context** — markdown cell summarizing the lecture topic and ISLP chapter
2. **Data loading** — reading the Impect CSV
3. **Preprocessing** — variable selection, null handling
4. **Modeling** — ISLP lab adapted to football data
5. **Visualizations** — using the project palette
6. **Interpretation** — markdown cell with analysis in the Brazilian football context

### Python style

- Variables and functions: `snake_case`
- Constants: `UPPER_CASE`
- Grouped imports: stdlib → third-party → local
- `pandas` for tabular data manipulation
- `scikit-learn` for models
- `matplotlib` / `seaborn` for visualizations

### Visualizations

- Prefer horizontal bar charts
- Use per-match averages as the base metric
- Always call `apply_style()` before plotting

---

## Domain Context

- Dataset with 1000+ columns — always prioritize variable selection and dimensionality
  reduction before modeling
- Key tactical metrics: pressure, PPDA, possession, progression, xG, defensive transitions
- Physical metrics: distance covered, sprints, intensity by field zone
- Results should always be interpreted in the context of Brazilian football (Série A 2025)

---

## Workflow Per Lecture

For each new lecture watched:

1. Inform Claude Code: lecture number, topic, and corresponding ISLP chapter
2. Claude Code creates the notebook with the standard structure pre-filled
3. Adapt the book's examples to the Impect dataset
4. Commit with a descriptive message:

```
git commit -m "lecture03: linear regression - predicting xG from Impect data"
```

---

## Main Dependencies

```
pandas
numpy
scikit-learn
matplotlib
seaborn
jupyter
islp
statsmodels
```

Install with: `pip install -r requirements.txt`
