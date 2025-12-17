import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import Button
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# VIDEO GAMES DATABASE - COMPREHENSIVE ANALYTICS PROJECT
# ============================================================================

class VideoGameAnalytics:
    def __init__(self):
        self.df = self.generate_video_game_data()
        self.setup_style()
        self.current_chart = 0
        self.total_charts = 10
    
    def generate_video_game_data(self):
        """Generate a comprehensive video game dataset"""
        np.random.seed(42)
        
        genres = ['Action', 'RPG', 'Strategy', 'Sports', 'Shooter', 'Adventure', 
                  'Racing', 'Puzzle', 'Simulation', 'Indie', 'Horror', 'Fighting']
        platforms = ['PS5', 'Xbox Series X', 'Nintendo Switch', 'PC', 'PS4', 
                     'Xbox One', 'Mobile', 'VR', 'Steam Deck']
        publishers = ['Sony', 'Microsoft', 'Nintendo', 'Activision Blizzard', 
                      'EA Sports', 'Ubisoft', 'Take-Two', 'Rockstar Games',
                      'Bethesda', 'Epic Games', 'Square Enix', 'Capcom']
        
        num_games = 500
        
        data = {
            'Game_ID': range(1, num_games + 1),
            'Game_Name': [f"Game_{i}" for i in range(1, num_games + 1)],
            'Genre': np.random.choice(genres, num_games),
            'Platform': np.random.choice(platforms, num_games),
            'Publisher': np.random.choice(publishers, num_games),
            'Release_Year': np.random.randint(2010, 2025, num_games),
            'Price_USD': np.random.uniform(5, 70, num_games),
            'Sales_Million': np.random.exponential(5, num_games) + 0.5,
            'Player_Count': np.random.randint(100, 10000000, num_games),
            'Rating': np.random.uniform(1, 10, num_games),
            'Development_Cost_Million': np.random.uniform(1, 300, num_games),
            'Playtime_Hours': np.random.uniform(2, 200, num_games),
            'Metacritic_Score': np.random.uniform(20, 98, num_games),
            'Copies_Sold_Million': np.random.exponential(3, num_games) + 0.1,
        }
        
        df = pd.DataFrame(data)
        df['Revenue_Million'] = df['Copies_Sold_Million'] * df['Price_USD']
        df['ROI_Percent'] = ((df['Revenue_Million'] - df['Development_Cost_Million']) 
                             / df['Development_Cost_Million'] * 100)
        df['Engagement_Score'] = (df['Rating'] * df['Player_Count'] / 1000000)
        
        return df
    
    def setup_style(self):
        """Setup matplotlib style"""
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
    
    def chart_1_sales_by_genre_bar(self):
        """Chart 1: Average Sales by Genre (Bar Chart)"""
        fig = plt.figure(figsize=(14, 9))
        gs = fig.add_gridspec(5, 1, height_ratios=[4, 1, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        genre_sales = self.df.groupby('Genre')['Sales_Million'].mean().sort_values(ascending=False)
        colors = plt.cm.viridis(np.linspace(0, 1, len(genre_sales)))
        bars = ax.bar(range(len(genre_sales)), genre_sales.values, color=colors, edgecolor='black', linewidth=1.5)
        
        ax.set_xticks(range(len(genre_sales)))
        ax.set_xticklabels(genre_sales.index, rotation=45, ha='right')
        ax.set_title('CHART 1: Average Sales by Genre (Bar Chart)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Average Sales (Million USD)', fontsize=11, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for i, (bar, val) in enumerate(zip(bars, genre_sales.values)):
            ax.text(bar.get_x() + bar.get_width()/2, val, f'${val:.2f}M', 
                   ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = f"CALCULATION: Average Sales per Genre = Total Sales / Number of Games per Genre"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=10, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        stats_text = f"""DETAILED ANALYSIS AND STATISTICS:

Total Genres: {len(genre_sales)}
Total Games: {len(self.df)}
Highest Average Sales: {genre_sales.max():.2f}M ({genre_sales.idxmax()})
Lowest Average Sales: {genre_sales.min():.2f}M ({genre_sales.idxmin()})
Overall Mean: {genre_sales.mean():.2f}M
Standard Deviation: {genre_sales.std():.2f}M
Median: {genre_sales.median():.2f}M
Range: {genre_sales.max() - genre_sales.min():.2f}M

TOP 3 GENRES BY SALES:
1. {genre_sales.index[0]}: ${genre_sales.values[0]:.2f}M
2. {genre_sales.index[1]}: ${genre_sales.values[1]:.2f}M
3. {genre_sales.index[2]}: ${genre_sales.values[2]:.2f}M"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=9, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_1_sales_by_genre.png', dpi=300, bbox_inches='tight')
        return fig
    
    def chart_2_sales_trend_line(self):
        """Chart 2: Sales Trend Over Years (Line Chart with Power Calculation)"""
        fig = plt.figure(figsize=(14, 9))
        gs = fig.add_gridspec(5, 1, height_ratios=[4, 1, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        yearly_sales = self.df.groupby('Release_Year')['Sales_Million'].sum().sort_index()
        power_sales = np.power(yearly_sales, 0.5)
        
        ax.plot(yearly_sales.index, yearly_sales.values, marker='o', linewidth=3, 
                markersize=8, label='Actual Sales', color='#1f77b4')
        ax.plot(yearly_sales.index, power_sales.values, marker='s', linewidth=2, 
                markersize=6, label='Power 0.5 (Square Root)', color='#ff7f0e', linestyle='--', alpha=0.7)
        
        ax.set_title('CHART 2: Sales Trend Over Years (Line Chart with Power Calculation)', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Release Year', fontsize=11, fontweight='bold')
        ax.set_ylabel('Sales (Million USD)', fontsize=11, fontweight='bold')
        ax.legend(fontsize=10, loc='upper left')
        ax.grid(True, alpha=0.3)
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = "CALCULATION: Power(x) = x^0.5 | This transformation shows growth normalized to prevent extreme values"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=10, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        year_growth = ((yearly_sales.iloc[-1] - yearly_sales.iloc[0]) / yearly_sales.iloc[0] * 100) if yearly_sales.iloc[0] != 0 else 0
        
        stats_text = f"""DETAILED TREND ANALYSIS AND CALCULATIONS:

Time Period: {yearly_sales.index.min()} - {yearly_sales.index.max()} ({yearly_sales.index.max() - yearly_sales.index.min() + 1} years)
Total Sales in Period: ${yearly_sales.sum():,.2f}M
Average Yearly Sales: ${yearly_sales.mean():,.2f}M
Peak Sales Year: {yearly_sales.idxmax()} (${yearly_sales.max():,.2f}M)
Lowest Sales Year: {yearly_sales.idxmin()} (${yearly_sales.min():,.2f}M)
Overall Trend Growth: {year_growth:.2f}%

Year-over-Year Changes:
{chr(10).join([f'{year}: ${sales:,.2f}M' for year, sales in yearly_sales.tail(5).items()])}

Power Transformation Analysis:
Applied Formula: sqrt(Sales) to normalize exponential growth patterns"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=9, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_2_sales_trend.png', dpi=300, bbox_inches='tight')
        return fig
    
    def chart_3_market_share_pie(self):
        """Chart 3: Market Share by Platform (Pie Chart)"""
        fig = plt.figure(figsize=(14, 9))
        gs = fig.add_gridspec(5, 1, height_ratios=[4, 1, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        platform_revenue = self.df.groupby('Platform')['Revenue_Million'].sum().sort_values(ascending=False)
        colors = plt.cm.Set3(np.linspace(0, 1, len(platform_revenue)))
        
        wedges, texts, autotexts = ax.pie(platform_revenue.values, labels=platform_revenue.index, 
                                           autopct='%1.1f%%', colors=colors, startangle=90,
                                           textprops={'fontsize': 10, 'weight': 'bold'})
        ax.set_title('CHART 3: Market Share by Platform (Pie Chart)', fontsize=14, fontweight='bold')
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = "CALCULATION: Market Share (%) = (Platform Revenue / Total Revenue) * 100"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=10, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        total_revenue = platform_revenue.sum()
        top_3_platforms = platform_revenue.head(3)
        
        stats_text = f"""MARKET SHARE ANALYSIS:

Total Platforms: {len(platform_revenue)}
Total Revenue: ${total_revenue:,.2f}M
Average Revenue per Platform: ${platform_revenue.mean():,.2f}M

MARKET SHARE BY PLATFORM:
{chr(10).join([f'{platform}: ${revenue:,.2f}M ({revenue/total_revenue*100:.1f}%)' 
               for platform, revenue in platform_revenue.items()])}

CONCENTRATION METRICS:
Top 3 Platforms Control: {top_3_platforms.sum()/total_revenue*100:.1f}% of market
Dominant Platform: {platform_revenue.idxmax()} ({platform_revenue.max()/total_revenue*100:.1f}%)"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=9, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_3_market_share.png', dpi=300, bbox_inches='tight')
        return fig
    
    def chart_4_price_vs_rating_scatter(self):
        """Chart 4: Price vs Rating Scatter Plot with Size = Sales"""
        fig = plt.figure(figsize=(14, 9))
        gs = fig.add_gridspec(5, 1, height_ratios=[4, 1, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        scatter = ax.scatter(self.df['Price_USD'], self.df['Rating'], 
                           s=self.df['Sales_Million']*2, alpha=0.6, 
                           c=self.df['Engagement_Score'], cmap='plasma', 
                           edgecolors='black', linewidth=0.5)
        
        ax.set_title('CHART 4: Price vs Rating (Bubble Size = Sales)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Price (USD)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Rating (1-10)', fontsize=11, fontweight='bold')
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Engagement Score', fontsize=11, fontweight='bold')
        ax.grid(True, alpha=0.3)
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = "CALCULATION: Engagement Score = (Rating * Player Count) / 1,000,000 | Correlation shows relationship strength"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=10, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        corr_price_rating = self.df['Price_USD'].corr(self.df['Rating'])
        corr_price_sales = self.df['Price_USD'].corr(self.df['Sales_Million'])
        corr_rating_sales = self.df['Rating'].corr(self.df['Sales_Million'])
        
        stats_text = f"""CORRELATION AND RELATIONSHIP ANALYSIS:

PRICE STATISTICS:
Average Price: ${self.df['Price_USD'].mean():.2f}
Price Range: ${self.df['Price_USD'].min():.2f} - ${self.df['Price_USD'].max():.2f}
Price Std Dev: ${self.df['Price_USD'].std():.2f}

RATING STATISTICS:
Average Rating: {self.df['Rating'].mean():.2f}/10
Rating Range: {self.df['Rating'].min():.2f} - {self.df['Rating'].max():.2f}
Rating Std Dev: {self.df['Rating'].std():.2f}

CORRELATION COEFFICIENTS:
Price vs Rating: {corr_price_rating:.4f} (Weak relationship)
Price vs Sales: {corr_price_sales:.4f}
Rating vs Sales: {corr_rating_sales:.4f}

ENGAGEMENT ANALYSIS:
Average Engagement Score: {self.df['Engagement_Score'].mean():.2f}
Max Engagement: {self.df['Engagement_Score'].max():.2f}"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=9, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_4_price_vs_rating.png', dpi=300, bbox_inches='tight')
        return fig
    
    def chart_5_rating_distribution_histogram(self):
        """Chart 5: Rating Distribution Histogram with Pi-based Calculation"""
        fig = plt.figure(figsize=(14, 9))
        gs = fig.add_gridspec(5, 1, height_ratios=[4, 1, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        pi_value = np.pi
        num_bins = int(10 * pi_value / 3)
        
        n, bins, patches = ax.hist(self.df['Rating'], bins=num_bins, edgecolor='black', 
                                   alpha=0.7, color='steelblue')
        
        colors = plt.cm.RdYlGn(np.linspace(0.2, 0.8, len(patches)))
        for patch, color in zip(patches, colors):
            patch.set_facecolor(color)
        
        mean_rating = self.df['Rating'].mean()
        median_rating = self.df['Rating'].median()
        ax.axvline(mean_rating, color='red', linestyle='--', linewidth=2.5, label=f'Mean: {mean_rating:.2f}')
        ax.axvline(median_rating, color='green', linestyle=':', linewidth=2.5, label=f'Median: {median_rating:.2f}')
        
        ax.set_title(f'CHART 5: Rating Distribution (Histogram with Pi-Based Bins)', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Rating', fontsize=11, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(axis='y', alpha=0.3)
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = f"CALCULATION: Number of Bins = int(10 * Pi / 3) = int(10 * {pi_value:.4f} / 3) = {num_bins} bins"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=10, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        skewness = (3 * (mean_rating - median_rating)) / self.df['Rating'].std()
        
        stats_text = f"""DISTRIBUTION ANALYSIS WITH PI CALCULATION:

MATHEMATICAL PI USAGE:
Pi (π) Value: {pi_value:.6f}
Formula: Bins = 10 * π / 3 = {10 * pi_value / 3:.4f} → {num_bins} bins
Binwidth: {(self.df['Rating'].max() - self.df['Rating'].min()) / num_bins:.4f}

DISTRIBUTION STATISTICS:
Total Games: {len(self.df)}
Mean Rating: {mean_rating:.4f}
Median Rating: {median_rating:.4f}
Mode Rating: {self.df['Rating'].mode()[0] if len(self.df['Rating'].mode()) > 0 else 'N/A'}
Standard Deviation: {self.df['Rating'].std():.4f}
Variance: {self.df['Rating'].var():.4f}
Skewness: {skewness:.4f}

RATING RANGES:
Min Rating: {self.df['Rating'].min():.2f}
Max Rating: {self.df['Rating'].max():.2f}
Range: {self.df['Rating'].max() - self.df['Rating'].min():.2f}
Quartile 1 (25%): {self.df['Rating'].quantile(0.25):.2f}
Quartile 3 (75%): {self.df['Rating'].quantile(0.75):.2f}
Interquartile Range: {self.df['Rating'].quantile(0.75) - self.df['Rating'].quantile(0.25):.2f}"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=8, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_5_rating_distribution.png', dpi=300, bbox_inches='tight')
        return fig
    
    def chart_6_correlation_heatmap(self):
        """Chart 6: Correlation Heatmap of Numeric Columns"""
        fig = plt.figure(figsize=(14, 10))
        gs = fig.add_gridspec(5, 1, height_ratios=[4.5, 0.5, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        correlation_matrix = self.df[numeric_cols].corr()
        
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                   ax=ax, vmin=-1, vmax=1)
        
        ax.set_title('CHART 6: Correlation Matrix Heatmap', fontsize=14, fontweight='bold')
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = "CALCULATION: Pearson Correlation = Covariance(X,Y) / (Std(X) * Std(Y)) | Range: -1 (inverse) to +1 (direct)"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=9, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        # Find strongest correlations
        corr_pairs = []
        for i in range(len(correlation_matrix.columns)):
            for j in range(i+1, len(correlation_matrix.columns)):
                corr_pairs.append((correlation_matrix.columns[i], correlation_matrix.columns[j], 
                                 correlation_matrix.iloc[i, j]))
        corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
        
        stats_text = f"""CORRELATION ANALYSIS:

Variables Analyzed: {len(numeric_cols)}
Total Correlations: {len(correlation_matrix) * (len(correlation_matrix) - 1) // 2}

STRONGEST POSITIVE CORRELATIONS:
{chr(10).join([f'{i+1}. {pair[0]} vs {pair[1]}: {pair[2]:.4f}' for i, pair in enumerate(corr_pairs[:3])])}

STRONGEST NEGATIVE CORRELATIONS:
{chr(10).join([f'{i+1}. {pair[0]} vs {pair[1]}: {pair[2]:.4f}' for i, pair in enumerate(corr_pairs[-3:]) if pair[2] < 0])}

INTERPRETATION GUIDE:
+1.0 = Perfect positive correlation (both increase together)
+0.7 to +0.99 = Strong positive correlation
+0.3 to +0.7 = Moderate positive correlation
0 = No correlation
-0.3 to -0.7 = Moderate negative correlation
-0.7 to -0.99 = Strong negative correlation
-1.0 = Perfect negative correlation (inverse relationship)"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=8, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_6_correlation_heatmap.png', dpi=300, bbox_inches='tight')
        return fig
    
    def chart_7_roi_by_publisher_box(self):
        """Chart 7: ROI Distribution by Publisher (Box Plot)"""
        fig = plt.figure(figsize=(14, 9))
        gs = fig.add_gridspec(5, 1, height_ratios=[4, 1, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        top_publishers = self.df['Publisher'].value_counts().head(8).index
        df_filtered = self.df[self.df['Publisher'].isin(top_publishers)]
        
        sns.boxplot(data=df_filtered, x='Publisher', y='ROI_Percent', ax=ax, palette='Set2')
        
        ax.set_title('CHART 7: ROI Distribution by Top Publishers (Box Plot)', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Publisher', fontsize=11, fontweight='bold')
        ax.set_ylabel('ROI (%)', fontsize=11, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = "CALCULATION: ROI % = ((Revenue - Cost) / Cost) * 100"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=10, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        pub_stats = df_filtered.groupby('Publisher')['ROI_Percent'].agg(['mean', 'median', 'std', 'min', 'max', 'count'])
        
        stats_text = f"""ROI ANALYSIS BY PUBLISHER:

Total Publishers Analyzed: {len(top_publishers)}
Total Games: {len(df_filtered)}
Overall Average ROI: {df_filtered['ROI_Percent'].mean():.2f}%
Overall Median ROI: {df_filtered['ROI_Percent'].median():.2f}%

BOX PLOT ELEMENTS EXPLANATION:
- Box: Middle 50% of data (25th to 75th percentile)
- Line in box: Median value
- Whiskers: Range from min to max (or 1.5*IQR)
- Dots: Outliers beyond whiskers

TOP PUBLISHERS BY AVERAGE ROI:
{chr(10).join([f'{i+1}. {pub}: {stats.iloc[0]:.2f}% (Median: {stats.iloc[1]:.2f}%, Std: {stats.iloc[2]:.2f}%)' 
               for i, (pub, stats) in enumerate(pub_stats.sort_values('mean', ascending=False).head(5).iterrows())])}

ROI INTERPRETATION:
Positive ROI: Profitable investment (revenue > cost)
Negative ROI: Loss-making investment (revenue < cost)
High Std Dev: Inconsistent performance across games"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=8, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_7_roi_by_publisher.png', dpi=300, bbox_inches='tight')
        return fig
    
    def chart_8_playtime_by_genre_violin(self):
        """Chart 8: Playtime Distribution by Genre (Violin Plot)"""
        fig = plt.figure(figsize=(14, 9))
        gs = fig.add_gridspec(5, 1, height_ratios=[4, 1, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        sns.violinplot(data=self.df, x='Genre', y='Playtime_Hours', ax=ax, palette='muted')
        
        ax.set_title('CHART 8: Playtime Distribution by Genre (Violin Plot)', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Genre', fontsize=11, fontweight='bold')
        ax.set_ylabel('Average Playtime (Hours)', fontsize=11, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = "CALCULATION: Violin Plot shows probability density distribution (kernel density estimation) of playtime per genre"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=10, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        genre_stats = self.df.groupby('Genre')['Playtime_Hours'].agg(['count', 'mean', 'median', 'std', 'min', 'max'])
        
        stats_text = f"""PLAYTIME ANALYSIS BY GENRE:

Total Genres: {len(self.df['Genre'].unique())}
Total Games: {len(self.df)}

OVERALL PLAYTIME STATISTICS:
Average Playtime: {self.df['Playtime_Hours'].mean():.2f} hours
Median Playtime: {self.df['Playtime_Hours'].median():.2f} hours
Std Deviation: {self.df['Playtime_Hours'].std():.2f} hours
Min Playtime: {self.df['Playtime_Hours'].min():.2f} hours
Max Playtime: {self.df['Playtime_Hours'].max():.2f} hours

TOP 5 GENRES BY AVERAGE PLAYTIME:
{chr(10).join([f'{i+1}. {genre}: {stats.iloc[1]:.2f} hrs (Count: {int(stats.iloc[0])})' 
               for i, (genre, stats) in enumerate(genre_stats.sort_values('mean', ascending=False).head(5).iterrows())])}

VIOLIN PLOT INTERPRETATION:
- Width = Density/Frequency at that playtime value
- Wider sections = More games have that playtime
- Thinner sections = Fewer games at that playtime"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=8, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='honeydew', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_8_playtime_by_genre.png', dpi=300, bbox_inches='tight')
        return fig
    
    def chart_9_stacked_revenue_area(self):
        """Chart 9: Stacked Area Chart - Revenue by Genre Over Years"""
        fig = plt.figure(figsize=(14, 9))
        gs = fig.add_gridspec(5, 1, height_ratios=[4, 1, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        pivot_data = self.df.pivot_table(values='Revenue_Million', index='Release_Year', 
                                        columns='Genre', aggfunc='sum', fill_value=0)
        
        ax.stackplot(pivot_data.index, *[pivot_data[col].values for col in pivot_data.columns],
                    labels=pivot_data.columns, alpha=0.8)
        
        ax.set_title('CHART 9: Cumulative Revenue by Genre Over Years (Stacked Area)', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Release Year', fontsize=11, fontweight='bold')
        ax.set_ylabel('Revenue (Million USD)', fontsize=11, fontweight='bold')
        ax.legend(loc='upper left', fontsize=8, ncol=2)
        ax.grid(True, alpha=0.3)
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = "CALCULATION: Stacked Area = Sum of revenues by genre for each year (cumulative)"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=10, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        total_revenue_year = pivot_data.sum(axis=1)
        total_revenue_genre = pivot_data.sum(axis=0).sort_values(ascending=False)
        
        stats_text = f"""REVENUE ANALYSIS BY GENRE AND YEAR:

Time Period: {pivot_data.index.min()} - {pivot_data.index.max()}
Total Years: {len(pivot_data)}
Total Genres: {len(pivot_data.columns)}

TOTAL REVENUE BY GENRE:
{chr(10).join([f'{i+1}. {genre}: ${revenue:,.2f}M ({revenue/pivot_data.values.sum()*100:.1f}%)' 
               for i, (genre, revenue) in enumerate(total_revenue_genre.head(5).items())])}

YEARLY REVENUE TRENDS:
Highest Revenue Year: {total_revenue_year.idxmax()} (${total_revenue_year.max():,.2f}M)
Lowest Revenue Year: {total_revenue_year.idxmin()} (${total_revenue_year.min():,.2f}M)
Average Revenue/Year: ${total_revenue_year.mean():,.2f}M

Recent Years Revenue:
{chr(10).join([f'{year}: ${revenue:,.2f}M' for year, revenue in total_revenue_year.tail(5).items()])}"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=8, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_9_stacked_revenue_area.png', dpi=300, bbox_inches='tight')
        return fig
    
    def chart_10_player_count_power_bubble(self):
        """Chart 10: Player Count Analysis with Power Law Calculation"""
        fig = plt.figure(figsize=(14, 9))
        gs = fig.add_gridspec(5, 1, height_ratios=[4, 1, 0.5, 1.5, 0.5])
        ax = fig.add_subplot(gs[0])
        
        genre_data = self.df.groupby('Genre').agg({
            'Player_Count': 'mean',
            'Sales_Million': 'mean',
            'Game_ID': 'count'
        }).reset_index()
        
        genre_data.columns = ['Genre', 'Avg_Players', 'Avg_Sales', 'Game_Count']
        genre_data['Player_Power'] = np.power(genre_data['Avg_Players'], 0.3)
        
        scatter = ax.scatter(genre_data['Avg_Sales'], genre_data['Avg_Players'],
                           s=genre_data['Game_Count']*30, alpha=0.6, 
                           c=genre_data['Player_Power'], cmap='viridis',
                           edgecolors='black', linewidth=2)
        
        for idx, row in genre_data.iterrows():
            ax.annotate(row['Genre'], (row['Avg_Sales'], row['Avg_Players']),
                       fontsize=9, fontweight='bold')
        
        ax.set_title('CHART 10: Player Count vs Sales by Genre (Power Law Visualization)', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Average Sales (Million USD)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Average Player Count', fontsize=11, fontweight='bold')
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Player Power (0.3)', fontsize=11, fontweight='bold')
        ax.grid(True, alpha=0.3)
        
        # Calculations section
        ax_calc = fig.add_subplot(gs[2])
        ax_calc.axis('off')
        calc_text = "CALCULATION: Player_Power = (Avg_Players)^0.3 (Cube Root-like transformation) | Bubble Size = Game Count"
        ax_calc.text(0.05, 0.8, calc_text, fontsize=10, fontweight='bold', transform=ax_calc.transAxes)
        
        # Statistics section
        ax_stats = fig.add_subplot(gs[3])
        ax_stats.axis('off')
        
        corr_sales_players = genre_data['Avg_Sales'].corr(genre_data['Avg_Players'])
        
        stats_text = f"""POWER LAW ANALYSIS:

POWER TRANSFORMATION FORMULA:
Player_Power = (Average_Players)^0.3
This is a cube-root-like transformation used to:
- Normalize extremely large player counts
- Compress the visualization scale
- Show exponential growth in manageable form

GENRE PLAYER ANALYSIS:
Total Genres: {len(genre_data)}
Total Games: {int(genre_data['Game_Count'].sum())}

HIGHEST PLAYER COUNT: {genre_data.loc[genre_data['Avg_Players'].idxmax(), 'Genre']} ({genre_data['Avg_Players'].max():,.0f} players)
LOWEST PLAYER COUNT: {genre_data.loc[genre_data['Avg_Players'].idxmin(), 'Genre']} ({genre_data['Avg_Players'].min():,.0f} players)

TOP 5 GENRES BY AVERAGE PLAYERS:
{chr(10).join([f'{i+1}. {row.iloc[0]}: {row.iloc[1]:,.0f} players, ${row.iloc[2]:.2f}M sales' 
               for i, (_, row) in enumerate(genre_data.nlargest(5, 'Avg_Players')[['Genre', 'Avg_Players', 'Avg_Sales']].iterrows())])}

CORRELATION: Sales vs Player Count = {corr_sales_players:.4f}
Bubble Size Represents: Number of games in each genre"""
        
        ax_stats.text(0.05, 0.95, stats_text, fontsize=8, verticalalignment='top', 
                     transform=ax_stats.transAxes, family='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.3))
        
        plt.tight_layout()
        plt.savefig('chart_10_player_count_power.png', dpi=300, bbox_inches='tight')
        return fig
    
    def print_summary_statistics(self):
        """Print comprehensive summary statistics"""
        print("\n" + "="*80)
        print("VIDEO GAMES ANALYTICS - SUMMARY STATISTICS")
        print("="*80)
        print(f"\nTotal Games in Database: {len(self.df):,}")
        print(f"Genres: {self.df['Genre'].nunique()}")
        print(f"Platforms: {self.df['Platform'].nunique()}")
        print(f"Publishers: {self.df['Publisher'].nunique()}")
        
        print(f"\n--- FINANCIAL METRICS ---")
        print(f"Total Revenue: ${self.df['Revenue_Million'].sum():,.2f}M")
        print(f"Average Price: ${self.df['Price_USD'].mean():.2f}")
        print(f"Average Sales: ${self.df['Sales_Million'].mean():.2f}M")
        print(f"Average ROI: {self.df['ROI_Percent'].mean():.2f}%")
        
        print(f"\n--- ENGAGEMENT METRICS ---")
        print(f"Total Players: {self.df['Player_Count'].sum():,.0f}")
        print(f"Average Rating: {self.df['Rating'].mean():.2f}/10")
        print(f"Average Playtime: {self.df['Playtime_Hours'].mean():.2f} hours")
        print(f"Average Metacritic: {self.df['Metacritic_Score'].mean():.2f}")
        
        print(f"\n--- TOP PERFORMERS ---")
        top_revenue = self.df.nlargest(3, 'Revenue_Million')[['Game_Name', 'Revenue_Million']]
        print("Top 3 by Revenue:")
        for idx, (_, row) in enumerate(top_revenue.iterrows(), 1):
            print(f"  {idx}. {row['Game_Name']}: ${row['Revenue_Million']:.2f}M")
        
        print(f"\n--- PI AND POWER CALCULATIONS USED ---")
        print(f"π (Pi) value: {np.pi:.6f}")
        print(f"Power calculations: 0.5 (sqrt), 0.3 (cube root), custom powers")
        print(f"Advanced statistics: Correlation, ROI, Engagement Score, Log scales")
        print("="*80 + "\n")
    
    def run_interactive_interface(self):
        """Run interactive interface to navigate through all charts"""
        self.charts = [
            self.chart_1_sales_by_genre_bar,
            self.chart_2_sales_trend_line,
            self.chart_3_market_share_pie,
            self.chart_4_price_vs_rating_scatter,
            self.chart_5_rating_distribution_histogram,
            self.chart_6_correlation_heatmap,
            self.chart_7_roi_by_publisher_box,
            self.chart_8_playtime_by_genre_violin,
            self.chart_9_stacked_revenue_area,
            self.chart_10_player_count_power_bubble
        ]
        
        self.current_chart = 0
        self.display_chart()
    
    def display_chart(self):
        """Display current chart with navigation buttons"""
        plt.close('all')
        
        fig = self.charts[self.current_chart]()
        
        # Add navigation buttons
        ax_prev = plt.axes([0.15, 0.02, 0.1, 0.05])
        ax_next = plt.axes([0.75, 0.02, 0.1, 0.05])
        ax_exit = plt.axes([0.45, 0.02, 0.1, 0.05])
        
        btn_prev = Button(ax_prev, 'PREVIOUS')
        btn_next = Button(ax_next, 'NEXT')
        btn_exit = Button(ax_exit, 'EXIT')
        
        def on_prev(event):
            self.current_chart = (self.current_chart - 1) % self.total_charts
            plt.close('all')
            self.display_chart()
        
        def on_next(event):
            self.current_chart = (self.current_chart + 1) % self.total_charts
            plt.close('all')
            self.display_chart()
        
        def on_exit(event):
            plt.close('all')
            print("\nExiting Interactive Interface...")
            self.print_summary_statistics()
        
        btn_prev.on_clicked(on_prev)
        btn_next.on_clicked(on_next)
        btn_exit.on_clicked(on_exit)
        
        # Add chart counter
        fig.text(0.5, 0.01, f'CHART {self.current_chart + 1} of {self.total_charts}', 
                ha='center', fontsize=12, fontweight='bold')
        
        plt.tight_layout(rect=[0, 0.08, 1, 1])
        plt.show()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("VIDEO GAME ANALYTICS DASHBOARD - INTERACTIVE INTERFACE")
    print("="*80)
    print("\nLoading database with 500 video games...")
    print("Preparing 10 detailed analytical charts with calculations...\n")
    
    analytics = VideoGameAnalytics()
    
    print("="*80)
    print("NAVIGATION INSTRUCTIONS:")
    print("- PREVIOUS: Move to previous chart")
    print("- NEXT: Move to next chart")
    print("- EXIT: Close and see summary statistics")
    print("- Each chart includes detailed calculations below the visualization")
    print("="*80 + "\n")
    
    analytics.run_interactive_interface()
