"""Charts package - Import all individual chart functions"""

from .chart_1 import chart_1_sales_by_genre_bar
from .chart_2 import chart_2_sales_trend_line
from .chart_3 import chart_3_market_share_pie
from .chart_4 import chart_4_price_vs_rating_scatter
from .chart_5 import chart_5_rating_distribution_histogram
from .chart_6 import chart_6_correlation_heatmap
from .chart_7 import chart_7_roi_by_publisher_box
from .chart_8 import chart_8_playtime_by_genre_violin
from .chart_9 import chart_9_stacked_revenue_area
from .chart_10 import chart_10_player_count_power_bubble

import matplotlib.pyplot as plt
import seaborn as sns


class ChartGenerator:
    """Generate all 10 professional charts"""
    
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
        return chart_1_sales_by_genre_bar(self.df)
    
    def chart_2_sales_trend_line(self):
        return chart_2_sales_trend_line(self.df)
    
    def chart_3_market_share_pie(self):
        return chart_3_market_share_pie(self.df)
    
    def chart_4_price_vs_rating_scatter(self):
        return chart_4_price_vs_rating_scatter(self.df)
    
    def chart_5_rating_distribution_histogram(self):
        return chart_5_rating_distribution_histogram(self.df)
    
    def chart_6_correlation_heatmap(self):
        return chart_6_correlation_heatmap(self.df)
    
    def chart_7_roi_by_publisher_box(self):
        return chart_7_roi_by_publisher_box(self.df)
    
    def chart_8_playtime_by_genre_violin(self):
        return chart_8_playtime_by_genre_violin(self.df)
    
    def chart_9_stacked_revenue_area(self):
        return chart_9_stacked_revenue_area(self.df)
    
    def chart_10_player_count_power_bubble(self):
        return chart_10_player_count_power_bubble(self.df)


__all__ = [
    'ChartGenerator',
    'chart_1_sales_by_genre_bar',
    'chart_2_sales_trend_line',
    'chart_3_market_share_pie',
    'chart_4_price_vs_rating_scatter',
    'chart_5_rating_distribution_histogram',
    'chart_6_correlation_heatmap',
    'chart_7_roi_by_publisher_box',
    'chart_8_playtime_by_genre_violin',
    'chart_9_stacked_revenue_area',
    'chart_10_player_count_power_bubble',
]
