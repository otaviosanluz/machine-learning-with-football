# ===================== PROJECT PALETTE =====================

import matplotlib.pyplot as plt

COLORS = {
    "primary":    "#1B4F72",
    "secondary":  "#2E86C1",
    "tertiary":   "#85C1E9",
    "accent":     "#E67E22",
    "neutral":    "#BDC3C7",
    "background": "#F4F6F7",
    "text":       "#1C2833",
}

SEQUENTIAL_PALETTE = [
    "#1B4F72", "#2E86C1", "#85C1E9",
    "#E67E22", "#F0B27A", "#BDC3C7",
]


def apply_style():
    plt.rcParams["axes.prop_cycle"]  = plt.cycler(color=SEQUENTIAL_PALETTE)
    plt.rcParams["figure.facecolor"] = COLORS["background"]
    plt.rcParams["axes.facecolor"]   = COLORS["background"]
    plt.rcParams["axes.labelcolor"]  = COLORS["text"]
    plt.rcParams["xtick.color"]      = COLORS["text"]
    plt.rcParams["ytick.color"]      = COLORS["text"]
    plt.rcParams["text.color"]       = COLORS["text"]
    plt.rcParams["axes.spines.top"]   = False
    plt.rcParams["axes.spines.right"] = False
