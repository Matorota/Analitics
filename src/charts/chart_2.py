import matplotlib.pyplot as plt
import seaborn as sns

def chart_2_sales_trend_line(df):
    """Chart 2: Top 10 Publishers by Total Sales"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
    ax = fig.add_subplot(gs[0])
    
    pub_sales = df.groupby('Publisher')['Sales_Million'].sum().sort_values(ascending=False).head(10)
    colors = sns.color_palette("viridis", len(pub_sales))
    bars = ax.barh(range(len(pub_sales)), pub_sales.values, color=colors, edgecolor='#212529', linewidth=2)
    
    ax.set_yticks(range(len(pub_sales)))
    ax.set_yticklabels(pub_sales.index, fontweight='bold', fontsize=10)
    ax.set_title('Chart 2: Top 10 Publishers by Total Sales', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Total Sales (Million USD)', fontsize=12, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    ax.invert_yaxis()
    
    for i, (bar, val) in enumerate(zip(bars, pub_sales.values)):
        ax.text(val, bar.get_y() + bar.get_height()/2, f' ${val:.1f}M',
               va='center', fontsize=9, fontweight='bold')
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    ax_legend.text(0.02, 0.3, "Dark = Highest Sales  |  Bright = Lower Sales", fontsize=9,
                  transform=ax_legend.transAxes, fontweight='bold', color='#2E86AB')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    text = f"Leader: {pub_sales.index[0]} (${pub_sales.values[0]:.1f}M) | Avg: ${pub_sales.mean():.1f}M | Total: ${pub_sales.sum():.1f}M"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#06A77D', linewidth=1.5))
    
    plt.tight_layout()
    return fig
