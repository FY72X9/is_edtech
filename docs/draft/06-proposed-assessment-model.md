# Proposed assessment model  -  IS EdTech Main Paper

**Word count target:** ~1000 words  
**Structure:** Operational indicators → Definitions → Assessment rubrics

---

\subsection{Assessment Model Philosophy}

 The assessment model acts as a theoretical rubric with operational definitions. It is conceptual-interpretive, designed to guide evaluations and support future scale development.

\subsection{Assessment Model Hierarchy}

The proposed model establishes a three-tier hierarchy consisting of:
\begin{enumerate}
  \item **Dimensions**: The three meta-theoretical quality pillars derived from D&M (TECH, PED, INST).
  \item **Indicators**: The 15 operationalized constructs representing specific platform capabilities (5 indicators per dimension).
  \item **Criteria**: The concrete evaluation guidelines (e.g., response latency under load, prompt stability, CEFR level precision) used by raters to assess platform performance.
\end{enumerate}

\subsection{Operational Definitions Matrix}

Table~tab:rubric presents the indicators, operational definitions, source theories, and evaluative uses.

\begin{table*}[t]
  \caption{Assessment Model Rubric and Operational Definitions}
  
  \centering
  \renewcommand{\arraystretch}{1.3}
  \small
  \renewcommand{\arraystretch}{1.1}
  \begin{tabular}{@{} L{2.0cm} L{5.4cm} L{3.1cm} L{3.1cm} @{} }
    \toprule
    **Indicator** & **Operational Definition** & **Source Theory** & **Evaluative Use** 
    \midrule
    **TECH-1** Stability & Reliability of platform architecture under load & ISO 25010~[b14] & Server uptime and response latency audit 
    **TECH-2** Interface & Ease of interaction and accessibility compliance & TAM~[b11]; Sweller~[b16] & Cognitive walkthrough and usability evaluation 
    **TECH-3** Adaptivity & IRT-based difficulty calibration and prompt stability & Adaptive Learning~[b15]; GenAI~[b37][b40] & Item difficulty calibration and prompt stability audit 
    **TECH-4** Multimedia & Quality of audio/graphics supporting listening/reading & Dual Coding~[b19]; Mayer~[b20] & Content media quality assessment 
    **TECH-5** Mobile & Responsive design and offline-first capabilities & MALL~[b5] & Accessibility and offline function check 
    \midrule
    **PED-1** Conformity & Materials matching IELTS/TOEFL standard rubrics & Authenticity~[b1]; Washback~[b21] & Item format and CEFR level matching 
    **PED-2** Feedback & Timeliness, diagnostic precision, and AI bias detection & Hattie & Timperley~[b17]; LLMs~[b38][b39] & Actionability review and AI hallucination detection 
    **PED-3** Micro-learning & Modular units designed for 5--15 minute sessions & Sweller~[b16]; Hug~[b22] & Session length and structural modularity check 
    **PED-4** Spacing & Performance-based spaced interval scheduling & Spacing Effect~[b23] & Forgetting-curve algorithm logic audit 
    **PED-5** Cognitive & Balancing extraneous and germane cognitive load & Sweller~[b16] & Task interface cognitive load inspection 
    **PED-6** Motivation & Auto-determination mechanics and anxiety reduction & SDT~[b12]; Flow~[b24] & Gamification and progress UI evaluation 
    **PED-7** Skills & Commensurate coverage of reading, writing, listening, speaking & CLT~[b25] & Multi-skill test matrix audit 
    \midrule
    **INST-1** Analytics & Progress data dashboards for academic staff & EFLA~[b9] & Visual representation granularity review 
    **INST-2** Interoperability & Integration with LMS/SIAKAD through LTI/API standards & IMS Standards~[b26] & Technical connection protocol audit 
    **INST-3** Monitoring & Student tracking and Early Warning alert triggers & Early Warning~[b27] & Risk alert threshold check 
    **INST-4** Decision & Reporting cost-utility and ROI metrics for renewal & IT Governance~[b18]; Diffusion~[b29] & Report layout and data export evaluation 
    **INST-5** Scalability & Capacity to scale infrastructure without latency spikes & Technology Sustainability~[b28] & Load architecture review 
    \bottomrule
  \end{tabular}
\end{table*}

The fifteen indicators in Table~\ref{tab:rubric} provide a systematic rubric for assessing platform performance across the three core dimensions. In the TECH dimension, Stability (TECH-1) and Adaptivity (TECH-3) are critical: Stability is assessed through server uptime and latency logs, while Adaptivity evaluates whether the platform's adaptive algorithm matches user proficiency levels (using Item Response Theory) and ensures prompt stability when using generative AI for speaking or writing practice. Under the PED dimension, Conformity (PED-1) and Feedback (PED-2) represent domain-specific language learning metrics: Conformity checks whether tasks conform to standardized IELTS/TOEFL rubrics, while Feedback measures the diagnostic accuracy and bias-detection of automated feedback systems. Under the INST dimension, Analytics (INST-1) and Decision-support (INST-4) enable academic monitoring and administrative evaluation, providing data-driven reports on ROI and cost-utility for renewal decisions.

The fifteen indicators in Table~\ref{tab:rubric} provide a systematic rubric for assessing platform performance across the three core dimensions. In the TECH dimension, Stability (TECH-1) and Adaptivity (TECH-3) are critical: Stability is assessed through server uptime and latency logs, while Adaptivity evaluates whether the platform's adaptive algorithm matches user proficiency levels (using Item Response Theory) and ensures prompt stability when using generative AI for speaking or writing practice. Under the PED dimension, Conformity (PED-1) and Feedback (PED-2) represent domain-specific language learning metrics: Conformity checks whether tasks conform to standardized IELTS/TOEFL rubrics, while Feedback measures the diagnostic accuracy and bias-detection of automated feedback systems. Under the INST dimension, Analytics (INST-1) and Decision-support (INST-4) enable academic monitoring and administrative evaluation, providing data-driven reports on ROI and cost-utility for renewal decisions.

% ============================================================

---

*Source: Extracted from ethe_main.tex  -  keep synchronized*  
*Status: ✅ Drafted | ☐ Peer-reviewed internally | ☐ Final*
