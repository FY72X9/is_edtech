# Methodology  -  IS EdTech Main Paper

**Word count target:** ~1000 words  
**Structure:** Research Design → Jabareen's CFA phases → DSR validation logic

---

\subsection{Philosophy and Approach}

This study adopts a hybrid methodological approach that integrates two complementary traditions in Information Systems (IS) research: *Conceptual Framework Analysis* (CFA) as proposed by Jabareen (2009) for the framework construction phase~[b6], and *Design Science Research* (DSR) as formalised by Hevner et al. (2004) for the artifact validation phase~[b34]. We hybridize these two methodologies because while CFA provides a rigorous, systematic procedure for identifying, deconstructing, and synthesizing concepts across different disciplines (Applied Linguistics, IS, and Education), it lacks a formal mechanism to evaluate the practical utility of the resulting framework. Conversely, DSR focuses heavily on the design and validation of artifacts to solve real-world problems, but does not specify how to perform the initial conceptual synthesis. By combining them, CFA is the generative engine for the framework's design, while DSR provides the validation scaffold. This integration provides a stronger epistemological foundation than pure conceptual development: the resulting framework functions as an **IS artifact** (a construct designed to address a practical problem, namely the fragmentation of EdTech evaluation frameworks) and is evaluated through rigorous mathematical and computational procedures.

In Gregor's (2006) taxonomy of IS theories, this study develops a **Type IV Theory (Explanatory and Predictive)**~[b35]. Rather than merely classifying dimensions (Type I), it formalises structural equations (Section~sec:structural_model) that predict how platform quality relates to outcomes. The study operates under a *critical realism* paradigm at the ontological level, asserting that success dimensions of EdTech platforms are real, though our access to them is mediated by theory~[b7]. Epistemologically, the study is post-positivist: knowledge is constructed through concept synthesis and validated through formal mathematical proofs and computational simulations that are reproducible and falsifiable.

Table~tab:philosophy summarizes the philosophical and methodological layers of this study. At the ontological layer, we adopt critical realism, which asserts that the dimensions of platform quality (technical reliability, pedagogical effectiveness, and institutional governance) are real, causal structures that exist independently of our observation of them. This stance justifies our attempt to map and measure these dimensions. Epistemologically, our post-positivist approach acknowledges that while our understanding of these dimensions is mediated by theory and subject to modification, we can still construct objective, generalizable knowledge through concept synthesis. Methodologically, the CFA-DSR tandem ensures that the framework's construction is grounded in literature (Phases 1--6) while its validation (Phase 7) is subjected to formal proofs and simulations. This approach ensures that the framework is not merely a descriptive checklist but a scientifically validated tool. At the ontological layer, we adopt critical realism, which asserts that the dimensions of platform quality (technical reliability, pedagogical effectiveness, and institutional governance) are real, causal structures that exist independently of our observation of them. This stance justifies our attempt to map and measure these dimensions. Epistemologically, our post-positivist approach acknowledges that while our understanding of these dimensions is mediated by theory and subject to modification, we can still construct objective, generalizable knowledge through concept synthesis. Methodologically, the CFA-DSR tandem ensures that the framework's construction is grounded in literature (Phases 1--6) while its validation (Phase 7) is subjected to formal proofs and simulations. This approach ensures that the framework is not merely a descriptive checklist but a scientifically validated tool.

\begin{table}[ht]
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

**The Role of DSR in This Study:** In Hevner et al.'s (2004) terminology~[b34], the TECH+PED+INST framework is an **IS artifact** (a construct designed to address a practical problem, namely the fragmentation of EdTech evaluation frameworks). DSR requires that the artifact be validated through evaluation activities that provide utility evidence. In this study, these activities comprise: (a) a coverage matrix cross-validation for completeness; (b) a formal linear programming proof for necessity; and (c) a Monte Carlo computational simulation for robustness. Thus, our methodological approach satisfies Hevner's three key DSR claims: utility, novelty, and rigor, supported by the Design Science Research Methodology (DSRM) guidelines of Peffers et al. (2007)~[b36] for structuring the research process. The structural flow of this research program is visually mapped in Figure~fig:program_arch. The architecture outlines the connection between our literature dataset, scoping review protocol, and Design Science Research validation. The integrative review (left column) is the primary data collection process, producing the corpus of 12 landmark frameworks. These frameworks are then inputted into the Conceptual Framework Analysis (CFA) engine (center column) to deconstruct and integrate concepts across Applied Linguistics and Information Systems. Finally, the resulting framework ($F^*$) is subjected to the three-layer DSR validation scaffold (right column) to evaluate its completeness (theoretical), necessity (mathematical LP proof), and robustness (computational Monte Carlo simulation). This structured path ensures that the resulting evaluation artifact is both theoretically grounded and mathematically validated.

\subsection{Eight Phases of CFA in This Study}

Following Jabareen (2009)~[b6], the framework was developed through eight iterative phases. Table~tab:cfa_phases details the procedures and conceptual outputs for each of these eight phases. The execution of these phases is inherently iterative, allowing for constant refinement of concepts as new literature is deconstructed. In Phase 1, mapping data sources provides the conceptual raw data from Web of Science, Scopus, and other databases, ensuring a broad multidisciplinary scope. Phases 2 through 5 deconstruct these sources to extract candidate concepts (e.g., washback, cognitive load, TAM variables) and integrate them into complementary dimensions, resolving theoretical overlaps. Phase 6 synthesizes these interlinked concepts into a coherent plane of understanding (Theoretical Framework v0.1). Phase 7 represents the validation stage, subjecting the framework to theoretical cross-validation, mathematical proofs, and sensitivity simulations. Finally, Phase 8 incorporates expert feedback to refine the indicators, producing the finalized assessment rubrics. The execution of these phases is inherently iterative, allowing for constant refinement of concepts as new literature is deconstructed. In Phase 1, mapping data sources provides the conceptual raw data from Web of Science, Scopus, and other databases, ensuring a broad multidisciplinary scope. Phases 2 through 5 deconstruct these sources to extract candidate concepts (e.g., washback, cognitive load, TAM variables) and integrate them into complementary dimensions, resolving theoretical overlaps. Phase 6 synthesizes these interlinked concepts into a coherent plane of understanding (Theoretical Framework v0.1). Phase 7 represents the validation stage, subjecting the framework to theoretical cross-validation, mathematical proofs, and sensitivity simulations. Finally, Phase 8 incorporates expert feedback to refine the indicators, producing the finalized assessment rubrics.

\begin{table*}[t]
  \caption{The Eight Phases of Conceptual Framework Analysis (CFA) applied in this study}
  
  \centering
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{@{} L{3.6cm} L{7.3cm} L{4.1cm} @{} }
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

The literature data collection and selection follow Arksey and O'Malley's (2005) five-stage scoping review framework, as mapped in Figure~\ref{fig:scoping_stages}. This process ensures a systematic, reproducible method for compiling the comparative database of evaluation frameworks.

\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig1_scoping_review_stages}
  \caption{Five-stage scoping review process (Arksey \& O'Malley, 2005) showing study-specific execution details.}
  \label{fig:scoping_stages}
\end{figure*}

Following Torraco (2005)~[b8], an integrative review was used to collect conceptual data. Unlike systematic reviews designed to aggregate effect sizes, the integrative review enables conceptual synthesis across empirical and theoretical literature to support theory development. The review protocol was guided by the question: *``What evaluation frameworks exist for digital educational platforms, and what assessment dimensions do they address or neglect in the context of higher education language learning?''* The search string combined keywords addressing educational technology evaluation, university context, and language learning. To operationalize this search, the scoping review protocol is structured around the Population-Concept-Context (PCC) framework recommended by Munn et al. (2018) for scoping reviews. Figure~fig:pcc_dims illustrates the relationship between these PCC scoping review elements and the three analytical dimensions of our theoretical framework. The Population element (learners, instructors, and administrators in higher education) and the Context element (institutional quality assurance and technology procurement) map directly onto the Institutional Governance (INST) dimension. Meanwhile, the Concept element (evaluation frameworks for digital language platforms) bridges the Technology Architecture (TECH) and Pedagogy Effectiveness (PED) dimensions, ensuring that both system quality and educational content are captured. This alignment guarantees that our literature search systematically extracts and maps the intersection of technical, pedagogical, and administrative requirements.

\subsection{Mathematical Framework Specification}

To meet DSR and Type IV theory standards, we specify the formal mathematical structures of the framework:

\subsubsection{Formalization of Coverage Score}
Let $\mathcal{F} = \{F_1, \ldots, F_{12}\}$ represent the set of reviewed frameworks, and $\mathcal{D} = \{D_1, D_2, D_3, D_4, D_6\}$ represent the set of evaluation dimensions. The coding function $s: \mathcal{F} \times \mathcal{D} \to \{0, 0.5, 1.0\}$ determines the *Coverage Score* (CS):
\begin{equation}
  \text{CS}(f) = \sum_{d \in \mathcal{D}} s(f,d), \quad \text{CS}(f) \in [0, 5.0]
\end{equation}
The proposed framework $F^*$ achieves $s(F^*, d) = 1.0$ for all $d$, resulting in $\text{CS}(F^*) = 5.0$. In comparison, the maximum score in the existing corpus is $\max_{f \in \mathcal{F}} \text{CS}(f) = 2.5$. The formulation of the Coverage Score (CS) in Equation~1 serves a vital diagnostic function in our Design Science Research design. By translating qualitative evaluations of existing frameworks into a standardized numeric index, it mathematically demonstrates the extent of the dimensional coverage gaps in the current literature. The coding function $s(f,d)$ scores frameworks based on their operational inclusion of the five key dimensions: D1 (Technology Architecture), D2 (Pedagogy Effectiveness), D3 (Institutional Governance), D4 (High-Stakes Specificity), and D6 (Multi-Stakeholder Perspective). Summing these scores yields an index ($\text{CS} \in [0, 5.0]$) that gauges framework completeness. The fact that the maximum score in the existing literature is only 2.5 establishes the empirical baseline that justifies the development of our proposed framework ($F^*$), which is designed to achieve a maximum score of 5.0.

\subsubsection{Composite Platform Quality Score}
Overall platform quality is formulated as a weighted composite score:
\begin{equation}
  Q_{\text{platform}} = \alpha \cdot Q_{\text{TECH}} + \beta \cdot Q_{\text{PED}} + \gamma \cdot Q_{\text{INST}}
\end{equation}
where $\alpha + \beta + \gamma = 1$, $\alpha, \beta, \gamma > 0$, and each component score is defined as:
\begin{equation}
  Q_{\text{TECH}} = \frac{\sum_{k} w_k \cdot x_k^{\text{TECH}}}{\sum_k w_k}, \quad Q_{\text{PED}} = \frac{\sum_{j} w_j \cdot x_j^{\text{PED}}}{\sum_j w_j}, \quad Q_{\text{INST}} = \frac{\sum_{l} w_l \cdot x_l^{\text{INST}}}{\sum_l w_l}
\end{equation}
where $x_k^{\text{TECH}} \in [0,1]$ is the score of the $k$-th indicator of the TECH dimension, and similarly for the other dimensions. The weight parameters $\alpha, \beta,$ and $\gamma$ represent the priority weights assigned to the technical, pedagogical, and institutional dimensions, respectively, while $w_k, w_j,$ and $w_l$ signify the individual weights allocated to specific indicators. This structure allows the adopting institution to calibrate the audit scores ($Q_{\text{TECH}}, Q_{\text{PED}}, Q_{\text{INST}}$) to fit its strategic procurement goals. The weighted linear formulation in Equation~2 and Equation~3 operationalizes the framework as a multi-criteria decision-support tool. It resolves a common critique of generic educational technology checklists, which typically treat all evaluative items with equal weight, ignoring institutional differences. By utilizing weights ($\alpha, \beta, \gamma$) at the dimensional level and weights ($w_k, w_j, w_l$) at the indicator level, university administrators can customize the platform quality score ($Q_{\text{platform}}$) to match their specific strategic goals. For example, an institution with limited technical support might allocate a higher weight ($\alpha$) to the TECH dimension to prioritize system stability, whereas a university focused on score gains might weight the PED dimension ($\beta$) higher. The division of each dimension score by the sum of its indicator weights in Equation~3 ensures that the resulting scores ($Q_{\text{TECH}}, Q_{\text{PED}}, Q_{\text{INST}}$) are normalized between 0 and 1, facilitating direct comparison and mathematical consistency across platform audits.

\subsubsection{Formal Structural Equations Preview}
The relationships between these quality dimensions and outcomes are previewed below (detailed in Section~sec:structural_model):
\begin{align}
  \text{PU} &= \beta_1 \cdot Q_{\text{TECH}} + \beta_2 \cdot Q_{\text{PED}} + \varepsilon_1 
  \text{SAT} &= \beta_3 \cdot Q_{\text{TECH}} + \beta_4 \cdot Q_{\text{PED}} + \varepsilon_2 
  \text{UX} &= \gamma_1 \cdot Q_{\text{TECH}} + \gamma_2 \cdot Q_{\text{PED}} + \gamma_3 \cdot (Q_{\text{TECH}} \times Q_{\text{PED}}) + \varepsilon_3 
  \text{USE} &= \beta_5 \cdot \text{PU} + \beta_6 \cdot \text{SAT} + \beta_7 \cdot Q_{\text{INST}} + \beta_8 \cdot \text{UX} + \varepsilon_4
\end{align}

The preview of the structural path model in Equations~4--7 establishes the predictive and causal logic of our framework, meeting Gregor's (2006) criteria for a Type IV theory. Rather than treating the platform evaluation dimensions as static checklists, this mathematical structure maps how platform qualities (TECH and PED) act as inputs that drive cognitive-affective responses (Perceived Usefulness, User Satisfaction, and User Experience), which in turn predict usage behaviors (USE) and institutional outcomes. The disturbance terms ($\varepsilon_1$ through $\varepsilon_4$) account for random error and variance not captured by the antecedents. This formal structure provides educational technology researchers with a set of testable path equations that can be empirically validated in future field studies using covariance-based or partial least squares structural equation modeling (SEM).

\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig6_pcc_and_dimensions}
  \caption{PCC Framework elements and analytical dimension grounding.}
  \label{fig:pcc_dims}
\end{figure*}

% ============================================================

---

*Source: Extracted from ethe_main.tex  -  keep synchronized*  
*Status: ✅ Drafted | ☐ Peer-reviewed internally | ☐ Final*
