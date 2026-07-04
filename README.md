# Eudragit L100 – All-Atom MD Simulation Study
## Submission Package

**Title:** pH Responsive Conformation, Plasticiser Interactions, and Film Formation in Eudragit L100: An All-Atom Molecular Dynamics Study

**Authors:** Vaibhav Ambudkar, Rashmi Chauhan, Soham Ambudkar

**Target Journal:** RSC Pharmaceutics

---

## Package Contents

### /documents
| File | Description |
|---|---|
| `manuscript_RSC_format_FINAL.docx` | Full RSC Advances two-column format manuscript, all 12 figures embedded, all text corrected |
| `ESI_FINAL.docx` | Complete ESI with all 13 tables corrected, all 12 figures inserted |
| `covering_letter_new_submission.docx` | Cover letter for new submission to RSC Pharmaceutics |
| `response_to_reviewers.docx` | Point-by-point response to reviewers (if resubmitting) |

### /figures
All 12 final, verified figures (Figures 1–12) as high-resolution PNG files.

### /graphical_abstracts
Three versions of the graphical abstract:
- `graphical_abstract_6panel.png` — 6-panel summary (recommended for submission)
- `graphical_abstract_simple.png` — 2-panel schematic (simplified version)
- `graphical_abstract_FINAL.png` — Full multi-panel version

---

## Analysis Scripts (on WSL machine: ~/ubupablo78@DESKTOP-9H7VLS1)

The following scripts should also be uploaded to GitHub/Zenodo:

| Script | Purpose |
|---|---|
| `figure01_real.py` through `figure12_real.py` | Generate all 12 manuscript figures from raw GROMACS output |
| `rg_unwrap_multichain.py` | Radius of gyration via MDAnalysis unwrap (replaces gmx gyrate) |
| `water_uptake.py` | Water molecules within 0.5 nm of polymer |
| `interchain_distance.py` | Inter-chain COM distance (minimum-image convention) |
| `na_coo_rdf.py` | Na⁺–COO⁻ radial distribution function |
| `chain_contact_fraction.py` | Inter-chain close-contact fraction (<0.5 nm criterion) |
| `build_ga_6panel.py` | Graphical abstract generation script |

---

## Simulation Details

- **Software:** GROMACS 2025.4
- **Force field:** GAFF2 + OPLS-AA
- **Water model:** SPC/E
- **GPU:** NVIDIA RTX 5050
- **OS:** Ubuntu 24 (WSL2)
- **Python analysis:** MDAnalysis, NumPy, Matplotlib

## Key Verified Findings

| Phase | Key Result |
|---|---|
| Phase 0 | Rg: +62.2% at full ionization; non-monotonic intermediate response |
| Phase 0b | Both TEC and PEG400 are vdW-dominant; TEC: lower, more stable energy |
| Phase 1 | No optimal TEC concentration within 8.91–35.65% w/w |
| Phase 2 | Water diffusion ≈ bulk water; no detectable barrier |
| Phase 3 | Rg +36%, water +30%, inter-chain distance +20% upon ionization |
| Phase 4 | NaHCO₃: −1.2% vs NaCl; Na₂CO₃: +16.9% (genuine expansion) |
| Phase 5 | Bulk modulus flat (~2.1–2.2 GPa); water-dominated throughout |

---

## Data Availability

Simulation scripts and raw data deposited at:
- **GitHub:** [to be added after account creation]
- **Zenodo DOI:** [to be added after upload]
