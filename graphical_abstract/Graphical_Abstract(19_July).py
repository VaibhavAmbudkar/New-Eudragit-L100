import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch

plt.rcParams.update({'font.size': 15, 'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans']})

BLUE="#2C5F8A"; ORANGE="#D96C3B"; GREEN="#2E8B57"; RED="#C0392B"; PURPLE="#7D3C98"; GOLD="#C9962C"

fig, axes = plt.subplots(2, 3, figsize=(19, 11))
fig.patch.set_facecolor('white')
fig.subplots_adjust(left=0.008, right=0.992, top=0.93, bottom=0.015, wspace=0.045, hspace=0.10)

def panel_frame(ax, bg, edge, title, subtitle):
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.1,0.1), 9.8, 9.8, boxstyle="round,pad=0.1",
                 facecolor=bg, edgecolor=edge, lw=2.6, zorder=0))
    ax.text(5, 9.3, title, ha='center', va='top', fontsize=22, fontweight='bold', color=edge)
    ax.text(5, 8.35, subtitle, ha='center', va='top', fontsize=15.5, color='#444', style='italic')

# ============ Panel 1: Ionization effect (non-monotonic) ============
ax = axes[0,0]
panel_frame(ax, "#EAF0F6", BLUE, "1. Ionization Effect", "Non-monotonic single-chain response")
ion = [0,10,30,40,50,80,100]
rg  = [0.752,0.691,0.702,0.704,0.645,0.749,0.795]
axins = ax.inset_axes([0.16, 0.40, 0.68, 0.24])
axins.plot(ion, rg, 'o-', color=BLUE, lw=3, ms=10, markeredgecolor='white', markeredgewidth=1.5)
axins.set_xlim(-5, 105)
axins.set_ylim(0.6, 0.83)
axins.set_xticks([0,20,40,60,80,100])
axins.set_yticks([0.6,0.65,0.7,0.75,0.8])
axins.set_xlabel("Ionization (%)", fontsize=14)
axins.set_ylabel("$R_g$ (nm)", fontsize=14)
axins.tick_params(labelsize=13)
axins.grid(alpha=0.25)
ax.text(5, 0.75, "Flat, non-monotonic \u2192\nswelling is NOT single-chain", ha='center', fontsize=13, fontweight='bold', color=BLUE, clip_on=True, linespacing=1.5)

# ============ Panel 2: TEC vs PEG400 ============
ax = axes[0,1]
panel_frame(ax, "#EAF6EE", GREEN, "2. TEC vs. PEG400", "TEC: stronger, more stable binding")
axins = ax.inset_axes([0.16, 0.40, 0.68, 0.26])
labels = ["TEC", "PEG400"]
coul = [-18.6, -8.8]
axins.bar([0,1], coul, width=0.55, color=[GREEN, ORANGE], edgecolor='black', linewidth=1.3)
for x,v in zip([0,1],coul):
    axins.text(x, v+1.3, f"{v}", ha='center', va='bottom', fontsize=15, fontweight='bold')
axins.set_xticks([0,1]); axins.set_xticklabels(labels, fontsize=15)
axins.set_ylabel("Coul-SR (kJ/mol)", fontsize=14)
axins.set_ylim(-22,1)
axins.set_yticks([-20,-15,-10,-5,0])
axins.tick_params(labelsize=13)
axins.grid(alpha=0.25, axis='y')
ax.text(5, 0.75, "2.1\u00d7 stronger Coulomb\n+ 2.4\u00d7 more H-bonds", ha='center', fontsize=13, fontweight='bold', color=GREEN, clip_on=True, linespacing=1.5)

# ============ Panel 3: TEC concentration effect ============
ax = axes[0,2]
panel_frame(ax, "#FBEEE6", ORANGE, "3. TEC Concentration", "Chain expands, free volume unchanged")
axins = ax.inset_axes([0.14, 0.40, 0.72, 0.26])
conc = [12.9,22.9,30.8,37.2]
rgc  = [1.494,1.573,2.267,2.269]
axins.plot(conc, rgc, 'o-', color=ORANGE, lw=3, ms=10, markeredgecolor='white', markeredgewidth=1.5)
axins.set_xlim(10, 40)
axins.set_ylim(1.4, 2.35)
axins.set_yticks([1.5,1.75,2.0,2.25])
axins.set_xlabel("TEC (% w/w)", fontsize=14)
axins.set_ylabel("Chain $R_g$ (nm)", fontsize=14)
axins.tick_params(labelsize=13)
axins.grid(alpha=0.25)
ax.text(5, 0.75, "$R_g$ 1.49\u21922.27 nm\nfree volume flat (~43%)", ha='center', fontsize=13, fontweight='bold', color=ORANGE, clip_on=True, linespacing=1.5)

# ============ Panel 4: pH-switch swelling ============
ax = axes[1,0]
panel_frame(ax, "#EAF0F6", RED, "4. pH-Switch Swelling", "Ionization drives coherent film swelling")
def blob(ax_,cx,cy,scale,seed,color):
    np.random.seed(seed)
    t=np.linspace(0,2*np.pi,100)
    r=scale*(1+0.15*np.sin(4*t+seed))
    ax_.plot(cx+r*np.cos(t), cy+r*0.75*np.sin(t), color=color, lw=2.6)
blob(ax, 2.7, 5.0, 1.2, 1, BLUE)
blob(ax, 7.3, 5.0, 1.75, 2, ORANGE)
ax.annotate('', xy=(5.9,5.0), xytext=(4.1,5.0),
            arrowprops=dict(arrowstyle='-|>', color='#333', lw=3, mutation_scale=28))
ax.text(2.7, 2.85, "acid, $R_g$=0.76", ha='center', fontsize=13.5, fontweight='bold', color=BLUE)
ax.text(7.3, 2.85, "intestinal, $R_g$=1.02 (+34%)", ha='center', fontsize=13.5, fontweight='bold', color=ORANGE)
ax.text(5, 0.75, "Water +62%  \u2022  Coulomb 4.1\u00d7\nTEC mobility +10\u00d7", ha='center', fontsize=13, fontweight='bold', color=RED, clip_on=True, linespacing=1.5)

# ============ Panel 5: Counterion effect ============
ax = axes[1,1]
panel_frame(ax, "#F3EEF6", PURPLE, "5. Counterion Effect", "Ion pairing controls chain size")
axins = ax.inset_axes([0.14, 0.40, 0.72, 0.26])
labels = ["NaCl", "NaHCO$_3$", "Na$_2$CO$_3$"]
rgvals = [0.740, 0.657, 1.413]
colors = [BLUE, GREEN, ORANGE]
bars = axins.bar([0,1,2], rgvals, width=0.6, color=colors, edgecolor='black', linewidth=1.3)
bars[2].set_hatch('///')
for x,v in zip([0,1,2],rgvals):
    axins.text(x, v+0.05, f"{v}", ha='center', fontsize=15, fontweight='bold')
axins.set_xticks([0,1,2]); axins.set_xticklabels(labels, fontsize=14)
axins.set_ylabel("$R_g$ (nm)", fontsize=14)
axins.set_ylim(0,1.65)
axins.set_yticks([0.0,0.5,1.0,1.5])
axins.tick_params(labelsize=13)
axins.grid(alpha=0.25, axis='y')
ax.text(5, 0.75, "NaHCO$_3$ \u221211%\nNa$_2$CO$_3$ +91% (non-equil.)", ha='center', fontsize=13, fontweight='bold', color=PURPLE, clip_on=True, linespacing=1.5)

# ============ Panel 6: Concentration & c* ============
ax = axes[1,2]
panel_frame(ax, "#EAF6EE", GOLD, "6. Overlap Concentration", "c* separates dilute from semi-dilute")
axins = ax.inset_axes([0.16, 0.40, 0.68, 0.26])
concn = [1.22,1.58,2.53,2.20,3.72,5.58,7.48,9.38]
rgn   = [0.839,0.816,0.794,0.757,0.733,0.736,0.732,0.735]
axins.plot(concn, rgn, 'o-', color=GOLD, lw=3, ms=9, markeredgecolor='white', markeredgewidth=1.3)
axins.set_xlim(0, 10)
axins.set_ylim(0.71, 0.86)
axins.set_yticks([0.72,0.76,0.80,0.84])
axins.axvspan(2.5, 3.0, color=RED, alpha=0.18)
axins.text(2.75, 0.795, "c*", ha='center', fontsize=15, fontweight='bold', color=RED)
axins.set_xlabel("Conc. (% w/v)", fontsize=14)
axins.set_ylabel("$R_g$ (nm)", fontsize=14)
axins.tick_params(labelsize=13)
axins.grid(alpha=0.25)
ax.text(5, 0.75, "c* \u2248 2.5\u20133.0% w/v\ncoating range 5\u201310% lies above c*", ha='center', fontsize=13, fontweight='bold', color=GOLD, clip_on=True, linespacing=1.5)

fig.text(0.5, 0.975, "Eudragit L100: Six Key Molecular-Level Findings",
         ha='center', fontsize=28, fontweight='bold')

fig.savefig("six_panel_abstract.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved six_panel_abstract.png")
