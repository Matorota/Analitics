import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

class ChartGenerator:
    """Generate 10 professional charts"""
    
    def __init__(self, df):
        self.df = df
        self.setup_style()
    
    def setup_style(self):
        """Setup matplotlib style"""
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
        plt.rcParams['figure.facecolor'] = '#FFFFFF'
        plt.rcParams['axes.facecolor'] = '#F8F9FA'
        plt.rcParams['font.size'] = 10
        plt.rcParams['font.family'] = 'sans-serif'
    
    def chart_1_sales_by_genre_bar(self):
        """Chart 1: Average Sales by Genre"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
        ax = fig.add_subplot(gs[0])
        
        genre_sales = self.df.groupby('Genre')['Sales_Million'].mean().sort_values(ascending=False)
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
    
    def chart_2_sales_trend_line(self):
        """Chart 2: Top 10 Publishers by Total Sales"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
        ax = fig.add_subplot(gs[0])
        
        pub_sales = self.df.groupby('Publisher')['Sales_Million'].sum().sort_values(ascending=False).head(10)
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
    
    def chart_3_market_share_pie(self):
        """Chart 3: Market Share by Platform"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 1, 1])
        ax = fig.add_subplot(gs[0])
        
        platform_revenue = self.df.groupby('Platform')['Revenue_Million'].sum().sort_values(ascending=False)
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
    
    def chart_4_price_vs_rating_scatter(self):
        """Chart 4: Average Rating by Platform"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
        ax = fig.add_subplot(gs[0])
        
        platform_rating = self.df.groupby('Platform')['Rating'].mean().sort_values(ascending=False)
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
    
    def chart_5_rating_distribution_histogram(self):
        """Chart 5: Rating Distribution (Pi-based bins)"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
        ax = fig.add_subplot(gs[0])
        
        bins = int(10 * np.pi / 3)
        n, edges, patches = ax.hist(self.df['Rating'], bins=bins, color='#2E86AB', 
                                     edgecolor='#212529', linewidth=1.5, alpha=0.85)
        
        for i, patch in enumerate(patches):
            patch.set_facecolor(plt.cm.Blues(0.4 + 0.6 * (i / len(patches))))
        
        mean_r = self.df['Rating'].mean()
        median_r = self.df['Rating'].median()
        
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
        excellent = len(self.df[self.df['Rating'] >= 9])
        very_good = len(self.df[(self.df['Rating'] >= 7) & (self.df['Rating'] < 9)])
        text = f"Excellent (≥9): {excellent} | Very Good (7-9): {very_good} | Avg: {mean_r:.2f} | Std: {self.df['Rating'].std():.2f}"
        ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                     bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#C73E1D', linewidth=1.5))
        
        plt.tight_layout()
        return fig
    
    def chart_6_correlation_heatmap(self):
        """Chart 6: Correlation Matrix"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
        ax = fig.add_subplot(gs[0])
        
        numeric_cols = ['Price_USD', 'Sales_Million', 'Player_Count', 'Rating', 
                       'Development_Cost_Million', 'Playtime_Hours', 'Revenue_Million', 'ROI_Percent']
        corr_matrix = self.df[numeric_cols].corr()
        
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
    
    def chart_7_roi_by_publisher_box(self):
        """Chart 7: Average Price by Genre"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
        ax = fig.add_subplot(gs[0])
        
        genre_price = self.df.groupby('Genre')['Price_USD'].mean().sort_values(ascending=False)
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
    
    def chart_8_playtime_by_genre_violin(self):
        """Chart 8: Playtime by Genre"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
        ax = fig.add_subplot(gs[0])
        
        sns.violinplot(data=self.df, x='Genre', y='Playtime_Hours', ax=ax, palette='muted', 
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
        genre_stats = self.df.groupby('Genre')['Playtime_Hours'].agg(['mean', 'median', 'count']).sort_values('mean', ascending=False)
        top_genre = genre_stats.index[0]
        text = f"Top Genre: {top_genre} (Avg: {genre_stats.loc[top_genre, 'mean']:.1f}h) | Overall Avg: {self.df['Playtime_Hours'].mean():.1f}h"
        ax_stats.text(0.01, 0.5, text, fontsize=9, verticalalignment='center', family='monospace',
                     bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFACD', edgecolor='#A23B72', linewidth=1.5))
        
        plt.tight_layout()
        return fig
    
    def chart_9_stacked_revenue_area(self):
        """Chart 9: Revenue Trends by Genre"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
        ax = fig.add_subplot(gs[0])
        
        top_genres = self.df.groupby('Genre')['Revenue_Million'].sum().nlargest(6).index
        df_top = self.df[self.df['Genre'].isin(top_genres)]
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
    
    def chart_10_player_count_power_bubble(self):
        """Chart 10: Revenue vs Copies Sold by Genre"""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.5, 1])
        ax = fig.add_subplot(gs[0])
        
        genre_metrics = self.df.groupby('Genre').agg({
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
        
        plt.tight_layout()
        return fig
