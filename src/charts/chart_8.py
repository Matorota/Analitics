import matplotlib.pyplot as plt
import seaborn as sns

def chart_8_playtime_by_genre_violin(df):
    """Chart 8: Playtime by Genre"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
    ax = fig.add_subplot(gs[0])
    
    sns.violinplot(data=df, x='Genre', y='Playtime_Hours', ax=ax, palette='muted', 
                  hue='Genre', legend=False, inner='box')
    
    ax.set_title('Chart 8: Playtime Distribution by Genre', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Genre', fontsize=11, fontweight='bold')
    ax.set_ylabel('Playtime (Hours)', fontsize=11, fontweight='bold')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, alpha=0.3, axis='y')
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    ax_legend.text(0.02, 0.3, "Violin width = Data density  |  Wider = More games at that playtime", 
                  fontsize=9, transform=ax_legend.transAxes, fontweight='bold', color='#2E86AB')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    genre_stats = df.groupby('Genre')['Playtime_Hours'].agg(['mean', 'median', 'count']).sort_values('mean', ascending=False)
    top_genre = genre_stats.index[0]
    text = f"Top Genre: {top_genre} (Avg: {genre_stats.loc[top_genre, 'mean']:.1f}h) | Overall Avg: {df['Playtime_Hours'].mean():.1f}h"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#A23B72', linewidth=1.5))
    
    plt.tight_layout()
    return fig
