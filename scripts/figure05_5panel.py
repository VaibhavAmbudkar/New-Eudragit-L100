import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 15, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 12,
    'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans'],
    'axes.linewidth': 1.4, 'xtick.major.width': 1.4, 'ytick.major.width': 1.4,
    'xtick.major.size': 6, 'ytick.major.size': 6,
})

BLUE="#2C5F8A"; RED="#C0392B"; GREEN="#2E8B57"; PURPLE="#7D3C98"

conc  = [12.9, 22.9, 30.8, 37.2]
rg    = [1.494, 1.573, 2.267, 2.269]; rg_sd = [0.293, 0.297, 0.118, 0.235]
diff  = [0.191, 0.409, 0.402, 0.367]; diff_sd = [0.12, 0.09, 0.05, 0.11]
fv    = [42.91, 43.02, 42.95, 42.96]
hb    = [0.0133, 0.0432, 0.0299, 0.1096]
coul  = [-0.39, -1.59, -1.40, -2.71]
lj    = [-1.26, -6.97, -2.57, -7.35]

fig = plt.figure(figsize=(16, 9.5))
gs = fig.add_gridspec(2, 3, hspace=0.38, wspace=0.30)

def style(ax, title):
    ax.set_xlabel("TEC concentration (% w/w)")
    ax.set_title(title, loc='left', fontweight='bold')
    ax.set_xlim(8, 42); ax.grid(alpha=0.25)

# (A) Rg
ax = fig.add_subplot(gs[0,0])
ax.errorbar(conc, rg, yerr=rg_sd, fmt='o-', color=BLUE, lw=2.2, ms=10,
            markeredgecolor='white', markeredgewidth=1.4, capsize=6, ecolor='#555')
ax.set_ylabel("L100 chain $R_g$ (nm)"); style(ax, "(A)")

# (B) diffusion
ax = fig.add_subplot(gs[0,1])
ax.errorbar(conc, diff, yerr=diff_sd, fmt='s-', color=RED, lw=2.2, ms=10,
            markeredgecolor='white', markeredgewidth=1.4, capsize=6, ecolor='#555')
ax.set_ylabel("TEC diffusion coeff. ($10^{-5}$ cm$^2$/s)"); style(ax, "(B)")

# (C) free volume
ax = fig.add_subplot(gs[0,2])
ax.plot(conc, fv, 'D-', color=GREEN, lw=2.2, ms=9, markeredgecolor='white', markeredgewidth=1.4)
ax.set_ylabel("Free volume fraction (%)"); ax.set_ylim(42.5, 43.3); style(ax, "(C)")

# (D) TEC-COO- H-bonds
ax = fig.add_subplot(gs[1,0])
ax.plot(conc, hb, '^-', color=PURPLE, lw=2.2, ms=10, markeredgecolor='white', markeredgewidth=1.4)
ax.set_ylabel("TEC\u2013COO$^-$ H-bonds / frame"); style(ax, "(D)")

# (E) Coul-SR / LJ-SR decomposition
ax = fig.add_subplot(gs[1,1:])
w = 3.0
xa = np.array(conc)
ax.bar(xa-1.6, coul, width=w, color="#4C72B0", edgecolor='black', linewidth=1.2, label="Coul-SR")
ax.bar(xa+1.6, lj, width=w, color="#DD8452", edgecolor='black', linewidth=1.2, label="LJ-SR")
ax.set_ylabel("Polymer\u2013TEC energy (kJ/mol)")
ax.axhline(0, color='black', lw=0.9)
ax.legend(frameon=True, framealpha=0.95, edgecolor='#CCCCCC')
style(ax, "(E)")

fig.suptitle("Phase 1: TEC concentration series on a single L100 chain",
             fontsize=17, fontweight='bold', y=0.98)
fig.savefig("figure05_5panel.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure05_5panel.png")
