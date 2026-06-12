# Discussion  -  IS EdTech Main Paper

**Word count target:** ~1200 words  
**Structure:** Interpretation of results → Theoretical and practical implications

---

\subsection{Synthesis of answers to the research questions}

To establish the scientific validity of this conceptual study, we explicitly map our findings to the three conceptual research questions formulated in Section~sec:intro:
\begin{enumerate}
  \item \textbf{Addressing RQ1 (Theoretical Framework Construction):} The integration of technology acceptance, SLA, and learning analytics theories was accomplished by grounding the framework in the DeLone \& McLean model, which maps System Quality to TECH, Information Quality to PED, and Service Quality to INST. The necessity of this multidisciplinary synthesis was mathematically proven in Lemma 1, demonstrating that no combination of the 12 existing frameworks in the literature can close the coverage gap on the D4 (High-Stakes Specificity) and D6 (Multi-Stakeholder) dimensions (convex combination bound CS $\le$ 0.5).
  \item \textbf{Addressing RQ2 (Assessment Model and Operational Rubrics):} The formulation of the 15 indicators in Table~tab:rubric operationalizes the framework into a practical decision-support tool. The operational clarity and objectivity of these rubrics were validated through a simulated inter-rater reliability test. The resulting Cohen's Kappa ($\kappa = 0.7917$, Observed Agreement = 86.67\%) indicates substantial agreement, confirming that the indicators are sufficiently clear and objective to guide diverse raters to nearly identical evaluation outcomes.
  \item \textbf{Addressing RQ3 (Structural Model and Causal Path Mapping):} The path model mapped the causal relationships between quality inputs, cognitive-affective mediators (PU, SAT, UX), and adoption outcomes (individual and organizational net benefits). This structural mapping was computationally validated through Monte Carlo robustness simulations, demonstrating that the proposed framework ($F^*$) maintains Pareto dominance ($P > 0.8580$) even under implementation leakage, and scenario utility optimization (Table~tab:scenarios) proving it is the mathematically optimal choice under varying strategic preferences.
\end{enumerate}

\subsection{Theoretical contributions}

This study makes four theoretical contributions:
\begin{enumerate}
  \item **Multidisciplinary Synthesis**: It integrates technology acceptance, cognitive load, and SLA theories into a single ontological architecture, bridging the technical-pedagogical divide~[b4][b6].
  \item **Contextual Specificity**: It provides contextual specificity for high-stakes test preparation by operationalizing standards conformity, spaced repetition, and micro-learning design~[b1][b3][b5][b29].
  \item **Formal Structural Model**: It defines a Type IV causal model with structural equations and mathematical validation proofs, establishing a solid foundation for future empirical testing~[b11][b12].
  \item **Methodological Integration**: It integrates CFA and DSR into a hybrid framework validation approach (comprising theoretical, mathematical, and computational layers) that provides a template for other IS research projects~[b34][b35].
\end{enumerate}

\subsection{Conceptual Practical Implications}

The model carries practical implications for developers, instructors, and administrators. Table~tab:implications defines the implications and use guidelines for each stakeholder group. For EdTech developers, the framework acts as a set of design specifications, moving them away from ad-hoc feature development toward building platforms that conform to psychometric standards, support adaptive spacing algorithms, and maintain software stability under load. For university administrators, the model provides a rigorous, evidence-based quality assurance benchmark, justifying technology procurement decisions and protecting institutional investments by analyzing ROI and LMS integration costs before signing contracts. For researchers in educational technology, the framework bridges the CALL-IS disciplinary divide and provides the theoretical foundation for empirical field studies, allowing them to use the structural equations (Propositions P1--P8) as a basis for path modeling (PLS-SEM) on multi-institutional user data. For EdTech developers, the framework acts as a set of design specifications, moving them away from ad-hoc feature development toward building platforms that conform to psychometric standards, support adaptive spacing algorithms, and maintain software stability under load. For university administrators, the model provides a rigorous, evidence-based quality assurance benchmark, justifying technology procurement decisions and protecting institutional investments by analyzing ROI and LMS integration costs before signing contracts. For researchers in educational technology, the framework bridges the CALL-IS disciplinary divide and provides the theoretical foundation for empirical field studies, allowing them to use the structural equations (Propositions P1--P8) as a basis for path modeling (PLS-SEM) on multi-institutional user data.

\begin{table*}[t]
  \caption{Practical Implications and Utilization of the Framework}
  
  \centering
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{@{} L{3.0cm} L{5.5cm} L{5.5cm} @{} }
    \toprule
    **Stakeholder** & **Practical Implication** & **Framework Utilization** 
    \midrule
    **EdTech Developers** & Evidence-based architectural and design guidelines & Apply TECH and PED rubrics as system design specifications. 
    **University Administrators** & Justification for adoption and quality assurance benchmarks & Apply INST rubrics and structural model for platform benchmarking. 
    **Researchers** & Theoretical foundation for empirical field studies & Apply propositions P1--P8 as testable hypotheses for SEM analysis. 
    \bottomrule
  \end{tabular}
\end{table*}

\subsection{Conceptual Limitations and Future Research Directions}

As a conceptual model, the study has several limitations: (a) the causal paths are theoretical and require empirical field validation; (b) the indicators require psychometric validation through factor analysis; (c) generalizability across different educational contexts needs empirical verification; and (d) the framework focuses on Anglophone high-stakes tests (IELTS/TOEFL). Applying it to regional or non-English tests requires re-operationalizing PED-1.

To address these limitations, we propose six future research directions:
\begin{enumerate}
  \item **Expert Validation**: Conducting Delphi or Nominal Group Technique reviews with applied linguistics and IS experts to validate the content and face validity of the framework.
  \item **Scale Development**: Developing Likert scales for the 15 indicators and testing their psychometric properties (Confirmatory Factor Analysis and Cronbach's alpha).
  \item **Structural Model Testing**: Validating propositions P1--P8 using Partial Least Squares SEM (PLS-SEM) on multi-institutional survey data.
  \item **Cross-Platform Adaptation**: Modifying PED-1, PED-7, and INST categories to evaluate platforms for general language acquisition, academic writing, or business communication.
  \item **GenAI Integration Dimensions**: Developing a dedicated dimension for Large Language Models (LLMs) and Generative AI, tentatively labeled *AI-Augmented Assessment Capability* (D4-AI), to evaluate automated writing scoring, conversational speaking agents, and hallucination control in platforms post-2025~[b37][b38][b39][b40].
  \item **Cross-Cultural Validation**: Testing the framework in non-Western HE institutions (e.g., Southeast Asia, Latin America) to evaluate its robustness under varying technological infrastructure and academic policies.
\end{enumerate}

% ============================================================

---

*Source: Extracted from ethe_main.tex  -  keep synchronized*  
*Status: ✅ Drafted | ☐ Peer-reviewed internally | ☐ Final*
