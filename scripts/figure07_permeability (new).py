import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch

plt.rcParams.update({'font.size': 13, 'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans']})

BLUE="#2C5F8A"; ORANGE="#D96C3B"; WATER="#8FC7E8"; GREEN="#2E8B57"; RED="#C0392B"

fig = plt.figure(figsize=(15, 9.5)); fig.patch.set_facecolor('white')
ax = fig.add_axes([0.02,0.02,0.96,0.92]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')

def chains(cx, cy, scale, color, n, seed, lw=2.6):
    np.random.seed(seed)
    for k in range(n):
        t=np.linspace(0,3*2*np.pi,200); ox,oy=np.random.uniform(-3,3,2)
        xx=cx+ox+scale*np.cos(t)*(1+0.18*np.sin(1.7*t+k))
        yy=cy+oy+scale*0.65*np.sin(t)*(1+0.13*np.cos(2.1*t+k))
        ax.plot(xx,yy,color=color,lw=lw,alpha=0.9,solid_capstyle='round',zorder=3)

def water_dots(cx, cy, n, spread, seed, color=WATER, size=0.45):
    np.random.seed(seed)
    for _ in range(n):
        dx,dy=np.random.uniform(-spread,spread,2)
        ax.add_patch(Circle((cx+dx,cy+dy), size, facecolor=color, edgecolor='white', lw=0.4, zorder=4))

# ============ Panel A: low ionization (3.5%, Phase 2) ============
ax.add_patch(FancyBboxPatch((3,12),44,70, boxstyle="round,pad=0.5", facecolor="#EAF0F6", edgecolor=BLUE, lw=2.2, zorder=1))
ax.text(25, 78.5, "Low ionization (3.5%)", ha='center', fontsize=21, fontweight='bold', color=BLUE)
ax.text(25, 74.5, "Phase 2 film model", ha='center', fontsize=15.5, color='#555', style='italic')

# compact film (tight chains, sparse water around)
chains(25, 58, 3.2, BLUE, 5, 1, lw=3)
water_dots(25, 60, 18, 14, 2, color=WATER, size=0.5)   # some water, but not flooding
# a "barrier" ring to show impermeability
circ = plt.Circle((25,60), 13, fill=False, edgecolor=RED, lw=2.2, linestyle='--', zorder=5)
ax.add_patch(circ)
ax.text(25, 36, "no detectable diffusion barrier", ha='center', fontsize=15.5, color=RED, fontweight='bold')

ax.add_patch(FancyBboxPatch((5,15),40,19, boxstyle="round,pad=0.3", facecolor='white', edgecolor=BLUE, lw=1.6, zorder=2))
ax.text(25,24.5, "Water diffusion\n$D$ = 2.56 \u00d7 10$^{-5}$ cm$^2$/s\n(\u2248 bulk water)", ha='center', va='center', fontsize=16, family='monospace')

# ============ Panel B: full ionization (100%, Phase 3) ============
ax.add_patch(FancyBboxPatch((53,12),44,70, boxstyle="round,pad=0.5", facecolor="#FBEEE6", edgecolor=ORANGE, lw=2.2, zorder=1))
ax.text(75, 78.5, "Full ionization (100%)", ha='center', fontsize=21, fontweight='bold', color=ORANGE)
ax.text(75, 74.5, "Phase 3: intestinal vs. acid", ha='center', fontsize=15.5, color='#555', style='italic')

# swollen film (chains apart, water flooding in)
chains(75, 58, 4.6, ORANGE, 5, 8, lw=3)
water_dots(75, 60, 55, 17, 9, color=WATER, size=0.5)   # lots of water flooding
# open arrows showing water ingress
for ang in [20,90,160,230,300]:
    a=np.radians(ang)
    ax.annotate('', xy=(75+16*np.cos(a),58+16*np.sin(a)), xytext=(75+9*np.cos(a),58+9*np.sin(a)),
                arrowprops=dict(arrowstyle='-|>', color="#1A5276", lw=1.8))
ax.text(75, 36, "water-accessible, permeable", ha='center', fontsize=15.5, color="#1A5276", fontweight='bold')

ax.add_patch(FancyBboxPatch((55,15),40,19, boxstyle="round,pad=0.3", facecolor='white', edgecolor=ORANGE, lw=1.6, zorder=2))
ax.text(75,24.5, "Water uptake near polymer\n925 \u2192 1501 (within 0.5 nm)\n+62% vs. acid state", ha='center', va='center', fontsize=16, family='monospace')

# ============ verdict + divider ============
ax.plot([50,50],[12,84],':',color='#AAAAAA',lw=2,zorder=0)
ax.add_patch(FancyBboxPatch((12,88),76,11, boxstyle="round,pad=0.3", facecolor="#F0F0F0", edgecolor='#888', lw=1.8, zorder=2))
ax.text(50, 93.5, "L100 stays protective at low pH, becomes water-accessible toward intestinal pH",
        ha='center', va='center', fontsize=17, fontweight='bold', color='#333')

fig.text(0.5, 0.975, "Ionization-dependent permeability of the L100 film",
         ha='center', fontsize=23, fontweight='bold')

leg=[mpatches.Patch(color=BLUE, label='L100 chain (low ioniz.)'),
     mpatches.Patch(color=ORANGE, label='L100 chain (ionized)'),
     plt.Line2D([0],[0],marker='o',color='w',markerfacecolor=WATER,ms=11,markeredgecolor='white',label='Water')]
ax.legend(handles=leg, loc='lower center', ncol=3, fontsize=15, frameon=True,
          framealpha=0.96, edgecolor='#CCCCCC', bbox_to_anchor=(0.5,-0.02))

fig.savefig("figure07_permeability.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure07_permeability.png")
