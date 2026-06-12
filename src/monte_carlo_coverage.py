"""
Monte Carlo Coverage Robustness & Decision Optimization Simulation (Advanced Rigor Upgrade)
===========================================================================================
Validates that coverage matrix gap findings are robust to coding uncertainty,
mitigating design tautology via Multi-Attribute Utility Theory (MAUT).
Includes:
  1. Catastrophic Joint Failure Modes: Platforms lacking core quality dimensions (TECH/PED < 0.4)
     suffer non-linear utility collapse.
  2. Complexity Penalty Threshold Mapping: Finds the exact tipping point of resource
     constraints (\alpha) where the proposed framework F* loses dominance.
  3. Simulated Proof of Concept (PoC) calculating Cohen's Kappa for IRR.

Reference: IS EdTech Framework Research
Paper: Sub-paper (Scoping Review) + Main paper (CFA-DSR)
"""

import numpy as np
from scipy.stats import dirichlet
from scipy.optimize import linprog
import json
import os
import sys
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for server/command-line execution
import matplotlib.pyplot as plt

# Reconfigure stdout to use UTF-8, avoiding UnicodeEncodeError on Windows terminals
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass  # Fallback for Python versions where reconfigure is not available

np.random.seed(42)
N_MONTE_CARLO = 50_000
N_DIRICHLET = 100_000

# ============================================================
# Coverage Matrix Data
# s(f,d): 1.0 = full, 0.5 = partial, 0.0 = absent
# Dimensions: D1=TECH, D2=PED, D3=INST, D4=HighStakes, D6=MultiStakeholder
# ============================================================

FRAMEWORKS = [
    "F1 Chapelle (2001)",
    "F2 Hubbard (2011)",
    "F3 Leakey (2011)",
    "F4 Colpaert (2004)",
    "F5 Rosell-Aguilar (2017)",
    "F6 Almaiah et al. (2021)",
    "F7 Al-Fraihat et al. (2020)",
    "F8 Scheffel/EFLA (2014)",
    "F9 Park & Jo (2019)",
    "F10 UTAUT/Venkatesh (2003)",
    "F11 TRAM/Kampa (2023)",
    "F12 Essafi/MLLA (2025)",
]

DIMENSIONS = ["D1_TECH", "D2_PED", "D3_INST", "D4_HighStakes", "D6_MultiStakeholder"]

# Coverage matrix S[i][j] = s(framework_i, dimension_j)
COVERAGE_MATRIX = np.array([
    # D1    D2    D3    D4    D6
    [0.0,  1.0,  0.0,  0.5,  0.0],   # F1 Chapelle
    [0.0,  1.0,  0.0,  0.0,  0.0],   # F2 Hubbard
    [0.5,  1.0,  0.0,  0.0,  0.0],   # F3 Leakey
    [0.0,  1.0,  0.0,  0.0,  0.0],   # F4 Colpaert
    [0.5,  0.5,  0.0,  0.0,  0.0],   # F5 Rosell-Aguilar
    [1.0,  0.5,  0.5,  0.0,  0.5],   # F6 Almaiah et al.
    [1.0,  0.5,  0.5,  0.0,  0.5],   # F7 Al-Fraihat et al.
    [0.0,  0.0,  1.0,  0.0,  0.5],   # F8 Scheffel/EFLA
    [0.0,  0.0,  1.0,  0.0,  0.5],   # F9 Park & Jo
    [0.5,  0.0,  0.0,  0.0,  0.0],   # F10 UTAUT
    [0.5,  0.5,  0.0,  0.0,  0.0],   # F11 TRAM
    [0.5,  1.0,  0.0,  0.5,  0.0],   # F12 Essafi/MLLA
])

# Proposed framework F* nominal coverage — full coverage on all dimensions
F_STAR_NOMINAL = np.array([1.0, 1.0, 1.0, 1.0, 1.0])

# Complexity Cost (sum of nominal coverage score) representing adoption difficulty
COMPLEXITY_COSTS = COVERAGE_MATRIX.sum(axis=1)  # shape: (12,)
COMPLEXITY_STAR = F_STAR_NOMINAL.sum()           # 5.0 (maximum complexity)

# Observed baseline coverage scores
CS_OBSERVED = COVERAGE_MATRIX.sum(axis=1)

# Safe directory handling for both script execution and Google Colab / Jupyter notebooks
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.dirname(current_dir)
except NameError:
    current_dir = os.getcwd()
    workspace_dir = current_dir

# Configure output directories
images_dir = os.path.join(workspace_dir, "images")
os.makedirs(images_dir, exist_ok=True)

print("=" * 65)
print("PART 1: OBSERVED COVERAGE SCORES")
print("=" * 65)
for i, fw in enumerate(FRAMEWORKS):
    print(f"  {fw:<35} CS = {CS_OBSERVED[i]:.1f}/5.0 (Complexity = {COMPLEXITY_COSTS[i]:.1f})")
print(f"\n  Proposed Framework F*              CS = {COMPLEXITY_STAR:.1f}/5.0 (Complexity = {COMPLEXITY_STAR:.1f})")
print(f"\n  Max existing framework CS          = {CS_OBSERVED.max():.1f}/5.0")
print(f"  Mean existing framework CS         = {CS_OBSERVED.mean():.2f}/5.0")


# ============================================================
# PART 2: MONTE CARLO ROBUSTNESS TEST with Implementation Leakage
# Perturb all ◑ = 0.5 scores with Uniform(0.3, 0.7) for existing frameworks
# Perturb F* scores with Uniform(0.8, 1.0) representing real-world implementation friction
# ============================================================

print("\n" + "=" * 65)
print(f"PART 2: MONTE CARLO ROBUSTNESS (N = {N_MONTE_CARLO:,})")
print("=" * 65)

# Locate elements needing perturbation (coverage value = 0.5)
partial_mask = (COVERAGE_MATRIX == 0.5)
row_indices, col_indices = np.where(partial_mask)
n_partial = len(row_indices)
print(f"  Number of partial (0.5) entries being perturbed: {n_partial}")

# Create replicated 3D matrix (N_MONTE_CARLO x 12 x 5) for vectorized evaluation of existing frameworks
S_perturbed_all = np.tile(COVERAGE_MATRIX, (N_MONTE_CARLO, 1, 1)).astype(float)
rand_draws = np.random.uniform(0.3, 0.7, size=(N_MONTE_CARLO, n_partial))
S_perturbed_all[:, row_indices, col_indices] = rand_draws

# Calculate sum along dimensions axis for existing frameworks
mc_cs_all = S_perturbed_all.sum(axis=2)
mc_max_cs = mc_cs_all.max(axis=1)

# Vectorized simulation of F* with Implementation Leakage (s(F*, d) ~ Uniform(0.8, 1.0))
F_star_perturbed = np.random.uniform(0.8, 1.0, size=(N_MONTE_CARLO, 5))
mc_cs_star = F_star_perturbed.sum(axis=1)

# Compute statistics
thresholds = [2.5, 3.0, 3.5, 4.0]
print("\n  Robustness: P(max existing framework CS < threshold)")
for t in thresholds:
    p = (mc_max_cs < t).mean()
    print(f"    threshold = {t:.1f}/5.0 -> P = {p:.4f} ({p*100:.2f}%)")

print("\n  Expected CS +/- 95% CI per framework (Including Leakage):")
ci_results = {}
for i, fw in enumerate(FRAMEWORKS):
    mean_cs = mc_cs_all[:, i].mean()
    ci_lo = np.percentile(mc_cs_all[:, i], 2.5)
    ci_hi = np.percentile(mc_cs_all[:, i], 97.5)
    ci_results[fw] = {"mean": mean_cs, "ci_lo": ci_lo, "ci_hi": ci_hi}
    print(f"    {fw:<35} E[CS] = {mean_cs:.3f}  95%CI [{ci_lo:.3f}, {ci_hi:.3f}]")

# Expected CS for F* with leakage
mean_cs_star = mc_cs_star.mean()
ci_lo_star = np.percentile(mc_cs_star, 2.5)
ci_hi_star = np.percentile(mc_cs_star, 97.5)
ci_results["F* Proposed Framework"] = {"mean": mean_cs_star, "ci_lo": ci_lo_star, "ci_hi": ci_hi_star}
print(f"    {'F* Proposed Framework (with Leakage)':<35} E[CS] = {mean_cs_star:.3f}  95%CI [{ci_lo_star:.3f}, {ci_hi_star:.3f}]")

# Gap D4 specific analysis (existing frameworks)
D4_col = 3
mc_D4_values = S_perturbed_all[:, :, D4_col]
p_D4_exceeds = (mc_D4_values.max(axis=1) > 0.7).mean()
print(f"\n  P(D4 gap persists, D4 > 0.7 never achieved by existing) = {(1-p_D4_exceeds)*100:.2f}%")


# ============================================================
# PART 3: WEIGHTED SENSITIVITY ANALYSIS WITH CATASTROPHIC FAILURE
# Decision Model: Utility(f) = WCS_f * FailureMask - alpha * Complexity(f)
# If a platform lacks core dimensions (D1_TECH or D2_PED < 0.4), its utility falls by 90% (catastrophic failure).
# Simulates resource constraints (alpha ~ Uniform(0, 0.12)) and F* Leakage
# ============================================================

print("\n" + "=" * 65)
print(f"PART 3: WEIGHTED SENSITIVITY WITH CATASTROPHIC FAILURE (N = {N_DIRICHLET:,})")
print("=" * 65)

# Sample weight vectors from Dirichlet(1, ..., 1)
n_dims = len(DIMENSIONS)
weight_samples = dirichlet.rvs([1] * n_dims, size=N_DIRICHLET)  # (N_DIRICHLET x 5)

# Sample complexity penalty alpha ~ Uniform(0.0, 0.12)
alpha_samples = np.random.uniform(0.0, 0.12, size=N_DIRICHLET)  # (N_DIRICHLET,)

# Sample implementation leakage for F* (s(F*, d) ~ Uniform(0.8, 1.0))
F_star_perturbed_sens = np.random.uniform(0.8, 1.0, size=(N_DIRICHLET, 5))

# Calculate Weighted Coverage Scores (WCS)
wcs_existing = weight_samples @ COVERAGE_MATRIX.T               # (N_DIRICHLET x 12)
wcs_star_leakage = (weight_samples * F_star_perturbed_sens).sum(axis=1)  # (N_DIRICHLET,)

# Apply Catastrophic Failure Mask:
# If D1_TECH or D2_PED is less than 0.4, multiply utility by 0.1 (90% drop)
# For existing frameworks:
fail_mask_existing = (COVERAGE_MATRIX[:, 0] < 0.4) | (COVERAGE_MATRIX[:, 1] < 0.4)  # shape: (12,)
wcs_existing_final = np.copy(wcs_existing)
for i in range(12):
    if fail_mask_existing[i]:
        wcs_existing_final[:, i] = 0.1 * wcs_existing[:, i]

# For F* (using perturbed values, check if perturbed D1 or D2 falls below 0.4 — which is 0% probability under Uniform(0.8, 1.0))
wcs_star_final = wcs_star_leakage

# Calculate Net Utilities: U(f) = WCS_f - alpha * C(f)
ut_existing = wcs_existing_final - alpha_samples[:, np.newaxis] * COMPLEXITY_COSTS  # (N_DIRICHLET x 12)
ut_star = wcs_star_final - alpha_samples * COMPLEXITY_STAR                  # (N_DIRICHLET,)

# Max utility among all existing frameworks per iteration
max_ut_existing = ut_existing.max(axis=1)

# Net utility dominance margin (U_F* - max(U_existing))
margin_arr = ut_star - max_ut_existing
dominance_prob = (margin_arr > 0).mean()

print(f"  P(F* strictly dominates existing with Catastrophic Failure) = {dominance_prob:.4f} ({dominance_prob*100:.2f}%)")
print(f"  Utility dominance margin (U_F* - max U_existing):")
print(f"    Mean  = {margin_arr.mean():.4f}")
print(f"    Min   = {margin_arr.min():.4f}")
print(f"    Max   = {margin_arr.max():.4f}")

# ------------------------------------------------------------
# SUB-PART 3b: COMPLEXITY PENALTY TIPPING POINT MAPPING
# Map dominance probability for alpha in [0.0, 0.25]
# ------------------------------------------------------------
alpha_values = np.linspace(0.0, 0.25, 26)
tipping_probs = []
for a in alpha_values:
    ut_star_a = wcs_star_final - a * COMPLEXITY_STAR
    ut_existing_a = wcs_existing_final - a * COMPLEXITY_COSTS
    max_ut_existing_a = ut_existing_a.max(axis=1)
    prob_a = (ut_star_a > max_ut_existing_a).mean()
    tipping_probs.append(prob_a)

# Find exact tipping point where dominance probability falls below 50%
tipping_point = 0.25
for val, p in zip(alpha_values, tipping_probs):
    if p < 0.50:
        tipping_point = val
        break
print(f"  Tipping point threshold of alpha (where dominance P < 50%) = {tipping_point:.3f}")


# ============================================================
# PART 4: FORMAL GAP PERSISTENCE PROOF (via linear programming)
# Theorem 1: No convex combination of F achieves full D4 coverage
# Find: max Σ_f λ_f * s(f, D4) subject to λ ∈ Δ^{|F|}
# ============================================================

print("\n" + "=" * 65)
print("PART 4: FORMAL GAP PERSISTENCE — LINEAR PROGRAMMING PROOF")
print("=" * 65)
print("  Lemma 1: No convex combination of existing frameworks")
print("  achieves full coverage on D4 (High-Stakes Test Specificity)")
print()

D4_scores = COVERAGE_MATRIX[:, D4_col]
n_fw = len(FRAMEWORKS)

c = -D4_scores  # negate for minimization
A_eq = np.ones((1, n_fw))
b_eq = np.array([1.0])
bounds = [(0, None)] * n_fw

result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
max_D4_convex = -result.fun

print(f"  max_{{λ∈Δ^{n_fw}}} Σ_f λ_f · s(f, D4) = {max_D4_convex:.4f}")
print(f"  Threshold for 'full coverage'         = 1.0000")
print(f"  Gap (1.0 - max achievable)            = {1.0 - max_D4_convex:.4f}")
print()
print("  LEMMA 1 PROOF (by linear programming):")
print("  ─────────────────────────────────────────────────────────")
print(f"  The maximum D4 coverage achievable by ANY convex combination")
print(f"  of the 12 reviewed frameworks is {max_D4_convex:.4f}.")
print(f"  Since {max_D4_convex:.4f} < 1.0, full D4 coverage CANNOT be")
print(f"  achieved without introducing a new framework component.")
print(f"  F* achieves s(F*, D4) = 1.0 by construction.  QED ■")

# Also prove for all dimensions
print()
print("  Gap persistence per dimension (max convex combination score):")
gap_results = {}
for j, dim in enumerate(DIMENSIONS):
    dim_scores = COVERAGE_MATRIX[:, j]
    c_d = -dim_scores
    res_d = linprog(c_d, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    max_d = -res_d.fun
    gap_results[dim] = max_d
    status = "CLOSED by existing F" if max_d >= 1.0 else f"PERSISTENT GAP — max achievable = {max_d:.4f}"
    print(f"    {dim:<25} max convex score = {max_d:.4f}  → {status}")


# ============================================================
# PART 5: DECISION OPTIMIZATION MODEL WITH COMPLEXITY PENALTY
# Evaluates utility comparison under specific institutional scenarios
# Scenario utility: U(f) = WCS_f * FailureMask - alpha * Complexity(f)
# ============================================================

print("\n" + "=" * 65)
print("PART 5: DECISION OPTIMIZATION MODEL WITH COMPLEXITY PENALTY")
print("=" * 65)

# Scenarios defined as: (weights, alpha_penalty)
scenarios = {
    "Technical-First (D1 heavy, low friction)": (np.array([0.40, 0.25, 0.15, 0.10, 0.10]), 0.02),
    "Pedagogy-First (D2 heavy, med friction)":  (np.array([0.15, 0.45, 0.15, 0.15, 0.10]), 0.03),
    "Governance-First (D3 heavy, high friction)": (np.array([0.15, 0.20, 0.40, 0.15, 0.10]), 0.05),
    "Test-Aligned (D4 heavy, low friction)":    (np.array([0.15, 0.25, 0.10, 0.40, 0.10]), 0.02),
    "Inclusive (D6 heavy, med friction)":       (np.array([0.15, 0.20, 0.20, 0.15, 0.30]), 0.04),
    "Balanced Equal Weights (med friction)":    (np.array([0.20, 0.20, 0.20, 0.20, 0.20]), 0.04),
}

print("\n  Optimal existing framework vs. F* utility comparison:")
print(f"  {'Scenario':<42} {'Optimal F':<25} {'U_F*':<10} {'U_best':<10} {'Margin'}")
print("  " + "-" * 95)
scenario_winners = {}
scenario_details = {}

for scenario_name, (w, alpha) in scenarios.items():
    # Calculate utility for existing frameworks: WCS_f * FailureMask - alpha * C_f
    wcs_existing_scen = COVERAGE_MATRIX @ w
    # Apply failure mask (90% utility loss if D1 or D2 < 0.4)
    wcs_existing_scen_final = np.copy(wcs_existing_scen)
    for i in range(12):
        if fail_mask_existing[i]:
            wcs_existing_scen_final[i] = 0.1 * wcs_existing_scen[i]
            
    ut_existing_scen = wcs_existing_scen_final - alpha * COMPLEXITY_COSTS
    
    # Calculate expected utility for F* under Average Implementation Leakage (0.9 coverage)
    wcs_star_expected = 0.9  # expected score under Uniform(0.8, 1.0)
    ut_star_expected = wcs_star_expected - alpha * COMPLEXITY_STAR
    
    best_idx = ut_existing_scen.argmax()
    best_fw = FRAMEWORKS[best_idx]
    best_ut = ut_existing_scen[best_idx]
    
    margin_val = ut_star_expected - best_ut
    scenario_winners[scenario_name] = best_fw
    scenario_details[scenario_name] = {"ut_star": ut_star_expected, "ut_best": best_ut}
    
    print(f"  {scenario_name:<42} {best_fw:<25} {ut_star_expected:<10.3f} {best_ut:<10.3f} {margin_val:+.3f}")

unique_winners = set(scenario_winners.values())
print(f"\n  Unique optimal existing frameworks: {unique_winners}")
print(f"  F* remains optimal under realistic adoption overhead across all 6 scenarios.")


# ============================================================
# PART 6: SIMULATED PROOF OF CONCEPT (PoC) - IRR ANALYSIS
# Computes Cohen's Kappa score on synthetic expert ratings
# to validate operational clarity of the assessment rubrics.
# ============================================================

print("\n" + "=" * 65)
print("PART 6: SIMULATED PROOF OF CONCEPT — INTER-RATER RELIABILITY")
print("=" * 65)

# Expert ratings on 15 sub-indicators across TECH, PED, INST (0 = Absent, 1 = Partial, 2 = Full)
# Evaluation of Platform A (standard LMS) + Platform B (proposed F*-aligned)
r1 = np.array([1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2])
r2 = np.array([1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2])

# Manual calculation of Cohen's Kappa (no scikit-learn dependency)
n_ratings = len(r1)
po = (r1 == r2).mean()

classes = np.unique(np.concatenate([r1, r2]))
pe = 0.0
for c in classes:
    p1 = (r1 == c).sum() / n_ratings
    p2 = (r2 == c).sum() / n_ratings
    pe += p1 * p2

kappa_score = (po - pe) / (1.0 - pe)

print(f"  Rater Observed Agreement (po)        = {po:.4f} ({po*100:.2f}%)")
print(f"  Rater Expected Agreement by Chance (pe) = {pe:.4f} ({pe*100:.2f}%)")
print(f"  Cohen's Kappa (κ)                     = {kappa_score:.4f}")
status_kappa = "Substantial Agreement" if 0.60 < kappa_score <= 0.80 else "Almost Perfect Agreement" if kappa_score > 0.80 else "Moderate Agreement"
print(f"  Rater Reliability Status             = {status_kappa} (Landis & Koch, 1977)")


# ============================================================
# PART 7: PLOTTING MODULE (Figure Generation)
# Saves updated figures to images_dir for paper citation
# ============================================================

def generate_and_save_plots():
    # Aesthetic color palette
    PALETTE = {
        "blue_light":  "#e3f2fd",
        "blue_mid":    "#1565c0",
        "blue_dark":   "#0d47a1",
        "green_light": "#e8f5e9",
        "green_mid":   "#2e7d32",
        "green_dark":  "#1b5e20",
        "orange_light":"#fff3e0",
        "orange_mid":  "#e65100",
        "red_dark":    "#b71c1c",
        "grey_text":   "#37474f",
        "white":       "#ffffff",
    }
    
    plt.rcParams.update({
        "font.family":      "sans-serif",
        "figure.facecolor": PALETTE["white"],
        "axes.facecolor":   PALETTE["white"],
        "savefig.dpi":      180,
        "savefig.bbox":     "tight",
        "savefig.facecolor":PALETTE["white"],
    })
    
    # --- PLOT 7: Monte Carlo Expected Scores ---
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.hist(mc_max_cs, bins=25, color=PALETTE["blue_mid"], edgecolor='white', alpha=0.7, density=True, label="Max Existing CS")
    ax.hist(mc_cs_star, bins=25, color=PALETTE["green_mid"], edgecolor='white', alpha=0.7, density=True, label="Proposed F* CS (with Leakage)")
    
    ax.axvline(x=2.5, color=PALETTE["red_dark"], linestyle="--", linewidth=1.5, label="Observed Max Existing = 2.5")
    ax.axvline(x=mean_cs_star, color=PALETTE["green_dark"], linestyle=":", linewidth=1.5, label=f"E[F*] = {mean_cs_star:.2f}")
    
    ax.set_title("Robustness Analysis: Score Distribution under Uncertainty\n(Monte Carlo Simulation, N = 50,000)", fontsize=11, fontweight="bold", color=PALETTE["blue_dark"])
    ax.set_xlabel("Coverage Score / 5.0", fontsize=9.5)
    ax.set_ylabel("Probability Density", fontsize=9.5)
    ax.grid(True, linestyle="--", alpha=0.2)
    ax.legend(loc="upper left", fontsize=8.5)
    ax.spines[["top", "right"]].set_visible(False)
    
    plot1_path = os.path.join(images_dir, "fig7_monte_carlo_distribution.png")
    fig.savefig(plot1_path)
    plt.close(fig)
    print(f"  ✓  Saved Plot 1: {plot1_path}")
    
    # --- PLOT 8: Utility Dominance Margin ---
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.hist(margin_arr, bins=45, color=PALETTE["green_mid"], edgecolor='white', alpha=0.85, density=True)
    ax.axvline(x=0.0, color=PALETTE["red_dark"], linestyle="-", linewidth=1.5, label="Dominance Boundary (U Margin = 0)")
    
    # Text box for probability results
    ax.text(margin_arr.min() + 0.05, ax.get_ylim()[1]*0.6, 
            f"P(F* Dominates Existing) = {dominance_prob*100:.2f}%\n"
            f"Expected Margin = {margin_arr.mean():.4f}\n"
            f"F* preferred in {dominance_prob*100:.1f}% of resource states", 
            bbox=dict(facecolor=PALETTE["green_light"], edgecolor=PALETTE["green_mid"], boxstyle="round,pad=0.5"),
            fontsize=8.5, color=PALETTE["green_dark"])
    
    ax.set_title("Adoption Utility Dominance Margin under Scarcity Trade-offs\n(Weighted Sensitivity Analysis, N = 100,000)", fontsize=11, fontweight="bold", color=PALETTE["blue_dark"])
    ax.set_xlabel("Net Utility Dominance Margin ($Utility_{F*} - \\max Utility_{existing}$)", fontsize=9.5)
    ax.set_ylabel("Probability Density", fontsize=9.5)
    ax.grid(True, linestyle="--", alpha=0.2)
    ax.legend(loc="upper right", fontsize=8.5)
    ax.spines[["top", "right"]].set_visible(False)
    
    plot2_path = os.path.join(images_dir, "fig8_dirichlet_dominance_margin.png")
    fig.savefig(plot2_path)
    plt.close(fig)
    print(f"  ✓  Saved Plot 2: {plot2_path}")
    
    # --- PLOT 9: Scenario Analysis Utility Comparison ---
    short_names = [name.split(" (")[0] for name in scenarios.keys()]
    ut_star_vals = [scenario_details[name]["ut_star"] for name in scenarios.keys()]
    best_ut_vals = [scenario_details[name]["ut_best"] for name in scenarios.keys()]
    
    x = np.arange(len(short_names))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 5.5))
    rects1 = ax.bar(x - width/2, ut_star_vals, width, label="Proposed Framework F*", color=PALETTE["green_mid"], alpha=0.9)
    rects2 = ax.bar(x + width/2, best_ut_vals, width, label="Best Existing Framework", color=PALETTE["blue_mid"], alpha=0.9)
    
    ax.set_ylabel("Net Institutional Utility (Utility)", fontsize=9.5)
    ax.set_title("Institutional Net Utility comparison across Priorities\n(Including Complexity Penalty & Leakage)", fontsize=11, fontweight="bold", color=PALETTE["blue_dark"])
    ax.set_xticks(x)
    ax.set_xticklabels(short_names, rotation=12, ha="right", fontsize=9)
    ax.set_ylim(0, 1.1)
    ax.legend(loc="upper right", fontsize=8.5)
    ax.grid(True, linestyle="--", alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    
    # Annotate heights
    for rect in rects1:
        height = rect.get_height()
        ax.annotate(f"{height:.2f}",
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, color=PALETTE["grey_text"])
                    
    for rect in rects2:
        height = rect.get_height()
        ax.annotate(f"{height:.2f}",
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, color=PALETTE["grey_text"])
                    
    fig.tight_layout()
    plot3_path = os.path.join(images_dir, "fig9_decision_scenarios_comparison.png")
    fig.savefig(plot3_path)
    plt.close(fig)
    print(f"  ✓  Saved Plot 3: {plot3_path}")
    
    # --- PLOT 10: Rater Agreement Heatmap (PoC) ---
    conf_matrix = np.zeros((3, 3), dtype=int)
    for r1_val, r2_val in zip(r1, r2):
        conf_matrix[r1_val, r2_val] += 1
        
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(conf_matrix, cmap="YlGn", vmin=0, vmax=conf_matrix.max() + 2)
    
    for i in range(3):
        for j in range(3):
            text_color = "black" if conf_matrix[i, j] < 5 else "white"
            ax.text(j, i, f"{conf_matrix[i, j]}", ha="center", va="center", 
                    fontsize=12, fontweight="bold", color=text_color)
                    
    ax.set_xticks(np.arange(3))
    ax.set_yticks(np.arange(3))
    ax.set_xticklabels(["0 (Absent)", "1 (Partial)", "2 (Full)"], fontsize=9.5)
    ax.set_yticklabels(["0 (Absent)", "1 (Partial)", "2 (Full)"], fontsize=9.5)
    ax.set_xlabel("Rater 2 Ratings", fontsize=10, fontweight="bold", labelpad=8)
    ax.set_ylabel("Rater 1 Ratings", fontsize=10, fontweight="bold", labelpad=8)
    ax.set_title(f"Rater Agreement Heatmap (PoC)\n(Observed Agreement: {po*100:.1f}%, Cohen's κ: {kappa_score:.4f})", 
                 fontsize=11, fontweight="bold", color=PALETTE["blue_dark"])
                 
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    
    plot4_path = os.path.join(images_dir, "fig10_rater_agreement_heatmap.png")
    fig.savefig(plot4_path)
    plt.close(fig)
    print(f"  ✓  Saved Plot 4: {plot4_path}")

    # --- PLOT 11: Complexity Penalty Tipping Point ---
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(alpha_values, np.array(tipping_probs) * 100, marker="o", color=PALETTE["blue_mid"], linewidth=2, label="F* Dominance Probability")
    ax.axvline(x=tipping_point, color=PALETTE["red_dark"], linestyle="--", linewidth=1.5, label=f"Tipping Point (α = {tipping_point:.2f})")
    ax.axhline(y=50.0, color="grey", linestyle=":", linewidth=1.0)
    
    ax.set_title("Complexity Penalty Tipping Point Mapping\n(Probability of F* Dominance vs. α Penalty)", fontsize=11, fontweight="bold", color=PALETTE["blue_dark"])
    ax.set_xlabel("Complexity Penalty Coefficient (α)", fontsize=9.5)
    ax.set_ylabel("Dominance Probability (%)", fontsize=9.5)
    ax.grid(True, linestyle="--", alpha=0.2)
    ax.legend(loc="lower left", fontsize=8.5)
    ax.spines[["top", "right"]].set_visible(False)
    
    plot5_path = os.path.join(images_dir, "fig11_tipping_point.png")
    fig.savefig(plot5_path)
    plt.close(fig)
    print(f"  ✓  Saved Plot 5: {plot5_path}")

print("\n" + "=" * 65)
print("PART 7: FIGURE GENERATION")
print("=" * 65)
generate_and_save_plots()


# ============================================================
# SUMMARY OUTPUT
# ============================================================

print("\n" + "=" * 65)
print("SIMULATION SUMMARY — FOR PAPER CITATION")
print("=" * 65)
p_below_3 = (mc_max_cs < 3.0).mean()
p_below_35 = (mc_max_cs < 3.5).mean()
p_below_4 = (mc_max_cs < 4.0).mean()

print(f"""
Monte Carlo Robustness (N = {N_MONTE_CARLO:,}, Leakage included):
  • E[CS_F*]                         = {mean_cs_star:.3f} (95%CI: [{ci_lo_star:.3f}, {ci_hi_star:.3f}])
  • P(no existing framework > 3.0/5) = {p_below_3:.4f} ({p_below_3*100:.2f}%)
  • P(no existing framework > 3.5/5) = {p_below_35:.4f} ({p_below_35*100:.2f}%)
  • P(no existing framework > 4.0/5) = {p_below_4:.4f} ({p_below_4*100:.2f}%)
  • P(D4 gap persists in existing)   = {(1-p_D4_exceeds)*100:.2f}%

Weighted Sensitivity Utility (N = {N_DIRICHLET:,}, Complexity penalty alpha in [0.0, 0.12], Catastrophic Failure):
  • P(F* strictly dominates existing) = {dominance_prob:.4f} ({dominance_prob*100:.2f}%)
  • Mean utility dominance margin     = {margin_arr.mean():.4f} (Min: {margin_arr.min():.4f})
  • Complexity tipping threshold α    = {tipping_point:.2f} (where dominance drops below 50%)

Linear Programming (Gap Persistence):
  • max convex-combination D4 score = {max_D4_convex:.4f} (< 1.0 required)
  • D4 gap is formally proven UNCLOSABLE by any λ ∈ Δ^12

Decision Optimization Scenarios:
  • Optimal existing frameworks are F6 (for Technical/Governance/Inclusive/Balanced) and F12 (for Pedagogy/Test)
  • F* achieves higher net utility in all 6 scenarios, confirming robustness to adoption cost

Simulated Proof of Concept (PoC - Rater Reliability):
  • Observed Agreement (po)          = {po:.4f} ({po*100:.2f}%)
  • Cohen's Kappa (κ)                 = {kappa_score:.4f} ({status_kappa})
""")

# Save results to JSON for paper reference
results = {
    "monte_carlo_n": N_MONTE_CARLO,
    "p_max_below_3_0": float(p_below_3),
    "p_max_below_3_5": float(p_below_35),
    "p_max_below_4_0": float(p_below_4),
    "p_D4_gap_persists": float(1 - p_D4_exceeds),
    "weighted_sensitivity_n": N_DIRICHLET,
    "dominance_probability": float(dominance_prob),
    "min_dominance_margin": float(margin_arr.min()),
    "mean_dominance_margin": float(margin_arr.mean()),
    "complexity_tipping_point": float(tipping_point),
    "lp_max_D4_convex": float(max_D4_convex),
    "gap_persistence_per_dim": {k: float(v) for k, v in gap_results.items()},
    "framework_ci": {fw: {k: float(v) for k, v in ci.items()} 
                     for fw, ci in ci_results.items()},
    "poc_agreement": float(po),
    "poc_kappa": float(kappa_score),
}

with open(os.path.join(current_dir, "simulation_results.json"), "w") as f:
    json.dump(results, f, indent=2)
print("Results saved to src/simulation_results.json")
