#!/usr/bin/env python
"""Comprehensive test of all charts - non-interactive"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt

from database import VideoGameDatabase
from charts import ChartGenerator

print("\n" + "="*80)
print("COMPREHENSIVE CHART TEST - NON-INTERACTIVE")
print("="*80)

# Initialize database
print("\nInitializing database...")
db = VideoGameDatabase(os.path.join(os.path.dirname(__file__), '..', 'data'))
df = db.load_database()
print(f"Loaded {len(df)} games successfully")

# Create chart generator
print("\nGenerating all 10 charts...")
chart_gen = ChartGenerator(df)

charts = [
    ("Chart 1: Sales by Genre", chart_gen.chart_1_sales_by_genre_bar),
    ("Chart 2: Top Publishers", chart_gen.chart_2_sales_trend_line),
    ("Chart 3: Market Share", chart_gen.chart_3_market_share_pie),
    ("Chart 4: Ratings by Platform", chart_gen.chart_4_price_vs_rating_scatter),
    ("Chart 5: Rating Distribution", chart_gen.chart_5_rating_distribution_histogram),
    ("Chart 6: Correlation Matrix", chart_gen.chart_6_correlation_heatmap),
    ("Chart 7: Price by Genre", chart_gen.chart_7_roi_by_publisher_box),
    ("Chart 8: Playtime by Genre", chart_gen.chart_8_playtime_by_genre_violin),
    ("Chart 9: Revenue Trends", chart_gen.chart_9_stacked_revenue_area),
    ("Chart 10: Revenue vs Copies", chart_gen.chart_10_player_count_power_bubble),
]

success_count = 0
error_count = 0

for name, chart_func in charts:
    try:
        print(f"\n  Generating {name}...", end=" ")
        fig = chart_func()
        plt.close(fig)
        print("OK")
        success_count += 1
    except Exception as e:
        print(f"ERROR: {str(e)}")
        error_count += 1

print("\n" + "="*80)
print("TEST RESULTS")
print("="*80)
print(f"Total Charts: 10")
print(f"Success: {success_count}/10")
print(f"Errors: {error_count}/10")

if error_count == 0:
    print("\nSTATUS: ALL TESTS PASSED!")
else:
    print(f"\nSTATUS: {error_count} ERROR(S) FOUND - SEE ABOVE")

print("="*80 + "\n")

if error_count > 0:
    sys.exit(1)
