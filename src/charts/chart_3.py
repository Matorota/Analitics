import matplotlib.pyplot as plt
import seaborn as sns

def chart_3_market_share_pie(df):
    """Chart 3: Market Share by Platform"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 1, 1])
    ax = fig.add_subplot(gs[0])
    
    platform_revenue = df.groupby('Platform')['Revenue_Million'].sum().sort_values(ascending=False)
    colors_pie = sns.color_palette("Set2", len(platform_revenue))
    
    wedges, texts, autotexts = ax.pie(platform_revenue.values, labels=platform_revenue.index,
                                       autopct='%1.1f%%', colors=colors_pie, startangle=90,
                                       textprops={'fontsize': 11, 'fontweight': 'bold'},
                                       wedgeprops={'edgecolor': '#212529', 'linewidth': 2})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
    
    ax.set_title('Chart 3: Platform Market Share', fontsize=16, fontweight='bold', pad=20)
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    top_3 = platform_revenue.head(3)
    total = platform_revenue.sum()
    text = f"Top 3: {top_3.index[0]} ({top_3.values[0]/total*100:.1f}%) | {top_3.index[1]} ({top_3.values[1]/total*100:.1f}%) | {top_3.index[2]} ({top_3.values[2]/total*100:.1f}%)"
    ax_legend.text(0.02, 0.5, text, fontsize=9, transform=ax_legend.transAxes, fontweight='bold')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    text = f"Total Revenue: ${total:.1f}M | Platforms: {len(platform_revenue)} | Leader: {platform_revenue.idxmax()} ({platform_revenue.max()/total*100:.1f}%)"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#06A77D', linewidth=1.5))
    
    plt.tight_layout()
    return fig
