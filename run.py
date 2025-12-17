import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from database import VideoGameDatabase
from charts import ChartGenerator
from interface import InteractiveInterface

def main():
    """Main entry point"""
    print("\n" + "="*80)
    print("VIDEO GAME ANALYTICS DASHBOARD")
    print("="*80)
    
    # Initialize database
    print("\nInitializing database...")
    db = VideoGameDatabase('data')
    df = db.load_database()
    
    print("\n" + "-"*80)
    print("DATABASE INFORMATION")
    print("-"*80)
    print(f"Location: {os.path.abspath('data/video_games.csv')}")
    print(f"Total Games: {len(df)}")
    print(f"Genres: {df['Genre'].nunique()}")
    print(f"Platforms: {df['Platform'].nunique()}")
    print(f"Publishers: {df['Publisher'].nunique()}")
    print(f"Data Columns: {len(df.columns)}")
    
    print(f"\nDatabase Preview (First 3 Games):")
    print("-"*80)
    for idx, row in df.head(3).iterrows():
        print(f"Game {int(row['Game_ID'])}: {row['Game_Name']} | Genre: {row['Genre']} | Platform: {row['Platform']} | Price: ${row['Price_USD']:.2f}")
    
    print(f"\nKey Statistics:")
    print("-"*80)
    print(f"Total Revenue: ${df['Revenue_Million'].sum():,.2f}M")
    print(f"Average Price: ${df['Price_USD'].mean():.2f}")
    print(f"Average Rating: {df['Rating'].mean():.2f}/10")
    print(f"Total Players: {df['Player_Count'].sum():,.0f}")
    print(f"Average ROI: {df['ROI_Percent'].mean():.2f}%")
    
    print("\n" + "="*80)
    print("INITIALIZING INTERACTIVE INTERFACE")
    print("="*80)
    
    chart_gen = ChartGenerator(df)
    interface = InteractiveInterface(chart_gen, total_charts=10)
    
    print("\nStarting menu system...")
    print("You can select any chart from 1-10, view it, and return to menu.\n")
    
    interface.run()

if __name__ == "__main__":
    main()
