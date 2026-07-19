import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, Ellipse

plt.rcParams.update({'font.size': 13, 'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans']})

POLY="#2C5F8A"; TECC="#2E8B57"; PEGC="#B06A2C"; HB="#C0392B"; VDW="#8E7CC3"
fig = plt.figure(figsize=(15, 10.5)); fig.patch.set_facecolor('white')
ax = fig.add_axes([0.02,0.02,0.96,0.93]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')

def polymer_chain(cx, cy, scale, seed, color=POLY, lw=3.2):
    np.random.seed(seed)
    t=np.linspace(0,3*2*np.pi,220); ox,oy=np.random.uniform(-1,1,2)
    xx=cx+ox+scale*np.cos(t)*(1+0.18*np.sin(1.7*t+seed))
    yy=cy+oy+scale*0.65*np.sin(t)*(1+0.13*np.cos(2.1*t+seed))
    ax.plot(xx,yy,color=color,lw=lw,alpha=0.9,solid_capstyle='round',zorder=3)

# ============ LEFT: TEC (taller box: y 12 -> 87) ============
ax.add_patch(FancyBboxPatch((3,12),44,75, boxstyle="round,pad=0.5",
             facecolor="#EAF6EE", edgecolor=TECC, lw=2.4, zorder=1))
ax.text(25, 83.5, "TEC", ha='center', fontsize=25, fontweight='bold', color=TECC)
ax.text(25, 79.5, "(triethyl citrate)", ha='center', fontsize=14, color='#555', style='italic')

# cartoon upper region
for i,(dx,dy) in enumerate([(16,70),(34,70),(25,60)]):
    polymer_chain(dx,dy,4.4,i*5+1)
np.random.seed(10)
for (tx,ty) in [(25,70),(20,64),(30,64),(25,76),(18,58),(32,58)]:
    ax.add_patch(Circle((tx,ty),1.4,facecolor=TECC,edgecolor='white',lw=1,zorder=6))
    ax.plot([tx,tx+2.6],[ty,ty+1.5],':',color=HB,lw=2.0,zorder=5)

# descriptor (larger fonts)
ax.text(25, 48, "Coulomb / H-bond\u2013driven binding", ha='center', fontsize=15.5, color=HB, fontweight='bold')
ax.text(25, 43.5, "directional, specific contacts", ha='center', fontsize=13.5, color='#444')

# data box (bigger, larger font)
ax.add_patch(FancyBboxPatch((6,17),38,20, boxstyle="round,pad=0.3",
             facecolor='white', edgecolor=TECC, lw=1.8, zorder=2))
tec_data=("Coul-SR  \u221218.6   LJ-SR \u221214.7 kJ/mol\n\n"
          "H-bonds  0.39/frame\n\n"
          "$R_g$  0.719 nm\n\n"
          "System E  \u2212336 636 kJ/mol")
ax.text(25, 27, tec_data, ha='center', va='center', fontsize=13, family='monospace')

# ============ RIGHT: PEG ============
ax.add_patch(FancyBboxPatch((53,12),44,75, boxstyle="round,pad=0.5",
             facecolor="#FBF1E8", edgecolor=PEGC, lw=2.4, zorder=1))
ax.text(75, 83.5, "PEG400", ha='center', fontsize=25, fontweight='bold', color=PEGC)
ax.text(75, 79.5, "(polyethylene glycol)", ha='center', fontsize=14, color='#555', style='italic')

for i,(dx,dy) in enumerate([(66,70),(84,70),(75,60)]):
    polymer_chain(dx,dy,4.5,i*7+3)
np.random.seed(20)
for (px,py) in [(75,76),(68,64),(83,64),(75,54)]:
    tt=np.linspace(0,2*np.pi,40)
    ax.plot(px+2.3*np.cos(tt), py+1.5*np.sin(tt), '-', color=PEGC, lw=2.6, zorder=6)
    ax.add_patch(Ellipse((px,py), 7.8, 5.2, facecolor=VDW, alpha=0.22, edgecolor=VDW, lw=1.2, zorder=4))

# vdW label moved DOWN (clear of coils at y~54-76) -> place at y=48
ax.text(75, 48, "van der Waals (dispersion)\u2013driven", ha='center', fontsize=15.5, color=VDW, fontweight='bold')
ax.text(75, 43.5, "diffuse, non-directional contact", ha='center', fontsize=13.5, color='#444')

ax.add_patch(FancyBboxPatch((56,17),38,20, boxstyle="round,pad=0.3",
             facecolor='white', edgecolor=PEGC, lw=1.8, zorder=2))
peg_data=("Coul-SR  \u22128.8    LJ-SR \u221228.1 kJ/mol\n\n"
          "H-bonds  0.16/frame\n\n"
          "$R_g$  0.779 nm\n\n"
          "System E  \u2212330 718 kJ/mol")
ax.text(75, 27, peg_data, ha='center', va='center', fontsize=13, family='monospace')

# center divider + verdict
ax.plot([50,50],[12,87],':',color='#AAAAAA',lw=2,zorder=0)
ax.add_patch(FancyBboxPatch((25,90),50,7, boxstyle="round,pad=0.3",
             facecolor="#EAF6EE", edgecolor=TECC, lw=2, zorder=2))
ax.text(50, 93.5, "TEC: stronger, directional coupling \u2192 better L100 plasticizer",
        ha='center', va='center', fontsize=14.5, fontweight='bold', color=TECC)

ax.text(50, 60, "2.1\u00d7\nCoulomb", ha='center', va='center', fontsize=12, fontweight='bold', color=TECC)
ax.text(50, 50, "2.4\u00d7\nH-bonds", ha='center', va='center', fontsize=12, fontweight='bold', color=TECC)

fig.text(0.5, 0.965, "Why TEC is the superior plasticizer for Eudragit L100",
         ha='center', fontsize=19, fontweight='bold')

leg=[Circle((0,0),1,facecolor=TECC,label='TEC'),
     mpatches.Patch(color=PEGC, label='PEG400'),
     mpatches.Patch(color=POLY, label='L100 chain'),
     plt.Line2D([0],[0],ls=':',color=HB,lw=2.2,label='H-bond (directional)'),
     mpatches.Patch(color=VDW, alpha=0.3, label='vdW contact (diffuse)')]
ax.legend(handles=leg, loc='lower center', ncol=5, fontsize=12.5, frameon=True,
          framealpha=0.96, edgecolor='#CCCCCC', bbox_to_anchor=(0.5,-0.02))

fig.savefig("figure04_tec_mechanism.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved figure04_tec_mechanism.png")
