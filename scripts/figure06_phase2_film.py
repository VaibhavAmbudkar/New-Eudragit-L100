import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 13, 'axes.labelsize': 14, 'axes.titlesize': 15,
    'xtick.labelsize': 12, 'ytick.labelsize': 12, 'legend.fontsize': 11.5,
    'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans'],
    'axes.linewidth': 1.4, 'xtick.major.width': 1.4, 'ytick.major.width': 1.4,
    'xtick.major.size': 5, 'ytick.major.size': 5,
})

BLUE="#2C5F8A"; ORANGE="#D96C3B"; GREEN="#2E8B57"; PURPLE="#7D3C98"

# Z-density data
z = [0.10,0.89,1.68,2.47,3.26,4.05,4.84,5.63,6.42,7.20,7.99,8.78,9.57]
poly = [12.4,9.9,11.1,4.2,7.4,16.6,22.4,22.0,15.9,22.1,24.4,24.3,15.8]
tec  = [6.4,7.4,5.2,4.3,10.4,13.5,9.3,9.3,10.0,8.5,8.0,5.5,7.1]
water= [976.7,974.1,975.0,985.0,973.7,969.7,964.0,970.2,968.3,964.1,968.2,965.8,975.8]

fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.subplots_adjust(left=0.08, right=0.94, top=0.92, bottom=0.08, hspace=0.42, wspace=0.30)

# (A) Z-density profile - polymer & TEC on left axis, water on right
ax = axes[0,0]
ax.plot(z, poly, 'o-', color=BLUE, lw=2.4, ms=7, label="Polymer")
ax.plot(z, tec, 's-', color=ORANGE, lw=2.4, ms=7, label="TEC")
ax.set_xlabel("z (nm)")
ax.set_ylabel("Polymer / TEC density (kg/m$^3$)")
ax.set_title("(A) Z-density profile", loc='left', fontweight='bold')
ax2 = ax.twinx()
ax2.plot(z, water, '^--', color="#E75C8D", lw=1.8, ms=6, alpha=0.85, label="Water")
ax2.set_ylabel("Water density (kg/m$^3$)", color="#E75C8D")
ax2.set_ylim(900, 1050)
# combined legend placed below the axes, outside the data area
l1,lab1 = ax.get_legend_handles_labels()
l2,lab2 = ax2.get_legend_handles_labels()
ax.legend(l1+l2, lab1+lab2, loc='upper center', bbox_to_anchor=(0.5, -0.18), ncol=3, frameon=True, framealpha=0.95, edgecolor='#CCCCCC')

ax.grid(alpha=0.2)

# (B) per-chain Rg (single stable value with error)
ax = axes[0,1]
ax.bar([0], [0.749], width=0.5, color=BLUE, edgecolor='black', linewidth=1.3,
       yerr=[0.021], capsize=10, error_kw=dict(lw=1.8))
ax.text(0, 0.749+0.021+0.02, "0.749 \u00b1 0.021 nm", ha='center', fontsize=13, fontweight='bold')
ax.set_xticks([0]); ax.set_xticklabels(["5-chain film"])
ax.set_ylabel("Per-chain $R_g$ (nm)")
ax.set_title("(B) Chain size (stable film)", loc='left', fontweight='bold')
ax.set_ylim(0, 1.0); ax.set_xlim(-0.8, 0.8)
ax.grid(alpha=0.2, axis='y')

# (C) water diffusion
ax = axes[1,0]
ax.bar([0], [2.563], width=0.5, color=GREEN, edgecolor='black', linewidth=1.3,
       yerr=[0.04], capsize=10, error_kw=dict(lw=1.8))
ax.text(0, 2.563+0.15, "2.563 \u00b1 0.04", ha='center', fontsize=13, fontweight='bold')
ax.set_xticks([0]); ax.set_xticklabels(["Water in film"])
ax.set_ylabel("Water diffusion ($10^{-5}$ cm$^2$/s)")
ax.set_title("(C) Water mobility", loc='left', fontweight='bold')
ax.set_ylim(0, 3.2); ax.set_xlim(-0.8, 0.8)
ax.grid(alpha=0.2, axis='y')

# (D) Coul/LJ decomposition of TEC-polymer interaction
ax = axes[1,1]
ax.bar([0], [-77.9], width=0.5, color="#4C72B0", edgecolor='black', linewidth=1.3, label="Coul-SR")
ax.bar([1], [-196.4], width=0.5, color="#DD8452", edgecolor='black', linewidth=1.3, label="LJ-SR")
for xi, v in zip([0,1], [-77.9, -196.4]):
    ax.text(xi, v-12, f"{v:.1f}", ha='center', va='top', fontsize=13, fontweight='bold')
ax.set_xticks([0,1]); ax.set_xticklabels(["Coul-SR", "LJ-SR"])
ax.set_ylabel("TEC\u2013polymer energy (kJ/mol)")
ax.set_title("(D) TEC\u2013L100 interaction", loc='left', fontweight='bold')
ax.axhline(0, color='black', lw=0.9)
ax.set_ylim(-230, 20)
ax.grid(alpha=0.2, axis='y')

fig.suptitle("Phase 2: Multi-chain film formation (5-chain L100 + 17 TEC)",
             fontsize=16, fontweight='bold', y=0.98)
fig.savefig("figure06_phase2_film.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure06_phase2_film.png")
