import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch

plt.rcParams.update({'font.size': 13, 'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans']})

WATER = "#8FC7E8"; BLUE = "#2C5F8A"; PURPLE = "#8E44AD"; RED = "#C0392B"

fig, axes = plt.subplots(1, 3, figsize=(16.5, 6.2))
fig.patch.set_facecolor('white')

def chain_blob(ax, cx, cy, scale, seed, color=BLUE, lw=2.4):
    np.random.seed(seed)
    t = np.linspace(0, 2*np.pi, 120)
    r = scale*(1 + 0.12*np.sin(4*t+seed) + 0.06*np.cos(7*t+seed*2))
    x = cx + r*np.cos(t); y = cy + r*np.sin(t)
    ax.plot(x, y, color=color, lw=lw, solid_capstyle='round')
    return cx, cy

def water_bg(ax, n, seed, xlim=(0,10), ylim=(0,10)):
    np.random.seed(seed)
    xs = np.random.uniform(*xlim, n); ys = np.random.uniform(*ylim, n)
    ax.scatter(xs, ys, s=18, color=WATER, zorder=1, alpha=0.85)

panel_specs = [
    dict(title="Dilute\n(below $c^*$)", n=2, conc="1.22% w/v", hb="0.00",
         centers=[(3.3,4.6),(6.2,5.8)], scale=1.1, seed=1, overlap=False),
    dict(title="Semidilute\n(at $c^*$)", n=8, conc="2.53% w/v", hb="1.82",
         centers=[(2.6,6.7),(3.6,7.0),(4.6,6.4),(2.9,5.1),(4.1,4.8),(6.8,6.5),(7.6,4.9),(6.4,3.9)],
         scale=1.0, seed=10, overlap=True),
    dict(title="Entangled\n(above $c^*$)", n=20, conc="3.72% w/v", hb="8.56",
         centers=[(2.0,7.6),(2.9,7.8),(3.7,7.3),(2.4,6.4),(3.3,6.6),(4.3,6.9),
                  (1.8,5.4),(2.7,5.6),(3.6,5.2),(4.5,5.7),(5.3,6.5),(5.9,5.4),
                  (6.7,6.8),(7.4,6.0),(6.2,4.3),(7.0,4.7),(2.3,3.9),(3.4,3.6),
                  (4.6,3.9),(5.7,3.7)],
         scale=0.68, seed=20, overlap=True),
]

for i, (ax, spec) in enumerate(zip(axes, panel_specs)):
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0,0),10,10, boxstyle="round,pad=0", facecolor="#EAF3FA",
                 edgecolor='#888', lw=1.6, zorder=0))
    water_bg(ax, 60, seed=100+i)
    for k,(cx,cy) in enumerate(spec['centers']):
        chain_blob(ax, cx, cy, spec['scale'], seed=spec['seed']+k)
    # H-bond dashed lines only where overlap occurs (semidilute/entangled)
    if spec['overlap']:
        np.random.seed(spec['seed']+99)
        cs = spec['centers']
        npairs = min(len(cs)*2, 14)
        for _ in range(npairs):
            a,b = np.random.choice(len(cs),2,replace=False)
            ax.plot([cs[a][0],cs[b][0]],[cs[a][1],cs[b][1]], ':', color=PURPLE, lw=1.3, alpha=0.75, zorder=2)
    ax.text(5, 9.85, spec['title'], ha='center', va='top', fontsize=14.5, fontweight='bold', linespacing=1.4)
    ax.text(5, 0.85, f"{spec['n']} chains, {spec['conc']}", ha='center', fontsize=12.5, color='#333')
    hb_color = RED if float(spec['hb'])>3 else (BLUE if float(spec['hb'])==0 else "#B8860B")
    ax.text(5, 0.35, f"H-bonds/frame: {spec['hb']}", ha='center', fontsize=12.5, fontweight='bold', color=hb_color)
    ax.text(0.3, 9.55, f"({chr(65+i)})", ha='left', va='top', fontsize=17, fontweight='bold')

fig.suptitle("Critical overlap concentration $c^*$ of the L100 chain",
             fontsize=18, fontweight='bold', y=1.0)
fig.text(0.5, -0.02,
         "Bulk modulus remains water-dominated ($\\approx$2.1\u20132.2 GPa) across this range,\n"
         "while inter-chain hydrogen bonding rises sharply beyond $c^*$ (\u2248 2.5\u20133.0% w/v)",
         ha='center', fontsize=12, style='italic')

fig.subplots_adjust(wspace=0.06, top=0.86, bottom=0.08)
fig.savefig("figure12_cstar.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure12_cstar.png")
