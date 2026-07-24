"""
Figure 3 - Plasticizer comparison: TEC vs PEG400 in the Eudragit L100 film.

Four panels (triplicate 50 ns replicates, mean +/- SD):
  (A) System potential energy
  (B) Per-chain radius of gyration
  (C) Polymer-plasticizer hydrogen bonds per frame
  (D) Polymer-plasticizer interaction energy, Coul-SR / LJ-SR decomposition

Data: all-atom MD (GROMACS), 5-chain L100 film with IPA co-solvent,
15 TEC or 10 PEG400 molecules, 3 x 50 ns replicates per system.

Output: figure03_plasticizer.png (300 dpi)
Run:    python figure03_plasticizer.py
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Data - per-replicate values; means and SDs are computed below
# ----------------------------------------------------------------------
systems = ["TEC", "PEG400"]
x = [0, 1]

# (A) system potential energy (kJ/mol): [mean, sd] from 3 replicates
pe    = [-336636, -330718]
pe_sd = [7, 42]

# (B) per-chain Rg (nm)  (rep1 mean; sd = chain-to-chain spread)
rg    = [0.719, 0.779]
rg_sd = [0.045, 0.095]

# (C) polymer-plasticizer H-bonds per frame - 3 replicates each
tec_hb = [0.49, 0.65, 0.04]
peg_hb = [0.14, 0.12, 0.22]

# (D) interaction energy (kJ/mol) - 3 replicates each
tec_coul = [-21.9, -31.2, -2.6]
tec_lj   = [-12.9, -25.8, -5.3]
peg_coul = [-8.0,  -6.2, -12.3]
peg_lj   = [-26.9, -19.9, -37.5]

# derived means / SDs
hb    = [np.mean(tec_hb),  np.mean(peg_hb)]
hb_sd = [np.std(tec_hb, ddof=1), np.std(peg_hb, ddof=1)]

# ----------------------------------------------------------------------
# Style
# ----------------------------------------------------------------------
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 16, 'axes.titlesize': 18,
    'xtick.labelsize': 14, 'ytick.labelsize': 14, 'legend.fontsize': 13,
    'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans'],
    'axes.linewidth': 1.4, 'xtick.major.width': 1.4, 'ytick.major.width': 1.4,
    'xtick.major.size': 6, 'ytick.major.size': 6,
})

TEC_C = "#2C5F8A"
PEG_C = "#D96C3B"

fig, axes = plt.subplots(2, 2, figsize=(13, 11))
fig.subplots_adjust(left=0.09, right=0.96, top=0.94, bottom=0.08,
                    hspace=0.30, wspace=0.28)


def style(ax, title):
    ax.set_xticks(x)
    ax.set_xticklabels(systems)
    ax.set_title(title, loc='left', fontweight='bold', pad=10)
    ax.grid(alpha=0.2, axis='y')


# (A) potential energy
ax = axes[0, 0]
ax.bar(x, pe, yerr=pe_sd, width=0.5, color=[TEC_C, PEG_C],
       edgecolor='black', linewidth=1.3, capsize=8, error_kw=dict(lw=1.6))
for xi, v in zip(x, pe):
    ax.text(xi, v / 2, f"{v:,.0f}", ha='center', va='center',
            fontsize=13, fontweight='bold', color='white')
ax.set_ylabel("System potential energy (kJ/mol)")
style(ax, "(A)")

# (B) per-chain Rg
ax = axes[0, 1]
ax.bar(x, rg, yerr=rg_sd, width=0.5, color=[TEC_C, PEG_C],
       edgecolor='black', linewidth=1.3, capsize=8, error_kw=dict(lw=1.6))
for xi, v, e in zip(x, rg, rg_sd):
    ax.text(xi, v + e + 0.02, f"{v:.3f}", ha='center', fontsize=13, fontweight='bold')
ax.set_ylabel("Per-chain $R_g$ (nm)")
ax.set_ylim(0, 1.0)
style(ax, "(B)")

# (C) H-bonds
ax = axes[1, 0]
ax.bar(x, hb, yerr=hb_sd, width=0.5, color=[TEC_C, PEG_C],
       edgecolor='black', linewidth=1.3, capsize=8, error_kw=dict(lw=1.6))
for xi, v, e in zip(x, hb, hb_sd):
    ax.text(xi, v + e + 0.03, f"{v:.2f}", ha='center', fontsize=13, fontweight='bold')
ax.set_ylabel("Polymer\u2013plasticizer H-bonds / frame")
ax.set_ylim(0, 0.95)
style(ax, "(C)")

# (D) Coul/LJ decomposition
ax = axes[1, 1]
w = 0.35
coul_m = [np.mean(tec_coul), np.mean(peg_coul)]
coul_s = [np.std(tec_coul, ddof=1), np.std(peg_coul, ddof=1)]
lj_m   = [np.mean(tec_lj), np.mean(peg_lj)]
lj_s   = [np.std(tec_lj, ddof=1), np.std(peg_lj, ddof=1)]
xa = np.arange(2)
ax.bar(xa - w / 2, coul_m, w, yerr=coul_s, label="Coul-SR", color="#4C72B0",
       edgecolor='black', linewidth=1.2, capsize=6, error_kw=dict(lw=1.4))
ax.bar(xa + w / 2, lj_m, w, yerr=lj_s, label="LJ-SR", color="#DD8452",
       edgecolor='black', linewidth=1.2, capsize=6, error_kw=dict(lw=1.4))
ax.set_xticks(xa)
ax.set_xticklabels(systems)
ax.set_ylabel("Interaction energy (kJ/mol)")
ax.set_title("(D)", loc='left', fontweight='bold', pad=10)
ax.axhline(0, color='black', lw=0.9)
ax.legend(frameon=True, framealpha=0.95, edgecolor='#CCCCCC')
ax.grid(alpha=0.2, axis='y')

fig.savefig("figure03_plasticizer.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure03_plasticizer.png")
