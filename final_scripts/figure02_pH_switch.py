"""
Figure 2 - Schematic of the pH-triggered swelling of an Eudragit L100 film.

Left  : gastric (acid, pH 1.2)   - protonated -COOH, compact film
Right : intestinal (pH 6.8)      - ionized -COO-, swollen and hydrated film

The molecular positions are schematic (for illustration); the Rg values and
the +34% change are the real film-scale MD results (5-chain L100/TEC film,
deprotonated carboxylate charge = -1.0 e).

Output: figure02_pH_switch.png (300 dpi)
Run:    python figure02_pH_switch.py
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle

plt.rcParams.update({
    'font.size': 14, 'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans'],
})

# ---- colours ----
BLUE = "#2C5F8A"; ORANGE = "#D96C3B"; PURPLE = "#7D3C98"
WATER = "#8FC7E8"; NA = "#F0A830"
BACK_ACID = "#FBEEE6"; BACK_INT = "#E8F0F8"

fig, (axL, axC, axR) = plt.subplots(
    1, 3, figsize=(15, 6.2), gridspec_kw={'width_ratios': [1, 0.28, 1]})
fig.patch.set_facecolor('white')


def chain(ax, cx, cy, scale, seed, color, n_loops):
    """Draw one wiggly polymer chain as a closed random loop."""
    np.random.seed(seed)
    t = np.linspace(0, n_loops * 2 * np.pi, 400)
    x = cx + scale * np.cos(t) * (1 + 0.20 * np.sin(1.7 * t + seed))
    y = cy + scale * 0.7 * np.sin(t) * (1 + 0.15 * np.cos(2.1 * t + seed))
    ax.plot(x, y, color=color, lw=3, alpha=0.9, solid_capstyle='round', zorder=3)


# ============ LEFT: ACID (collapsed) ============
ax = axL
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
ax.add_patch(mpatches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6,
             boxstyle="round,pad=0.1", facecolor=BACK_ACID,
             edgecolor='none', zorder=0))
for i, (cx, cy) in enumerate([(5, 5), (3.8, 6), (6.2, 6), (4, 3.8), (6.2, 4)]):
    chain(ax, cx, cy, 0.85, i * 7 + 1, BLUE, 3)
np.random.seed(1)
for _ in range(14):
    ax.add_patch(Circle((np.random.uniform(3, 7), np.random.uniform(3, 7)),
                 0.12, facecolor="#C0392B", edgecolor='white', lw=0.8, zorder=5))
for _ in range(18):
    ax.plot(np.random.uniform(0.6, 9.4), np.random.uniform(0.6, 9.4), 'o',
            color=WATER, ms=7, alpha=0.5, markeredgecolor='white', mew=0.6, zorder=2)
ax.text(5, 9.2, "Gastric (acid, pH 1.2)", ha='center', fontsize=15,
        fontweight='bold', color="#922B21")
ax.text(5, 8.4, "$R_g$ = 0.758 nm", ha='center', fontsize=14,
        fontweight='bold', color=BLUE)
ax.text(5, 0.75, "Protonated -COOH\ncompact film", ha='center',
        fontsize=12.5, color=BLUE)

# ============ CENTER: arrow ============
ax = axC
ax.set_xlim(0, 1); ax.set_ylim(0, 10); ax.axis('off')
ax.annotate('', xy=(0.85, 5), xytext=(0.15, 5),
            arrowprops=dict(arrowstyle='-|>', color='#444444', lw=3, mutation_scale=32))
ax.text(0.5, 6.0, "pH \u2191", ha='center', fontsize=17, fontweight='bold')
ax.text(0.5, 5.5, "ionization", ha='center', fontsize=12)
ax.text(0.5, 3.9, "+34% $R_g$", ha='center', fontsize=13,
        fontweight='bold', color=ORANGE)

# ============ RIGHT: INTESTINAL (expanded) ============
ax = axR
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
ax.add_patch(mpatches.FancyBboxPatch((0.2, 0.2), 9.6, 9.6,
             boxstyle="round,pad=0.1", facecolor=BACK_INT,
             edgecolor='none', zorder=0))
for i, (cx, cy) in enumerate([(5, 5), (2.8, 6.8), (7.2, 6.8), (2.6, 3), (7.4, 3)]):
    chain(ax, cx, cy, 1.15, i * 7 + 3, ORANGE, 5)
np.random.seed(4)
for _ in range(16):
    ax.add_patch(Circle((np.random.uniform(1.5, 8.5), np.random.uniform(1.5, 8.5)),
                 0.12, facecolor=PURPLE, edgecolor='white', lw=0.8, zorder=5))
for _ in range(12):
    x, y = np.random.uniform(1, 9), np.random.uniform(1, 9)
    ax.add_patch(plt.Polygon([[x, y + 0.13], [x - 0.11, y - 0.08], [x + 0.11, y - 0.08]],
                 facecolor=NA, edgecolor='white', lw=0.8, zorder=5))
for _ in range(34):
    ax.plot(np.random.uniform(0.6, 9.4), np.random.uniform(0.6, 9.4), 'o',
            color=WATER, ms=7, alpha=0.55, markeredgecolor='white', mew=0.6, zorder=2)
ax.text(5, 9.2, "Intestinal (ionized, pH 6.8)", ha='center', fontsize=15,
        fontweight='bold', color="#1A5276")
ax.text(5, 8.4, "$R_g$ = 1.015 nm", ha='center', fontsize=14,
        fontweight='bold', color=ORANGE)
ax.text(5, 0.75, "Ionized -COO\u207b\nswollen, hydrated film", ha='center',
        fontsize=12.5, color=ORANGE)

# ---- shared legend ----
leg = [
    mpatches.Patch(color="#C0392B", label='-COOH (protonated)'),
    mpatches.Patch(color=PURPLE, label='-COO\u207b (ionized)'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=WATER, ms=12,
               markeredgecolor='white', label='Water'),
    plt.Line2D([0], [0], marker='^', color='w', markerfacecolor=NA, ms=12,
               markeredgecolor='white', label='Na\u207a'),
]
fig.legend(handles=leg, loc='lower center', ncol=4, fontsize=12.5,
           frameon=True, framealpha=0.96, edgecolor='#CCCCCC',
           bbox_to_anchor=(0.5, -0.02))

fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.10, wspace=0.05)
fig.savefig("figure02_pH_switch.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure02_pH_switch.png")
