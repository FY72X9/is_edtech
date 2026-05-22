--

# **CONCEPT DRAFT v0.1 — PURELY CONCEPTUAL**

## **A Theoretical Framework and Assessment Model for Evaluating High-Stakes Language Test Preparation Platforms in Higher Education: A Conceptual Framework Analysis**

---

## **1. INTRODUCTION**

### **1.1. Background and Conceptual Gap**

Higher education in the digital era faces a fundamental challenge in evaluating the EdTech platforms adopted for *high-stakes* language test preparation — specifically IELTS and TOEFL. The literature indicates that existing *Computer-Assisted Language Learning* (CALL) platform evaluation is fragmented: it either centres on linguistic aspects without considering information systems architecture, or conversely skews too technical without interrogating pedagogical validity [1][2]. This gap is compounded by the absence of any evaluation framework explicitly designed for the *test preparation* context, which demands precision metrics for *micro-learning*, *spaced repetition*, and alignment with international test standards [3].

A survey of the *International Journal of Educational Technology in Higher Education* (ETHE) and other leading *educational technology* journals reveals that conceptual research developing *theoretical frameworks* and *assessment models* for self-directed learning technologies receives significant attention — particularly when it bridges the disciplines of Information Systems and Applied Linguistics [4][5]. Yet to date, no *theoretical framework* explicitly integrates the technology, pedagogy, and institutional dimensions into a single evaluation model for language test preparation platforms.

### **1.2. Conceptual Research Questions**

Based on the gap identification above, three conceptual research questions are examined:

1. **How can a *theoretical framework* be constructed that synthesises technology acceptance theory, computer-assisted language learning theory, and *learning analytics* theory for evaluating high-stakes language test preparation platforms?**

2. **How can an *assessment model* be formulated — with indicators and operational definitions — capable of evaluating platforms from a multi-stakeholder perspective (learners, instructors, administrators) at the conceptual level?**

3. **How can the theoretical relationships among evaluation dimensions be mapped in a conceptual structural model that is amenable to empirical testing in the future?**

### **1.3. Research Objectives**

| **Objective** | **Conceptual Output** |
|:---|:---|
| TK1 | Synthesise multidisciplinary literature to identify core platform evaluation concepts |
| TK2 | Construct a multidimensional *theoretical framework* through *conceptual framework analysis* |
| TK3 | Formulate an *assessment model* with evaluation rubrics and operational definitions |
| TK4 | Develop a conceptual structural model with theoretical propositions for future empirical testing |

---

## **2. METHODOLOGY: CONCEPTUAL FRAMEWORK ANALYSIS**

### **2.1. Philosophy and Approach**

This study adopts **Conceptual Framework Analysis (CFA)** as proposed by Jabareen (2009) — a qualitative method for constructing conceptual frameworks for multidisciplinary phenomena [6]. Unlike empirically oriented predictive research, CFA is interpretive, concept-based (rather than variable-based), and emphasises deep understanding of complex phenomena through networks of interlinked concepts [6][7].

```mermaid
graph LR
    subgraph "Jabareen's Eight-Phase CFA (2009)"
        A[1. Mapping Data Sources] --> B[2. Extensive Reading & Categorization]
        B --> C[3. Identifying Concepts]
        C --> D[4. Deconstructing Concepts]
        D --> E[5. Integrating Concepts]
        E --> F[6. Synthesis & Resynthesis]
        F --> G[7. Validation]
        G --> H[8. Rethinking & Revision]
    end
    
    style A fill:#e3f2fd
    style B fill:#e3f2fd
    style C fill:#e3f2fd
    style D fill:#e3f2fd
    style E fill:#e3f2fd
    style F fill:#e3f2fd
    style G fill:#e3f2fd
    style H fill:#e3f2fd
```

### **2.2. Eight Phases of CFA in This Study**

| **Phase** | **Procedure** | **Output** |
|:---|:---|:---|
| **1. Mapping Data Sources** | *Systematic Literature Review* (SLR) following the PRISMA 2020 protocol [8] across Scopus, Web of Science, ERIC, and IEEE Xplore databases, using search strings related to CALL evaluation, TAM language learning, learning analytics assessment, and high-stakes testing technology | Literature corpus map and primary literature corpus |
| **2. Extensive Reading & Categorization** | Classification of literature by discipline of origin (applied linguistics, information systems, education, cognitive psychology) and framework type (evaluative, predictive, design, adoption) | Literature categorisation matrix |
| **3. Identifying Concepts** | Extraction of core concepts that recur significantly: *language learning potential*, *learner fit*, *perceived usefulness*, *cognitive load*, *learning analytics*, *institutional adoption* | List of candidate concepts |
| **4. Deconstructing Concepts** | Component, historical, and relational analysis of each concept based on its source theory (e.g. *cognitive load* from Sweller; *perceived usefulness* from Davis) | Componential definition per concept |
| **5. Integrating Concepts** | Integration of concepts from different disciplines into mutually complementary evaluation dimensions | Preliminary framework dimensions |
| **6. Synthesis & Resynthesis** | Construction of a *network of interlinked concepts* forming a *plane of understanding* of the platform evaluation phenomenon | Theoretical framework v0.1 |
| **7. Validation** | *Expert validation* through a *nominal group technique* or conceptual *Delphi method* with domain experts to assess *content validity* and *logical coherence* of the framework | Validated framework v0.2 |
| **8. Rethinking & Revision** | Iterative revision based on expert input and *cross-mapping* with existing frameworks to ensure *novelty* and *non-redundancy* | Final theoretical framework |

### **2.3. Systematic Literature Review (SLR as Data Source)**

```mermaid
graph TD
    subgraph "SLR as Data Source for CFA"
        A[Identification<br/>Scopus, WoS, ERIC, IEEE] -->|n=...| B[Screening<br/>Title & Abstract]
        B -->|Excluded| C[Irrelevant]
        B -->|n=...| D[Eligibility<br/>Full-text Review]
        D -->|Excluded| E[No framework/theory<br/>Empirical-only<br/>Non-English]
        D -->|n=...| F[Included Studies<br/>Framework Analysis]
        
        F --> G[CALL Evaluation Frameworks]
        F --> H[Technology Acceptance Models]
        F --> I[Learning Analytics Frameworks]
        F --> J[Cognitive Load & Gamification]
        F --> K[Institutional Adoption Models]
        
        G --> L[Data Extraction<br/>Concepts, Dimensions, Indicators]
        H --> L
        I --> L
        J --> L
        K --> L
        
        L --> M[Conceptual Framework<br/>Analysis Input]
    end
    
    style A fill:#fff3e0
    style B fill:#fff3e0
    style D fill:#fff3e0
    style F fill:#fff3e0
    style L fill:#fff3e0
    style M fill:#ffcc80
```

---

## **3. LITERATURE SYNTHESIS: MAPPING EXISTING FRAMEWORKS**

### **3.1. Theoretical Map of CALL Evaluation**

```mermaid
graph TD
    subgraph "Existing Frameworks Mapped by Discipline & Focus"
        A[CALL Evaluation] --> B[Chapelle 2001<br/>SLA-based 6 Criteria]
        A --> C[Hubbard 2011<br/>Process-oriented]
        A --> D[Leakey 2011<br/>Integrated 12 Criteria]
        A --> E[McMurry 2016<br/>Formal Evaluation]
        
        F[Mobile/CALL Apps] --> G[Rosell-Aguilar 2017<br/>MALL Taxonomy]
        F --> H[Essafi 2025<br/>MLLA 3-Aspect]
        F --> I[Almaiah 2021<br/>Delphi 6-Dimension]
        
        J[Tech Acceptance] --> K[Davis 1989<br/>TAM]
        J --> L[Venkatesh 2003<br/>UTAUT]
        J --> M[Kampa 2024<br/>TRAM Language Ed]
        
        N[Learning Analytics] --> O[Scheffel 2014<br/>EFLA]
        N --> P[Park & Jo 2019<br/>LAD Kirkpatrick]
        
        Q[Design & Pedagogy] --> R[Colpaert 2004<br/>RBRO Model]
        Q --> S[Mishra 2006<br/>TPACK]
    end
    
    style A fill:#e8f5e9
    style B fill:#e8f5e9
    style C fill:#e8f5e9
    style D fill:#e8f5e9
    style E fill:#e8f5e9
    style F fill:#e1f5fe
    style G fill:#e1f5fe
    style H fill:#e1f5fe
    style I fill:#e1f5fe
    style J fill:#fff3e0
    style K fill:#fff3e0
    style L fill:#fff3e0
    style M fill:#fff3e0
    style N fill:#fce4ec
    style O fill:#fce4ec
    style P fill:#fce4ec
    style Q fill:#f3e5f5
    style R fill:#f3e5f5
    style S fill:#f3e5f5
```

### **3.2. Conceptual Gap Analysis**

Based on the deconstruction of existing frameworks through CFA, five principal conceptual gaps are identified:

| **No.** | **Conceptual Gap** | **Manifestation in Literature** |
|:---:|:---|:---|
| 1 | **Contextuality** | CALL/MALL frameworks are generic; none explicitly specifies metrics for *high-stakes testing preparation* (test standard precision, *micro-learning*, *spaced repetition*) [1][3][5] |
| 2 | **Multidisciplinarity** | Frameworks originate from disciplinary silos: linguistics (Chapelle, Leakey) or information systems (Almaiah) without theoretical synthesis that integrates both [2][4] |
| 3 | **Institutionality** | *Learning analytics* and *decision-making* aspects for institutional administrators are almost entirely absent from self-directed learning evaluation frameworks [9][10] |
| 4 | **Structurality** | The relationships among dimensions (e.g. how technology quality affects learning through motivation mediation) have not been mapped in a conceptual causal model for this context [11][12] |
| 5 | **Operationality** | Many frameworks take the form of reflective checklists without adequate operational definitions for systematic measurement [6][13] |

---

## **4. PROPOSED THEORETICAL FRAMEWORK**

### **4.1. Framework Philosophy**

This framework is conceptualised as a **network of interlinked concepts** that is interpretive and indeterminate [6]. Each dimension is not an independent/dependent variable in the quantitative sense, but rather a **mutually articulating concept** providing comprehensive understanding of the platform evaluation phenomenon [6][7].

```mermaid
graph TB
    subgraph "PROPOSED THEORETICAL FRAMEWORK<br/>Network of Interlinked Concepts"
        A[Platform Evaluation<br/>as Multidimensional Phenomenon] --> B[Concept: Technology<br/>Architecture]
        A --> C[Concept: Pedagogy<br/>Effectiveness]
        A --> D[Concept: Institutional<br/>Governance]
        
        B --> B1[System Stability]
        B --> B2[Interface Quality]
        B --> B3[Adaptive Algorithm]
        B --> B4[Multimedia Integration]
        B --> B5[Mobile Accessibility]
        
        C --> C1[Test Standards Alignment]
        C --> C2[Automated Feedback Quality]
        C --> C3[Micro-Learning Design]
        C --> C4[Spaced Repetition]
        C --> C5[Cognitive Load Management]
        C --> C6[Motivation & Engagement]
        C --> C7[Skill Coverage]
        
        D --> D1[Analytics Dashboard]
        D --> D2[Data Interoperability]
        D --> D3[Instructor Monitoring]
        D --> D4[Administrative Decision-Support]
        D --> D5[Sustainability]
        
        %% Cross-cutting concepts
        E[Concept: User Experience] -.-> B
        E -.-> C
        F[Concept: Language Learning Potential] -.-> C
        G[Concept: Perceived Usefulness] -.-> B
        G -.-> C
        H[Concept: Practicality] -.-> D
        
        %% Interlinkages
        B3 -.->|enables| C3
        B3 -.->|enables| C4
        C2 -.->|feeds| D1
        D3 -.->|informs| C6
        C5 -.->|moderates| C6
    end
    
    style A fill:#ffe0b2
    style B fill:#e1f5fe
    style C fill:#e8f5e9
    style D fill:#f3e5f5
    style E fill:#fff8e1
    style F fill:#fff8e1
    style G fill:#fff8e1
    style H fill:#fff8e1
```

### **4.2. Theoretical Justification per Dimension**

#### **Dimension 1: Technology Architecture (TECH)**

This dimension synthesises *Human-Computer Interaction* (HCI) theory, the *Technology Acceptance Model* (TAM), and technical CALL evaluation criteria [1][2][11]. The concept of *System Stability* is adopted from software engineering evaluation frameworks that foreground system reliability as a prerequisite for the *learning experience* [14]. *Adaptive Algorithm* derives from *intelligent tutoring systems* and *adaptive learning* theory, which hold that content personalisation is a primary determinant of self-directed learning effectiveness [15]. *Interface Quality* — grounded in *zero UI* and minimalist design principles — is integrated from *cognitive load* theory, which holds that complex interfaces increase *extraneous cognitive load* and reduce available capacity for language processing [16].

#### **Dimension 2: Pedagogy Effectiveness (PED)**

This dimension synthesises *Second Language Acquisition* (SLA) theory from Chapelle [1], feedback theory from Hattie & Timperley [17], and *micro-learning* theory from the *mobile learning* literature [5]. *Test Standards Alignment* is a necessary concept because in *high-stakes testing* contexts, material *authenticity* extends beyond communicative relevance to encompass alignment with the format, rubrics, and *band descriptors* of the target test [3]. *Cognitive Load Management* is adopted from Sweller to ensure that pedagogical design does not overburden the learner's *working memory* [16]. *Motivation & Engagement* is integrated from *Self-Determination Theory* (SDT), which holds that *autonomy*, *competence*, and *relatedness* mediate learner engagement on self-directed platforms [12].

#### **Dimension 3: Institutional Governance (INST)**

This dimension synthesises the *Evaluation Framework for Learning Analytics* (EFLA) [9], Tornatzky & Fleischer's theory of *organisational adoption of IT* [18], and a *university governance* perspective from the *educational technology in higher education* literature [4][10]. *Analytics Dashboard* and *Instructor Monitoring* concepts derive from EFLA, which emphasises that analytic tools must generate *awareness*, *reflection*, and *impact* not only for learners but also for instructors [9]. *Administrative Decision-Support* is integrated from *IT governance* literature, which holds that the adoption of educational technology in institutions requires *evidence-based justification* for resource allocation [18].

### **4.3. Cross-Cutting Concepts**

| **Concept** | **Theoretical Origin** | **Function in Framework** |
|:---|:---|:---|
| *Language Learning Potential* | Chapelle (2001) [1] | Central criterion articulating all pedagogical dimensions |
| *Perceived Usefulness & Ease of Use* | Davis (1989) [11] | Linking concept between technology architecture and learner engagement |
| *User Experience* | Rosell-Aguilar (2017) [5] | Holistic concept articulating the quality of learner interaction with technology and pedagogy |
| *Practicality* | Chapelle (2001) [1]; Hubbard (2011) [2] | Concept articulating the feasibility of institutional implementation in real contexts |

---

## **5. PROPOSED ASSESSMENT MODEL**

### **5.1. Assessment Model Philosophy**

The assessment model is conceptualised as a **theoretical rubric** comprising dimensions, indicators, and operational definitions. The model is **conceptual-interpretive** in character: designed to guide evaluation and serve as the foundation for empirical instrument development in the future — not as a psychometrically validated measurement instrument [6][13].

### **5.2. Assessment Model Hierarchy**

```mermaid
graph TD
    subgraph "Assessment Model Hierarchy"
        A[Assessment Model<br/>for High-Stakes Test Prep Platforms] --> B[Dimension 1<br/>Technology Architecture]
        A --> C[Dimension 2<br/>Pedagogy Effectiveness]
        A --> D[Dimension 3<br/>Institutional Governance]
        
        B --> B1[Indicator: System Stability]
        B1 --> B1a[Criterion: Uptime reliability]
        B1 --> B1b[Criterion: Response latency]
        
        B --> B2[Indicator: Interface Quality]
        B2 --> B2a[Criterion: Intuitive navigation]
        B2 --> B2b[Criterion: Visual consistency]
        B2 --> B2c[Criterion: Accessibility compliance]
        
        B --> B3[Indicator: Adaptive Algorithm]
        B3 --> B3a[Criterion: Difficulty calibration]
        B3 --> B3b[Criterion: Responsiveness to performance shift]
        
        C --> C1[Indicator: Test Standards Alignment]
        C1 --> C1a[Criterion: Format similarity to IELTS/TOEFL]
        C1 --> C1b[Criterion: CEFR level accuracy]
        
        C --> C2[Indicator: Automated Feedback Quality]
        C2 --> C2a[Criterion: Diagnostic precision]
        C2 --> C2b[Criterion: Actionable recommendations]
        C2 --> C2c[Criterion: Timeliness]
        
        C --> C3[Indicator: Micro-Learning Design]
        C3 --> C3a[Criterion: Unit duration 5-15 min]
        C3 --> C3b[Criterion: Modular structure]
        
        C --> C4[Indicator: Spaced Repetition]
        C4 --> C4a[Criterion: Personalized schedule]
        C4 --> C4b[Criterion: Forgetting curve alignment]
        
        C --> C5[Indicator: Cognitive Load Management]
        C5 --> C5a[Criterion: Minimal extraneous load]
        C5 --> C5b[Criterion: Optimized germane load]
        
        D --> D1[Indicator: Analytics Dashboard]
        D1 --> D1a[Criterion: Real-time visualization]
        D1 --> D1b[Criterion: Granular progress tracking]
        
        D --> D2[Indicator: Data Interoperability]
        D2 --> D2a[Criterion: API availability]
        D2 --> D2b[Criterion: Campus system compatibility]
        
        D --> D3[Indicator: Administrative Decision-Support]
        D3 --> D3a[Criterion: Cost-effectiveness metrics]
        D3 --> D3b[Criterion: Usage-outcome correlation]
    end
    
    style A fill:#ffe0b2
    style B fill:#e1f5fe
    style C fill:#e8f5e9
    style D fill:#f3e5f5
```

### **5.3. Operational Definitions Matrix**

#### **Technology Architecture Dimension**

| **Indicator** | **Conceptual Operational Definition** | **Source Theory** | **Use in Evaluation** |
|:---|:---|:---|:---|
| TECH-1 System Stability | Reliability of the system architecture in maintaining service availability under variable user loads, assessed from an infrastructure resilience perspective | *Software Quality Models* (ISO 25010) [14] | Technical evaluation of server capacity, *load balancing*, and *fault tolerance* |
| TECH-2 Interface Quality | Degree of interface quality enabling learner-platform interaction with minimal cognitive load, drawing on *zero UI* and *minimalist design* principles | *Cognitive Load Theory* [16]; *TAM* [11] | Heuristic interface analysis; *cognitive walkthrough* |
| TECH-3 Adaptive Algorithm Performance | Capacity of *item response theory* or *machine learning* algorithms to dynamically adjust content difficulty to individual proficiency | *Intelligent Tutoring Systems* [15]; *Adaptive Learning* | Algorithm logic evaluation; adjustment *convergence rate* |
| TECH-4 Multimedia Integration | Completeness and quality of multimedia elements (audio, video, graphics) supporting multimodal language processing | *Dual Coding Theory* [19]; *Multimedia Learning* [20] | Content analysis; media quality |
| TECH-5 Mobile Accessibility | Availability of platform access through mobile devices with equivalent functionality, including *offline-first* features for limited-connectivity contexts | *Mobile-Assisted Language Learning* (MALL) [5] | Responsiveness evaluation; *offline capability audit* |

#### **Pedagogy Effectiveness Dimension**

| **Indicator** | **Conceptual Operational Definition** | **Source Theory** | **Use in Evaluation** |
|:---|:---|:---|:---|
| PED-1 Test Standards Alignment | Degree of alignment of materials, item formats, assessment rubrics, and *task types* with international test standards (IELTS/TOEFL) and the *Common European Framework of Reference* (CEFR) | *Authenticity* in SLA [1]; *Washback Theory* [21] | *Content analysis* of alignment with *band descriptors* |
| PED-2 Automated Feedback Quality | Quality of automated *feedback*, assessed by diagnostic precision, completeness of *actionable recommendations*, and timeliness of delivery | *Feedback Model* Hattie & Timperley [17]; *Formative Assessment* | *Feedback loop* analysis; diagnostic evaluation |
| PED-3 Micro-Learning Design | Effectiveness of short, structured learning unit design for maximum retention in minimum time, drawing on *attention span* and *working memory* constraints | *Micro-Learning Theory* [22]; *Cognitive Load Theory* [16] | Content architecture evaluation; unit duration and structure |
| PED-4 Spaced Repetition | Effectiveness of scheduled repetition algorithms in optimising *retention intervals* based on individual historical performance | *Spacing Effect* (Ebbinghaus; Cepeda) [23] | *Scheduling* algorithm evaluation; *interval* logic |
| PED-5 Cognitive Load Management | Capacity of pedagogical design to minimise *extraneous load* and maximise *germane load* during language processing | *Cognitive Load Theory* (Sweller) [16] | *Heuristic evaluation* of cognitive load per task |
| PED-6 Motivation & Engagement | Impact of design elements (gamification, *progress visualisation*, *social comparison*) on intrinsic motivation and reduction of *foreign language anxiety* | *Self-Determination Theory* (Deci & Ryan) [12]; *Flow Theory* [24] | Analysis of motivational mechanics; *anxiety reduction* features |
| PED-7 Skill Coverage | Completeness of language skill coverage (*reading*, *writing*, *listening*, *speaking*) with proportional distribution and depth commensurate with test complexity | *Communicative Language Teaching* [25]; *Integrated Skills Approach* | *Content mapping* against *test specifications* |

#### **Institutional Governance Dimension**

| **Indicator** | **Conceptual Operational Definition** | **Source Theory** | **Use in Evaluation** |
|:---|:---|:---|:---|
| INST-1 Learning Analytics Dashboard | Availability of an analytic interface presenting learner progress data in a visual format that supports *awareness* and *reflection* for instructors | *Evaluation Framework for Learning Analytics* (EFLA) [9] | Dashboard feature evaluation; data granularity |
| INST-2 Data Interoperability | Capacity of the platform to exchange data with campus information systems (SIAKAD, LMS) through open protocol standards (API, LTI, xAPI) | *Interoperability Standards* [26]; *Enterprise Architecture* | Technical interoperability audit |
| INST-3 Instructor Monitoring | Availability of mechanisms enabling instructors to monitor progress, identify *at-risk students*, and intervene based on analytic data | *Teacher Dashboard Design* [10]; *Early Warning Systems* [27] | Monitoring feature evaluation; *alert mechanisms* |
| INST-4 Administrative Decision-Support | Availability of metrics and visualisations supporting adoption, licence renewal, or platform termination decisions by administrators | *IT Governance* [18]; *Evidence-Based Management* | *Reporting features* evaluation; ROI metrics |
| INST-5 Sustainability & Scalability | Platform capacity to scale with growing user numbers and evolving institutional needs without quality degradation | *Technology Sustainability Models* [28] | *Scalability* architecture evaluation; developer roadmap |

---

## **6. CONCEPTUAL STRUCTURAL MODEL**

### **6.1. Mapping of Theoretical Relationships**

Based on the synthesis of concepts from TAM, SDT, and EFLA, a **conceptual structural model** is proposed that maps the theoretical relationships among dimensions. The model is causal-theoretical in nature and is designed to serve as a foundation for future empirical testing through *Structural Equation Modelling* (SEM), but in this conceptual context it is presented as **theoretical propositions** (*theoretical propositions*) [11][12].

```mermaid
graph TB
    subgraph "Conceptual Structural Model<br/>Theoretical Propositions"
        EX1[Dimension: Technology<br/>Architecture] --> M1[Concept: Perceived<br/>Usefulness]
        EX2[Dimension: Pedagogy<br/>Effectiveness] --> M1
        EX3[Dimension: Institutional<br/>Governance] --> M2[Concept: Perceived<br/>Ease of Use]
        
        M1 --> M3[Concept: Motivation<br/>Intrinsic]
        M2 --> M3
        
        CC1[Concept: User<br/>Experience] -.->|mediates| M3
        CC2[Concept: Language<br/>Learning Potential] -.->|mediates| M3
        
        M3 --> EN1[Outcome: Learning<br/>Effectiveness]
        M3 --> EN2[Outcome: Student<br/>Engagement]
        
        EX3 --> EN3[Outcome: Institutional<br/>Adoption Intention]
        
        MOD1[Moderator:<br/>Proficiency Level] -.-> M3
        MOD2[Moderator:<br/>Learning Style] -.-> M3
        MOD3[Moderator:<br/>Test Type Target] -.-> EN1
    end
    
    style EX1 fill:#e1f5fe
    style EX2 fill:#e8f5e9
    style EX3 fill:#f3e5f5
    style M1 fill:#fff3e0
    style M2 fill:#fff3e0
    style M3 fill:#fff3e0
    style EN1 fill:#ffebee
    style EN2 fill:#ffebee
    style EN3 fill:#ffebee
    style CC1 fill:#f1f8e9
    style CC2 fill:#f1f8e9
    style MOD1 fill:#e0e0e0
    style MOD2 fill:#e0e0e0
    style MOD3 fill:#e0e0e0
```

### **6.2. Theoretical Propositions**

| **Code** | **Theoretical Proposition** | **Theoretical Argument Basis** |
|:---|:---|:---|
| P1 | Superior technology architecture directly enhances *Perceived Usefulness* of the platform for learners | TAM: PU is determined by system quality and task relevance [11] |
| P2 | Pedagogical effectiveness directly enhances *Perceived Usefulness* and *Language Learning Potential* | Chapelle: *language learning potential* is the central criterion of CALL evaluation [1] |
| P3 | Sound institutional governance directly enhances *Perceived Ease of Use* for instructors and administrators | EFLA: the *impact* dimension must encompass the institution [9] |
| P4 | *Perceived Usefulness* and *Perceived Ease of Use* collectively enhance intrinsic motivation of learners | Extended TAM-SDT: the need for *autonomy* and *competence* is satisfied through technology-pedagogy design [12] |
| P5 | *User Experience* mediates the relationship between technology-pedagogy dimensions and intrinsic motivation | *Flow Theory*: optimal UX is achieved when challenge and skill are in balance [24] |
| P6 | Intrinsic motivation directly influences *Learning Effectiveness* and *Student Engagement* | SDT: intrinsic motivation is the primary predictor of engagement and achievement [12] |
| P7 | Institutional governance directly influences *Institutional Adoption Intention* | *Diffusion of Innovations*: organisational adoption decisions are influenced by infrastructure availability and evidence of impact [29] |
| P8 | Language proficiency level, learning style, and target test type moderate the relationship between evaluation dimensions and *outcomes* | *APT Model* (Person-Task-Technology Fit): the contextuality of learner-technology interaction determines effectiveness [30] |

---

## **7. CONCEPTUAL DISCUSSION**

### **7.1. Theoretical Contributions**

This conceptual research makes three principal theoretical contributions:

**First**, a **multidisciplinary synthesis** across Information Systems (TAM, *learning analytics*), Applied Linguistics (CALL, SLA), and Cognitive Psychology (*cognitive load*, motivation). This framework bridges the divide that has historically separated technical evaluation from pedagogical evaluation in the *educational technology* literature [4][6].

**Second**, **contextual specificity** for the phenomenon of *high-stakes language test preparation*. Unlike generic CALL or MALL frameworks, this framework explicitly integrates concepts unique to the high-stakes testing context: *test standards alignment*, *spaced repetition*, *micro-learning design*, and *administrative decision-support* [1][3][5].

**Third**, a **conceptual structural model** mapping causal-theoretical relationships among dimensions. Unlike existing evaluation frameworks — which typically take the form of checklists or taxonomies — this model provides a foundation for future empirical hypothesis testing through quantitative techniques such as SEM [11][12].

### **7.2. Conceptual Practical Implications**

Although conceptual in nature, this framework carries practical implications for three *stakeholder* groups:

| **Stakeholder** | **Practical Implications** | **How to Use the Framework** |
|:---|:---|:---|
| **EdTech Developers** | Evidence-based system architecture guidelines | Use TECH and PED rubrics as *design specifications* |
| **Higher Education Administrators** | Adoption justification and *quality assurance* framework | Use INST rubric and structural model for platform *benchmarking* |
| **Researchers** | Theoretical foundation for future empirical studies | Use propositions P1–P8 as hypotheses for SEM testing |

### **7.3. Conceptual Limitations and Future Research Directions**

As conceptual research, this study carries inherent limitations: (a) the proposed causal relationships are theoretical and require empirical testing; (b) the operational definitions require psychometric validation through *Delphi method* and *Confirmatory Factor Analysis* at subsequent research stages; (c) the generalisability of the framework to different cultural contexts or educational systems requires cross-cultural empirical examination.

Recommended future research directions include: (1) *expert validation* through a *nominal group technique* to establish the *content validity* of the framework; (2) development and validation of measurement instruments based on this framework; (3) testing the structural model through SEM with data from multiple institutions; and (4) adaptation of the framework for other language learning platform types (*general English*, *business English*, *academic writing*).

---

## **8. CONCLUSION**

This study successfully constructs a *theoretical framework* and *assessment model* for evaluating high-stakes language test preparation platforms in higher education through *Conceptual Framework Analysis* (Jabareen, 2009). The proposed framework comprises three conceptual dimensions — **Technology Architecture**, **Pedagogy Effectiveness**, and **Institutional Governance** — integrated with cross-cutting concepts from TAM, SDT, and EFLA. The formulated *assessment model* provides evaluation rubrics with clear operational definitions for each indicator. A conceptual structural model comprising eight theoretical propositions is established as a foundation for future empirical testing. The principal contribution lies in providing a multidisciplinary theoretical foundation that fills the gap in the fragmented and contextually deficient CALL evaluation literature.

---

## **REFERENCES**

[1] C. A. Chapelle, *Computer Applications in Second Language Acquisition: Foundations for Teaching, Testing and Research*. Cambridge, U.K.: Cambridge Univ. Press, 2001.

[2] P. Hubbard, "Evaluation of courseware and websites," in *Present and Future Promises of CALL: From Theory and Research to New Directions in Foreign Language Teaching*, L. Ducate and N. Arnold, Eds. San Marcos, TX: CALICO, 2011, pp. 407–440.

[3] J. Leakey, *Evaluating Computer-Assisted Language Learning: An Integrated Approach to Effectiveness Research in CALL*. Bern, Switzerland: Peter Lang, 2011.

[4] B. L. McMurry et al., "An evaluation framework for CALL," *TESL-EJ*, vol. 20, no. 2, pp. 1–31, 2016.

[5] F. Rosell-Aguilar, "State of the app: A taxonomy and framework for evaluating language learning mobile applications," *CALICO J.*, vol. 34, no. 2, pp. 243–258, 2017.

[6] Y. Jabareen, "Building a conceptual framework: Philosophy, definitions, and procedure," *Int. J. Qual. Methods*, vol. 8, no. 4, pp. 49–62, 2009.

[7] C. Kivunja, "Distinguishing between theory, theoretical framework, and conceptual framework," *Int. J. High. Educ.*, vol. 7, no. 6, pp. 44–53, 2018.

[8] M. J. Page et al., "The PRISMA 2020 statement: An updated guideline for reporting systematic reviews," *BMJ*, vol. 372, p. n71, 2021.

[9] M. Scheffel et al., "The evaluation framework for learning analytics," in *Proc. LAK*, 2014, pp. 16–20.

[10] Y. Park and I.-H. Jo, "Development of the learning analytics dashboard to support students' learning performance," *J. Comput. Assist. Learn.*, vol. 35, no. 4, pp. 556–568, 2019.

[11] F. D. Davis, "Perceived usefulness, perceived ease of use, and user acceptance of information technology," *MIS Quart.*, vol. 13, no. 3, pp. 319–340, 1989.

[12] Y. Yang and S. Lou, "Self-determination theory and TAM in mobile language learning: An integrated model," *Comput. Assist. Lang. Learn.*, vol. 37, no. 4, pp. 1123–1145, 2024.

[13] P. Antonenko, "The instrumental value of conceptual frameworks in educational technology research," *Educ. Technol. Res. Dev.*, vol. 63, no. 1, pp. 53–71, 2015.

[14] ISO/IEC 25010:2011, *Systems and Software Engineering — Systems and Software Quality Requirements and Evaluation (SQuaRE) — System and Software Quality Models*. Geneva, Switzerland: ISO, 2011.

[15] B. P. Woolf, *Building Intelligent Interactive Tutors: Student-centered Strategies for Revolutionizing E-learning*. Burlington, MA: Morgan Kaufmann, 2009.

[16] J. Sweller, "Cognitive load during problem solving: Effects on learning," *Cogn. Sci.*, vol. 12, no. 2, pp. 257–285, 1988.

[17] J. Hattie and H. Timperley, "The power of feedback," *Rev. Educ. Res.*, vol. 77, no. 1, pp. 81–112, 2007.

[18] L. G. Tornatzky and J. J. Fleischer, *The Processes of Technological Innovation*. Lexington, MA: Lexington Books, 1990.

[19] A. Paivio, *Mental Representations: A Dual Coding Approach*. New York, NY: Oxford Univ. Press, 1986.

[20] R. E. Mayer, *Multimedia Learning*, 2nd ed. New York, NY: Cambridge Univ. Press, 2009.

[21] L. Cheng, "Washback, impact and consequences," in *Encyclopedia of Language and Education*, 2nd ed., vol. 7, E. Shohamy and N. H. Hornberger, Eds. New York, NY: Springer, 2008, pp. 2933–2944.

[22] T. Hug, "Micro learning and narration: Exploring possibilities of micro learning for developing narrative knowledge," in *Didactics of Microlearning: Concepts, Discourses and Examples*, T. Hug, Ed. Münster, Germany: Waxmann, 2007, pp. 63–73.

[23] N. J. Cepeda et al., "Distributed practice in verbal recall tasks: A review and quantitative synthesis," *Psychol. Bull.*, vol. 132, no. 3, pp. 354–380, 2006.

[24] M. Csikszentmihalyi, *Flow: The Psychology of Optimal Experience*. New York, NY: Harper & Row, 1990.

[25] D. L. Lange and R. M. Paige, "Culture as the core: Perspectives on culture in second language learning," in *Culture as the Core: Perspectives on Culture in Second Language Education*, D. L. Lange and R. M. Paige, Eds. Greenwich, CT: Information Age Publishing, 2003, pp. 1–18.

[26] IMS Global Learning Consortium, *Learning Information Services Specification*. Lake Mary, FL: IMS Global, 2018.

[27] D. G. Oblinger and J. L. Oblinger, *Educating the Net Generation*. Boulder, CO: EDUCAUSE, 2005.

[28] T. M. Choquette, "Sustainability of educational technology," in *Handbook of Research on Educational Communications and Technology*, 4th ed., J. M. Spector et al., Eds. New York, NY: Springer, 2014, pp. 723–730.

[29] E. M. Rogers, *Diffusion of Innovations*, 5th ed. New York, NY: Free Press, 2003.

[30] D. L. Goodhue and R. L. Thompson, "Task-technology fit and individual performance," *MIS Quart.*, vol. 19, no. 2, pp. 213–236, 1995.

---
