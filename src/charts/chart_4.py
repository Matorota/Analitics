import matplotlib.pyplot as plt
import seaborn as sns

def chart_4_price_vs_rating_scatter(df):
    """Chart 4: Average Rating by Platform"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
    ax = fig.add_subplot(gs[0])
    
    platform_rating = df.groupby('Platform')['Rating'].mean().sort_values(ascending=False)
    colors = sns.color_palette("coolwarm", len(platform_rating))
    bars = ax.bar(range(len(platform_rating)), platform_rating.values, color=colors, edgecolor='#212529', linewidth=2)
    
    ax.set_xticks(range(len(platform_rating)))
    ax.set_xticklabels(platform_rating.index, rotation=45, ha='right', fontweight='bold', fontsize=11)
    ax.set_title('Chart 4: Average Game Rating by Platform', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Average Rating (1-10)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, 10)
    ax.grid(axis='y', alpha=0.3)
    
    for bar, val in zip(bars, platform_rating.values):
        ax.text(bar.get_x() + bar.get_width()/2, val, f'{val:.2f}',
               ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    ax_legend.text(0.02, 0.3, "Red = Highest Rated  |  Blue = Lower Rated", fontsize=9,
                  transform=ax_legend.transAxes, fontweight='bold', color='#2E86AB')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    top_platform = platform_rating.idxmax()
    text = f"Best Rated: {top_platform} ({platform_rating[top_platform]:.2f}/10) | Avg: {platform_rating.mean():.2f} | Range: {platform_rating.min():.2f}-{platform_rating.max():.2f}"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#F18F01', linewidth=1.5))
    
    plt.tight_layout()
    return fig
