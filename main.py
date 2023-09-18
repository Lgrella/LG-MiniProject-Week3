"""
Created on Fri Sep 15 15:03:11 2023
@author: lillygrella
"""
import polars as pl
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter


def make_line_graph(d_f):
    """
    Make Line Graph
    """
    _, axs = plt.subplots(1, 1, layout="constrained", figsize=(6, 6))
    locator = mdates.AutoDateLocator(minticks=12, maxticks=13)
    formatter = mdates.ConciseDateFormatter(locator)
    axs.xaxis.set_major_locator(locator)
    axs.xaxis.set_major_formatter(formatter)
    axs.yaxis.set_major_formatter(FuncFormatter(dollars))

    axs.plot("Date", "Close", data=d_f)
    axs.set_xlim((np.datetime64("2022-09-15"), np.datetime64("2023-09-15")))
    axs.set_title("SPY Closing Prices Over Time")
    axs.set_xlabel("Date")
    axs.set_ylabel("Closing Price")

    plt.savefig("SPY_Closing.png")


def readin():
    """
    read in CSV
    Create Daily Price Change Variable
    """
    d_f = pl.read_csv("SPY.csv", try_parse_dates=True)
    return d_f


def get_summ_stats(d_f):
    """
    Return Summary Stats
    """
    stats = d_f["Close"].describe()
    return stats


def dollars(value, _):
    """
    Format floats to dollars
    'The two args are the value and tick position'
    """
    return f"${value:.0f}"


def main():
    """
    Main function to perform actions
    """
    spy = readin()
    stats = get_summ_stats(spy)
    make_line_graph(spy)

    string = f'''
# This is the generated report for [SPY.csv](https://github.com/nogibjj/LG-Week2-Pandas/blob/main/SPY.csv).
# It includes both summary statistics and a data visualization

## Summary statistics for the Close Variable

{stats.to_pandas().to_markdown()}

## Data Visualization

### Line Graph of SPY closing prices
![LineGraph](SPY_Closing.png)

    '''

    # output markdown file
    filepath = "Report.md"

    with open(filepath, "w", encoding="utf-8") as md_file:
        md_file.write(string)

if __name__ == "__main__":
    main()
