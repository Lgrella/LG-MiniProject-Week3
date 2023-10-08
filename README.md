# Python Template
---
This repo is for mini-project 3 in the IDS 706 Data Engineering Systems class.

The intention is to use polars for data exploration and analysis.

Using the past year of data for SPY stock, this project reads in the data as a pandas dataframe, charts the SPY daily closing price using matplotlib, and provides summary statistics.

Dataset: [SPY.csv](/SPY.csv)

Refer to the generated [report](/Report.md) for the summary statistics and the data visualization. This is directly outputted from `main.py`.

## Summary statistics for Close Price of SPY

|    | statistic   |    value |
|---:|:------------|---------:|
|  0 | count       | 252      |
|  1 | null_count  |   0      |
|  2 | mean        | 409.341  |
|  3 | std         |  26.0028 |
|  4 | min         | 356.56   |
|  5 | 25%         | 391.56   |
|  6 | 50%         | 407.38   |
|  7 | 75%         | 436.17   |
|  8 | max         | 457.79   |

## Data Visualization

### Line Graph of SPY closing prices
![LineGraph](SPY_Closing.png)
