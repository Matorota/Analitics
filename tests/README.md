# Tests Folder

This folder contains all test scripts for the Video Game Analytics Dashboard.

## Test Files

### `test.py`

Quick test to verify:

- Database loads correctly
- Menu system is functional
- Chart methods are accessible

**Run:**

```bash
python tests/test.py
```

### `test_charts.py`

Comprehensive test of all 10 charts with visual feedback.

**Run:**

```bash
python tests/test_charts.py
```

### `test_all_charts.py`

Full test of all 10 charts in non-interactive mode with detailed results.

**Run:**

```bash
python tests/test_all_charts.py
```

## Running Tests

From the project root:

```bash
# Quick test
python tests/test.py

# Chart generation test
python tests/test_charts.py

# Comprehensive test
python tests/test_all_charts.py
```

All tests verify that the 10 charts generate without errors.
