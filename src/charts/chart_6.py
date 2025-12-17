import matplotlib.pyplot as plt
import seaborn as sns

def chart_6_correlation_heatmap(df):
    """Chart 6: Correlation Matrix"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
    ax = fig.add_subplot(gs[0])
    
    numeric_cols = ['Price_USD', 'Sales_Million', 'Player_Count', 'Rating', 
                   'Development_Cost_Million', 'Playtime_Hours', 'Revenue_Million', 'ROI_Percent']
    corr_matrix = df[numeric_cols].corr()
    
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
               square=True, ax=ax, cbar_kws={'label': 'Correlation'}, vmin=-1, vmax=1,
               linewidths=1.5, linecolor='#212529', annot_kws={'fontsize': 9, 'fontweight': 'bold'})
    
    ax.set_title('Chart 6: Correlation Matrix (Pearson)', fontsize=16, fontweight='bold', pad=20)
    
    ax_legend = fig.add_subplot(gs[1])
    ax_legend.axis('off')
    ax_legend.text(0.02, 0.3, "Red = Positive Correlation  |  White = No Correlation  |  Blue = Negative", 
                  fontsize=9, transform=ax_legend.transAxes, fontweight='bold', color='#2E86AB')
    
    ax_stats = fig.add_subplot(gs[2])
    ax_stats.axis('off')
    corr_flat = [(numeric_cols[i], numeric_cols[j], corr_matrix.iloc[i, j]) 
                for i in range(len(numeric_cols)) for j in range(i+1, len(numeric_cols))]
    corr_flat.sort(key=lambda x: abs(x[2]), reverse=True)
    top = corr_flat[0]
    text = f"Strongest: {top[0]} ↔ {top[1]} ({top[2]:+.3f}) | Scale: -1 to +1"
    ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#6C757D', linewidth=1.5))
    
    plt.tight_layout()
    return fig
