# Charts Package

This folder contains individual Python files for each of the 10 analytics charts.

## Chart Files

- `chart_1.py` - Average Sales by Genre (Bar Chart)
- `chart_2.py` - Top 10 Publishers by Total Sales (Horizontal Bar)
- `chart_3.py` - Market Share by Platform (Pie Chart)
- `chart_4.py` - Average Rating by Platform (Bar Chart)
- `chart_5.py` - Rating Distribution (Histogram with π-based bins)
- `chart_6.py` - Correlation Matrix (Heatmap)
- `chart_7.py` - Average Price by Genre (Horizontal Bar)
- `chart_8.py` - Playtime Distribution by Genre (Violin Plot)
- `chart_9.py` - Revenue Trends by Genre (Stacked Area Chart)
- `chart_10.py` - Revenue vs Copies Sold by Genre (Bubble Chart)

## Usage

### As a Package

```python
from src.charts import ChartGenerator

chart_gen = ChartGenerator(df)
fig = chart_gen.chart_1_sales_by_genre_bar()
plt.show()
```

### Individual Chart Functions

```python
from src.charts.chart_1 import chart_1_sales_by_genre_bar

fig = chart_1_sales_by_genre_bar(df)
plt.show()
```

## Structure

```
charts/
├── __init__.py           # Package initialization with ChartGenerator
├── chart_1.py           # Individual chart function
├── chart_2.py
├── ...
├── chart_10.py
└── README.md            # This file
```

## Adding New Charts

1. Create `chart_XX.py` with a function `chart_XX_description(df)`
2. Import it in `__init__.py`
3. Add a method to `ChartGenerator` class that calls the function
4. Update `__all__` list
