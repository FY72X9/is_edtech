"""
Generate all figures for research-concept-sub-paper-en.md
Outputs saved to: images/ folder at workspace root
"""

import os
import sys
import numpy as np

# Reconfigure stdout to use UTF-8, avoiding UnicodeEncodeError on Windows terminals
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass  # Fallback for Python versions where reconfigure is not available
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
# FIG 2 — Five-Stage Scoping Review Process
# ─────────────────────────────────────────────────────────────────────────────
def fig1_scoping_stages():
    fig, ax = plt.subplots(figsize=(15, 5.5))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 5.5)
    ax.axis("off")

    stages = [
        ("Stage 1", "Research\nQuestion", "Define 3 RQs mapping\nCALL, IS, & governance\nfragmentation"),
        ("Stage 2", "Identify\nRelevant Studies", "Search Scopus, WoS,\nIEEE, & ERIC databases\n(2001-2025)"),
        ("Stage 3", "Study\nSelection", "Screen 1,200+ articles;\napply PCC criteria to select\n12 core frameworks"),
        ("Stage 4", "Chart\nthe Data", "Chart dimensions:\nTECH, PED, INST,\nHigh-Stakes, & Rater Rigor"),
        ("Stage 5", "Collate, Summarize\n& Report", "Generate coverage matrix;\nidentify gaps; justify\nintegrative model ($F^*$)"),
    ]

    box_w, box_h = 2.4, 2.8
    pad = 0.1
    visual_w = box_w + 2 * pad  # 2.6
    visual_h = box_h + 2 * pad  # 3.0
    gap = 0.35  # Distance between visual edges
    total_w = len(stages) * visual_w + (len(stages) - 1) * gap
    start_x = (15 - total_w) / 2
    y_center = 2.65

    for i, (stage, label, details) in enumerate(stages):
        v_left = start_x + i * (visual_w + gap)
        x = v_left + pad
        # Shadow
        ax.add_patch(FancyBboxPatch(
            (x + 0.05, y_center - box_h / 2 - 0.05), box_w, box_h,
            boxstyle="round,pad=0.1", linewidth=0,
            facecolor="#b0bec5", zorder=1))
        # Main box
        ax.add_patch(FancyBboxPatch(
            (x, y_center - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.1", linewidth=1.5,
            edgecolor=PALETTE["blue_mid"], facecolor=PALETTE["blue_light"], zorder=2))
        
        # Center of visual box
        v_center_x = v_left + visual_w / 2
        
        # Stage label (top)
        ax.text(v_center_x, y_center + box_h/2 - 0.4,
                stage, ha="center", va="center",
                fontsize=10.0, fontweight="bold", color=PALETTE["blue_dark"], zorder=3)
        # Divider
        ax.plot([v_left + 0.2, v_left + visual_w - 0.2],
                [y_center + box_h/2 - 0.7, y_center + box_h/2 - 0.7],
                color=PALETTE["blue_mid"], lw=0.8, zorder=3)
        # Description
        ax.text(v_center_x, y_center + box_h/2 - 1.1,
                label, ha="center", va="center",
                fontsize=9.5, fontweight="bold", color=PALETTE["grey_text"], zorder=3)
        # Details
        ax.text(v_center_x, y_center - 0.6,
                details, ha="center", va="center",
                fontsize=8.0, color="#546e7a", zorder=3, style="italic", multialignment="center")

        # Arrow to next
        if i < len(stages) - 1:
            v_right = v_left + visual_w
            v_next_left = v_right + gap
            arrow = FancyArrowPatch(
                (v_right + 0.02, y_center), (v_next_left - 0.02, y_center),
                arrowstyle="-|>", mutation_scale=15, color=PALETTE["blue_mid"],
                lw=2.0, zorder=4
            )
            ax.add_patch(arrow)

    # Title
    ax.text(7.5, 5.0,
            "Five-Stage Scoping Review Framework (Arksey & O'Malley, 2005)",
            ha="center", va="center", fontsize=13, fontweight="bold",
            color=PALETTE["blue_dark"])

    # Footer caption
    ax.text(7.5, 0.3,
            "Reported in accordance with PRISMA-ScR (Tricco et al., 2018)",
            ha="center", va="center", fontsize=9, color="#78909c", style="italic")

    path = os.path.join(IMAGES_DIR, "fig1_scoping_review_stages.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 4 — Coverage Matrix Heatmap
# ─────────────────────────────────────────────────────────────────────────────
def fig2_coverage_matrix():
    frameworks = [
        "F1  Chapelle (2001)",
        "F2  Hubbard (2011)",
        "F3  Leakey (2011)",
        "F4  Colpaert (2004)",
        "F5  Rosell-Aguiar (2017)",
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

    fig = plt.figure(figsize=(12.5, 7.8))
    gs  = GridSpec(1, 2, figure=fig, width_ratios=[5, 1.25], wspace=0.05)
    ax_heat = fig.add_subplot(gs[0])
    ax_bar  = fig.add_subplot(gs[1])

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "cov", ["#ffcdd2", "#fff9c4", "#c8e6c9"], N=256)

    sns.heatmap(matrix, ax=ax_heat, cmap=cmap, vmin=0, vmax=1,
                xticklabels=dims, yticklabels=frameworks,
                linewidths=0.5, linecolor="#eceff1",
                cbar=False, annot=False)

    for r in range(n_f):
        for c in range(n_d):
            sym = symbols[r * n_d + c]
            color = (PALETTE["full"] if sym == "✓"
                     else PALETTE["partial"] if sym == "◑"
                     else PALETTE["absent"])
            ax_heat.text(c + 0.5, r + 0.5, sym,
                         ha="center", va="center",
                         fontsize=14.5, fontweight="bold", color=color)

    ax_heat.set_title(
        "Dimensional Coverage Matrix — 12 Evaluation Frameworks × 5 Dimensions",
        fontsize=11.5, fontweight="bold", color=PALETTE["blue_dark"], pad=14)
    ax_heat.tick_params(axis="x", labelsize=9.5)
    ax_heat.tick_params(axis="y", labelsize=8.5)
    
    for label in ax_heat.get_xticklabels():
        label.set_fontweight("bold")
    ax_heat.set_xlabel("Evaluation Dimension", fontsize=10, labelpad=8)

    y_pos = np.arange(n_f) + 0.5
    colors_bar = [PALETTE["full"] if s >= 2.0
                  else PALETTE["partial"] if s >= 1.0
                  else PALETTE["absent"] for s in scores]
    bars = ax_bar.barh(y_pos, scores, color=colors_bar, height=0.6,
                       edgecolor="white", linewidth=0.8)
    ax_bar.set_xlim(0, 5.5)
    ax_bar.axvline(x=2.5, color=PALETTE["red_dark"], lw=1.5, ls="--", alpha=0.7)
    ax_bar.set_yticks(y_pos)
    ax_bar.set_yticklabels([])
    ax_bar.set_xlabel("Coverage Score /5", fontsize=9.5, labelpad=8)
    ax_bar.set_title("Score", fontsize=10, fontweight="bold",
                     color=PALETTE["blue_dark"], pad=14)
    ax_bar.tick_params(axis="x", labelsize=9)
    ax_bar.set_ylim(n_f, 0)
    
    for bar, s in zip(bars, scores):
        ax_bar.text(s + 0.1, bar.get_y() + bar.get_height() / 2,
                    f"{s:.1f}", va="center", fontsize=8.5, fontweight="bold", color=PALETTE["grey_text"])

    legend_items = [
        mpatches.Patch(color=PALETTE["full"],    label="✓  Full coverage (1.0)"),
        mpatches.Patch(color=PALETTE["partial"], label="◑  Partial (0.5)"),
        mpatches.Patch(color=PALETTE["absent"],  label="✗  Absent (0.0)"),
    ]
    fig.legend(handles=legend_items, loc="lower center", ncol=3,
               fontsize=9.5, frameon=True, framealpha=0.9,
               bbox_to_anchor=(0.5, -0.01))

    fig.text(0.5, -0.05,
             "†D5 Rigor Indicator not shown in heatmap — assessed separately as framework meta-quality, not a coverage dimension.",
             ha="center", fontsize=8, color="#78909c", style="italic")

    fig.subplots_adjust(left=0.22, right=0.96, top=0.88, bottom=0.13)

    path = os.path.join(IMAGES_DIR, "fig2_coverage_matrix_heatmap.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 5 — Coverage Scores Bar Chart (ranked)
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

    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, scores, color=bar_colors, height=0.6,
                   edgecolor="white", linewidth=0.8, alpha=0.88)

    ax.axvline(x=2.5, color=PALETTE["red_dark"], lw=1.5, ls="--",
               label="Max achieved (2.5 / 5.0)")
    ax.axvline(x=5.0, color="#78909c", lw=1.0, ls=":",
               label="Theoretical maximum (5.0)")

    for bar, s in zip(bars, scores):
        ax.text(s + 0.08, bar.get_y() + bar.get_height() / 2,
                f"{s:.1f}", va="center", fontsize=9.5, fontweight="bold", color=PALETTE["grey_text"])

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=9.5)
    ax.set_xlim(0, 5.8)
    ax.set_xlabel("Dimensional Coverage Score (out of 5.0)", fontsize=10, labelpad=8)
    ax.set_title(
        "Coverage Scores Across 12 Evaluation Frameworks\n"
        "(5 Object-Level Dimensions: D1 TECH, D2 PED, D3 INST, D4 High-Stakes, D6 Multi-Stakeholder)",
        fontsize=11.5, fontweight="bold", color=PALETTE["blue_dark"], pad=14)
    ax.invert_yaxis()
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="x", labelsize=9)

    disc_patches = [mpatches.Patch(color=c, label=f"{d} discipline")
                    for d, c in disc_colors.items()]
    all_handles = disc_patches + ax.get_legend_handles_labels()[0]
    ax.legend(handles=all_handles, loc="lower right", fontsize=9,
              frameon=True, framealpha=0.9, ncol=2)

    ax.text(2.58, 0.3, "← Max 50% coverage\n   achieved by any\n   single framework",
            fontsize=8, color=PALETTE["red_dark"], va="top", fontweight="bold")

    fig.tight_layout()
    path = os.path.join(IMAGES_DIR, "fig3_coverage_scores_ranked.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 6 — Four Coverage Gaps Diagram
# ─────────────────────────────────────────────────────────────────────────────
def fig4_coverage_gaps():
    fig, ax = plt.subplots(figsize=(12.5, 7.5))
    ax.set_xlim(0, 12.5)
    ax.set_ylim(0, 7.5)
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

    gaps = [
        # Top-Left
        (0.4, 4.5, 4.1, 2.1,
         "Gap 1: Contextual Specificity\n\n"
         "D4 (High-Stakes Test Specificity)\n"
         "never achieves full coverage\n"
         "(max ◑ across all 12 frameworks)",
         PALETTE["red_light"], PALETTE["absent"]),

        # Top-Right
        (8.0, 4.5, 4.1, 2.1,
         "Gap 2: Disciplinary Silos\n\n"
         "CALL frameworks lack D1 & D3\n"
         "while IS frameworks lack D2\n"
         "domain-specific depth",
         PALETTE["red_light"], PALETTE["absent"]),

        # Bottom-Left
        (0.4, 0.9, 4.1, 2.1,
         "Gap 3: Institutional Blindspot\n\n"
         "D3 (Institutional Governance) only\n"
         "found in LA (F8/F9); absent from\n"
         "all 10 CALL/MALL frameworks",
         PALETTE["red_light"], PALETTE["absent"]),

        # Bottom-Right
        (8.0, 0.9, 4.1, 2.1,
         "Gap 4: Single-Stakeholder Bias\n\n"
         "D6 (Multi-Stakeholder Perspective)\n"
         "never achieves full coverage\n"
         "(max ◑ across all 12 frameworks)",
         PALETTE["red_light"], PALETTE["absent"]),
    ]

    for (x, y, w, h, txt, fc, ec) in gaps:
        rounded_box(ax, x, y, w, h, txt, fc, ec, fontsize=9)

    # ── Central finding box ──────────────────────────────────────────────────
    cx, cy, cw, ch = 4.8, 3.2, 2.9, 1.1
    ax.add_patch(FancyBboxPatch((cx, cy), cw, ch,
                                boxstyle="round,pad=0.2",
                                facecolor=PALETTE["red_dark"],
                                edgecolor="#7f0000",
                                linewidth=2.0, zorder=4))
    ax.text(cx + cw / 2, cy + ch / 2,
            "No single framework\nexceeds 2.5 / 5.0\n(50% maximum coverage\nacross all 12 reviewed)",
            ha="center", va="center", fontsize=9.5, fontweight="bold",
            color="white", zorder=5, multialignment="center")

    # ── Rigor finding box (dashed) ───────────────────────────────────────────
    rx, ry, rw, rh = 3.8, 0.12, 4.9, 0.65
    ax.add_patch(FancyBboxPatch((rx, ry), rw, rh,
                                boxstyle="round,pad=0.15",
                                facecolor=PALETTE["purple_light"],
                                edgecolor=PALETTE["purple_mid"],
                                linewidth=1.5, linestyle="--", zorder=2))
    ax.text(rx + rw / 2, ry + rh / 2,
            "Rigor Finding — D5 (Separate Meta-Quality Indicator)\n"
            "7/12 frameworks: ◑ partial definitions   ·   5/12: ✗ checklist only",
            ha="center", va="center", fontsize=8.5, color=PALETTE["purple_mid"],
            fontweight="bold", zorder=3, multialignment="center")

    # ── Arrows: gaps → central box ───────────────────────────────────────────
    arrow_props = dict(arrowstyle="-|>", color="#c62828", lw=1.8, mutation_scale=12)
    arrow_coords = [
        ((4.5, 4.6), (4.8, 4.0)),        # Gap 1 → Central
        ((8.0, 4.6), (7.7, 4.0)),        # Gap 2 → Central
        ((4.5, 2.9), (4.8, 3.5)),        # Gap 3 → Central
        ((8.0, 2.9), (7.7, 3.5)),        # Gap 4 → Central
    ]
    for (x1, y1), (x2, y2) in arrow_coords:
        arrow = FancyArrowPatch((x1, y1), (x2, y2), **arrow_props, zorder=3)
        ax.add_patch(arrow)

    # ── Dashed arrow: rigor → central box ────────────────────────────────────
    arrow_rigor = FancyArrowPatch(
        (rx + rw / 2, ry + rh), (cx + cw / 2, cy),
        arrowstyle="-|>", color=PALETTE["purple_mid"],
        lw=1.2, linestyle="dashed", mutation_scale=12, zorder=3
    )
    ax.add_patch(arrow_rigor)
    
    ax.text(6.25, 2.0,
            "framework quality finding\n(not a coverage gap)",
            fontsize=8, color=PALETTE["purple_mid"], style="italic",
            ha="center", va="center", fontweight="bold")

    # ── Title ────────────────────────────────────────────────────────────────
    ax.text(6.25, 7.15,
            "Four Systematic Coverage Gaps Identified from Dimensional Analysis",
            ha="center", va="center", fontsize=11.5, fontweight="bold",
            color=PALETTE["blue_dark"])

    path = os.path.join(IMAGES_DIR, "fig4_coverage_gaps_diagram.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 1 — Research Program Architecture (Redesigned Research Workflow)
# ─────────────────────────────────────────────────────────────────────────────
def fig5_research_architecture():
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 6.2)
    ax.axis("off")

    def card(ax, x, y, w, h, title, lines, facecolor, edgecolor):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                   boxstyle="round,pad=0.2",
                                   facecolor=facecolor,
                                   edgecolor=edgecolor,
                                   linewidth=2.0, zorder=2))
        # Title band
        ax.add_patch(FancyBboxPatch((x + 0.05, y + h - 0.65), w - 0.1, 0.6,
                                   boxstyle="round,pad=0.05",
                                   facecolor=edgecolor, edgecolor="none", zorder=3))
        ax.text(x + w / 2, y + h - 0.35,
                title, ha="center", va="center",
                fontsize=9.5, fontweight="bold", color="white", zorder=4)
        for i, line in enumerate(lines):
            # Check if this line is a separator
            if line.startswith("───"):
                ax.text(x + w / 2, y + h - 1.0 - i * 0.45,
                        line, ha="center", va="center", fontsize=8.0,
                        color="#b0bec5", zorder=3)
            else:
                ax.text(x + 0.25, y + h - 1.0 - i * 0.45,
                        line, va="center", fontsize=8.5,
                        color=PALETTE["grey_text"], zorder=3)

    lines_col1 = [
        "• Context: HE language platforms",
        "• Search Protocol: PRISMA-ScR",
        "• Sources: Scopus, WoS, IEEE, ERIC",
        "• Selection Criteria: CALL / MALL / LMS",
        "─────────────────────────────────",
        "• Output: Literature Dataset & Matrix",
        "  (12 landmark frameworks mapped",
        "  across 5 analytical dimensions)"
    ]

    lines_col2 = [
        "• Phase 1-5: Concept Extraction &",
        "  Deconstruction (Washback, TAM, SLA)",
        "• Phase 6: Multi-disciplinary Synthesis",
        "• Meta-Theory: DeLone & McLean Success",
        "─────────────────────────────────",
        "• Output: Proposed Framework F*",
        "  (15 operational criteria resolving",
        "  pedagogical & technical gaps)"
    ]

    lines_col3 = [
        "• Layer 1: Theoretical Completeness",
        "  (Coverage matrix cross-validation)",
        "• Layer 2: Mathematical Necessity",
        "  (Convex combination bound LP proof)",
        "• Layer 3: Computational Robustness",
        "  (Monte Carlo sensitivity under MAUT",
        "  complexity & failure constraints)",
        "─────────────────────────────────",
        "• Output: Validated Evaluation Model"
    ]

    card(ax, 0.4, 0.7, 3.2, 4.8,
         "I. Integrative Review & Dataset",
         lines_col1,
         PALETTE["blue_light"], PALETTE["blue_mid"])

    card(ax, 4.15, 0.7, 3.2, 4.8,
         "II. Conceptual Synthesis (CFA)",
         lines_col2,
         PALETTE["purple_light"], PALETTE["purple_mid"])

    card(ax, 7.9, 0.7, 3.2, 4.8,
         "III. Design Science Validation",
         lines_col3,
         PALETTE["green_light"], PALETTE["green_mid"])

    arrow_props = dict(arrowstyle="-|>", color=PALETTE["grey_text"], lw=2.0, mutation_scale=15)
    
    arrow1 = FancyArrowPatch((3.65, 3.1), (4.1, 3.1), **arrow_props, zorder=4)
    ax.add_patch(arrow1)
    
    arrow2 = FancyArrowPatch((7.4, 3.1), (7.85, 3.1), **arrow_props, zorder=4)
    ax.add_patch(arrow2)

    # Title
    ax.text(5.75, 5.85,
            "Research Program Workflow and Methodological Framework",
            ha="center", va="center", fontsize=12, fontweight="bold",
            color=PALETTE["blue_dark"])

    # Footer
    ax.text(5.75, 0.25,
            "Sequential logical flow from empirical literature data collection (Stage I), through concept synthesis (Stage II), to multi-layer artifact validation (Stage III)",
            ha="center", va="center", fontsize=8.5,
            color=PALETTE["grey_text"], style="italic")

    path = os.path.join(IMAGES_DIR, "fig5_research_program_architecture.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"  ✓  {path}")


# ─────────────────────────────────────────────────────────────────────────────
# FIG 3 — PCC Framework & Analytical Dimensions (Supplementary)
# ─────────────────────────────────────────────────────────────────────────────
def fig6_pcc_and_dimensions():
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 6.2))
    fig.suptitle(
        "Methodological Framework: PCC Scoping Review Design & Analytical Dimensions",
        fontsize=11.5, fontweight="bold", color=PALETTE["blue_dark"], y=0.98)

    # ── Left: PCC table ──────────────────────────────────────────────────────
    ax = axes[0]
    ax.axis("off")
    ax.set_title("PCC Framework (Munn et al., 2018)", fontsize=10.5,
                 fontweight="bold", color=PALETTE["blue_dark"], pad=14)

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

    y_tops = [0.74, 0.44, 0.14]
    for i, (elem, defn) in enumerate(pcc_data):
        y_top = y_tops[i]
        ax.add_patch(FancyBboxPatch((0.02, y_top - 0.05), 0.19, 0.13,
                                   boxstyle="round,pad=0.02",
                                   transform=ax.transAxes,
                                   facecolor=colors_pcc[i], edgecolor="none",
                                   zorder=2, clip_on=False))
        ax.text(0.115, y_top + 0.015, elem,
                ha="center", va="center", fontsize=10, fontweight="bold",
                color="white", transform=ax.transAxes, zorder=3)
        ax.text(0.24, y_top + 0.015, defn,
                ha="left", va="center", fontsize=9,
                color=PALETTE["grey_text"], transform=ax.transAxes)
        if i < 2:
            ax.plot([0.02, 0.98], [y_top - 0.08, y_top - 0.08],
                    color="#cfd8dc", lw=0.8, transform=ax.transAxes)

    # ── Right: Analytical dimensions ─────────────────────────────────────────
    ax2 = axes[1]
    ax2.axis("off")
    ax2.set_title("Analytical Dimensions & Theoretical Grounding",
                  fontsize=10.5, fontweight="bold", color=PALETTE["blue_dark"], pad=14)

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

    y_pos_dims = [0.84, 0.69, 0.54, 0.39, 0.24, 0.09]
    for i, (code, name, source, color) in enumerate(dims_data):
        y = y_pos_dims[i]
        dashed = (code == "D5†")
        ax2.add_patch(FancyBboxPatch((0.01, y - 0.045), 0.11, 0.09,
                                    boxstyle="round,pad=0.02",
                                    transform=ax2.transAxes,
                                    facecolor=color, edgecolor="none",
                                    zorder=2, clip_on=False,
                                    alpha=0.6 if dashed else 1.0))
        ax2.text(0.065, y, code,
                 ha="center", va="center", fontsize=10, fontweight="bold",
                 color="white", transform=ax2.transAxes, zorder=3)
        ax2.text(0.15, y + 0.022, name,
                 ha="left", va="center", fontsize=9.5, fontweight="bold",
                 color=color, transform=ax2.transAxes,
                 style="italic" if dashed else "normal")
        ax2.text(0.15, y - 0.022, source,
                 ha="left", va="center", fontsize=8,
                 color=PALETTE["grey_text"], transform=ax2.transAxes)
        if i < len(dims_data) - 1:
            ax2.plot([0.01, 0.99], [y - 0.065, y - 0.065],
                     color="#cfd8dc", lw=0.6, ls="--" if i == 4 else "-",
                     transform=ax2.transAxes)

    ax2.text(0.5, -0.05,
             "†D5 is a framework meta-quality indicator — not counted in coverage score.",
             ha="center", va="center", fontsize=8.5, color="#78909c",
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
    print(f"\nGenerating figures -> {IMAGES_DIR}\n")
    fig1_scoping_stages()
    fig2_coverage_matrix()
    fig3_coverage_scores()
    fig4_coverage_gaps()
    fig5_research_architecture()
    fig6_pcc_and_dimensions()
    print("\nAll figures generated successfully.")
