#!/usr/bin/env python
"""Test script to verify charts display correctly"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

from database import VideoGameDatabase
from charts import ChartGenerator

# Create database
print("Loading database...")
db = VideoGameDatabase(os.path.join(os.path.dirname(__file__), '..', 'data'))
df = db.load_database()

# Generate all 10 charts
chart_gen = ChartGenerator(df)
charts = [
    ("Chart 1", chart_gen.chart_1_sales_by_genre_bar),
    ("Chart 2", chart_gen.chart_2_sales_trend_line),
    ("Chart 3", chart_gen.chart_3_market_share_pie),
    ("Chart 4", chart_gen.chart_4_price_vs_rating_scatter),
    ("Chart 5", chart_gen.chart_5_rating_distribution_histogram),
    ("Chart 6", chart_gen.chart_6_correlation_heatmap),
    ("Chart 7", chart_gen.chart_7_roi_by_publisher_box),
    ("Chart 8", chart_gen.chart_8_playtime_by_genre_violin),
    ("Chart 9", chart_gen.chart_9_stacked_revenue_area),
    ("Chart 10", chart_gen.chart_10_player_count_power_bubble),
]

print(f"\nGenerating {len(charts)} charts...")
success_count = 0

for name, chart_func in charts:
    try:
        fig = chart_func()
        print(f"✓ {name} - Generated successfully")
        plt.close(fig)
        success_count += 1
    except Exception as e:
        print(f"✗ {name} - Error: {str(e)}")

print(f"\n{'='*60}")
print(f"Results: {success_count}/{len(charts)} charts generated successfully")
print(f"{'='*60}")

if success_count == len(charts):
    print("✓ All charts working correctly!")
    sys.exit(0)
else:
    print("✗ Some charts failed")
    sys.exit(1)
