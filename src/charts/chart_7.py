import matplotlib.pyplot as plt
import seaborn as sns

def chart_7_roi_by_publisher_box(df):
    """Chart 7: Average Price by Genre"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
    ax = fig.add_subplot(gs[0])
    
    genre_price = df.groupby('Genre')['Price_USD'].mean().sort_values(ascending=False)
    colors = sns.color_palette("rocket", len(genre_price))
    bars = ax.barh(range(len(genre_price)), genre_price.values, color=colors, edgecolor='#212529', linewidth=2)
    
    ax.set_yticks(range(len(genre_price)))
    ax.set_yticklabels(genre_price.index, fontweight='bold', fontsize=10)
    ax.set_title('Chart 7: Average Game Price by Genre', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Average Price (USD)', fontsize=12, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    ax.invert_yaxis()
    
    for i, (bar, val) in enumerate(zip(bars, genre_price.values)):
        ax.text(val, bar.get_y() + bar.get_height()/2, f' ${val:.2f}',
               va='center', fontsize=9, fontweight='bold')
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    ax_legend.text(0.02, 0.3, "Dark Red = Most Expensive  |  Yellow = Most Affordable", fontsize=9,
                  transform=ax_legend.transAxes, fontweight='bold', color='#2E86AB')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    text = f"Most Expensive: {genre_price.index[0]} (${genre_price.values[0]:.2f}) | Avg: ${genre_price.mean():.2f} | Range: ${genre_price.min():.2f}-${genre_price.max():.2f}"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#C73E1D', linewidth=1.5))
    
    plt.tight_layout()
    return fig
