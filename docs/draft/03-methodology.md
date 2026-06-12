# Methodology — IS EdTech Main Paper

**Word count target:** ~1000 words  
**Structure:** Research Design → Jabareen's CFA phases → DSR validation logic

---

\subsection{Philosophy and Approach}

This study adopts a hybrid methodological approach that integrates two complementary traditions in Information Systems (IS) research: *Conceptual Framework Analysis* (CFA) as proposed by Jabareen (2009) for the framework construction phase~[b6], and *Design Science Research* (DSR) as formalised by Hevner et al. (2004) for the artifact validation phase~[b34]. This integration provides a stronger epistemological foundation than pure conceptual development: the resulting framework functions as an **IS artifact** designed to address a real-world evaluation gap.

In Gregor's (2006) taxonomy of IS theories, this study develops a **Type IV Theory (Explanatory and Predictive)**~[b35]. Rather than merely classifying dimensions (Type I), it formalises structural equations (Section~sec:structural_model) that predict how platform quality relates to outcomes. The study operates under a *critical realism* paradigm at the ontological level, asserting that success dimensions of EdTech platforms are real, though our access to them is mediated by theory~[b7]. Epistemologically, the study is post-positivist: knowledge is constructed through concept synthesis and validated through formal mathematical proofs and computational simulations that are reproducible and falsifiable.

Table~tab:philosophy summarizes the philosophical and methodological layers of this study.

\begin{table}[h]
  \caption{Philosophical and Methodological Foundation}
  
  \centering
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{@{} L{3.5cm} L{4.5cm} L{6.5cm} @{} }
    \toprule
    **Layer** & **Position** & **Methodological Implications** 
    \midrule
    **Ontology** & Critical realism & The framework is ontologically grounded, not arbitrary 
    **Epistemology** & Post-positivism & CFA (construction) + DSR (validation) tandem approach 
    **Methodology** & CFA + DSR & CFA for Phases 1--6; DSR for validation (Phase 7) 
    **Literature Review** & Integrative review~[b8] & Multi-disciplinary synthesis as conceptual data 
    **Validation** & Math proofs & simulation & Falsifiable validation without primary participant data 
    \bottomrule
  \end{tabular}
\end{table}

**The Role of DSR in This Study:** In Hevner et al.'s (2004) terminology~[b34], the TECH+PED+INST framework serves as an **IS artifact**---a construct designed to solve a practical problem (the fragmentation of EdTech evaluation frameworks). DSR requires that the artifact be validated through evaluation activities that provide utility evidence. In this study, these activities comprise: (a) a coverage matrix cross-validation for completeness; (b) a formal linear programming proof for necessity; and (c) a Monte Carlo computational simulation for robustness. Thus, our methodological approach satisfies Hevner's three key DSR claims: utility, novelty, and rigor, supported by the Design Science Research Methodology (DSRM) guidelines of Peffers et al. (2007)~[b36] for structuring the research process.

\subsection{Eight Phases of CFA in This Study}

Following Jabareen (2009)~[b6], the framework was developed through eight iterative phases. Table~tab:cfa_phases details the procedures and conceptual outputs for each of these eight phases.

\begin{table*}[t]
  \caption{The Eight Phases of Conceptual Framework Analysis (CFA) applied in this study}
  
  \centering
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{@{} L{4.0cm} L{7.5cm} L{4.5cm} @{} }
    \toprule
    **Phase** & **Procedure** & **Output** 
    \midrule
    **1. Mapping Data Sources** & Integrative literature review~[b8] across Scopus, Web of Science, ERIC, and IEEE Xplore. Inclusion criteria: frameworks/models evaluating digital learning platforms in HE, CALL, MALL, or LMS (2001--2025, English). & Corpus of frameworks for conceptual analysis 
    **2. Extensive Reading & Categorization** & Classifying literature by discipline of origin (applied linguistics, IS, education, cognitive psychology) and type of framework (evaluative, predictive, design, adoption). & Literature categorization matrix 
    **3. Identifying Concepts** & Extracting repeating core concepts: language learning potential, learner fit, perceived usefulness, cognitive load, learning analytics, institutional adoption. & List of candidate concepts 
    **4. Deconstructing Concepts** & Component, history, and relationship analysis of concepts based on source theories (e.g., Sweller's cognitive load; Davis's TAM). & Componential definitions per concept 
    **5. Integrating Concepts** & Synthesis of concepts from different disciplines into complementary evaluation dimensions. & Preliminary framework dimensions 
    **6. Synthesis & Resynthesis** & Construction of a network of interlinked concepts forming a plane of understanding of platform evaluation. & Theoretical framework v0.1 
    **7. Validation** & Three-layer DSR validation~[b34]: Layer 1 (Theoretical) coverage matrix cross-validation; Layer 2 (Mathematical) convex combination bound (Lemma 1); Layer 3 (Computational) Monte Carlo sensitivity simulation (Proposition 1). & Validated framework v1.0, simulation results, formal proofs 
    **8. Rethinking & Revision** & Iterative revisions based on expert feedback and cross-mapping to ensure novelty and non-redundancy. & Final theoretical framework 
    \bottomrule
  \end{tabular}
\end{table*}

\subsection{Integrative Review Protocol as CFA Data Source}

Following Torraco (2005)~[b8], an integrative review was used to collect conceptual data. Unlike systematic reviews designed to aggregate effect sizes, the integrative review enables conceptual synthesis across empirical and theoretical literature to support theory development. The review protocol was guided by the question: *``What evaluation frameworks exist for digital educational platforms, and what assessment dimensions do they address or neglect in the context of higher education language learning?''* The search string combined keywords addressing educational technology evaluation, university context, and language learning.

\subsection{Mathematical Framework Specification}

To meet DSR and Type IV theory standards, we specify the formal mathematical structures of the framework:

\subsubsection{Formalization of Coverage Score}
Let $\mathcal{F} = \{F_1, \ldots, F_{12}\}$ represent the set of reviewed frameworks, and $\mathcal{D} = \{D_1, D_2, D_3, D_4, D_6\}$ represent the set of evaluation dimensions. The coding function $s: \mathcal{F} \times \mathcal{D} \to \{0, 0.5, 1.0\}$ yields the *Coverage Score* (CS):
\begin{equation}
  \text{CS}(f) = \sum_{d \in \mathcal{D}} s(f,d), \quad \text{CS}(f) \in [0, 5.0]
\end{equation}
The proposed framework $F^*$ achieves $s(F^*, d) = 1.0$ for all $d$, resulting in $\text{CS}(F^*) = 5.0$. In comparison, the maximum score in the existing corpus is $\max_{f \in \mathcal{F}} \text{CS}(f) = 2.5$.

\subsubsection{Composite Platform Quality Score}
Overall platform quality is formulated as a weighted composite score:
\begin{equation}
  Q_{\text{platform}} = \alpha \cdot Q_{\text{TECH}} + \beta \cdot Q_{\text{PED}} + \gamma \cdot Q_{\text{INST}}
\end{equation}
where $\alpha + \beta + \gamma = 1$, $\alpha, \beta, \gamma > 0$, and each component score is defined as:
\begin{equation}
  Q_{\text{TECH}} = \frac{\sum_{k} w_k \cdot x_k^{\text{TECH}}}{\sum_k w_k}, \quad Q_{\text{PED}} = \frac{\sum_{j} w_j \cdot x_j^{\text{PED}}}{\sum_j w_j}, \quad Q_{\text{INST}} = \frac{\sum_{l} w_l \cdot x_l^{\text{INST}}}{\sum_l w_l}
\end{equation}
where $x_k^{\text{TECH}} \in [0,1]$ is the score of the $k$-th indicator of the TECH dimension, and similarly for the other dimensions.

\subsubsection{Formal Structural Equations Preview}
The relationships between these quality dimensions and outcomes are previewed below (detailed in Section~sec:structural_model):
\begin{align}
  \text{PU} &= \beta_1 \cdot Q_{\text{TECH}} + \beta_2 \cdot Q_{\text{PED}} + \varepsilon_1 
  \text{SAT} &= \beta_3 \cdot Q_{\text{TECH}} + \beta_4 \cdot Q_{\text{PED}} + \varepsilon_2 
  \text{UX} &= \gamma_1 \cdot Q_{\text{TECH}} + \gamma_2 \cdot Q_{\text{PED}} + \gamma_3 \cdot (Q_{\text{TECH}} \times Q_{\text{PED}}) + \varepsilon_3 
  \text{USE} &= \beta_5 \cdot \text{PU} + \beta_6 \cdot \text{SAT} + \beta_7 \cdot Q_{\text{INST}} + \beta_8 \cdot \text{UX} + \varepsilon_4
\end{align}

\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig6_pcc_and_dimensions}
  \caption{PCC Framework elements and analytical dimension grounding.}
  
\end{figure*}

% ============================================================

---

*Source: Extracted from ethe_main.tex — keep synchronized*  
*Status: ✅ Drafted | ☐ Peer-reviewed internally | ☐ Final*
