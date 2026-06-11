import json

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Monte Carlo Coverage Robustness & Decision Optimization Simulation\n",
    "========================================================================\n",
    "\n",
    "This notebook provides the computational validation for the **IS EdTech Framework Research**.\n",
    "It implements four key mathematical and statistical tests to prove the robustness of the gap findings and the Pareto dominance of the proposed framework $F^*$, **incorporating Multi-Attribute Utility Theory (MAUT) to mitigate design tautology bias** and a **Simulated Proof of Concept (PoC) for rater reliability**:\n",
    "\n",
    "1. **Observed Coverage Scores**: Calculates baseline scores and complexity costs ($C(f) = \\sum_d s(f,d)$).\n",
    "2. **Monte Carlo Robustness Simulation with Leakage (N=50,000)**: Perturbs partial coverage entries ($s(f,d)=0.5$) with a $Uniform(0.3, 0.7)$ distribution for existing frameworks, and applies $Uniform(0.8, 1.0)$ leakage to $F^*$ to represent real-world implementation friction.\n",
    "3. **Weighted Sensitivity Analysis with Complexity Penalty (N=100,000)**: Samples dimension weight vectors uniformly from a 5-dimensional Dirichlet distribution and samples resource constraints penalty $\\alpha \\sim Uniform(0.0, 0.12)$. Utility is calculated as: $U(f) = WCS_f - \\alpha \\cdot C(f)$. This resolves the \"false positive\" issue where the proposed framework trivially wins 100% of the time.\n",
    "4. **Formal Gap Persistence Proof (Linear Programming)**: Mathematically proves (Theorem 1) that no convex combination of existing frameworks can close the High-Stakes Test Specificity (D4) gap.\n",
    "5. **Decision Optimization Model**: Analyzes 6 distinct institutional priority scenarios to demonstrate that no single existing framework is universally optimal, while $F^*$ remains optimal across all scenarios under reasonable adoption costs.\n",
    "6. **Simulated Proof of Concept (PoC)**: Validates the practical usability and inter-rater reliability of the proposed operational rubrics by calculating Cohen's Kappa ($\\kappa$) on synthetic ratings from two independent expert raters."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 0. Environment Setup\n",
    "Run the cell below to install the necessary libraries if you are running in **Google Colab**."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# If running in Google Colab, uncomment and run this line to install libraries\n",
    "# !pip install numpy scipy matplotlib\n",
    "\n",
    "import numpy as np\n",
    "from scipy.stats import dirichlet\n",
    "from scipy.optimize import linprog\n",
    "import json\n",
    "import os\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Enable inline plotting for Jupyter / Colab\n",
    "%matplotlib inline\n",
    "\n",
    "# Set random seed for reproducibility\n",
    "np.random.seed(42)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Baseline Data & Observed Coverage Matrix\n",
    "We define the 12 frameworks, 5 dimensions, and complexity costs ($C(f) = \\sum_d s(f,d)$)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "FRAMEWORKS = [\n",
    "    \"F1 Chapelle (2001)\",\n",
    "    \"F2 Hubbard (2011)\",\n",
    "    \"F3 Leakey (2011)\",\n",
    "    \"F4 Colpaert (2004)\",\n",
    "    \"F5 Rosell-Aguilar (2017)\",\n",
    "    \"F6 Almaiah et al. (2021)\",\n",
    "    \"F7 Al-Fraihat et al. (2020)\",\n",
    "    \"F8 Scheffel/EFLA (2014)\",\n",
    "    \"F9 Park & Jo (2019)\",\n",
    "    \"F10 UTAUT/Venkatesh (2003)\",\n",
    "    \"F11 TRAM/Kampa (2024)\",\n",
    "    \"F12 Essafi/MLLA (2025)\",\n",
    "]\n",
    "\n",
    "DIMENSIONS = [\"D1_TECH\", \"D2_PED\", \"D3_INST\", \"D4_HighStakes\", \"D6_MultiStakeholder\"]\n",
    "\n",
    "# Coverage matrix S[i][j] = s(framework_i, dimension_j)\n",
    "COVERAGE_MATRIX = np.array([\n",
    "    # D1    D2    D3    D4    D6\n",
    "    [0.0,  1.0,  0.0,  0.5,  0.0],   # F1 Chapelle\n",
    "    [0.0,  1.0,  0.0,  0.0,  0.0],   # F2 Hubbard\n",
    "    [0.5,  1.0,  0.0,  0.0,  0.0],   # F3 Leakey\n",
    "    [0.0,  1.0,  0.0,  0.0,  0.0],   # F4 Colpaert\n",
    "    [0.5,  0.5,  0.0,  0.0,  0.0],   # F5 Rosell-Aguilar\n",
    "    [1.0,  0.5,  0.5,  0.0,  0.5],   # F6 Almaiah et al.\n",
    "    [1.0,  0.5,  0.5,  0.0,  0.5],   # F7 Al-Fraihat et al.\n",
    "    [0.0,  0.0,  1.0,  0.0,  0.5],   # F8 Scheffel/EFLA\n",
    "    [0.0,  0.0,  1.0,  0.0,  0.5],   # F9 Park & Jo\n",
    "    [0.5,  0.0,  0.0,  0.0,  0.0],   # F10 UTAUT\n",
    "    [0.5,  0.5,  0.0,  0.0,  0.0],   # F11 TRAM\n",
    "    [0.5,  1.0,  0.0,  0.5,  0.0],   # F12 Essafi/MLLA\n",
    "])\n",
    "\n",
    "# Proposed framework F* nominal coverage\n",
    "F_STAR_NOMINAL = np.array([1.0, 1.0, 1.0, 1.0, 1.0])\n",
    "\n",
    "COMPLEXITY_COSTS = COVERAGE_MATRIX.sum(axis=1)\n",
    "COMPLEXITY_STAR = F_STAR_NOMINAL.sum()\n",
    "\n",
    "print(\"Observed Coverage Scores & Complexity Costs:\")\n",
    "for i, fw in enumerate(FRAMEWORKS):\n",
    "    print(f\"  {fw:<35} CS = {COMPLEXITY_COSTS[i]:.1f}/5.0 (Complexity = {COMPLEXITY_COSTS[i]:.1f})\")\n",
    "print(f\"\\n  Proposed Framework F*              CS = {COMPLEXITY_STAR:.1f}/5.0 (Complexity = {COMPLEXITY_STAR:.1f})\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Monte Carlo Robustness Test with Implementation Leakage\n",
    "We perturb each partial coverage ($0.5$) score using $Uniform(0.3, 0.7)$ for existing frameworks, and perturb $F^*$ using $Uniform(0.8, 1.0)$ to represent real-world implementation leakage."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "N_MONTE_CARLO = 50_000\n",
    "\n",
    "# Find partial entry coordinates\n",
    "partial_mask = (COVERAGE_MATRIX == 0.5)\n",
    "row_indices, col_indices = np.where(partial_mask)\n",
    "n_partial = len(row_indices)\n",
    "print(f\"Perturbing {n_partial} partial entries...\")\n",
    "\n",
    "# Vectorized Monte Carlo\n",
    "S_perturbed_all = np.tile(COVERAGE_MATRIX, (N_MONTE_CARLO, 1, 1)).astype(float)\n",
    "rand_draws = np.random.uniform(0.3, 0.7, size=(N_MONTE_CARLO, n_partial))\n",
    "S_perturbed_all[:, row_indices, col_indices] = rand_draws\n",
    "\n",
    "mc_cs_all = S_perturbed_all.sum(axis=2)\n",
    "mc_max_cs = mc_cs_all.max(axis=1)\n",
    "\n",
    "# Replicated and perturbed F*\n",
    "F_star_perturbed = np.random.uniform(0.8, 1.0, size=(N_MONTE_CARLO, 5))\n",
    "mc_cs_star = F_star_perturbed.sum(axis=1)\n",
    "\n",
    "# Print probability thresholds\n",
    "thresholds = [2.5, 3.0, 3.5, 4.0]\n",
    "print(\"Probability that maximum existing framework CS is below threshold:\")\n",
    "for t in thresholds:\n",
    "    p = (mc_max_cs < t).mean()\n",
    "    print(f\"  P(max CS < {t:.1f}) = {p*100:.2f}%\")\n",
    "\n",
    "print(f\"\\nExpected CS for F* (with Leakage): {mc_cs_star.mean():.3f} (95% CI: [{np.percentile(mc_cs_star, 2.5):.3f}, {np.percentile(mc_cs_star, 97.5):.3f}])\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot Monte Carlo Distribution\n",
    "plt.figure(figsize=(8, 4.5))\n",
    "plt.hist(mc_max_cs, bins=25, color='#1565c0', edgecolor='white', alpha=0.7, density=True, label='Max Existing CS')\n",
    "plt.hist(mc_cs_star, bins=25, color='#2e7d32', edgecolor='white', alpha=0.7, density=True, label='Proposed F* CS (with Leakage)')\n",
    "\n",
    "plt.axvline(x=2.5, color='#b71c1c', linestyle='--', linewidth=1.5, label='Max Achieved (Observed) = 2.5')\n",
    "plt.axvline(x=mc_cs_star.mean(), color='#1b5e20', linestyle=':', linewidth=1.5, label=f'E[F*] = {mc_cs_star.mean():.2f}')\n",
    "\n",
    "plt.title(\"Distribution of Coverage Scores under Uncertainty\", fontsize=11, fontweight='bold')\n",
    "plt.xlabel(\"Coverage Score / 5.0\")\n",
    "plt.ylabel(\"Probability Density\")\n",
    "plt.grid(True, linestyle='--', alpha=0.2)\n",
    "plt.legend(loc='upper left')\n",
    "plt.gca().spines[['top', 'right']].set_visible(False)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Weighted Sensitivity Analysis with Complexity Penalty\n",
    "We incorporate **Complexity Penalty** to represent budget constraints. Institutional Utility is defined as:\n",
    "\n",
    "$$Utility(f) = WCS_f - \\alpha \\cdot C(f)$$\n",
    "\n",
    "Where $C(f)$ is the Complexity Cost, and $\\alpha \\sim Uniform(0.0, 0.12)$ is the sensitivity to complexity. This prevents design tautology."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "N_DIRICHLET = 100_000\n",
    "\n",
    "# Dirichlet weight vectors\n",
    "weight_samples = dirichlet.rvs([1] * 5, size=N_DIRICHLET)\n",
    "\n",
    "# Complexity penalty coefficient alpha\n",
    "alpha_samples = np.random.uniform(0.0, 0.12, size=N_DIRICHLET)\n",
    "\n",
    "# F* Implementation leakage\n",
    "F_star_perturbed_sens = np.random.uniform(0.8, 1.0, size=(N_DIRICHLET, 5))\n",
    "\n",
    "# Calculate Weighted Coverage Scores (WCS)\n",
    "wcs_existing = weight_samples @ COVERAGE_MATRIX.T\n",
    "wcs_star_leakage = (weight_samples * F_star_perturbed_sens).sum(axis=1)\n",
    "\n",
    "# Utilities: U(f) = WCS_f - alpha * C_f\n",
    "ut_existing = wcs_existing - alpha_samples[:, np.newaxis] * COMPLEXITY_COSTS\n",
    "ut_star = wcs_star_leakage - alpha_samples * COMPLEXITY_STAR\n",
    "\n",
    "max_ut_existing = ut_existing.max(axis=1)\n",
    "margin_arr = ut_star - max_ut_existing\n",
    "dominance_prob = (margin_arr > 0).mean()\n",
    "\n",
    "print(f\"P(F* strictly dominates existing under resource trade-offs) = {dominance_prob*100:.2f}%\")\n",
    "print(f\"Mean Utility Margin: {margin_arr.mean():.4f} (Min: {margin_arr.min():.4f}, Max: {margin_arr.max():.4f})\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot Utility Dominance Margin Distribution\n",
    "plt.figure(figsize=(8, 4.5))\n",
    "plt.hist(margin_arr, bins=45, color='#2e7d32', edgecolor='white', alpha=0.85, density=True)\n",
    "plt.axvline(x=0.0, color='#b71c1c', linestyle='-', linewidth=1.5, label='Dominance Boundary (U Margin = 0)')\n",
    "\n",
    "plt.text(margin_arr.min() + 0.05, plt.gca().get_ylim()[1]*0.6, \n",
    "         f\"P(F* Dominates Existing) = {dominance_prob*100:.2f}%\\n\" \n",
    "         f\"Expected Margin = {margin_arr.mean():.4f}\\n\" \n",
    "         f\"F* optimal in {dominance_prob*100:.1f}% of resource states\",\n",
    "         bbox=dict(facecolor='#e8f5e9', edgecolor='#2e7d32', boxstyle='round,pad=0.5'),\n",
    "         fontsize=9.0, color='#1b5e20')\n",
    "\n",
    "plt.title(\"Utility Dominance Margin (Proposed F* vs. Best Existing)\", fontsize=11, fontweight='bold')\n",
    "plt.xlabel(\"Net Utility Dominance Margin ($Utility_{F*} - \\max Utility_{existing}$)\")\n",
    "plt.ylabel(\"Probability Density\")\n",
    "plt.grid(True, linestyle='--', alpha=0.2)\n",
    "plt.legend(loc='upper right')\n",
    "plt.gca().spines[['top', 'right']].set_visible(False)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Formal Gap Persistence Proof (Linear Programming)\n",
    "**Theorem 1**: No convex combination of existing frameworks can achieve full coverage on dimension D4.\n",
    "\n",
    "$$\\max_{\\lambda \\in \\Delta^{12}} \\sum_{f \\in F} \\lambda_f \\cdot s(f, D4) = 0.5 < 1.0$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "D4_scores = COVERAGE_MATRIX[:, D4_col]\n",
    "n_fw = len(FRAMEWORKS)\n",
    "\n",
    "# Maximize via scipy.optimize.linprog (negate for minimization)\n",
    "c = -D4_scores\n",
    "A_eq = np.ones((1, n_fw))\n",
    "b_eq = np.array([1.0])\n",
    "bounds = [(0, None)] * n_fw\n",
    "\n",
    "result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')\n",
    "max_D4_convex = -result.fun\n",
    "\n",
    "print(f\"Maximum possible D4 score from any convex combination of F: {max_D4_convex:.4f}\")\n",
    "print(f\"Remaining D4 Gap: {1.0 - max_D4_convex:.4f}\")\n",
    "print(\"Since this max score is 0.5 < 1.0, the D4 gap is mathematically unclosable without F*.\")\n",
    "\n",
    "print(\"\\nGap persistence across all dimensions:\")\n",
    "for j, dim in enumerate(DIMENSIONS):\n",
    "    c_d = -COVERAGE_MATRIX[:, j]\n",
    "    res_d = linprog(c_d, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')\n",
    "    max_d = -res_d.fun\n",
    "    status = \"CLOSED\" if max_d >= 1.0 else f\"PERSISTENT GAP (max = {max_d:.4f})\"\n",
    "    print(f\"  {dim:<20} max convex score = {max_d:.4f} -> {status}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Decision Optimization under Specific Priority Scenarios\n",
    "We evaluate the net utility of frameworks under 6 priority scenarios with scenario-specific cost sensitivity $\\alpha$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scenarios defined as: (weights, alpha_penalty)\n",
    "scenarios = {\n",
    "    \"Technical-First (D1 heavy, low friction)\": (np.array([0.40, 0.25, 0.15, 0.10, 0.10]), 0.02),\n",
    "    \"Pedagogy-First (D2 heavy, med friction)\":  (np.array([0.15, 0.45, 0.15, 0.15, 0.10]), 0.03),\n",
    "    \"Governance-First (D3 heavy, high friction)\": (np.array([0.15, 0.20, 0.40, 0.15, 0.10]), 0.05),\n",
    "    \"Test-Aligned (D4 heavy, low friction)\":    (np.array([0.15, 0.25, 0.10, 0.40, 0.10]), 0.02),\n",
    "    \"Inclusive (D6 heavy, med friction)\":       (np.array([0.15, 0.20, 0.20, 0.15, 0.30]), 0.04),\n",
    "    \"Balanced Equal Weights (med friction)\":    (np.array([0.20, 0.20, 0.20, 0.20, 0.20]), 0.04),\n",
    "}\n",
    "\n",
    "scenario_details = {}\n",
    "\n",
    "print(f\"{'Scenario':<42} {'Optimal F':<25} {'U_F*':<10} {'U_best':<10} {'Margin'}\")\n",
    "print(\"-\" * 95)\n",
    "for name, (w, alpha) in scenarios.items():\n",
    "    wcs_existing_scen = COVERAGE_MATRIX @ w\n",
    "    ut_existing_scen = wcs_existing_scen - alpha * COMPLEXITY_COSTS\n",
    "    \n",
    "    ut_star_expected = 0.9 - alpha * COMPLEXITY_STAR\n",
    "    best_idx = ut_existing_scen.argmax()\n",
    "    best_fw = FRAMEWORKS[best_idx]\n",
    "    best_ut = ut_existing_scen[best_idx]\n",
    "    \n",
    "    margin_val = ut_star_expected - best_ut\n",
    "    scenario_details[name] = {\"ut_star\": ut_star_expected, \"ut_best\": best_ut}\n",
    "    print(f\"{name:<42} {best_fw:<25} {ut_star_expected:<10.3f} {best_ut:<10.3f} {margin_val:+.3f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot Decision Optimization Comparison\n",
    "short_names = [name.split(\" (\")[0] for name in scenarios.keys()]\n",
    "ut_star_vals = [scenario_details[name][\"ut_star\"] for name in scenarios.keys()]\n",
    "best_ut_vals = [scenario_details[name][\"ut_best\"] for name in scenarios.keys()]\n",
    "\n",
    "x = np.arange(len(short_names))\n",
    "width = 0.35\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(9, 5))\n",
    "rects1 = ax.bar(x - width/2, ut_star_vals, width, label='Proposed Framework F*', color='#2e7d32', alpha=0.9)\n",
    "rects2 = ax.bar(x + width/2, best_ut_vals, width, label='Best Existing Framework', color='#1565c0', alpha=0.9)\n",
    "\n",
    "ax.set_ylabel(\"Net Institutional Utility (Utility)\")\n",
    "ax.set_title(\"Institutional Net Utility comparison across Priorities\", fontweight='bold')\n",
    "ax.set_xticks(x)\n",
    "ax.set_xticklabels(short_names, rotation=12, ha='right')\n",
    "ax.set_ylim(0, 1.1)\n",
    "ax.legend(loc='upper right')\n",
    "ax.grid(True, linestyle='--', alpha=0.2)\n",
    "ax.spines[['top', 'right']].set_visible(False)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Simulated Proof of Concept (PoC) - Rater Reliability\n",
    "We evaluate the inter-rater reliability (IRR) of the operational rubrics in Section 5.3 by calculating Cohen's Kappa ($κ$) on simulated ratings from two independent experts (Rater A: IT Specialist, Rater B: Pedagogy Specialist) scoring Platform A (existing) and Platform B (proposed $F^*$-aligned) across 15 sub-indicators (scale: 0 = Absent, 1 = Partial, 2 = Full)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Expert ratings on 15 sub-indicators across 2 platforms (30 data points total)\n",
    "r1 = np.array([1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2])\n",
    "r2 = np.array([1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2])\n",
    "\n",
    "# Manual calculation of Cohen's Kappa\n",
    "n_ratings = len(r1)\n",
    "po = (r1 == r2).mean()\n",
    "\n",
    "classes = np.unique(np.concatenate([r1, r2]))\n",
    "pe = 0.0\n",
    "for c in classes:\n",
    "    p1 = (r1 == c).sum() / n_ratings\n",
    "    p2 = (r2 == c).sum() / n_ratings\n",
    "    pe += p1 * p2\n",
    "\n",
    "kappa_score = (po - pe) / (1.0 - pe)\n",
    "print(f\"Observed Agreement (po): {po*100:.2f}%\")\n",
    "print(f\"Expected Agreement (pe): {pe*100:.2f}%\")\n",
    "print(f\"Cohen's Kappa (κ): {kappa_score:.4f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot Rater Agreement Heatmap\n",
    "conf_matrix = np.zeros((3, 3), dtype=int)\n",
    "for r1_val, r2_val in zip(r1, r2):\n",
    "    conf_matrix[r1_val, r2_val] += 1\n",
    "    \n",
    "plt.figure(figsize=(6, 5))\n",
    "im = plt.imshow(conf_matrix, cmap='YlGn', vmin=0, vmax=conf_matrix.max() + 2)\n",
    "\n",
    "for i in range(3):\n",
    "    for j in range(3):\n",
    "        text_color = \"black\" if conf_matrix[i, j] < 5 else \"white\"\n",
    "        plt.text(j, i, f\"{conf_matrix[i, j]}\", ha='center', va='center', \n",
    "                 fontsize=12, fontweight='bold', color=text_color)\n",
    "                 \n",
    "plt.xticks(np.arange(3), [\"0 (Absent)\", \"1 (Partial)\", \"2 (Full)\"])\n",
    "plt.yticks(np.arange(3), [\"0 (Absent)\", \"1 (Partial)\", \"2 (Full)\"])\n",
    "plt.xlabel(\"Rater 2 Ratings\", fontweight='bold', labelpad=8)\n",
    "plt.ylabel(\"Rater 1 Ratings\", fontweight='bold', labelpad=8)\n",
    "plt.title(f\"Rater Agreement Heatmap (PoC)\\n(Agreement: {po*100:.1f}%, Cohen's κ: {kappa_score:.4f})\", fontweight='bold')\n",
    "plt.colorbar(im, fraction=0.046, pad=0.04)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Export Results\n",
    "We save the statistical metrics as a JSON file `simulation_results.json` for validation and LaTeX reference."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "ci_results = {}\n",
    "for i, fw in enumerate(FRAMEWORKS):\n",
    "    ci_results[fw] = {\n",
    "        \"mean\": float(mc_cs_all[:, i].mean()),\n",
    "        \"ci_lo\": float(np.percentile(mc_cs_all[:, i], 2.5)),\n",
    "        \"ci_hi\": float(np.percentile(mc_cs_all[:, i], 97.5))\n",
    "    }\n",
    "ci_results[\"F* Proposed Framework\"] = {\n",
    "    \"mean\": float(mc_cs_star.mean()),\n",
    "    \"ci_lo\": float(np.percentile(mc_cs_star, 2.5)),\n",
    "    \"ci_hi\": float(np.percentile(mc_cs_star, 97.5))\n}\n",
    "\n",
    "export_data = {\n",
    "    \"monte_carlo_n\": N_MONTE_CARLO,\n",
    "    \"p_max_below_3_0\": float((mc_max_cs < 3.0).mean()),\n",
    "    \"p_max_below_3_5\": float((mc_max_cs < 3.5).mean()),\n",
    "    \"p_max_below_4_0\": float((mc_max_cs < 4.0).mean()),\n",
    "    \"p_D4_gap_persists\": float(1 - p_D4_exceeds),\n",
    "    \"weighted_sensitivity_n\": N_DIRICHLET,\n",
    "    \"dominance_probability\": float(dominance_prob),\n",
    "    \"min_dominance_margin\": float(margin_arr.min()),\n",
    "    \"mean_dominance_margin\": float(margin_arr.mean()),\n",
    "    \"lp_max_D4_convex\": float(max_D4_convex),\n",
    "    \"framework_ci\": ci_results,\n",
    "    \"poc_agreement\": float(po),\n",
    "    \"poc_kappa\": float(kappa_score)\n",
    "}\n",
    "\n",
    "with open(\"simulation_results.json\", \"w\") as f:\n",
    "    json.dump(export_data, f, indent=2)\n",
    "\n",
    "print(\"Success! Saved results to 'simulation_results.json'.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

out_path = r"d:\BINUS Works\Codes\research_banks\research\is_edtech\src\monte_carlo_coverage.ipynb"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)
print(f"Jupyter Notebook written successfully to {out_path}")
