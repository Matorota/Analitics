"""
Quick test script to verify database and menu structure
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from database import VideoGameDatabase
from charts import ChartGenerator
from interface import InteractiveInterface

# Initialize database
print("="*80)
print("VIDEO GAME ANALYTICS DASHBOARD - TEST")
print("="*80)

db = VideoGameDatabase('data')
df = db.load_database()

print(f"\nDatabase Status:")
print(f"  Location: {os.path.abspath('data/video_games.csv')}")
print(f"  Total Games: {len(df)}")
print(f"  Genres: {df['Genre'].nunique()}")
print(f"  Platforms: {df['Platform'].nunique()}")

print(f"\nChart Menu Available:")
chart_gen = ChartGenerator(df)
interface = InteractiveInterface(chart_gen, total_charts=10)

for i, (name, _) in enumerate(interface.chart_methods, 1):
    print(f"  {i}. {name}")

print(f"\nDatabase Ready: YES")
print(f"Menu System: WORKING")
print(f"\nTo start: Run 'python run.py' and select charts 1-10")
print("="*80)
