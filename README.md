# Eudragit L100 – All-Atom MD Simulation Study
## Submission Package

**Title:** pH Responsive Conformation, Plasticiser Interactions, and Film Formation in Eudragit L100: An All-Atom Molecular Dynamics Study

**Authors:** Vaibhav Ambudkar, Rashmi Chauhan, Soham Ambudkar

**Target Journal:** RSC Pharmaceutics

---

## Data Availability

| Resource | Link |
|---|---|
| **GitHub Repository** | https://github.com/VaibhavAmbudkar/New-Eudragit-L100 |
| **Zenodo Dataset (DOI)** | https://doi.org/10.5281/zenodo.21195465 |

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21195465.svg)](https://doi.org/10.5281/zenodo.21195465)

> **Note on this version:** this repository reflects a corrected re-analysis of the full multi-phase dataset (charge-assignment fix for ionized carboxylate groups, corrected TEC concentration labels, and a consistent single analysis pipeline for the Phase 5 concentration series). Findings and figures here **supersede** any earlier draft manuscript, ESI, or figure set referencing the values previously reported for Phases 0, 1, 3, and 4.

---

## Package Contents

### /documents
| File | Description |
|---|---|
| `Manuscript_RSC_format_CORRECTED.docx` | Full RSC-format manuscript, all 12 figures embedded, all text and data corrected |
| `ESI_CORRECTED.docx` | Complete ESI with all data tables corrected, all 12 figures inserted |
| `covering_letter_new_submission.docx` | Cover letter for new submission |
| `response_to_reviewers.docx` | Point-by-point response to reviewers (if resubmitting) |

### /figures
All 12 final, verified figures (Figures 1–12) as high-resolution PNG files, each with a matching standalone Python plotting script (see `/scripts`).

### /graphical_abstracts
| File | Description |
|---|---|
| `graphical_abstract.png` | Single-panel narrative graphical abstract — pH-triggered film swelling via electrostatic coupling (acid vs. intestinal film, headline numbers) |
| `six_panel_abstract.png` | Six-panel key-findings summary — one mini-figure per major result (ionization effect, TEC vs. PEG400, TEC concentration, pH-switch swelling, counterion effect, overlap concentration c*) |

### /scripts
Standalone Python plotting scripts (Matplotlib/NumPy) for every figure, each with the underlying data hard-coded so it reproduces the exact published figure independently:
`figure01_deprotonation.py`, `figure02_pH_switch_schematic.py`, `figure03_plasticizer.py`, `figure04_tec_mechanism.py`, `figure05_tec_concentration.py`, `figure06_phase2_film.py`, `figure07_permeability.py`, `figure08_phase3_pHswitch.py`, `figure09_mechanism_cascade.py`, `figure10_counterion.py`, `figure11_phase5_concentration.py`, `figure12_cstar.py`, `graphical_abstract.py`, `six_panel_abstract.py`

---

## Zenodo Dataset Contents

Raw simulation data and analysis scripts deposited at [10.5281/zenodo.21195465](https://doi.org/10.5281/zenodo.21195465):

| File / Folder | Description |
|---|---|
| `figure01_deprotonation.py` – `figure12_cstar.py` | Figure generation scripts (data hard-coded from verified GROMACS output) |
| `rg_unwrap_multichain.py` | Per-chain radius of gyration via MDAnalysis, with explicit periodic-boundary unwrapping |
| `water_uptake.py` | Water molecules within 0.5 nm of the polymer (MDAnalysis direct count) |
| `interchain_distance.py` | Inter-chain center-of-mass distance (minimum-image convention) |
| `na_coo_rdf.py` | Counterion–COO⁻ radial distribution function |
| `interchain_hbonds.py` | Inter-chain hydrogen bonds per frame (direct geometric criterion) — used throughout Phase 5 in place of the earlier close-contact-fraction metric |
| `bulk_modulus_from_volume.py` | Bulk modulus from isothermal volume fluctuations (NPT), K = ⟨V⟩k_BT/⟨(δV)²⟩ |
| `tec_diffusion_msd.py` | TEC diffusion coefficient via `gmx msd` / MDAnalysis MSD |
| `energy_decomposition_rerun.py` | Coul-SR/LJ-SR interaction-energy decomposition via `mdrun -rerun` with energy groups |
| `*.xvg` / `*.dat` | Raw GROMACS/MDAnalysis analysis outputs (Rg, SASA, density, MSD, RDF, energy) underlying every figure |
| Topology files (`.itp`, `.top`) | L100 chain, TEC, PEG400, CO₃²⁻ (Na₂CO₃) parameter files |

---

## Simulation Details

| Parameter | Value |
|---|---|
| Software | GROMACS 2025.4 |
| Force field | GAFF2 (L100, TEC) + OPLS-AA (PEG400, isopropanol co-solvent) |
| Water model | SPC/E |
| GPU | NVIDIA RTX 5050 (~160–200 ns/day typical) |
| OS | Ubuntu 24 (WSL2) |
| Python analysis | MDAnalysis, NumPy, Matplotlib |

---

## Key Verified Findings

| Phase | Key Result |
|---|---|
| **Phase 0** — Deprotonation series | Non-monotonic, largely flat single-chain Rg (0.65–0.80 nm across 0–100% ionization); SASA tracks Rg closely (r = 0.98). Single-chain ionization alone is **not** the primary swelling mechanism. |
| **Phase 0b** — TEC vs. PEG400 (triplicate) | TEC binds via Coulomb/H-bond contacts (Coul-SR −18.6 kJ/mol, 0.39 H-bonds/frame); PEG400 binds via van der Waals contact (LJ-SR −28.1 kJ/mol, 0.16 H-bonds/frame). TEC gives lower system energy (−336,636 vs. −330,718 kJ/mol) and a more compact chain (0.719 vs. 0.779 nm) — TEC is the mechanistically preferable plasticizer. |
| **Phase 1** — TEC concentration series (single chain) | Chain Rg rises progressively with TEC loading, 1.49 → 2.27 nm across 12.9–37.2% w/w; free volume stays essentially flat (~42.9–43.0%). Direct, sustained TEC–polymer contact is limited at this dilute, single-chain scale. |
| **Phase 2** — Multi-chain film (5 chains + 17 TEC) | Water mobility within the film ≈ bulk water (D = 2.563 × 10⁻⁵ cm²/s); no detectable diffusion barrier. TEC is strongly bound within the film (Coul-SR −77.9, LJ-SR −196.4 kJ/mol) — far stronger than the dilute single-chain case, confirming TEC–polymer association is a concentrated, multi-chain-film phenomenon. |
| **Phase 3** — Acid → intestinal pH-switch | Coherent, multi-scale swelling upon ionization: Rg +34% (0.758 → 1.015 nm), water uptake +62% (925 → 1501 molecules), inter-chain separation +30% (4.19 → 5.46 nm). Driven by a 4.1-fold strengthening of the polymer–solvent Coulomb interaction; TEC mobility increases 10-fold (confirmed, coupled mechanism). |
| **Phase 4** — Counterion identity | NaHCO₃: **−11%** Rg vs. NaCl (genuinely more compact, tightest Na⁺–COO⁻ ion pairing, g(r) = 421). Na₂CO₃: **+91%** Rg vs. NaCl (substantial expansion, weakest/most diffuse ion pairing, g(r) = 114; single-chain system did not reach a stable conformation over 50 ns — value is indicative, not converged). |
| **Phase 5** — Extended concentration series (2–50 chains) | Per-chain Rg declines 0.84 → 0.73 nm with concentration before plateauing; inter-chain hydrogen bonding rises steadily (0 → 33.3 bonds/frame); bulk modulus stays water-dominated and flat (~2.1–2.3 GPa) throughout. Identifies the critical overlap concentration **c* ≈ 2.5–3.0% w/v** — the practical aqueous coating window (5–10% w/v) lies well above c*, in the semi-dilute regime. |

---

## Citation

If you use this data or code, please cite:

> Ambudkar V., Chauhan R., Ambudkar S. (2026). *pH Responsive Conformation, Plasticiser Interactions, and Film Formation in Eudragit L100: An All-Atom Molecular Dynamics Study.* RSC Pharmaceutics. https://doi.org/10.5281/zenodo.21195465

---

## License

This dataset is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
