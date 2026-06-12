# OSF Pre-Registration Protocol
## Mapping Evaluation Frameworks for Language Learning Platforms in Higher Education: A Scoping Review

**Study registration type:** Scoping Review Protocol  
**OSF Pre-registration category:** Systematic Reviews and Meta-Analyses  
**Date of protocol:** 2026-06-12  
**OSF DOI:** [INSERT upon registration at osf.io/register]  
**Status:** DRAFT — To be submitted to OSF before initiating data search phase

---

> [!IMPORTANT]
> This protocol must be registered on OSF BEFORE executing the database search phase. Once registered, the search dates must match. The OSF timestamp serves as proof of a priori methodology commitment.

---

## 1. Study Information

**Title:** Mapping Evaluation Frameworks for Language Learning Platforms in Higher Education: A Scoping Review of Assessment Dimensions and Coverage Gaps

**Authors:** [Author 1 Name], [Author 2 Name]  
**Affiliation:** [Department, Faculty, Institution], [City, Country]

**Corresponding author:** [Name] | [email@institution.ac.id] | ORCID: [0000-0000-0000-0000]

---

## 2. Background and Rationale

The proliferation of digital language learning platforms in higher education has not been matched by adequate evaluation frameworks. Existing frameworks originate from disparate disciplines (CALL, IS, instructional design) and each provides only partial coverage of dimensions relevant to platform quality. No systematic mapping of the dimensional coverage of these frameworks has been conducted. This scoping review addresses that gap by mapping the dimensional landscape and identifying consistent underrepresentation.

---

## 3. Research Questions

1. What evaluation frameworks have been developed for digital language learning platforms and EdTech in higher education contexts over the past two decades (2001–2025)?
2. Which evaluation dimensions are consistently covered, and which are systematically underrepresented across the existing corpus of frameworks?
3. Does any single framework simultaneously cover the technology, pedagogy, and institutional governance dimensions with adequate operational definitions?

---

## 4. Methodology

**Framework:** Scoping review as formalised by Arksey & O'Malley (2005), extended by Levac et al. (2010), and updated by Munn et al. (2018).

**Reporting standard:** PRISMA-ScR (Tricco et al., 2018) — DOI: 10.7326/M18-0850

**Population-Concept-Context (PCC) framework (Munn et al., 2018):**
- **Population:** Higher education institutions and their stakeholders (learners, instructors, administrators)
- **Concept:** Frameworks and evaluation models designed for digital language learning platforms (CALL/MALL/EdTech/LMS)
- **Context:** Institutional adoption, quality assurance, and decision-making in higher education

---

## 5. Search Strategy

**Databases:** Scopus (primary), Web of Science, ERIC, IEEE Xplore

**Search period:** 2001–2025 (from Chapelle 2001 as first landmark CALL evaluation framework)

**Search strings:**

```
String A (core):
("evaluation framework" OR "assessment model" OR "quality framework"
 OR "evaluation criteria" OR "assessment dimensions")
AND
("educational technology" OR "e-learning" OR "CALL" OR "MALL"
 OR "language learning platform" OR "EdTech" OR "LMS"
 OR "digital learning platform" OR "mobile learning")
AND
("higher education" OR "university" OR "tertiary" OR "college")

String B (language-specific):
("CALL evaluation" OR "MALL evaluation" OR "language app evaluation"
 OR "test preparation platform" OR "IELTS platform" OR "TOEFL platform")
AND
("framework" OR "model" OR "criteria" OR "dimensions")
```

**Language:** English only

---

## 6. Inclusion and Exclusion Criteria

### Inclusion
- Papers that present, propose, or critique an EdTech/CALL evaluation framework or model
- Context: Higher education; language learning; CALL/MALL/EdTech/LMS
- Source type: Journal articles, book chapters, peer-reviewed conference proceedings
- Index: Scopus-indexed, WoS-indexed, ERIC, or IEEE Xplore
- Year: 2001–2025

### Exclusion
- Empirical studies that use a framework without developing/critiquing it
- K-12 only; corporate training; non-educational platforms
- Gray literature, white papers, blogs, institutional reports
- Non-indexed journals; predatory journals (checked via Beall's List or Cabells Blacklist)
- Non-English language papers

### Operational Definition
"Evaluation framework" = a conceptual instrument designed to assess the quality of a digital platform from the perspective of system quality, content quality, or institutional service. Teacher competency frameworks (e.g. TPACK) are excluded. Technology acceptance models (e.g. UTAUT) are included conditionally if their constructs have been adapted as platform evaluation dimensions.

---

## 7. Data Charting (Extraction) Plan

Each included framework will be coded against five analytical dimensions using a standardized extraction form:

| Code | Dimension | Coding Criteria |
|---|---|---|
| D1 | Technology Architecture | Covers technical system quality: stability, adaptivity, accessibility, UI |
| D2 | Pedagogy Effectiveness | Covers content and instructional design: curriculum alignment, feedback, cognitive load, skill coverage |
| D3 | Institutional Governance | Covers institutional aspects: analytics, monitoring, decision-support, data interoperability |
| D4 | High-Stakes Test Specificity | Explicitly operationalizes metrics for high-stakes testing (IELTS, TOEFL, CEFR) |
| D6 | Multi-Stakeholder Perspective | Accommodates multiple stakeholders (learner + instructor + administrator) |

**Coding scale:**
- ✓ (1.0) = Fully covered — dimension explicitly defined and operationalized
- ◑ (0.5) = Partially covered — mentioned but not operationally defined, or only implicit
- ✗ (0.0) = Not covered — dimension absent

**D5 (Framework Rigor) assessed separately as meta-level indicator — not counted in coverage score.**

**Coverage Score formula:** CS = Σ s_i where s_i ∈ {0, 0.5, 1.0} for i ∈ {D1, D2, D3, D4, D6}. Maximum = 5.0.

---

## 8. Inter-Rater Reliability Plan

- Primary coder codes all included frameworks
- Second coder independently codes ≥ 20% of all frameworks (random sample)
- Agreement metric: Cohen's Kappa (κ) — target: κ ≥ 0.80 for acceptable agreement
- Disagreement resolution: consensus discussion; third arbitrator for unresolved cases
- IRR results reported per dimension in methodology section

---

## 9. Analysis Plan

The analysis will produce:
1. A dimensional coverage matrix (frameworks × dimensions)
2. Per-dimension coverage frequency analysis
3. Identification of persistent gaps (dimensions never achieving full coverage)
4. Discipline-origin analysis (CALL vs. IS vs. LA coverage patterns)
5. D5 rigor analysis (separate from coverage score)

No statistical meta-analysis. No effect size calculation. Analysis is descriptive/comparative.

---

## 10. Relationship to Main Paper

This scoping review is a precursor study to a companion paper: "A Theoretical Framework and Assessment Model for Evaluating High-Stakes Language Test Preparation Platforms in Higher Education: A Conceptual Framework Analysis." Both papers share a literature dataset but present wholly distinct contributions. This relationship will be fully disclosed to all journal editors. No duplicate content exists between papers.

---

## 11. Data Availability Commitment

Upon acceptance, the following will be made publicly available in this OSF repository:
- This pre-registered protocol
- Extraction form template (JSON schema)
- Final coded extraction forms for all included frameworks
- Coverage matrix data (CSV)
- PRISMA-ScR flow diagram data

---

*Protocol version: 1.0*  
*To be registered at: https://osf.io/register*  
*Registration type: OSF Preregistration*
