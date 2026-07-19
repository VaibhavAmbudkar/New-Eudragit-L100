import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 13, 'axes.labelsize': 15, 'axes.titlesize': 16,
    'xtick.labelsize': 12.5, 'ytick.labelsize': 12.5, 'legend.fontsize': 12,
    'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans'],
    'axes.linewidth': 1.3, 'xtick.major.width': 1.3, 'ytick.major.width': 1.3,
    'xtick.major.size': 5, 'ytick.major.size': 5,
})

BLUE = "#2C5F8A"; ORANGE = "#D96C3B"
cond = ["Acid\n(gastric)", "Intestinal\n(ionized)"]
x = [0, 1]

fig, axes = plt.subplots(2, 3, figsize=(15, 9.5))
fig.subplots_adjust(left=0.06, right=0.98, top=0.92, bottom=0.08, hspace=0.32, wspace=0.30)

def bars(ax, vals, ylabel, title, fmt, ymax, errs=None, pct=True):
    b = ax.bar(x, vals, width=0.55, color=[BLUE, ORANGE], edgecolor='black',
               linewidth=1.3, yerr=errs, capsize=7 if errs else 0,
               error_kw=dict(lw=1.5) if errs else {})
    for xi, v in zip(x, vals):
        off = (errs[xi] if errs else 0) + ymax*0.02
        ax.text(xi, v+off if v>=0 else v-off*3, fmt.format(v), ha='center',
                va='bottom' if v>=0 else 'top', fontsize=12.5, fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels(cond)
    ax.set_ylabel(ylabel); ax.set_title(title, loc='left', fontweight='bold')
    ax.grid(alpha=0.2, axis='y')
    if ymax>0: ax.set_ylim(0, ymax)
    if pct and vals[0]!=0:
        p = (vals[1]-vals[0])/abs(vals[0])*100
        ax.text(0.5, 0.93, f"{'+' if p>=0 else ''}{p:.0f}%", transform=ax.transAxes,
                ha='center', va='top', fontsize=15, fontweight='bold', color=ORANGE)

# A: per-chain Rg
bars(axes[0,0], [0.758, 1.015], "Per-chain $R_g$ (nm)", "(A) Chain size",
     "{:.3f}", 1.25, errs=[0.03, 0.025])
# B: water uptake
bars(axes[0,1], [925, 1501], "Water within 0.5 nm", "(B) Hydration",
     "{:.0f}", 1750)
# C: inter-chain distance
bars(axes[0,2], [4.187, 5.464], "Inter-chain distance (nm)", "(C) Separation",
     "{:.2f}", 6.6, errs=[0.84, 0.24])
# D: Coul-SR decomposition
ax = axes[1,0]
coul = [-6779, -27854]; lj = [-1229, 1072]
w = 0.35; xa = np.arange(2)
ax.bar(xa-w/2, coul, w, color="#4C72B0", edgecolor='black', linewidth=1.2, label="Coul-SR")
ax.bar(xa+w/2, lj, w, color="#DD8452", edgecolor='black', linewidth=1.2, label="LJ-SR")
ax.set_xticks(xa); ax.set_xticklabels(cond)
ax.set_ylabel("Polymer\u2013solvent energy (kJ/mol)")
ax.set_title("(D) Electrostatic driver", loc='left', fontweight='bold')
ax.axhline(0, color='black', lw=0.9); ax.grid(alpha=0.2, axis='y')
ax.legend(frameon=True, framealpha=0.95, edgecolor='#CCCCCC', loc='lower left')
ax.text(0.5, 0.06, "Coul 4.1\u00d7 stronger", transform=ax.transAxes,
        ha='center', fontsize=12.5, fontweight='bold', color="#4C72B0")
# E: TEC diffusion
bars(axes[1,1], [0.053, 0.556], "D(TEC) ($\\times10^{-5}$ cm$^2$/s)", "(E) Plasticizer mobility",
     "{:.3f}", 0.68, pct=False)
axes[1,1].text(0.5, 0.93, "10\u00d7 faster", transform=axes[1,1].transAxes,
        ha='center', va='top', fontsize=15, fontweight='bold', color=ORANGE)
# F: summary of % changes
ax = axes[1,2]
metrics = ["$R_g$", "Water", "Sep.", "Coul", "D(TEC)"]
changes = [34, 62, 30, 311, 950]  # % changes; Coul (6779->27854)=311%, D 0.053->0.556=950%
colors = [ORANGE]*3 + ["#4C72B0", "#2E8B57"]
b = ax.barh(metrics[::-1], changes[::-1], color=colors[::-1], edgecolor='black', linewidth=1.2)
for i,(m,c) in enumerate(zip(metrics[::-1], changes[::-1])):
    ax.text(c+15, i, f"+{c}%", va='center', fontsize=12, fontweight='bold')
ax.set_xlabel("Change on ionization (%)")
ax.set_title("(F) Summary", loc='left', fontweight='bold')
ax.set_xlim(0, 1100); ax.grid(alpha=0.2, axis='x')

fig.suptitle("Phase 3: Acid \u2192 Intestinal pH-switch (5-chain L100 film)",
             fontsize=17, fontweight='bold', y=0.98)
fig.savefig("figure08_final.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure08_final.png")
