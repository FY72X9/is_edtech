================================================================================
ANTIGRAVITY IDE - RESEARCH WRITING LOG
================================================================================
PROJECT: Evaluating High-Stakes Language Test Prep Platforms in HE
RESEARCHER: Asus
CURRENT VERSION: v1.2
LAST SESSION: 2026-06-12 17:03:50
CUMULATIVE ENTRIES: 3
TOTAL SECTIONS MODIFIED: 3
================================================================================

================================================================================
LOG ENTRY #1
================================================================================
TIMESTAMP: 2026-06-12 16:57:20 UTC
SESSION ID: f5ce1e6a-4dee-40ac-8f1d-b28db8c7298f
USER QUERY/REQUEST: /writings bab 2 yang banyak formula dan gambar tapi kurang penjelasan. tambahkan agar tidak seperti hanya menuangkan formula dan gambar saja dan minim penjelasan maksud dari gambar dan formula itu apa.

--- SECTION MODIFIED ---
DOCUMENT: docs/latex/journal/ethe_main.tex
SECTION: Section 2 (Methodology: CFA--DSR integrated approach)
PARAGRAPH/LINE: Lines 213--222 (Formal structural equations preview)

--- NATURE OF INTERVENTION ---
TYPE: Expansion / Argumentation Strengthening / Language Elevation

--- BEFORE (Excerpt) ---
\subsubsection{Formal structural equations preview}
The relationships between these quality dimensions and outcomes are previewed below (detailed in Section~\sec:structural_model):
\begin{align}
  \text{PU} &= \beta_1 \cdot Q_{\text{TECH}} + \beta_2 \cdot Q_{\text{PED}} + \varepsilon_1 \\
  \text{SAT} &= \beta_3 \cdot Q_{\text{TECH}} + \beta_4 \cdot Q_{\text{PED}} + \varepsilon_2 \\
  \text{UX} &= \gamma_1 \cdot Q_{\text{TECH}} + \gamma_2 \cdot Q_{\text{PED}} + \gamma_3 \cdot (Q_{\text{TECH}} \times Q_{\text{PED}}) + \varepsilon_3 \\
  \text{USE} &= \beta_5 \cdot \text{PU} + \beta_6 \cdot \text{SAT} + \beta_7 \cdot Q_{\text{INST}} + \beta_8 \cdot \text{UX} + \varepsilon_4
\end{align}

--- AFTER (Excerpt) ---
\subsubsection{Formal structural equations preview}
The relationships between these quality dimensions and outcomes are previewed below (detailed in Section~\ref{sec:structural_model}):
\begin{align}
  \text{PU} &= \beta_1 \cdot Q_{\text{TECH}} + \beta_2 \cdot Q_{\text{PED}} + \varepsilon_1 \\
  \text{SAT} &= \beta_3 \cdot Q_{\text{TECH}} + \beta_4 \cdot Q_{\text{PED}} + \varepsilon_2 \\
  \text{UX} &= \gamma_1 \cdot Q_{\text{TECH}} + \gamma_2 \cdot Q_{\text{PED}} + \gamma_3 \cdot (Q_{\text{TECH}} \times Q_{\text{PED}}) + \varepsilon_3 \\
  \text{USE} &= \beta_5 \cdot \text{PU} + \beta_6 \cdot \text{SAT} + \beta_7 \cdot Q_{\text{INST}} + \beta_8 \cdot \text{UX} + \varepsilon_4
\end{align}

The preview of the structural path model in Equations~(4)--(7) establishes the predictive and causal logic of our framework, meeting Gregor's (2006) criteria for a Type IV theory. Rather than treating the platform evaluation dimensions as static checklists, this mathematical structure maps how platform qualities (TECH and PED) act as inputs that drive cognitive-affective responses (Perceived Usefulness, User Satisfaction, and User Experience), which in turn predict usage behaviors (USE) and institutional outcomes. The disturbance terms ($\varepsilon_1$ through $\varepsilon_4$) account for random error and variance not captured by the antecedents. This formal structure provides educational technology researchers with a set of testable path equations that can be empirically validated in future field studies using covariance-based or partial least squares structural equation modeling (SEM).

--- RATIONALE ---
1. Academic weakness identified: The structural preview formulas were presented without descriptive explanation of their prediction model type, theoretical category under Gregor (2006), or the meaning of their residuals.
2. Theoretical/methodological principle applied: Mapped to Gregor's (2006) Type IV theory (Explanatory and Predictive) to position the causal path equations as testable hypotheses for future structural equation modeling (SEM).
3. Expected enhancement to scholarly quality: The reader receives immediate clarification on the role of platform qualities as antecedents driving cognitive-affective mediators and behavioural outcomes, rather than facing formula-dumping.
4. Preempting reviewer objections: Clarified the inclusion of disturbance terms ($\varepsilon_i$) and specified PLS-SEM/CB-SEM as empirical verification methods.

--- ARGUMENTATIVE ENHANCEMENT ---
- Explicit claim-evidence alignment linking input dimensions (TECH, PED) to individual cognitive states.
- Methodological justification of using testable math path equations.

--- REFERENCES/FRAMEWORKS INVOKED ---
- DeLone & McLean (2003) success model
- Gregor (2006) Type IV Theory framework

STATUS: COMPLETED
================================================================================

================================================================================
LOG ENTRY #2
================================================================================
TIMESTAMP: 2026-06-12 16:58:01 UTC
SESSION ID: f5ce1e6a-4dee-40ac-8f1d-b28db8c7298f
USER QUERY/REQUEST: Synchronization of methodology updates to markdown draft (03-methodology.md)

--- SECTION MODIFIED ---
DOCUMENT: docs/draft/03-methodology.md
SECTION: Sections 2.1, 2.3, and 2.4 (Philosophy, Scoping Review, Math Specification)
PARAGRAPH/LINE: Various lines (added Figure 5 description, Figure 6 description, Eq 1 description, Eq 2 & 3 descriptions, and Equations 4-7 descriptions)

--- NATURE OF INTERVENTION ---
TYPE: Expansion / Content Synchronization

--- BEFORE (Excerpt) ---
...supported by the Design Science Research Methodology (DSRM) guidelines of Peffers et al. (2007)~[b36] for structuring the research process.

\subsection{Eight Phases of CFA in This Study}
...
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig6_pcc_and_dimensions}
  \caption{PCC Framework elements and analytical dimension grounding.}
  
\end{figure*}

--- AFTER (Excerpt) ---
...supported by the Design Science Research Methodology (DSRM) guidelines of Peffers et al. (2007)~[b36] for structuring the research process. The structural flow of this research program is visually mapped in Figure~fig:program_arch. The architecture outlines the connection between our literature dataset, scoping review protocol, and Design Science Research validation. The integrative review (left column) serves as the primary data collection process, producing the corpus of 12 landmark frameworks. These frameworks are then inputted into the Conceptual Framework Analysis (CFA) engine (center column) to deconstruct and integrate concepts across Applied Linguistics and Information Systems. Finally, the resulting framework ($F^*$) is subjected to the three-layer DSR validation scaffold (right column) to evaluate its completeness (theoretical), necessity (mathematical LP proof), and robustness (computational Monte Carlo simulation). This structured path ensures that the resulting evaluation artifact is both theoretically grounded and mathematically validated.

\subsection{Eight Phases of CFA in This Study}
...
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig6_pcc_and_dimensions}
  \caption{PCC Framework elements and analytical dimension grounding.}
  \label{fig:pcc_dims}
\end{figure*}

--- RATIONALE ---
1. Academic weakness identified: The draft methodology section had completely missing figure and formula explanations that are present in the final paper, violating document synchronization rules.
2. Theoretical/methodological principle applied: Ensured structural parity between drafts and primary submissions.
3. Expected enhancement to scholarly quality: Readers of the draft can follow the logical flow and meaning of Figure 5, Figure 6, and the formulas (1), (2), (3), and (4-7) without reading only the LaTeX version.
4. Preempting reviewer objections: Alignment of figure references and descriptions prevents reviewer confusion in early-stage reviews of drafts.

--- ARGUMENTATIVE ENHANCEMENT ---
- Synthesized and aligned all explanations across LaTeX and draft.

--- REFERENCES/FRAMEWORKS INVOKED ---
- DSR (Hevner, 2004)
- PCC Framework (Munn et al., 2018)
- MAUT & LP proofs

STATUS: COMPLETED
================================================================================

================================================================================
LOG ENTRY #3
================================================================================
TIMESTAMP: 2026-06-12 17:04:35 UTC
SESSION ID: f5ce1e6a-4dee-40ac-8f1d-b28db8c7298f
USER QUERY/REQUEST: /humanizer tolong humanize draft latex kita docs/latex/journal/ethe_main.tex

--- SECTION MODIFIED ---
DOCUMENT: docs/latex/journal/ethe_main.tex & docs/draft/*.md
SECTION: Sections 2, 3, 4, 5, 6
PARAGRAPH/LINE: Various lines (replaces AI-isms like "serves as", "align with", "crucial", "yielding", non-locative "where")

--- NATURE OF INTERVENTION ---
TYPE: Language Elevation / Humanization

--- BEFORE (Excerpt) ---
...customise the platform quality score ($Q_{\text{platform}}$) to align with their specific strategic goals...
...which are crucial for score improvement...
...yielding a net utility of 0.600, whereas $F^*$ yields 0.800...

--- AFTER (Excerpt) ---
...customise the platform quality score ($Q_{\text{platform}}$) to match their specific strategic goals...
...which are essential for score improvement...
...producing a net utility of 0.600, whereas $F^*$ generates 0.800...

--- RATIONALE ---
1. Academic weakness identified: Use of post-2023 AI-favored patterns ("align with", "serves as", "crucial", and "yielding" for results) that are flags for AI writing.
2. Theoretical/methodological principle applied: Applied the Wikipedia "Signs of AI writing" academic adaptation.
3. Expected enhancement to scholarly quality: Polishes style to a more natural, traditional, and precise academic register.
4. Preempting reviewer objections: Avoids automatic AI-detection and style filtering by reviewers.

--- ARGUMENTATIVE ENHANCEMENT ---
- Replaces informal phrases ("yielding", "linked to", non-locative "where") with precise connectors ("producing", "associated with", "with").

--- REFERENCES/FRAMEWORKS INVOKED ---
- Custom /humanizer academic writing guidelines

STATUS: COMPLETED
================================================================================
