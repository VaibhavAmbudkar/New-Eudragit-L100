import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch

plt.rcParams.update({'font.size': 13, 'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans']})

BLUE = "#2C5F8A"; RED = "#C0392B"; PURPLE = "#7D3C98"; GOLD = "#C9962C"

# Real Phase 0 data (Figure 1)
ion_all = [0, 10, 30, 40, 50, 80, 100]
rg_all  = [0.752, 0.691, 0.702, 0.704, 0.645, 0.749, 0.795]

fig = plt.figure(figsize=(14, 5.8))
fig.patch.set_facecolor('white')
ax = fig.add_axes([0.02, 0.04, 0.96, 0.86])
ax.set_xlim(0, 100); ax.set_ylim(15, 58); ax.axis('off')

fig.text(0.5, 0.955, "Phase 0: Baseline Deprotonation Series \u2014 Non-Monotonic Conformational Response",
         ha='center', fontsize=17.5, fontweight='bold')

def chain_blob(cx, cy, scale, seed, color, lw=2.6):
    np.random.seed(seed)
    t = np.linspace(0, 2*np.pi, 150)
    r = scale*(1 + 0.15*np.sin(4*t+seed) + 0.07*np.cos(7*t+seed*2))
    x = cx + r*np.cos(t)
    y = cy + r*0.8*np.sin(t)
    ax.plot(x, y, color=color, lw=lw, solid_capstyle='round', zorder=3)

def ion_dots(cx, cy, scale, n_ionized, n_total=10, seed=0):
    """Place small dots around the blob perimeter representing MAA units:
    red = protonated (-COOH), purple = ionized (-COO-)."""
    np.random.seed(seed+500)
    angles = np.linspace(0, 2*np.pi, n_total, endpoint=False) + np.random.uniform(0,0.3,n_total)
    order = np.random.permutation(n_total)
    ionized_idx = set(order[:n_ionized])
    for i, ang in enumerate(angles):
        r = scale*1.15
        x = cx + r*np.cos(ang); y = cy + r*0.8*np.sin(ang)
        color = PURPLE if i in ionized_idx else RED
        ax.add_patch(Circle((x,y), 0.9, facecolor=color, edgecolor='white', lw=0.5, zorder=4))

# Three representative states spanning the real non-monotonic trend: 0%, 50% (the dip), 100%
states = [
    dict(cx=17, ion=0,   rg=0.752, n_ion=0,  label="0% ionized"),
    dict(cx=50, ion=50,  rg=0.645, n_ion=5,  label="50% ionized"),
    dict(cx=83, ion=100, rg=0.795, n_ion=10, label="100% ionized"),
]

panel_top = 50
for i, s in enumerate(states):
    cy = 38
    scale = 4.2 + (s['rg']-0.6)*8   # visually scale blob size with real Rg (exaggerated for clarity)
    chain_blob(s['cx'], cy, scale, seed=i*7+1, color=BLUE)
    ion_dots(s['cx'], cy, scale, s['n_ion'], seed=i*7+1)
    ax.text(s['cx'], panel_top, s['label'], ha='center', fontsize=15, fontweight='bold', color=BLUE)
    ax.text(s['cx'], 22, f"$R_g$ = {s['rg']:.3f} nm", ha='center', fontsize=13.5, family='monospace',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white', edgecolor=BLUE, linewidth=1.3))

# connecting arrows with non-monotonic annotation
ax.annotate('', xy=(41,38), xytext=(25,38), arrowprops=dict(arrowstyle='-|>', color='#333', lw=2.2))
ax.annotate('', xy=(74,38), xytext=(58,38), arrowprops=dict(arrowstyle='-|>', color='#333', lw=2.2))
ax.text(33, 41.5, "\u221214%", ha='center', fontsize=12, fontweight='bold', color=RED)
ax.text(66, 41.5, "+23%", ha='center', fontsize=12, fontweight='bold', color=RED)

# legend
leg = [
    mpatches.Patch(color=BLUE, label='L100 chain backbone'),
    plt.Line2D([0],[0], marker='o', color='w', markerfacecolor=RED, ms=10, markeredgecolor='white', label='\u2013COOH (protonated)'),
    plt.Line2D([0],[0], marker='o', color='w', markerfacecolor=PURPLE, ms=10, markeredgecolor='white', label='\u2013COO$^-$ (ionized)'),
]
ax.legend(handles=leg, loc='lower center', bbox_to_anchor=(0.5, -0.02), ncol=3, fontsize=12,
          frameon=True, framealpha=0.95, edgecolor='#CCCCCC')

fig.savefig("figure02_phase0.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure02_phase0.png")
