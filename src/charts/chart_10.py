import matplotlib.pyplot as plt
import seaborn as sns

def chart_10_player_count_power_bubble(df):
    """Chart 10: Revenue vs Copies Sold by Genre"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
    ax = fig.add_subplot(gs[0])
    
    genre_metrics = df.groupby('Genre').agg({
        'Revenue_Million': 'sum',
        'Copies_Sold_Million': 'sum',
        'Game_ID': 'count'
    }).reset_index()
    genre_metrics.columns = ['Genre', 'Revenue', 'Copies', 'Count']
    
    scatter = ax.scatter(genre_metrics['Copies'], genre_metrics['Revenue'], 
                        s=genre_metrics['Count']*30, c=range(len(genre_metrics)), 
                        cmap='tab10', alpha=0.7, edgecolors='#212529', linewidth=2)
    
    for idx, row in genre_metrics.iterrows():
        ax.annotate(row['Genre'], (row['Copies'], row['Revenue']), 
                   fontsize=9, fontweight='bold', ha='center')
    
    ax.set_title('Chart 10: Revenue vs Copies Sold by Genre', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Total Copies Sold (Million)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Total Revenue (Million $)', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    ax_legend.text(0.02, 0.3, "X-axis = Copies Sold  |  Y-axis = Revenue  |  Bubble Size = Number of Games", fontsize=9,
                  transform=ax_legend.transAxes, fontweight='bold', color='#2E86AB')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    corr = genre_metrics['Copies'].corr(genre_metrics['Revenue'])
    top_genre = genre_metrics.loc[genre_metrics['Revenue'].idxmax()]
    text = f"Correlation: {corr:+.3f} | Top: {top_genre['Genre']} (${top_genre['Revenue']:.1f}M) | Avg Revenue: ${genre_metrics['Revenue'].mean():.1f}M"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#2E86AB', linewidth=1.5))
    
    plt.tight_layout()
    return fig
