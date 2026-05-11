# CLAUDE.md — machine-learning-football

## Project Overview

Personal study repository for Machine Learning applied to football, based on the book
**ISLP — An Introduction to Statistical Learning with Applications in Python**
(James, Witten, Hastie, Tibshirani, Taylor — 2023).

Each notebook is created from a YouTube course lecture, adapting the book's concepts
and labs to real football data from **StatsBomb Open Data** (free, publicly available).

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
│   └── laliga_2015_16_team_match.csv   # not versioned in git
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

- **Source:** StatsBomb Open Data (`statsbombpy` library — free, no credentials needed)
- **Competition:** La Liga 2015/16 (Spain) — full season, 380 matches
- **Granularity:** team level per match (760 team-match observations)
- **Local file:** `data/laliga_2015_16_team_match.csv` — pre-processed, not versioned in git
- **How it is built:** shot events from StatsBomb are aggregated to team-match level
  (see preprocessing section below)

### Key columns in the pre-processed dataset

| Column | Description |
|---|---|
| `XG_TOTAL` | Sum of `shot_statsbomb_xg` per team per match — **main target** |
| `SHOTS_TOTAL` | Total shots taken |
| `SHOTS_IN_BOX` | Shots from inside the penalty area (x > 102, 18 < y < 62) |
| `SHOTS_ON_TARGET` | Shots heading toward goal (outcome: Goal or Saved) |
| `SHOTS_CLOSE_RANGE` | Shots from very close range (x > 110) |
| `SHOTS_MID_RANGE` | Shots from outside the box (x ≤ 102) |
| `SHOTS_HEADER` | Headers |
| `SHOTS_OPEN_PLAY` | Shots from open play (excludes corners, free kicks, penalties) |
| `SHOTS_UNDER_PRESSURE` | Shots taken while under opponent pressure |
| `SHOTS_FIRST_TIME` | First-time shots |
| `DEFENDERS_IN_FF_TOTAL` | Total defenders visible in freeze frame across all shots |

### Leakage note
`DEFENDERS_IN_FF_TOTAL` partially overlaps with StatsBomb's xG model inputs (freeze frame
data is used internally). Use it as a predictor with caution and document this in notebooks.
All shot-count features (SHOTS_*) are safe — no leakage.

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
2. **Data loading** — reading the pre-processed CSV from `data/`
3. **Preprocessing** — variable selection, null handling
4. **Modeling** — ISLP lab adapted to football data
5. **Visualizations** — using the project palette
6. **Interpretation** — markdown cell with analysis in the La Liga football context
7. **Conclusion** — brief summary and next steps

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

- StatsBomb pitch coordinates: 120 × 80 yards. Box threshold: x > 102, 18 < y < 62.
- `shot_statsbomb_xg` is a post-shot xG model (uses freeze frame: keeper position,
  defenders between shooter and goal). Analogous to POSTSHOT_XG in Impect.
- Results should always be interpreted in the context of La Liga 2015/16 football.

---

## Workflow Per Lecture

For each new lecture watched:

1. Inform Claude Code: lecture number, topic, and corresponding ISLP chapter
2. Claude Code creates the notebook with the standard structure pre-filled
3. Adapt the book's examples to the Impect dataset
4. Commit with a descriptive message:

```
git commit -m "lecture03: linear regression - predicting xG from StatsBomb data"
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
statsbombpy
```

Install with: `pip install -r requirements.txt`
