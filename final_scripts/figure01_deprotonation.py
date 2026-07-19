import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 16, 'axes.titlesize': 20,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans'],
    'axes.linewidth': 1.4, 'xtick.major.width': 1.4, 'ytick.major.width': 1.4,
    'xtick.major.size': 6, 'ytick.major.size': 6,
})

# block-averaged data (2-10 ns, 4 blocks): mean +/- SD
ion    = [0, 10, 30, 40, 50, 80, 100]
rg     = [0.7522, 0.6906, 0.7018, 0.7039, 0.6453, 0.7487, 0.7950]
rg_sd  = [0.0526, 0.0231, 0.0417, 0.0116, 0.0004, 0.0132, 0.0466]
sasa   = [17.4214, 16.7464, 16.4857, 16.7647, 15.4199, 17.6383, 18.7970]
sasa_sd= [0.9125, 0.4499, 0.5343, 0.4844, 0.0501, 0.3979, 0.3691]
labels = [f"{i}%" for i in ion]

drg   = [(r-rg[0])/rg[0]*100 for r in rg]
dsasa = [(s-sasa[0])/sasa[0]*100 for s in sasa]

BLUE = "#2C5F8A"; ORANGE = "#D96C3B"

fig, axes = plt.subplots(2, 2, figsize=(13.5, 11))
fig.subplots_adjust(left=0.08, right=0.95, top=0.94, bottom=0.08, hspace=0.28, wspace=0.28)

# (A) Rg with error bars
ax = axes[0,0]
ax.errorbar(ion, rg, yerr=rg_sd, fmt='o-', color=BLUE, lw=2.4, ms=11,
            markeredgecolor='white', markeredgewidth=1.6,
            capsize=6, capthick=1.6, ecolor='#555555', zorder=3)
ax.set_xlabel("Degree of ionization (%)")
ax.set_ylabel("Radius of gyration, $R_g$ (nm)")
ax.set_xlim(-8,108); ax.set_ylim(0.55, 0.90)
ax.set_title("(A)", loc='left', fontweight='bold'); ax.grid(alpha=0.2)

# (B) SASA with error bars
ax = axes[0,1]
ax.errorbar(ion, sasa, yerr=sasa_sd, fmt='s-', color=ORANGE, lw=2.4, ms=11,
            markeredgecolor='white', markeredgewidth=1.6,
            capsize=6, capthick=1.6, ecolor='#555555', zorder=3)
ax.set_xlabel("Degree of ionization (%)")
ax.set_ylabel("SASA (nm$^2$)")
ax.set_xlim(-8,108); ax.set_ylim(14.5, 19.8)
ax.set_title("(B)", loc='left', fontweight='bold'); ax.grid(alpha=0.2)

# (C) Delta bars with propagated error
ax = axes[1,0]
x = np.arange(len(ion)); w = 0.38
# error on delta% ~ (sd/mean0)*100 approx
drg_e   = [rg_sd[i]/rg[0]*100 for i in range(len(ion))]
dsasa_e = [sasa_sd[i]/sasa[0]*100 for i in range(len(ion))]
ax.bar(x-w/2, drg, w, yerr=drg_e, label="$\\Delta R_g$ (%)", color=BLUE,
       edgecolor="black", linewidth=1.2, capsize=4, error_kw=dict(lw=1.2))
ax.bar(x+w/2, dsasa, w, yerr=dsasa_e, label="$\\Delta$SASA (%)", color=ORANGE,
       edgecolor="black", linewidth=1.2, capsize=4, error_kw=dict(lw=1.2))
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.set_xlabel("Degree of ionization (%)")
ax.set_ylabel("Change from 0% (%)")
ax.set_title("(C)", loc='left', fontweight='bold')
ax.axhline(0, color='black', lw=0.9)
ax.legend(frameon=True, framealpha=0.95, edgecolor='#CCCCCC')
ax.grid(alpha=0.2, axis='y')

# (D) Rg-SASA correlation with error bars both axes
ax = axes[1,1]
ax.errorbar(rg, sasa, xerr=rg_sd, yerr=sasa_sd, fmt='none',
            ecolor='#999999', capsize=4, lw=1.2, zorder=2)
sc = ax.scatter(rg, sasa, c=ion, cmap='viridis', s=200, zorder=3,
                edgecolors='black', linewidths=1.4)
corr = np.corrcoef(rg, sasa)[0,1]
m,b = np.polyfit(rg, sasa, 1)
xf = np.linspace(min(rg)-0.02, max(rg)+0.02, 50)
ax.plot(xf, m*xf+b, '--', color='#C0392B', lw=2, label=f"Linear fit (r = {corr:.2f})")
ax.set_xlabel("Radius of gyration, $R_g$ (nm)")
ax.set_ylabel("SASA (nm$^2$)")
ax.set_title("(D)", loc='left', fontweight='bold')
ax.legend(loc='upper left', frameon=True, framealpha=0.95, edgecolor='#CCCCCC')
ax.grid(alpha=0.2)
cb = plt.colorbar(sc, ax=ax); cb.set_label("Ionization (%)", fontsize=13)

fig.savefig("figure01_errorbars.png", dpi=300, bbox_inches="tight", facecolor='white')
print(f"saved. r = {corr:.3f}")
