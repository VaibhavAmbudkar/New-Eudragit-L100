import MDAnalysis as mda
from MDAnalysis.lib.distances import distance_array
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import subprocess
import os

HOME = os.path.expanduser('~')
CHAIN_LEN = 266

SYSTEMS = [
    {'label': 'chain2',  'n':  2, 'pct_wv': 2.04, 'dir': 'phase2_5_batch/dilute',       'tpr': 'prod_extend30.tpr', 'xtc': 'prod_full30.xtc'},
    {'label': 'chain5',  'n':  5, 'pct_wv': 2.64, 'dir': 'phase2_5_batch/semidilute',   'tpr': 'prod_extend30.tpr', 'xtc': 'prod_full30.xtc'},
    {'label': 'chain8',  'n':  8, 'pct_wv': 4.21, 'dir': 'phase2_5_batch/concentrated', 'tpr': 'prod_extend30.tpr', 'xtc': 'prod_full30.xtc'},
    {'label': 'chain12', 'n': 12, 'pct_wv': 3.66, 'dir': 'phase2_5_batch/dense',        'tpr': 'prod_extend30.tpr', 'xtc': 'prod_full30.xtc'},
    {'label': 'chain20', 'n': 20, 'pct_wv': 6.00, 'dir': 'phase5_cstar/chain20',        'tpr': 'prod.tpr', 'xtc': 'prod.xtc'},
    {'label': 'chain30', 'n': 30, 'pct_wv': 9.00, 'dir': 'phase5_cstar/chain30',        'tpr': 'prod.tpr', 'xtc': 'prod.xtc'},
    {'label': 'chain40', 'n': 40, 'pct_wv': 12.0, 'dir': 'phase5_cstar/chain40',        'tpr': 'prod.tpr', 'xtc': 'prod.xtc'},
    {'label': 'chain50', 'n': 50, 'pct_wv': 15.0, 'dir': 'phase5_cstar/chain50',        'tpr': 'prod.tpr', 'xtc': 'prod.xtc'},
]

def calc_rg_perchain(u, n_chains, chain_len):
    chains = [u.select_atoms(f'index {i*chain_len}-{(i+1)*chain_len-1}') for i in range(n_chains)]
    all_rgs = []
    for ts in u.trajectory[::10]:
        frame_rgs = []
        for chain in chains:
            com = np.average(chain.positions, weights=chain.masses, axis=0)
            diff = chain.positions - com
            rg2 = np.sum(chain.masses * np.sum(diff**2, axis=1)) / chain.total_mass()
            frame_rgs.append(np.sqrt(rg2) / 10)
        all_rgs.append(np.mean(frame_rgs))
    return np.mean(all_rgs), np.std(all_rgs)

def calc_bulk_modulus_from_edr(sysdir, edr_name='prod.edr'):
    edr = os.path.join(HOME, sysdir, edr_name)
    if not os.path.exists(edr):
        return None
    try:
        subprocess.run(f'echo "Volume\n" | {HOME}/miniconda3/bin/gmx energy -f {edr} -o /tmp/vol_tmp.xvg 2>/dev/null', shell=True)
        if not os.path.exists('/tmp/vol_tmp.xvg'):
            return None
        data = np.loadtxt('/tmp/vol_tmp.xvg', comments=['#','@'])
        if data.ndim < 2 or len(data) < 10:
            return None
        V = data[:,1] * 1e-27
        kB = 1.380649e-23
        T = 298.0
        V_mean = np.mean(V)
        dV2 = np.var(V)
        if dV2 == 0:
            return None
        return kB * T * V_mean / dV2 / 1e6
    except:
        return None

def calc_hbonds_perchain(u, n_chains, chain_len, cutoff=3.5):
    chains = [u.select_atoms(f'index {i*chain_len}-{(i+1)*chain_len-1}') for i in range(n_chains)]
    hb_counts = []
    n_pairs = n_chains * (n_chains-1) / 2
    for ts in u.trajectory[::10]:
        count = 0
        for i in range(n_chains):
            for j in range(i+1, n_chains):
                d_i = chains[i].select_atoms('name O*')
                a_j = chains[j].select_atoms('name O*')
                if len(d_i) == 0 or len(a_j) == 0:
                    continue
                dist_mat = distance_array(d_i.positions, a_j.positions, box=u.dimensions)
                count += np.sum(dist_mat < cutoff)
        hb_counts.append(count / n_pairs)
    return np.mean(hb_counts), np.std(hb_counts)

def calc_close_contact(u, n_chains, chain_len, cutoff=5.0):
    chains = [u.select_atoms(f'index {i*chain_len}-{(i+1)*chain_len-1}') for i in range(n_chains)]
    contact_counts = np.zeros(n_chains)
    n_frames = 0
    for ts in u.trajectory[::10]:
        in_contact = np.zeros(n_chains, dtype=bool)
        for i in range(n_chains):
            for j in range(n_chains):
                if i == j:
                    continue
                dist_mat = distance_array(chains[i].positions, chains[j].positions, box=u.dimensions)
                if dist_mat.min() < cutoff:
                    in_contact[i] = True
                    break
        contact_counts += in_contact
        n_frames += 1
    return (contact_counts / n_frames).mean() * 100

results = []
for sys in SYSTEMS:
    tpr = os.path.join(HOME, sys['dir'], sys['tpr'])
    xtc = os.path.join(HOME, sys['dir'], sys['xtc'])
    if not os.path.exists(tpr) or not os.path.exists(xtc):
        print(f"SKIPPING {sys['label']}: files not found")
        continue
    print(f"\nAnalysing {sys['label']} ({sys['n']} chains, {sys['pct_wv']:.2f}% w/v)...")
    u = mda.Universe(tpr, xtc)
    n = sys['n']
    rg_mean, rg_std = calc_rg_perchain(u, n, CHAIN_LEN)
    K = calc_bulk_modulus_from_edr(sys['dir'])
    hb_mean, hb_std = calc_hbonds_perchain(u, n, CHAIN_LEN)
    contact = calc_close_contact(u, n, CHAIN_LEN)
    print(f"  Rg: {rg_mean:.3f} +/- {rg_std:.3f} nm")
    print(f"  Bulk modulus: {K:.1f} MPa" if K else "  Bulk modulus: n/a")
    print(f"  H-bonds/chain-pair: {hb_mean:.3f} +/- {hb_std:.3f}")
    print(f"  Close contact: {contact:.1f}%")
    results.append({'label': sys['label'], 'n': n, 'pct_wv': sys['pct_wv'],
                    'rg': rg_mean, 'rg_std': rg_std, 'K': K if K else 0,
                    'hb': hb_mean, 'contact': contact})

results.sort(key=lambda x: x['pct_wv'])
pcts = [r['pct_wv'] for r in results]

fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle('Eudragit L100: c* Concentration Series', fontsize=17, fontweight='bold')

axes[0,0].errorbar(pcts, [r['rg'] for r in results], yerr=[r['rg_std'] for r in results], fmt='o-', color='#1A4E8A', lw=2, ms=7, capsize=4)
axes[0,0].set_xlabel('Concentration (% w/v)', fontsize=12); axes[0,0].set_ylabel('Per-chain Rg (nm)', fontsize=12)
axes[0,0].set_title('(A) Per-chain Rg', fontsize=13, fontweight='bold')
axes[0,0].axvspan(5, 10, alpha=0.1, color='red', label='Practical window'); axes[0,0].legend(fontsize=9); axes[0,0].grid(alpha=0.3)

axes[0,1].plot(pcts, [r['hb'] for r in results], 's-', color='#8172B2', lw=2, ms=7)
axes[0,1].set_xlabel('Concentration (% w/v)', fontsize=12); axes[0,1].set_ylabel('H-bonds per chain-pair', fontsize=12)
axes[0,1].set_title('(B) Inter-chain H-bonding', fontsize=13, fontweight='bold'); axes[0,1].axvspan(5, 10, alpha=0.1, color='red'); axes[0,1].grid(alpha=0.3)

valid_K = [(r['pct_wv'], r['K']) for r in results if r['K'] > 0]
if valid_K:
    axes[1,0].plot([v[0] for v in valid_K], [v[1] for v in valid_K], '^-', color='#C44E52', lw=2, ms=7)
axes[1,0].set_xlabel('Concentration (% w/v)', fontsize=12); axes[1,0].set_ylabel('Bulk modulus (MPa)', fontsize=12)
axes[1,0].set_title('(C) Bulk Modulus', fontsize=13, fontweight='bold'); axes[1,0].axvspan(5, 10, alpha=0.1, color='red'); axes[1,0].grid(alpha=0.3)

axes[1,1].plot(pcts, [r['contact'] for r in results], 'D-', color='#55A868', lw=2, ms=7)
axes[1,1].set_xlabel('Concentration (% w/v)', fontsize=12); axes[1,1].set_ylabel('Chains in close contact (%)', fontsize=12)
axes[1,1].set_title('(D) Inter-chain Contact Fraction', fontsize=13, fontweight='bold'); axes[1,1].axvspan(5, 10, alpha=0.1, color='red'); axes[1,1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(HOME, 'phase5_cstar_analysis_FIXED.png'), dpi=300, bbox_inches='tight')
print(f"\nSaved: ~/phase5_cstar_analysis_FIXED.png")

print("\n=== CORRECTED SUMMARY TABLE ===")
print(f"{'System':<12} {'% w/v':<8} {'Rg (nm)':<12} {'K (MPa)':<12} {'HB/pair':<12} {'Contact%'}")
print('-'*68)
for r in results:
    K_str = f"{r['K']:.1f}" if r['K'] > 0 else "n/a"
    print(f"{r['label']:<12} {r['pct_wv']:<8.2f} {r['rg']:<12.3f} {K_str:<12} {r['hb']:<12.3f} {r['contact']:.1f}%")
