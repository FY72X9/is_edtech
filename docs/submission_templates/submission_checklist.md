# Pre-Submission Checklist — IS EdTech Main Paper (ETHE)

**Paper:** A Theoretical Framework and Assessment Model for Evaluating High-Stakes Language Test Preparation Platforms in Higher Education  
**Target Journal:** International Journal of Educational Technology in Higher Education (ETHE, Springer)  
**Status:** ☐ Draft | ☐ Near-final | ☐ Submission-ready

---

## A. Content Completeness

### Abstract
- [ ] Abstract ≤ 250 words (ETHE limit)
- [ ] Follows structure: Background → Gap → Method → Key Findings → Contribution/Impact
- [ ] No citations in abstract
- [ ] Keywords: exactly 5 terms; none repeating words from title

### Introduction
- [ ] Funnel structure: broad HE EdTech context → specific test prep platforms → evaluation gap
- [ ] Three research questions explicitly stated
- [ ] All claims cite Scopus-indexed sources

### Methodology
- [ ] CFA (Jabareen, 2009) properly explained with 8-phase table
- [ ] DSR (Hevner et al., 2004) integration articulated
- [ ] Gregor (2006) Type IV Theory classification stated
- [ ] Philosophical stance (critical realism + post-positivism) consistent throughout
- [ ] Integrative review protocol (Torraco, 2005) differentiated from systematic review

### Literature Synthesis
- [ ] Coverage matrix has ≥ 12 frameworks
- [ ] D&M mapping table present
- [ ] Boundary conditions table present
- [ ] All 5 gaps enumerated and linked to matrix evidence

### Theoretical Framework
- [ ] 3 dimensions derived deductively from D&M (not inductively)
- [ ] Cross-cutting concepts table complete (5 concepts)
- [ ] Dimension justification paragraphs include citations

### Assessment Model
- [ ] 15 indicators clearly tabulated (5 per dimension)
- [ ] Each indicator has: name, operational definition, source theory, evaluative use
- [ ] Assessment model hierarchy described (3 tiers)

### Structural Model
- [ ] 8 propositions tabulated with Type, Statement, and Theoretical Justification
- [ ] Formal structural equations present (6 equations)
- [ ] Parameter sign table present
- [ ] Theorem 1 (LP proof) with equations and QED marker
- [ ] Theorem 2 (Monte Carlo) with dominance probability stated
- [ ] IRR PoC results stated (κ = 0.7917)

### Discussion
- [ ] 4 theoretical contributions enumerated
- [ ] Practical implications table (3 stakeholders)
- [ ] 6 limitations acknowledged
- [ ] 6 future research directions proposed
- [ ] "So what?" answered for each finding

### Conclusion
- [ ] Directly answers all 3 research questions
- [ ] No new claims introduced in conclusion
- [ ] < 400 words

---

## B. Technical/Formatting

- [ ] Word count within journal limit (~8,000–10,000 words body text)
- [ ] All in-text citations use format \cite{bXX}
- [ ] All 40 references in bibliography match in-text citations
- [ ] No undefined \cite{} keys (compile without warnings)
- [ ] All 10 figures generate without error (run generate_subpaper_figures.py + monte_carlo_coverage.py)
- [ ] All figure captions present and accurate
- [ ] All table captions present
- [ ] No hardcoded author names in LaTeX (anonymized version if double-blind)
- [ ] Author affiliations complete (Name, email, ORCID)
- [ ] `\graphicspath` resolves correctly from LaTeX file location
- [ ] validate_latex.py passes without errors

---

## C. Submission Ethics & Declarations

- [ ] Cover letter prepared (cover_letter_ethe.md)
- [ ] Companion paper relationship disclosed in cover letter
- [ ] OSF pre-registration completed → OSF DOI: [INSERT]
- [ ] Data availability statement includes OSF repository link
- [ ] Conflict of interest declaration: None
- [ ] Funding statement: No external funding
- [ ] Author contributions statement present
- [ ] All figures: original (not copied from other papers)
- [ ] No copyrighted content reproduced without permission

---

## D. Language Quality

- [ ] Active voice > 80% of sentences
- [ ] No Indonesian words or phrases (check: adopsi, sesuai, dengan, dan, dll)
- [ ] No repetitive sentence openers (however, therefore, furthermore)
- [ ] Academic vocabulary consistent with IELTS Band 8 standard
- [ ] British vs. American English: consistent throughout (choose one)
- [ ] Turnitin/iThenticate similarity check: < 15%

---

## E. Reference Verification

Critical references requiring DOI verification before submission:

| Ref | Author | Status |
|---|---|---|
| b9 | Scheffel et al. (2014) | ⚠️ No stable DOI — verify journal archive URL |
| b12 | Yang & Lou (2024) | ⚠️ Verify DOI 10.1080/09588221.2022.2081048 maps correctly |
| b25 | Lange & Paige (2003) | ⚠️ Book chapter — verify ISBN and page range |
| b28 | Choquette (2014) | ⚠️ Verify Springer chapter DOI |
| All | — | Cross-check all 40 DOIs via doi.org before submission |

---

## F. Final Sign-off

- [ ] All co-authors have read and approved the final manuscript
- [ ] Corresponding author details confirmed
- [ ] Journal submission system account created
- [ ] Manuscript file (.tex and .pdf) compiled without errors
- [ ] Supplementary files (Python scripts) packaged
- [ ] Cover letter finalized

**Submission target date:** [INSERT]
