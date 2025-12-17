VIDEO GAME ANALYTICS DASHBOARD - INTERACTIVE INTERFACE

# OVERVIEW

This project provides a professional data analytics platform for visualizing and analyzing
video game industry data with 10 different chart types, each including detailed calculations
and statistical explanations.

# FEATURES

1. INTERACTIVE NAVIGATION

   - Navigate between 10 different charts using PREVIOUS/NEXT buttons
   - Current chart counter displayed
   - EXIT button to return to summary statistics

2. COMPREHENSIVE CALCULATIONS DISPLAYED
   Each chart includes:

   - Visual representation of data
   - Mathematical calculation formulas
   - Detailed statistical analysis
   - Interpretation guidelines
   - Key metrics and comparisons

3. PROFESSIONAL VISUALIZATIONS
   - Publication-quality charts (300 DPI)
   - Color-coded data representations
   - Clear labeling and legends
   - Automatic PNG file saving

# DATABASE SPECIFICATIONS

Total Games: 500
Genres: 12 (Action, RPG, Strategy, Sports, Shooter, Adventure, Racing, Puzzle,
Simulation, Indie, Horror, Fighting)
Platforms: 9 (PS5, Xbox Series X, Nintendo Switch, PC, PS4, Xbox One, Mobile, VR, Steam Deck)
Publishers: 12 (Sony, Microsoft, Nintendo, Activision Blizzard, EA Sports, Ubisoft,
Take-Two, Rockstar Games, Bethesda, Epic Games, Square Enix, Capcom)
Time Period: 2010-2024
Data Points: 14 metrics per game

# CHART DESCRIPTIONS

CHART 1: Average Sales by Genre (Bar Chart)
Description: Compares average sales revenue across different game genres
Calculation: Average Sales = Total Sales / Number of Games per Genre
Shows: Top performing genres, revenue distribution, market leaders

CHART 2: Sales Trend Over Years (Line Chart with Power Calculation)
Description: Visualizes sales growth trends from 2010 to 2024
Calculation: Power(x) = x^0.5 (square root transformation for normalized growth)
Shows: Yearly sales trends, growth patterns, peak performance years

CHART 3: Market Share by Platform (Pie Chart)
Description: Shows revenue distribution across gaming platforms
Calculation: Market Share (%) = (Platform Revenue / Total Revenue) \* 100
Shows: Platform dominance, market concentration, competitive landscape

CHART 4: Price vs Rating (Scatter Plot)
Description: Relationship between game price and player ratings
Calculation: Engagement Score = (Rating _ Player Count) / 1,000,000
Pearson Correlation coefficient = Covariance(X,Y) / (Std(X) _ Std(Y))
Shows: Price-rating correlation, engagement levels, bubble sizes = sales

CHART 5: Rating Distribution (Histogram with Pi-Based Calculation)
Description: Frequency distribution of game ratings
Calculation: Number of Bins = int(10 \* π / 3) = 10 bins
π (Pi) = 3.141593...
Shows: Distribution shape, mean/median values, rating patterns

CHART 6: Correlation Matrix (Heatmap)
Description: Analyzes relationships between all numeric variables
Calculation: Pearson Correlation for each pair of variables
Range: -1 (inverse) to +1 (direct relationship)
Shows: Strong correlations, weak relationships, variable dependencies

CHART 7: ROI by Publisher (Box Plot)
Description: Return on Investment distribution across top publishers
Calculation: ROI (%) = ((Revenue - Development Cost) / Development Cost) \* 100
Shows: Profitability patterns, publisher performance, outliers

CHART 8: Playtime by Genre (Violin Plot)
Description: Distribution of average playtime across genres
Calculation: Kernel Density Estimation (probability density visualization)
Shows: Average playtime per genre, distribution shape, engagement patterns

CHART 9: Revenue by Genre Over Years (Stacked Area Chart)
Description: Cumulative revenue trends by genre across time
Calculation: Sum of revenues by genre for each year
Shows: Genre growth, market evolution, temporal trends

CHART 10: Player Count vs Sales (Power Law Bubble Chart)
Description: Relationship between player count and sales with power transformation
Calculation: Player_Power = (Average_Players)^0.3 (cube-root transformation)
Bubble Size = Number of Games per Genre
Shows: Player engagement impact, genre clusters, market segments

# MATHEMATICAL CONCEPTS USED

POWER CALCULATIONS:

- Power 0.5 (x^0.5): Square root transformation - normalizes exponential growth
- Power 0.3 (x^0.3): Cube-root-like transformation - compresses large ranges
- Used to: Prevent extreme values from dominating visualization scale

PI (π) IN CALCULATIONS:

- π = 3.141593...
- Used in Chart 5 for bin calculation: Bins = int(10 \* π / 3)
- Application: Optimal histogram binning for distribution visualization

CORRELATION ANALYSIS:

- Pearson Correlation coefficient: measures linear relationship strength
- Range: -1 (perfect negative) to +1 (perfect positive)
- Used in: Charts 4, 6 for relationship analysis

STATISTICAL MEASURES:

- Mean: Average value
- Median: Middle value (50th percentile)
- Standard Deviation: Measure of data spread
- Variance: Squared standard deviation
- Skewness: Asymmetry of distribution
- Quartiles: 25th, 50th, 75th percentiles

KERNEL DENSITY ESTIMATION (KDE):

- Used in violin plots for smooth probability distribution visualization
- Shows density (width) of data at each point
- Better for understanding distribution shape than histograms

# RUNNING THE PROJECT

Installation:
pip install pandas numpy matplotlib seaborn

Running:
python DataAnalitics.py

Navigation:

1. Charts display automatically with interactive buttons
2. Use PREVIOUS and NEXT to navigate
3. Use EXIT to finish and see summary statistics
4. All charts are saved as PNG files in the project directory

# OUTPUT FILES

Each chart is saved as a high-resolution PNG file:

- chart_1_sales_by_genre.png
- chart_2_sales_trend.png
- chart_3_market_share.png
- chart_4_price_vs_rating.png
- chart_5_rating_distribution.png
- chart_6_correlation_heatmap.png
- chart_7_roi_by_publisher.png
- chart_8_playtime_by_genre.png
- chart_9_stacked_revenue_area.png
- chart_10_player_count_power.png

# UNDERSTANDING THE EXPLANATIONS

Below each chart you will find:

CALCULATION SECTION:
Shows the mathematical formula used to calculate the displayed data

DETAILED ANALYSIS SECTION:
Includes:

- Total count of data elements
- Statistical measures (mean, median, std dev, etc.)
- Top performers or trends
- Range and distribution metrics
- Interpretation guides for the visualization type

INTERPRETATION GUIDE:
Explains what the chart elements mean and how to read them

KEY METRICS:
Shows most important numbers and comparisons for the data

# SYSTEM REQUIREMENTS

- Python 3.10+
- pandas (data manipulation)
- numpy (numerical calculations)
- matplotlib (visualization)
- seaborn (statistical visualization)
- Virtual environment recommended

# TIPS FOR BEST EXPERIENCE

1. View charts on a large screen for better readability
2. Take note of calculations shown below each chart
3. Compare metrics across different charts to identify trends
4. Use PNG files for presentations or reports
5. Pay attention to correlation values for identifying relationships
6. Review statistical measures to understand data spread and distribution

For questions or modifications, review the calculation sections below each chart
for detailed mathematical explanations.

VERSION: 1.0
CREATED: December 2024
LICENSE: Educational Use
