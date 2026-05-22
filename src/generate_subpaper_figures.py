"""
Generate all figures for research-concept-sub-paper-en.md
Outputs saved to: images/ folder at workspace root
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.gridspec import GridSpec
import seaborn as sns

# ── Paths ────────────────────────────────────────────────────────────────────
WORKSPACE = r"d:\BINUS Works\Codes\research_banks\research\is_edtech"
IMAGES_DIR = os.path.join(WORKSPACE, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# ── Shared style ─────────────────────────────────────────────────────────────
PALETTE = {
    "blue_light":  "#e3f2fd",
    "blue_mid":    "#1565c0",
    "blue_dark":   "#0d47a1",
    "green_light": "#e8f5e9",
    "green_mid":   "#2e7d32",
    "orange_light":"#fff3e0",
    "orange_mid":  "#e65100",
    "red_dark":    "#b71c1c",
    "red_light":   "#ffebee",
    "purple_light":"#e8eaf6",
    "purple_mid":  "#4527a0",
    "grey_bg":     "#f5f5f5",
    "grey_text":   "#37474f",
    "white":       "#ffffff",
    "full":        "#2e7d32",   # ✓
    "partial":     "#f57f17",   # ◑
    "absent":      "#c62828",   # ✗
}

plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "figure.facecolor": PALETTE["white"],
    "axes.facecolor":   PALETTE["white"],
    "savefig.dpi":      180,
    "savefig.bbox":     "tight",
    "savefig.facecolor":PALETTE["white"],
})

# ─────────────────────────────────────────────────────────────────────────────
# FIG 1 — Five-Stage Scoping Review Process
# ─────────────────────────────────────────────────────────────────────────────
def fig1_scoping_stages():
    fig, ax = plt.subplots(figsize=(15, 4.5))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 4.5)
    ax.axis("off")

    stages = [
        ("Stage 1", "Research\nQuestion"),
        ("Stage 2", "Identify\nRelevant Studies"),
        ("Stage 3", "Study\nSelection"),
        ("Stage 4", "Chart\nthe Data"),
        ("Stage 5", "Collate, Summarize\n& Report"),
    ]

    box_w, box_h = 2.2, 1.8
    gap = 0.6
    total_w = len(stages) * box_w + (len(stages) - 1) * gap
    start_x = (15 - total_w) / 2
    y_center = 2.25

    for i, (stage, label) in enumerate(stages):
        x = start_x + i * (box_w + gap)
        # Shadow
        ax.add_patch(FancyBboxPatch(
            (x + 0.06, y_center - box_h / 2 - 0.06), box_w, box_h,
            boxstyle="round,pad=0.1", linewidth=0,
            facecolor="#b0bec5", zorder=1))
        # Main box
        ax.add_patch(FancyBboxPatch(
            (x, y_center - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.1", linewidth=1.5,
            edgecolor=PALETTE["blue_mid"], facecolor=PALETTE["blue_light"], zorder=2))
        # Stage label (top)
        ax.text(x + box_w / 2, y_center + box_h / 2 - 0.36,
                stage, ha="center", va="center",
                fontsize=9, fontweight="bold", color=PALETTE["blue_dark"], zorder=3)
        # Divider
        ax.plot([x + 0.15, x + box_w - 0.15],
                [y_center + box_h / 2 - 0.56, y_center + box_h / 2 - 0.56],
                color=PALETTE["blue_mid"], lw=0.8, zorder=3)
        # Description
        ax.text(x + box_w / 2, y_center - 0.1,
                label, ha="center", va="center",
                fontsize=8.5, color=PALETTE["grey_text"], zorder=3)

        # Arrow to next
        if i < len(stages) - 1:
            ax.annotate("", xy=(x + box_w + gap, y_center),
                        xytext=(x + box_w, y_center),
                        arrowprops=dict(arrowstyle="->", color=PALETTE["blue_mid"],
                                        lw=2.0), zorder=4)

    # Title
    ax.text(7.5, 4.2,
            "Five-Stage Scoping Review Framework (Arksey & O'Malley, 2005)",
            ha="center", va="center", fontsize=12, fontweight="bold",
            color=PALETTE["blue_dark"])

    # Footer caption
    ax.text(7.5, 0.15,
            "Reported in accordance with PRISMA-ScR (Tricco et al., 2018)",
            ha="center", va="center", fontsize=8, color="#78909c", style="italic")

    path = os.path.join(IMAGES_DIR, "fig1_scoping_review_stages.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 2 — Coverage Matrix Heatmap
# ─────────────────────────────────────────────────────────────────────────────
def fig2_coverage_matrix():
    frameworks = [
        "F1  Chapelle (2001)",
        "F2  Hubbard (2011)",
        "F3  Leakey (2011)",
        "F4  Colpaert (2004)",
        "F5  Rosell-Aguilar (2017)",
        "F6  Almaiah et al. (2021)",
        "F7  Al-Fraihat et al. (2020)",
        "F8  Scheffel / EFLA (2014)",
        "F9  Park & Jo (2019)",
        "F10 UTAUT / Venkatesh (2003)",
        "F11 TRAM / Kampa (2024)",
        "F12 Essafi / MLLA (2025)",
    ]
    dims = ["D1\nTECH", "D2\nPED", "D3\nINST", "D4\nHigh-Stakes", "D6\nMulti-Stakeholder"]
    symbols = ["✗", "✓", "✗", "◑", "✗",
               "✗", "✓", "✗", "✗", "✗",
               "◑", "✓", "✗", "✗", "✗",
               "✗", "✓", "✗", "✗", "✗",
               "◑", "◑", "✗", "✗", "✗",
               "✓", "◑", "◑", "✗", "◑",
               "✓", "◑", "◑", "✗", "◑",
               "✗", "✗", "✓", "✗", "◑",
               "✗", "✗", "✓", "✗", "◑",
               "◑", "✗", "✗", "✗", "✗",
               "◑", "◑", "✗", "✗", "✗",
               "◑", "✓", "✗", "◑", "✗"]
    scores  = [1.5, 1.0, 1.5, 1.0, 1.0, 2.5, 2.5, 1.5, 1.5, 0.5, 1.0, 2.0]

    sym_map = {"✓": 1.0, "◑": 0.5, "✗": 0.0}
    n_f, n_d = len(frameworks), len(dims)
    matrix = np.array([sym_map[s] for s in symbols]).reshape(n_f, n_d)

    fig = plt.figure(figsize=(13, 8))
    gs  = GridSpec(1, 2, figure=fig, width_ratios=[5, 1.1], wspace=0.03)
    ax_heat = fig.add_subplot(gs[0])
    ax_bar  = fig.add_subplot(gs[1])

    # Custom color map: absent → partial → full
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "cov", ["#ffcdd2", "#fff9c4", "#c8e6c9"], N=256)

    sns.heatmap(matrix, ax=ax_heat, cmap=cmap, vmin=0, vmax=1,
                xticklabels=dims, yticklabels=frameworks,
                linewidths=0.5, linecolor="#eceff1",
                cbar=False, annot=False)

    # Overlay symbols
    for r in range(n_f):
        for c in range(n_d):
            sym = symbols[r * n_d + c]
            color = (PALETTE["full"] if sym == "✓"
                     else PALETTE["partial"] if sym == "◑"
                     else PALETTE["absent"])
            ax_heat.text(c + 0.5, r + 0.5, sym,
                         ha="center", va="center",
                         fontsize=14, fontweight="bold", color=color)

    ax_heat.set_title(
        "Dimensional Coverage Matrix — 12 Evaluation Frameworks × 5 Dimensions",
        fontsize=11, fontweight="bold", color=PALETTE["blue_dark"], pad=12)
    ax_heat.tick_params(axis="x", labelsize=8.5)
    ax_heat.tick_params(axis="y", labelsize=8)
    ax_heat.set_xlabel("Evaluation Dimension", fontsize=9, labelpad=6)

    # Coverage score bar
    y_pos = np.arange(n_f)
    colors_bar = [PALETTE["full"] if s >= 2.0
                  else PALETTE["partial"] if s >= 1.0
                  else PALETTE["absent"] for s in scores]
    bars = ax_bar.barh(y_pos, scores, color=colors_bar, height=0.65,
                       edgecolor="white", linewidth=0.8)
    ax_bar.set_xlim(0, 5.5)
    ax_bar.axvline(x=2.5, color=PALETTE["red_dark"], lw=1.2, ls="--", alpha=0.7)
    ax_bar.set_yticks(y_pos)
    ax_bar.set_yticklabels([])
    ax_bar.set_xlabel("Coverage Score /5", fontsize=8.5, labelpad=6)
    ax_bar.set_title("Score", fontsize=9, fontweight="bold",
                     color=PALETTE["blue_dark"], pad=12)
    ax_bar.tick_params(axis="x", labelsize=8)
    ax_bar.set_ylim(-0.5, n_f - 0.5)
    ax_bar.invert_yaxis()
    for bar, s in zip(bars, scores):
        ax_bar.text(s + 0.08, bar.get_y() + bar.get_height() / 2,
                    f"{s:.1f}", va="center", fontsize=8, color=PALETTE["grey_text"])

    # Legend
    legend_items = [
        mpatches.Patch(color=PALETTE["full"],    label="✓  Full coverage (1.0)"),
        mpatches.Patch(color=PALETTE["partial"], label="◑  Partial (0.5)"),
        mpatches.Patch(color=PALETTE["absent"],  label="✗  Absent (0.0)"),
    ]
    fig.legend(handles=legend_items, loc="lower center", ncol=3,
               fontsize=8.5, frameon=True, framealpha=0.9,
               bbox_to_anchor=(0.5, -0.02))

    fig.text(0.5, -0.06,
             "†D5 Rigor Indicator not shown in heatmap — assessed separately as framework meta-quality, not a coverage dimension.",
             ha="center", fontsize=7.5, color="#78909c", style="italic")

    path = os.path.join(IMAGES_DIR, "fig2_coverage_matrix_heatmap.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 3 — Coverage Scores Bar Chart (ranked)
# ─────────────────────────────────────────────────────────────────────────────
def fig3_coverage_scores():
    data = [
        ("F6  Almaiah et al. (2021)",      2.5, "IS"),
        ("F7  Al-Fraihat et al. (2020)",   2.5, "IS"),
        ("F12 Essafi / MLLA (2025)",       2.0, "Linguistics"),
        ("F1  Chapelle (2001)",            1.5, "Linguistics"),
        ("F3  Leakey (2011)",              1.5, "Linguistics"),
        ("F8  Scheffel / EFLA (2014)",     1.5, "LA"),
        ("F9  Park & Jo (2019)",           1.5, "LA"),
        ("F2  Hubbard (2011)",             1.0, "Linguistics"),
        ("F4  Colpaert (2004)",            1.0, "Linguistics"),
        ("F5  Rosell-Aguilar (2017)",      1.0, "Linguistics"),
        ("F11 TRAM / Kampa (2024)",        1.0, "IS"),
        ("F10 UTAUT / Venkatesh (2003)",   0.5, "IS"),
    ]
    data.sort(key=lambda x: x[1], reverse=True)

    labels  = [d[0] for d in data]
    scores  = [d[1] for d in data]
    discs   = [d[2] for d in data]

    disc_colors = {
        "IS":          "#1565c0",
        "Linguistics": "#2e7d32",
        "LA":          "#6a1b9a",
    }
    bar_colors = [disc_colors[d] for d in discs]

    fig, ax = plt.subplots(figsize=(11, 6.5))
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, scores, color=bar_colors, height=0.62,
                   edgecolor="white", linewidth=0.8, alpha=0.88)

    # Reference lines
    ax.axvline(x=2.5, color=PALETTE["red_dark"], lw=1.5, ls="--",
               label="Max achieved (2.5 / 5.0)")
    ax.axvline(x=5.0, color="#78909c", lw=1.0, ls=":",
               label="Theoretical maximum (5.0)")

    # Score labels
    for bar, s in zip(bars, scores):
        ax.text(s + 0.05, bar.get_y() + bar.get_height() / 2,
                f"{s:.1f}", va="center", fontsize=9, color=PALETTE["grey_text"])

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlim(0, 5.8)
    ax.set_xlabel("Dimensional Coverage Score (out of 5.0)", fontsize=10, labelpad=8)
    ax.set_title(
        "Coverage Scores Across 12 Evaluation Frameworks\n"
        "(5 Object-Level Dimensions: D1 TECH, D2 PED, D3 INST, D4 High-Stakes, D6 Multi-Stakeholder)",
        fontsize=11, fontweight="bold", color=PALETTE["blue_dark"], pad=12)
    ax.invert_yaxis()
    ax.spines[["top", "right"]].set_visible(False)

    # Discipline legend
    disc_patches = [mpatches.Patch(color=c, label=f"{d} discipline")
                    for d, c in disc_colors.items()]
    all_handles = disc_patches + ax.get_legend_handles_labels()[0]
    ax.legend(handles=all_handles, loc="lower right", fontsize=8.5,
              frameon=True, framealpha=0.9, ncol=2)

    # Annotation: no framework > 50%
    ax.text(2.55, 0.3, "← Max 50% coverage\n   achieved by any\n   single framework",
            fontsize=7.5, color=PALETTE["red_dark"], va="top")

    fig.tight_layout()
    path = os.path.join(IMAGES_DIR, "fig3_coverage_scores_ranked.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 4 — Four Coverage Gaps Diagram
# ─────────────────────────────────────────────────────────────────────────────
def fig4_coverage_gaps():
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8)
    ax.axis("off")

    def rounded_box(ax, x, y, w, h, text, facecolor, edgecolor,
                    fontsize=9, bold=False, text_color="black"):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                   boxstyle="round,pad=0.15",
                                   facecolor=facecolor, edgecolor=edgecolor,
                                   linewidth=1.5, zorder=2))
        ax.text(x + w / 2, y + h / 2, text,
                ha="center", va="center", fontsize=fontsize,
                fontweight="bold" if bold else "normal",
                color=text_color, zorder=3,
                multialignment="center", wrap=True)

    # ── Gap boxes (4 corners) ────────────────────────────────────────────────
    gaps = [
        (0.4, 5.2, 5.0, 2.1,
         "Gap 1: Contextual Specificity\n"
         "D4 (High-Stakes Test Specificity)\nnever achieves full coverage\n"
         "— max ◑ across all 12 frameworks",
         PALETTE["red_light"], PALETTE["absent"]),

        (7.6, 5.2, 5.0, 2.1,
         "Gap 2: Disciplinary Silos\n"
         "CALL frameworks lack D1 + D3\n"
         "IS frameworks lack D2\n"
         "domain-specific depth",
         PALETTE["red_light"], PALETTE["absent"]),

        (0.4, 2.0, 5.0, 2.1,
         "Gap 3: Institutional Blindspot\n"
         "D3 found only in LA tools (F8/F9)\n"
         "— absent from ALL CALL/MALL\n"
         "frameworks",
         PALETTE["red_light"], PALETTE["absent"]),

        (7.6, 2.0, 5.0, 2.1,
         "Gap 4: Single-Stakeholder Bias\n"
         "D6 (Multi-Stakeholder Perspective)\nnever achieves full coverage\n"
         "— max ◑ across all 12 frameworks",
         PALETTE["red_light"], PALETTE["absent"]),
    ]

    for (x, y, w, h, txt, fc, ec) in gaps:
        rounded_box(ax, x, y, w, h, txt, fc, ec, fontsize=9)

    # ── Central finding box ──────────────────────────────────────────────────
    cx, cy, cw, ch = 3.8, 3.55, 5.4, 1.0
    ax.add_patch(FancyBboxPatch((cx, cy), cw, ch,
                                boxstyle="round,pad=0.2",
                                facecolor=PALETTE["red_dark"],
                                edgecolor="#7f0000",
                                linewidth=2.0, zorder=4))
    ax.text(cx + cw / 2, cy + ch / 2,
            "No single framework exceeds 2.5 / 5.0\n(50% maximum coverage — all 12 frameworks reviewed)",
            ha="center", va="center", fontsize=10, fontweight="bold",
            color="white", zorder=5, multialignment="center")

    # ── Rigor finding box (dashed) ───────────────────────────────────────────
    rx, ry, rw, rh = 4.0, 0.3, 5.0, 1.1
    ax.add_patch(FancyBboxPatch((rx, ry), rw, rh,
                                boxstyle="round,pad=0.15",
                                facecolor=PALETTE["purple_light"],
                                edgecolor=PALETTE["purple_mid"],
                                linewidth=1.5, linestyle="--", zorder=2))
    ax.text(rx + rw / 2, ry + rh / 2,
            "Rigor Finding — D5 (separate, not a coverage gap)\n"
            "7 / 12 frameworks: ◑ partial definitions   ·   5 / 12: ✗ reflective checklist only",
            ha="center", va="center", fontsize=8.5, color=PALETTE["purple_mid"],
            zorder=3, multialignment="center")

    # ── Arrows: gaps → central box ───────────────────────────────────────────
    arrow_props = dict(arrowstyle="->", color="#c62828", lw=1.8)
    arrow_coords = [
        ((0.4 + 5.0, 5.2 + 1.05), (cx, cy + ch)),        # Gap 1 → box
        ((7.6, 5.2 + 1.05),        (cx + cw, cy + ch)),   # Gap 2 → box
        ((0.4 + 5.0, 2.0 + 1.05), (cx, cy)),              # Gap 3 → box
        ((7.6, 2.0 + 1.05),        (cx + cw, cy)),         # Gap 4 → box
    ]
    for (x1, y1), (x2, y2) in arrow_coords:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=arrow_props, zorder=3)

    # ── Dashed arrow: rigor → central box ────────────────────────────────────
    ax.annotate("", xy=(cx + cw / 2, cy),
                xytext=(rx + rw / 2, ry + rh),
                arrowprops=dict(arrowstyle="->", color=PALETTE["purple_mid"],
                                lw=1.4, linestyle="dashed"), zorder=3)
    ax.text(7.5, 1.55,
            "framework quality finding\n(not a coverage gap)",
            fontsize=7.5, color=PALETTE["purple_mid"], style="italic",
            ha="center", va="center")

    # ── Title ────────────────────────────────────────────────────────────────
    ax.text(6.5, 7.7,
            "Four Systematic Coverage Gaps Identified from Dimensional Analysis",
            ha="center", va="center", fontsize=12, fontweight="bold",
            color=PALETTE["blue_dark"])

    path = os.path.join(IMAGES_DIR, "fig4_coverage_gaps_diagram.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 5 — Research Program Architecture
# ─────────────────────────────────────────────────────────────────────────────
def fig5_research_architecture():
    fig, ax = plt.subplots(figsize=(13, 6.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    def card(ax, x, y, w, h, title, lines, facecolor, edgecolor, title_color):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                   boxstyle="round,pad=0.2",
                                   facecolor=facecolor,
                                   edgecolor=edgecolor,
                                   linewidth=2.0, zorder=2))
        # Title band
        ax.add_patch(FancyBboxPatch((x + 0.05, y + h - 0.78), w - 0.1, 0.7,
                                   boxstyle="round,pad=0.05",
                                   facecolor=edgecolor, edgecolor="none", zorder=3))
        ax.text(x + w / 2, y + h - 0.42,
                title, ha="center", va="center",
                fontsize=10, fontweight="bold", color="white", zorder=4)
        for i, line in enumerate(lines):
            ax.text(x + 0.25, y + h - 1.1 - i * 0.42,
                    line, va="center", fontsize=8.5,
                    color=PALETTE["grey_text"], zorder=3)

    # Sub-paper card
    card(ax, 0.4, 0.8, 4.8, 5.0,
         "Sub-Paper  ·  Scoping Review",
         ["Mapping Evaluation Frameworks...",
          "─────────────────────────────────",
          "Methodology:  Scoping Review",
          "               (Arksey & O'Malley, 2005)",
          "Output:         Coverage Matrix",
          "                12 frameworks × 5 dimensions",
          "Contribution: Gap Evidence",
          "Venue:          Scopus Q2 / Conference"],
         PALETTE["blue_light"], PALETTE["blue_mid"],
         PALETTE["blue_mid"])

    # Main paper card
    card(ax, 7.8, 0.8, 4.8, 5.0,
         "Main Paper  ·  Conceptual Framework",
         ["A Theoretical Framework and...",
          "─────────────────────────────────",
          "Methodology:  CFA + Integrative Review",
          "Output:         Framework + Assessment",
          "                Model (D1–D4, D6 + D&M)",
          "Contribution: Framework Construction",
          "Venue:          Scopus Q1",
          "Cites sub-paper as gap evidence"],
         PALETTE["green_light"], PALETTE["green_mid"],
         PALETTE["green_mid"])

    # Shared data box
    sx, sy, sw, sh = 4.4, 0.1, 4.2, 1.1
    ax.add_patch(FancyBboxPatch((sx, sy), sw, sh,
                                boxstyle="round,pad=0.12",
                                facecolor=PALETTE["orange_light"],
                                edgecolor=PALETTE["orange_mid"],
                                linewidth=1.5, linestyle="--", zorder=2))
    ax.text(sx + sw / 2, sy + sh / 2,
            "Phase 2: Literature Search + Coverage Matrix Data\n"
            "Shared Output — 100% overlap, zero additional cost",
            ha="center", va="center", fontsize=8.5,
            color=PALETTE["orange_mid"], fontweight="bold", zorder=3)

    # Arrows: shared data → both papers
    ax.annotate("",
                xy=(0.4 + 4.8, 0.8 + 0.55),
                xytext=(sx, sy + sh / 2),
                arrowprops=dict(arrowstyle="->", color=PALETTE["orange_mid"],
                                lw=1.8), zorder=4)
    ax.annotate("",
                xy=(7.8, 0.8 + 0.55),
                xytext=(sx + sw, sy + sh / 2),
                arrowprops=dict(arrowstyle="->", color=PALETTE["orange_mid"],
                                lw=1.8), zorder=4)

    # Arrow: sub-paper → main paper (cited)
    ax.annotate("",
                xy=(7.8, 0.8 + 3.0),
                xytext=(0.4 + 4.8, 0.8 + 3.0),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.2",
                                color=PALETTE["blue_mid"], lw=2.0), zorder=4)
    ax.text(6.5, 3.95,
            "cited as\ngap evidence", ha="center", va="bottom",
            fontsize=8, color=PALETTE["blue_mid"], style="italic")

    # Submission order badge
    ax.text(6.5, 0.55,
            "Recommended order: Submit sub-paper first → acceptance → submit main paper",
            ha="center", va="center", fontsize=8,
            color=PALETTE["grey_text"], style="italic")

    # Title
    ax.text(6.5, 6.2,
            "Research Program Architecture: Sub-Paper ↔ Main Paper Relationship",
            ha="center", va="center", fontsize=12, fontweight="bold",
            color=PALETTE["blue_dark"])

    path = os.path.join(IMAGES_DIR, "fig5_research_program_architecture.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 6 — PCC Framework & Analytical Dimensions (Supplementary)
# ─────────────────────────────────────────────────────────────────────────────
def fig6_pcc_and_dimensions():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    fig.suptitle(
        "Methodological Framework: PCC Scoping Review Design & Analytical Dimensions",
        fontsize=11, fontweight="bold", color=PALETTE["blue_dark"], y=1.01)

    # ── Left: PCC table ──────────────────────────────────────────────────────
    ax = axes[0]
    ax.axis("off")
    ax.set_title("PCC Framework (Munn et al., 2018)", fontsize=10,
                 fontweight="bold", color=PALETTE["blue_dark"], pad=8)

    pcc_data = [
        ["Population",
         "Higher education institutions and their stakeholders:\n"
         "learners, instructors, and platform administrators"],
        ["Concept",
         "Frameworks and evaluation models designed for\n"
         "digital language learning platforms\n"
         "(CALL / MALL / EdTech / LMS)"],
        ["Context",
         "Institutional adoption, quality assurance, and\n"
         "decision-making contexts in higher education"],
    ]
    colors_pcc = [PALETTE["blue_mid"], PALETTE["green_mid"], PALETTE["purple_mid"]]

    for i, (elem, defn) in enumerate(pcc_data):
        y_top = 0.88 - i * 0.31
        # Element badge
        ax.add_patch(FancyBboxPatch((0.02, y_top - 0.06), 0.18, 0.22,
                                   boxstyle="round,pad=0.02",
                                   transform=ax.transAxes,
                                   facecolor=colors_pcc[i], edgecolor="none",
                                   zorder=2, clip_on=False))
        ax.text(0.11, y_top + 0.05, elem,
                ha="center", va="center", fontsize=10, fontweight="bold",
                color="white", transform=ax.transAxes, zorder=3)
        # Definition
        ax.text(0.25, y_top + 0.05, defn,
                ha="left", va="center", fontsize=8.5,
                color=PALETTE["grey_text"], transform=ax.transAxes)
        if i < 2:
            ax.plot([0.02, 0.98], [y_top - 0.06, y_top - 0.06],
                    color="#cfd8dc", lw=0.8, transform=ax.transAxes)

    # ── Right: Analytical dimensions ─────────────────────────────────────────
    ax2 = axes[1]
    ax2.axis("off")
    ax2.set_title("Analytical Dimensions & Theoretical Grounding",
                  fontsize=10, fontweight="bold", color=PALETTE["blue_dark"], pad=8)

    dims_data = [
        ("D1", "Technology\nArchitecture",  "D&M: System Quality",         PALETTE["blue_mid"]),
        ("D2", "Pedagogy\nEffectiveness",   "D&M: Information Quality",    PALETTE["green_mid"]),
        ("D3", "Institutional\nGovernance", "D&M: Service Quality",        PALETTE["purple_mid"]),
        ("D4", "High-Stakes Test\nSpecificity",
         "Bachman & Palmer (2010);\nChapelle (2001)",                       "#e65100"),
        ("D6", "Multi-Stakeholder\nPerspective",
         "Scheffel et al. (2014)",                                           "#6a1b9a"),
        ("D5†","Framework Rigor\n(meta-level)",
         "Munn et al. (2018)\n[separate indicator]",                        "#546e7a"),
    ]

    for i, (code, name, source, color) in enumerate(dims_data):
        y = 0.88 - i * 0.155
        dashed = (code == "D5†")
        ax2.add_patch(FancyBboxPatch((0.01, y - 0.055), 0.12, 0.12,
                                    boxstyle="round,pad=0.02",
                                    transform=ax2.transAxes,
                                    facecolor=color, edgecolor="none",
                                    zorder=2, clip_on=False,
                                    alpha=0.6 if dashed else 1.0))
        ax2.text(0.07, y + 0.005, code,
                 ha="center", va="center", fontsize=10, fontweight="bold",
                 color="white", transform=ax2.transAxes, zorder=3)
        ax2.text(0.17, y + 0.032, name,
                 ha="left", va="center", fontsize=8.5, fontweight="bold",
                 color=color, transform=ax2.transAxes,
                 style="italic" if dashed else "normal")
        ax2.text(0.17, y - 0.022, source,
                 ha="left", va="center", fontsize=7.5,
                 color=PALETTE["grey_text"], transform=ax2.transAxes)
        if i < len(dims_data) - 1:
            ax2.plot([0.01, 0.99], [y - 0.055, y - 0.055],
                     color="#cfd8dc", lw=0.6, ls="--" if i == 4 else "-",
                     transform=ax2.transAxes)

    ax2.text(0.5, -0.04,
             "†D5 is a framework meta-quality indicator — not counted in coverage score.",
             ha="center", va="center", fontsize=7.5, color="#78909c",
             style="italic", transform=ax2.transAxes)

    fig.tight_layout()
    path = os.path.join(IMAGES_DIR, "fig6_pcc_and_dimensions.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# Run all
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\nGenerating figures → {IMAGES_DIR}\n")
    fig1_scoping_stages()
    fig2_coverage_matrix()
    fig3_coverage_scores()
    fig4_coverage_gaps()
    fig5_research_architecture()
    fig6_pcc_and_dimensions()
    print("\nAll figures generated successfully.")
