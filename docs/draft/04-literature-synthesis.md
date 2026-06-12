# Literature Synthesis  -  IS EdTech Main Paper

**Word count target:** ~2000 words  
**Structure:** Literature review map → Gap analysis matrix → Theoretical foundation

---

\subsection{Theoretical Map of CALL Evaluation}

The literature map reveals a fragmented landscape divided by disciplines. Applied Linguistics researchers focus on rich pedagogical models that ignore system architectures~[b1][b2][b3], whereas IS researchers focus on technology acceptance and technical quality while treating pedagogy as generic information quality~[b4][b5]. Learning analytics frameworks address institutional monitoring but are disconnected from second language acquisition (SLA) principles~[b9][b10]. 

This division creates an academic barrier: on one hand, linguists evaluate the *language learning potential* of tools without assessing system architecture reliability, algorithm performance, or mobile responsiveness. On the other hand, information systems researchers employ models like TAM~[b11] or UTAUT to predict adoption, yet fail to integrate variables specific to language testing. A comprehensive framework must bridge this technical-pedagogical divide.

\subsection{Conceptual Gap Analysis}

Table~tab:gaps defines the five principal conceptual gaps identified in the existing literature. These gaps highlight why existing evaluation models are inadequate for high-stakes test preparation. Contextuality (Gap 1) is a critical issue because generic CALL frameworks do not evaluate platforms against psychometric test format standards or spacing algorithms, which are essential for score improvement. Multidisciplinarity (Gap 2) indicates that frameworks remain siloed, forcing practitioners to choose between assessing pedagogical value or system stability. Institutionality (Gap 3) is a major blocker for university adoption, as existing models ignore learning analytics dashboards and LMS integration, preventing administrators from tracking institutional ROI. Structurality (Gap 4) refers to the lack of mapped causal pathways between platform design and user satisfaction, which prevents developers from optimizing specific components. Finally, Operationality (Gap 5) is a common limitation of qualitative checklists, which lack systematic, objective rubrics, leading to high rater subjectivity. These gaps highlight why existing evaluation models are inadequate for high-stakes test preparation. Contextuality (Gap 1) is a critical issue because generic CALL frameworks do not evaluate platforms against psychometric test format standards or spacing algorithms, which are essential for score improvement. Multidisciplinarity (Gap 2) indicates that frameworks remain siloed, forcing practitioners to choose between assessing pedagogical value or system stability. Institutionality (Gap 3) is a major blocker for university adoption, as existing models ignore learning analytics dashboards and LMS integration, preventing administrators from tracking institutional ROI. Structurality (Gap 4) refers to the lack of mapped causal pathways between platform design and user satisfaction, which prevents developers from optimizing specific components. Finally, Operationality (Gap 5) is a common limitation of qualitative checklists, which lack systematic, objective rubrics, leading to high rater subjectivity.

\begin{table}[ht]
  \caption{Identified Conceptual Gaps in the Literature}
  
  \centering
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{@{} C{0.8cm} L{3.6cm} L{9.6cm} @{} }
    \toprule
    **No.** & **Gap** & **Manifestation in the Literature** 
    \midrule
    1 & **Contextuality** & General CALL frameworks lack specific metrics for high-stakes test prep (test standard precision, micro-learning, spaced repetition)~[b1][b3][b5]. 
    2 & **Multidisciplinarity** & Frameworks originate from silos (linguistics vs. IS) without theoretical integration~[b2][b4]. 
    3 & **Institutionality** & Learning analytics and governance decision-support are absent from self-directed platform evaluation~[b9][b10]. 
    4 & **Structurality** & Causal path relationships between design quality, user perception, and outcomes are unmapped~[b11][b12]. 
    5 & **Operationality** & Most frameworks rely on reflective checklists rather than systematic operational definitions~[b6][b13]. 
    \bottomrule
  \end{tabular}
\end{table}

\subsubsection{Coverage Matrix: Empirical Evidence of Conceptual Gaps}

To provide empirical proof of these gaps, Table~tab:matrix maps 12 landmark frameworks against the evaluation dimensions (TECH, PED, INST, High-Stakes specificity, Multi-Stakeholder perspective, and Rigor). An analysis of the matrix reveals that early linguistic models such as Chapelle (2001) (F1), Hubbard (2011) (F2), and Leakey (2011) (F3) offer deep pedagogical coverage but completely ignore institutional governance (D3) and technical architecture (D1). Conversely, IS-centric frameworks like Venkatesh's UTAUT (F10) and Kampa's TRAM (F11) focus on technology acceptance but lack domain-specific language learning metrics (D4) and multi-stakeholder perspectives (D6), treating the learning material as generic information. Furthermore, while governance-focused models like Scheffel et al. (F8) and Park & Jo (F9) provide progress tracking and dashboard monitoring, they are disconnected from SLA pedagogy and technical design. The maximum coverage score among all existing frameworks is only 2.5 out of 5.0, achieved by Almaiah et al. (F6) and Al-Fraihat et al. (F7), but even these models do not address high-stakes test specificity or multi-skill coverage. The proposed framework ($F^*$) is designed to close all these gaps, achieving a full coverage score of 5.0. An analysis of the matrix reveals that early linguistic models such as Chapelle (2001) (F1), Hubbard (2011) (F2), and Leakey (2011) (F3) offer deep pedagogical coverage but completely ignore institutional governance (D3) and technical architecture (D1). Conversely, IS-centric frameworks like Venkatesh's UTAUT (F10) and Kampa's TRAM (F11) focus on technology acceptance but lack domain-specific language learning metrics (D4) and multi-stakeholder perspectives (D6), treating the learning material as generic information. Furthermore, while governance-focused models like Scheffel et al. (F8) and Park & Jo (F9) provide progress tracking and dashboard monitoring, they are disconnected from SLA pedagogy and technical design. The maximum coverage score among all existing frameworks is only 2.5 out of 5.0, achieved by Almaiah et al. (F6) and Al-Fraihat et al. (F7), but even these models do not address high-stakes test specificity or multi-skill coverage. The proposed framework ($F^*$) is designed to close all these gaps, achieving a full coverage score of 5.0.

\begin{table*}[t]
  \caption{Dimensional Coverage Matrix ($✓{}$ Full~=~1.0;\; $○{}$ Partial~=~0.5;\; ×{} Absent~=~0.0.\; D5 Rigor is a separate indicator.)}
  
  \centering
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}} L{4.2cm} C{1.0cm} C{1.0cm} C{1.0cm} C{1.5cm} C{1.8cm} C{1.2cm} C{1.2cm} @{}}
    \toprule
    **Framework** & **D1 TECH** & **D2 PED** & **D3 INST** & **D4 High-Stakes** & **D6 Multi-Stakeholder** & **Score /5.0** & **D5 Rigor** 
    \midrule
    F1 Chapelle (2001)~[b1] & × & ✓ & × & ○ & × & 1.5 & ○ 
    F2 Hubbard (2011)~[b2] & × & ✓ & × & × & × & 1.0 & ○ 
    F3 Leakey (2011)~[b3] & ○ & ✓ & × & × & × & 1.5 & ○ 
    F4 Colpaert (2004)~[b41] & × & ✓ & × & × & × & 1.0 & ○ 
    F5 Rosell-Aguilar (2017)~[b5] & ○ & ○ & × & × & × & 1.0 & × 
    F6 Almaiah et al. (2021)~[b42] & ✓ & ○ & ○ & × & ○ & 2.5 & × 
    F7 Al-Fraihat et al. (2020)~[b4] & ✓ & ○ & ○ & × & ○ & 2.5 & ○ 
    F8 Scheffel et al. (EFLA) (2014)~[b9] & × & × & ✓ & × & ○ & 1.5 & ○ 
    F9 Park & Jo (LAD) (2019)~[b10] & × & × & ✓ & × & ○ & 1.5 & ○ 
    F10 UTAUT/Venkatesh (2003)~[b43] & ○ & × & × & × & × & 0.5 & × 
    F11 TRAM/Kampa (2023)~[b44] & ○ & ○ & × & × & × & 1.0 & × 
    F12 Essafi/MLLA (2025)~[b45] & ○ & ✓ & × & ○ & × & 2.0 & × 
    \midrule
    **Proposed Framework ($F^*$)** & **✓** & **✓** & **✓** & **✓** & **✓** & **5.0** & **✓** 
    \bottomrule
  \end{tabular*}
\end{table*}

\subsection{Meta-Theoretical Foundation: DeLone & McLean IS Success Model}

To avoid an arbitrary selection of dimensions, the framework is grounded in the **DeLone & McLean IS Success Model** (D&M, 2003)~[b31]. D&M posits that IS success depends on three quality constructs: System Quality, Information Quality, and Service Quality. These are deductively mapped to our three core dimensions as shown in Table~tab:dm_mapping. The theoretical rationale for this mapping is grounded in the causal logic of the D&M model: system, information, and service qualities are the three primary inputs that determine how users interact with and benefit from an information system. In the context of language test preparation, System Quality corresponds to the technical foundation (TECH), as system reliability, latency, and mobile responsiveness are prerequisites for user interaction. Information Quality corresponds to pedagogical content (PED) because the educational material (conforming to CEFR bands and containing diagnostic feedback) represents the primary information resource. Service Quality corresponds to institutional support (INST) because progress monitoring, LMS integration, and administrative reporting are the primary service mechanisms that universities require to support the platform's adoption.
\begin{itemize}
  \item **Technology Architecture (TECH)** maps to *System Quality* (stability, adaptivity, and interface reliability).
  \item **Pedagogy Effectiveness (PED)** maps to *Information Quality* (relevance, accuracy, and utility of learning material).
  \item **Institutional Governance (INST)** maps to *Service Quality* (monitoring tools, integration, and institutional support).
\end{itemize}

\begin{table}[ht]
  \caption{Deductive Mapping of DeLone & McLean (2003) Model to proposed EdTech Dimensions}
  
  \centering
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{@{} L{3.5cm} L{6.0cm} L{4.5cm} @{} }
    \toprule
    **D&M Construct** & **Operationalization in Language EdTech** & **Framework Dimension** 
    \midrule
    System Quality & Technical reliability, adaptive algorithm performance, interface layout, mobile responsiveness & Technology Architecture (TECH) 
    Information Quality & Pedagogical content quality: standard conformity, automated diagnostics, cognitive load management, skill coverage & Pedagogy Effectiveness (PED) 
    Service Quality & Academic governance support: progress dashboard, LMS interoperability, monitoring alerts, decision reporting & Institutional Governance (INST) 
    Net Benefits & Individual language capability improvement (Language Learning Potential) and institutional adoption success & Outcome 
    \bottomrule
  \end{tabular}
\end{table}

This mapping ensures that the framework's dimensions are theoretically grounded. D&M has been empirically validated across educational technologies, showing that system, information, and service qualities jointly determine system usage and user satisfaction, which in turn drive net benefits~[b32].

\subsection{Boundary Conditions of D&M: Why CALL and SLA Theory Remain Essential}

While D&M provides an ontological scaffold, it does not define domain-specific parameters. D&M treats information quality generically, whereas language test preparation requires specific conformity to psychometric test format standards (e.g., IELTS rubrics). Similarly, D&M's service quality does not capture the academic governance requirements of higher education institutions (e.g., learning analytics and Early Warning Systems). Therefore, CALL theory~[b1], SLA principles, and learning analytics frameworks~[b9] are necessary to fill these domain gaps, acting as complementary extensions to D&M. Table~tab:dm_boundaries defines the boundary conditions and specific theoretical fillers. This integration is necessary because while the D&M success model provides a general ontological scaffold, its constructs are too broad and generic for language learning technology. D&M treats System Quality as technical infrastructure, but in EdTech, system design must minimize extraneous cognitive load and support mobile-assisted learning (MALL) design. Similarly, D&M's Information Quality does not specify SLA principles (such as language learning potential, authentic task design, and washback effects), which are necessary to drive actual capability improvement. Finally, Service Quality in D&M represents IT support, whereas universities require academic governance tools, progress tracking dashboards, and early warning systems. Therefore, we integrate SLA theory (Chapelle, 2001) and learning analytics frameworks (Scheffel, 2014) to fill these domain gaps, extending the boundaries of the D&M model. This integration is necessary because while the D&M success model provides a general ontological scaffold, its constructs are too broad and generic for language learning technology. D&M treats System Quality as technical infrastructure, but in EdTech, system design must minimize extraneous cognitive load and support mobile-assisted learning (MALL) design. Similarly, D&M's Information Quality does not specify SLA principles (such as language learning potential, authentic task design, and washback effects), which are necessary to drive actual capability improvement. Finally, Service Quality in D&M represents IT support, whereas universities require academic governance tools, progress tracking dashboards, and early warning systems. Therefore, we integrate SLA theory (Chapelle, 2001) and learning analytics frameworks (Scheffel, 2014) to fill these domain gaps, extending the boundaries of the D&M model.

\begin{table}[ht]
  \caption{Boundary Conditions of DeLone & McLean Model and Domain-Specific Extensions}
  
  \centering
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{@{} L{3.5cm} L{5.0cm} L{5.5cm} @{} }
    \toprule
    **D&M Construct** & **D&M Boundary Limitation** & **Domain-Specific Theoretical Filler** 
    \midrule
    Information Quality & Fails to define quality for the SLA domain & CALL theory (Chapelle, 2001)~[b1]; Language Learning Potential; Washback Theory~[b21] 
    Service Quality & Does not operationalise academic governance & EFLA (Scheffel et al., 2014)~[b9]; IT Governance (Tornatzky & Fleischer, 1990)~[b18] 
    Net Benefits & Broadly defined at organizational/individual levels & Language Learning Potential + Institutional Adoption Intention 
    \bottomrule
  \end{tabular}
\end{table}

\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig4_coverage_matrix_heatmap}
  \caption{Heatmap of the dimensional coverage matrix showing the gaps across reviewed frameworks.}
\end{figure*}

\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{fig5_coverage_scores_ranked}
  \caption{Ranked coverage scores of reviewed frameworks.}
\end{figure}

\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig6_coverage_gaps_diagram}
  \caption{Theoretical gap diagram highlighting the unaddressed conceptual areas.}
\end{figure*}

% ============================================================

---

*Source: Extracted from ethe_main.tex  -  keep synchronized*  
*Status: ✅ Drafted | ☐ Peer-reviewed internally | ☐ Final*
