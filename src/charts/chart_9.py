import matplotlib.pyplot as plt
import seaborn as sns

def chart_9_stacked_revenue_area(df):
    """Chart 9: Revenue Trends by Genre"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
    ax = fig.add_subplot(gs[0])
    
    top_genres = df.groupby('Genre')['Revenue_Million'].sum().nlargest(6).index
    df_top = df[df['Genre'].isin(top_genres)]
    pivot = df_top.pivot_table(values='Revenue_Million', index='Release_Year', columns='Genre', aggfunc='sum', fill_value=0)
    
    colors = sns.color_palette("husl", len(pivot.columns))
    ax.stackplot(pivot.index, pivot.T, labels=pivot.columns, colors=colors, alpha=0.8, 
                edgecolor='#212529', linewidth=1.5)
    
    ax.set_title('Chart 9: Revenue Trends by Genre Over Time', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Year', fontsize=11, fontweight='bold')
    ax.set_ylabel('Revenue (Million $)', fontsize=11, fontweight='bold')
    ax.legend(loc='upper left', fontsize=8, ncol=2)
    ax.grid(True, alpha=0.3)
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    ax_legend.text(0.02, 0.3, "Each color = Different genre  |  Height = Revenue contribution  |  Top 6 genres shown", 
                  fontsize=9, transform=ax_legend.transAxes, fontweight='bold', color='#2E86AB')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    year_totals = pivot.sum(axis=1)
    text = f"Peak Year: {year_totals.idxmax()} (${year_totals.max():.1f}M) | Total Revenue: ${year_totals.sum():.1f}M"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#F18F01', linewidth=1.5))
    
    plt.tight_layout()
    return fig
