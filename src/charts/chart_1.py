import matplotlib.pyplot as plt
import seaborn as sns

def chart_1_sales_by_genre_bar(df):
    """Chart 1: Average Sales by Genre"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
    ax = fig.add_subplot(gs[0])
    
    genre_sales = df.groupby('Genre')['Sales_Million'].mean().sort_values(ascending=False)
    colors = sns.color_palette("coolwarm", len(genre_sales))
    bars = ax.bar(range(len(genre_sales)), genre_sales.values, color=colors, edgecolor='#212529', linewidth=2)
    
    ax.set_xticks(range(len(genre_sales)))
    ax.set_xticklabels(genre_sales.index, rotation=45, ha='right', fontweight='bold', fontsize=11)
    ax.set_title('Chart 1: Average Sales by Genre', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Average Sales (Million USD)', fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    for bar, val in zip(bars, genre_sales.values):
        ax.text(bar.get_x() + bar.get_width()/2, val, f'${val:.1f}M',
               ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    ax_legend.text(0.02, 0.3, "Red = High Sales  |  Blue = Low Sales", fontsize=9, 
                  transform=ax_legend.transAxes, fontweight='bold', color='#2E86AB')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    top_3 = genre_sales.head(3)
    text = f"Top 3: {top_3.index[0]} (${top_3.values[0]:.1f}M) | {top_3.index[1]} (${top_3.values[1]:.1f}M) | {top_3.index[2]} (${top_3.values[2]:.1f}M) | Avg: ${genre_sales.mean():.1f}M"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#2E86AB', linewidth=1.5))
    
    plt.tight_layout()
    return fig
