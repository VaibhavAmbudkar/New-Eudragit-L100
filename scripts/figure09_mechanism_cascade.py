import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.size': 13, 'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans']})

BLUE="#2C5F8A"; ORANGE="#D96C3B"; PURPLE="#7D3C98"; GREEN="#2E8B57"
WATER="#8FC7E8"; NA="#F0A830"; RED="#C0392B"; DRUG="#B03A6E"

fig = plt.figure(figsize=(15, 11))
fig.patch.set_facecolor('white')
ax = fig.add_axes([0.02, 0.02, 0.96, 0.92]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')

col_x = [18, 50, 82]
row_y = [68, 27]
R = 12.5; Ry = 12.5

titles = ["1. pH rises", "2. Ionization", "3. Electrostatics",
          "4. Swelling", "5. Plasticizer mobility", "6. Drug release"]
notes = [
    "gastric \u2192 intestinal\npH 1.2 \u2192 6.8",
    "\u2013COOH \u2192 \u2013COO\u207b\ncarboxyls deprotonate",
    "Coulomb 4.1\u00d7 stronger\n\u22126779 \u2192 \u221227854 kJ/mol",
    "$R_g$ +34%, water +62%\nseparation +30%",
    "TEC diffusion 10\u00d7 faster\n0.05 \u2192 0.56 \u00d710\u207b\u2075 cm\u00b2/s",
    "swollen hydrated film\nenables intestinal release",
]
bgs = ["#FBEEE6", "#F3EEF6", "#EAF0F6", "#E8F0F8", "#EAF6EE", "#FBEAF1"]

def center(i): return col_x[i%3], row_y[i//3]
def panel_bg(cx, cy, color):
    ax.add_patch(FancyBboxPatch((cx-R, cy-Ry), 2*R, 2*Ry, boxstyle="round,pad=0.4",
                 facecolor=color, edgecolor='#BBBBBB', lw=1.3, zorder=1))
def chains(cx, cy, scale, color, n, seed):
    np.random.seed(seed)
    for k in range(n):
        t=np.linspace(0, 3*2*np.pi, 200); ox,oy=np.random.uniform(-3.5,3.5,2)
        xx=cx+ox+scale*np.cos(t)*(1+0.2*np.sin(1.7*t+k))
        yy=cy+oy+scale*0.7*np.sin(t)*(1+0.15*np.cos(2.1*t+k))
        ax.plot(xx,yy,color=color,lw=1.8,alpha=0.9,solid_capstyle='round',zorder=3)
def dots(cx, cy, n, color, spread, seed, marker='o', size=45):
    np.random.seed(seed)
    for _ in range(n):
        dx,dy=np.random.uniform(-spread,spread,2)
        if marker=='o':
            ax.add_patch(Circle((cx+dx, cy+dy), 0.42, facecolor=color, edgecolor='white', lw=0.5, zorder=5))
        else:
            ax.scatter(cx+dx, cy+dy, marker=marker, s=size, c=color, edgecolors='white', linewidths=0.5, zorder=5)

# panels
cx,cy=center(0); panel_bg(cx,cy,bgs[0]); chains(cx,cy,2.0,BLUE,3,1); dots(cx,cy,8,RED,5.5,2)
ax.text(cx,cy+Ry-2,"pH \u2191",ha='center',fontsize=17,fontweight='bold',color="#922B21")

cx,cy=center(1); panel_bg(cx,cy,bgs[1]); chains(cx,cy,2.2,BLUE,3,3); dots(cx,cy,10,PURPLE,6,4); dots(cx,cy,6,NA,6.5,5,marker='^',size=55)
ax.text(cx,cy+Ry-2,"COO\u207b",ha='center',fontsize=16,fontweight='bold',color=PURPLE)

cx,cy=center(2); panel_bg(cx,cy,bgs[2]); chains(cx,cy,2.4,BLUE,3,6); dots(cx,cy,10,PURPLE,6.5,7)
for ang in range(0,360,60):
    a=np.radians(ang)
    ax.annotate('',xy=(cx+8*np.cos(a),cy+8*np.sin(a)),xytext=(cx+3.5*np.cos(a),cy+3.5*np.sin(a)),arrowprops=dict(arrowstyle='-|>',color=RED,lw=2.0))
ax.text(cx,cy+Ry-2,"repulsion",ha='center',fontsize=14,fontweight='bold',color=RED)

cx,cy=center(3); panel_bg(cx,cy,bgs[3]); chains(cx,cy,3.4,ORANGE,4,8); dots(cx,cy,45,WATER,9.5,9); dots(cx,cy,8,PURPLE,9,10)
ax.text(cx,cy+Ry-2,"swollen",ha='center',fontsize=15,fontweight='bold',color="#1A5276")

cx,cy=center(4); panel_bg(cx,cy,bgs[4]); chains(cx,cy,3.4,ORANGE,4,11)
np.random.seed(12)
for _ in range(7):
    tx,ty=cx+np.random.uniform(-7,7), cy+np.random.uniform(-7,7)
    ax.add_patch(Circle((tx,ty),0.85,facecolor=GREEN,edgecolor='white',lw=0.7,zorder=6))
    a=np.random.uniform(0,2*np.pi)
    ax.annotate('',xy=(tx+3*np.cos(a),ty+3*np.sin(a)),xytext=(tx,ty),arrowprops=dict(arrowstyle='-|>',color=GREEN,lw=1.7))
ax.text(cx,cy+Ry-2,"TEC mobile",ha='center',fontsize=14,fontweight='bold',color=GREEN)

cx,cy=center(5); panel_bg(cx,cy,bgs[5]); chains(cx,cy,3.6,ORANGE,3,13); dots(cx,cy,30,WATER,10,14)
np.random.seed(15)
for _ in range(9):
    a=np.random.uniform(0,2*np.pi); r=np.random.uniform(2,9); dx,dy=r*np.cos(a),r*np.sin(a)
    ax.add_patch(Circle((cx+dx,cy+dy),0.7,facecolor=DRUG,edgecolor='white',lw=0.6,zorder=6))
    ax.annotate('',xy=(cx+dx*1.4,cy+dy*1.4),xytext=(cx+dx,cy+dy),arrowprops=dict(arrowstyle='-|>',color=DRUG,lw=1.4))
ax.text(cx,cy+Ry-2,"release",ha='center',fontsize=15,fontweight='bold',color=DRUG)

# titles + notes
for i in range(6):
    cx,cy=center(i)
    ax.text(cx, cy-Ry-2.4, titles[i], ha='center', fontsize=14.5, fontweight='bold')
    ax.add_patch(FancyBboxPatch((cx-R, cy-Ry-12), 2*R, 8.0, boxstyle="round,pad=0.2",
                 facecolor='#F7F7F7', edgecolor='#DDDDDD', lw=1, zorder=1))
    ax.text(cx, cy-Ry-7.6, notes[i], ha='center', va='center', fontsize=14)

# ---- flow arrows ----
def harrow(x0,x1,y):
    ax.annotate('',xy=(x1,y),xytext=(x0,y),arrowprops=dict(arrowstyle='-|>',color='#333333',lw=2.8,mutation_scale=28))
# top row 1->2->3
harrow(col_x[0]+R+0.3, col_x[1]-R-0.3, row_y[0])
harrow(col_x[1]+R+0.3, col_x[2]-R-0.3, row_y[0])
# bottom row 4->5->6
harrow(col_x[0]+R+0.3, col_x[1]-R-0.3, row_y[1])
harrow(col_x[1]+R+0.3, col_x[2]-R-0.3, row_y[1])
# (wrap arrow removed per request)

fig.text(0.5, 0.965, "pH-Triggered Swelling & Release Mechanism of the Eudragit L100 Film",
         ha='center', fontsize=18, fontweight='bold')

leg = [
    mpatches.Patch(color=RED, label='\u2013COOH'),
    mpatches.Patch(color=PURPLE, label='\u2013COO\u207b'),
    plt.Line2D([0],[0],marker='^',color='w',markerfacecolor=NA,ms=11,markeredgecolor='white',label='Na\u207a'),
    plt.Line2D([0],[0],marker='o',color='w',markerfacecolor=WATER,ms=11,markeredgecolor='white',label='Water'),
    plt.Line2D([0],[0],marker='o',color='w',markerfacecolor=GREEN,ms=11,markeredgecolor='white',label='TEC'),
    plt.Line2D([0],[0],marker='o',color='w',markerfacecolor=DRUG,ms=11,markeredgecolor='white',label='Drug'),
]
ax.legend(handles=leg, loc='lower center', ncol=6, fontsize=11.5, frameon=True,
          framealpha=0.96, edgecolor='#CCCCCC', bbox_to_anchor=(0.5, -0.02))

fig.savefig("figure09_6panel.png", dpi=300, bbox_inches='tight', facecolor='white')
print("saved")
