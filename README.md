VIDEO GAME ANALYTICS DASHBOARD - INTERACTIVE INTERFACE

# OVERVIEW

This project provides a professional data analytics platform for visualizing and analyzing
video game industry data with 10 different chart types, each including detailed calculations
and statistical explanations.

python run.py

python tests/test.py # Quick test
python tests/test_charts.py # Chart test
python tests/test_all_charts.py # Full test

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

# GETTING STARTED FROM SCRATCH

To start this project on a new PC from Git:

## Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd Analitics-python
```

## Step 2: Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run the Project

```bash
python run.py
```

## Step 5: Verify Everything Works

```bash
python tests/test.py
```

That's it! The database will auto-generate on first run.

# TIPS FOR BEST EXPERIENCE

1. View charts on a large screen for better readability
2. Take note of calculations shown below each chart
3. Compare metrics across different charts to identify trends
4. Use PNG files for presentations or reports
5. Pay attention to correlation values for identifying relationships
6. Review statistical measures to understand data spread and distribution

For questions or modifications, review the calculation sections below each chart
for detailed mathematical explanations.
