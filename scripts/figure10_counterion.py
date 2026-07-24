import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 15, 'axes.titlesize': 17,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans'],
    'axes.linewidth': 1.4, 'xtick.major.width': 1.4, 'ytick.major.width': 1.4,
    'xtick.major.size': 6, 'ytick.major.size': 6,
})

r = [0.000,0.040,0.080,0.120,0.160,0.200,0.240,0.280,0.320,0.360,0.400,0.440,0.480,0.520,0.560,0.600,0.640,0.680,0.720,0.760,0.800]
g_nacl = [0.0,0.0,0.0,0.0,0.0,0.0,87.2,6.0,2.7,1.9,2.9,3.2,2.4,2.4,2.6,2.9,3.8,3.9,2.0,1.9,2.2]
g_nahco3 = [0.0,0.0,0.0,0.0,0.0,0.8,420.6,11.5,8.2,6.3,3.3,3.4,1.9,1.5,2.4,3.4,6.0,9.7,8.9,10.5,11.6]
g_na2co3 = [0.0,0.0,0.0,0.0,0.0,0.1,113.6,5.6,3.7,5.2,5.9,4.9,3.4,2.7,3.6,3.9,3.9,4.0,3.5,4.1,3.9]

C_NACL = "#2C5F8A"; C_HCO3 = "#2E8B57"; C_CO3 = "#D96C3B"
labels = ["NaCl", "NaHCO$_3$", "Na$_2$CO$_3$"]
colors = [C_NACL, C_HCO3, C_CO3]

# Na2CO3 SASA value (placeholder - update with real computed value)
SASA_CO3 = 21.58

fig, axes = plt.subplots(1, 3, figsize=(16, 5.4))
fig.subplots_adjust(left=0.06, right=0.98, top=0.88, bottom=0.15, wspace=0.30)

# ---- Panel A: RDF ----
ax = axes[0]
ax.plot(r, g_nacl, '-', color=C_NACL, lw=2.6, label="NaCl (peak 87)")
ax.plot(r, g_nahco3, '-', color=C_HCO3, lw=2.6, label="NaHCO$_3$ (peak 421)")
ax.plot(r, g_na2co3, '-', color=C_CO3, lw=2.6, label="Na$_2$CO$_3$ (peak 114)")
ax.set_xlabel("r (nm)")
ax.set_ylabel("g(r), Na$^+$\u2013COO$^-$")
ax.set_title("(A) Counterion\u2013COO$^-$ RDF", loc='left', fontweight='bold')
ax.set_xlim(0, 0.8); ax.set_ylim(0, 460)
ax.legend(frameon=True, framealpha=0.95, edgecolor='#CCCCCC', loc='upper right')
ax.grid(alpha=0.2)
# CHANGE 1: annotation moved to LEFT of peak
ax.annotate("contact pair\n0.24 nm", xy=(0.24, 421), xytext=(0.02, 340),
            fontsize=12, arrowprops=dict(arrowstyle='->', color='#555555', lw=1.4))

# ---- Panel B: Rg ----
ax = axes[1]
rg = [0.740, 0.657, 1.413]
rg_err = [0.02, 0.02, 0.255]
x = [0, 1, 2]
bars = ax.bar(x, rg, width=0.6, color=colors, edgecolor='black', linewidth=1.3,
              yerr=rg_err, capsize=8, error_kw=dict(lw=1.6))
bars[2].set_hatch('///'); bars[2].set_alpha(0.75)
for xi, v, e in zip(x, rg, rg_err):
    ax.text(xi, v+e+0.04, f"{v:.3f}", ha='center', fontsize=13, fontweight='bold')
# CHANGE 2: removed "not equilibrated" text
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.set_ylabel("Radius of gyration, $R_g$ (nm)")
ax.set_title("(B) Chain size", loc='left', fontweight='bold')
ax.set_ylim(0, 1.85)
ax.grid(alpha=0.2, axis='y')

# ---- Panel C: SASA ----
ax = axes[2]
sasa = [17.37, 15.71, SASA_CO3]
sasa_err = [0.46, 0.43, 0.59]
x = [0, 1, 2]
bars = ax.bar(x, sasa, width=0.6, color=colors, edgecolor='black', linewidth=1.3,
              yerr=sasa_err, capsize=8, error_kw=dict(lw=1.6))
bars[2].set_hatch('///'); bars[2].set_alpha(0.75)
# CHANGE 3: removed "variable unequil" text
# CHANGE 4: show SASA value on Na2CO3 bar
for xi, v, e in zip(x, sasa, sasa_err):
    ax.text(xi, v+e+0.3, f"{v:.2f}", ha='center', fontsize=13, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.set_ylabel("SASA (nm$^2$)")
ax.set_title("(C) Surface area", loc='left', fontweight='bold')
ax.set_ylim(0, 24)
ax.grid(alpha=0.2, axis='y')

fig.suptitle("Phase 4: Counterion identity effect",
             fontsize=16, fontweight='bold', y=0.99)
fig.savefig("figure10_counterion.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure10_counterion.png with SASA_CO3 =", SASA_CO3)
