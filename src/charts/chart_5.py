import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def chart_5_rating_distribution_histogram(df):
    """Chart 5: Rating Distribution (Pi-based bins)"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
    ax = fig.add_subplot(gs[0])
    
    bins = int(10 * np.pi / 3)
    n, edges, patches = ax.hist(df['Rating'], bins=bins, color='#2E86AB', 
                                 edgecolor='#212529', linewidth=1.5, alpha=0.85)
    
    for i, patch in enumerate(patches):
        patch.set_facecolor(plt.cm.Blues(0.4 + 0.6 * (i / len(patches))))
    
    mean_r = df['Rating'].mean()
    median_r = df['Rating'].median()
    
    ax.axvline(mean_r, color='#C73E1D', linestyle='--', linewidth=2.5, label=f'Mean: {mean_r:.2f}')
    ax.axvline(median_r, color='#06A77D', linestyle='-.', linewidth=2.5, label=f'Median: {median_r:.2f}')
    
    ax.set_title(f'Chart 5: Rating Distribution (Bins={bins} from 10π/3)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Rating', fontsize=11, fontweight='bold')
    ax.set_ylabel('Count', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    ax.legend(fontsize=9)
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    ax_legend.text(0.02, 0.3, f"Bins calculated as int(10 × π/3) = {bins}  |  Red = Mean  |  Green = Median", 
                  fontsize=9, transform=ax_legend.transAxes, fontweight='bold', color='#2E86AB')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    excellent = len(df[df['Rating'] >= 9])
    very_good = len(df[(df['Rating'] >= 7) & (df['Rating'] < 9)])
    text = f"Excellent (≥9): {excellent} | Very Good (7-9): {very_good} | Avg: {mean_r:.2f} | Std: {df['Rating'].std():.2f}"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#C73E1D', linewidth=1.5))
    
    plt.tight_layout()
    return fig
