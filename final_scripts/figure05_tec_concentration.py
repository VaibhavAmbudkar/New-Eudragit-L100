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

BLUE = "#2C5F8A"; RED = "#C0392B"; GREEN = "#2E8B57"

conc = [12.9, 22.9, 30.8, 37.2]   # % w/w TEC relative to polymer
rg    = [1.494, 1.573, 2.267, 2.269]; rg_sd = [0.293, 0.297, 0.118, 0.235]
diff  = [0.191, 0.409, 0.402, 0.367]; diff_sd = [0.12, 0.09, 0.05, 0.11]
fv    = [42.91, 43.02, 42.95, 42.96]; fv_sd = [0.09, 0.09, 0.09, 0.09]

fig, axes = plt.subplots(1, 3, figsize=(16, 5.3))
fig.subplots_adjust(left=0.06, right=0.98, top=0.90, bottom=0.15, wspace=0.28)

# (A) Rg
ax = axes[0]
ax.errorbar(conc, rg, yerr=rg_sd, fmt='o-', color=BLUE, lw=2.4, ms=11,
            markeredgecolor='white', markeredgewidth=1.6, capsize=7, capthick=1.6, ecolor='#555555')
ax.set_xlabel("TEC concentration (% w/w)")
ax.set_ylabel("L100 chain $R_g$ (nm)")
ax.set_title("(A)", loc='left', fontweight='bold')
ax.set_xlim(8, 42); ax.set_ylim(1.0, 2.8); ax.grid(alpha=0.25)

# (B) diffusion
ax = axes[1]
ax.errorbar(conc, diff, yerr=diff_sd, fmt='s-', color=RED, lw=2.4, ms=11,
            markeredgecolor='white', markeredgewidth=1.6, capsize=7, capthick=1.6, ecolor='#555555')
ax.set_xlabel("TEC concentration (% w/w)")
ax.set_ylabel("TEC diffusion coeff. ($10^{-5}$ cm$^2$/s)")
ax.set_title("(B)", loc='left', fontweight='bold')
ax.set_xlim(8, 42); ax.set_ylim(0, 0.6); ax.grid(alpha=0.25)

# (C) free volume
ax = axes[2]
ax.errorbar(conc, fv, yerr=fv_sd, fmt='D-', color=GREEN, lw=2.4, ms=10,
            markeredgecolor='white', markeredgewidth=1.6, capsize=7, capthick=1.6, ecolor='#555555')
ax.set_xlabel("TEC concentration (% w/w)")
ax.set_ylabel("Free volume fraction (%)")
ax.set_title("(C)", loc='left', fontweight='bold')
ax.set_xlim(8, 42); ax.set_ylim(42.0, 44.0); ax.grid(alpha=0.25)

fig.suptitle("Phase 1: TEC concentration series (single L100 chain)",
             fontsize=16, fontweight='bold', y=0.99)
fig.savefig("figure05_tec_concentration.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure05_tec_concentration.png")
