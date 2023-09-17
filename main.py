"""
Created on Fri Sep 15 15:03:11 2023
@author: lillygrella
"""
import polars as pl
from matplotlib import pyplot as plt, dates
from matplotlib.ticker import FuncFormatter


def readin():
    """
    read in CSV
    Create Daily Price Change Variable
    """
    d_f = pl.read_csv('SPY.csv',try_parse_dates=True)
    print(d_f.head(5))
    return d_f


def get_summ_stats(d_f):
    """
    Return Summary Stats
    """

    #d_f2 = pl.DataFrame({"Summary Stats": d_f["Close"].describe()})

    #axes = plt.subplot(921, frame_on=False)
    #axes.xaxis.set_visible(False)
    #axes.yaxis.set_visible(False)

    #plt.

    #table(axes, d_f2, loc="center")

    print(d_f["Close"].describe().to_pandas().set_index('Statistic').to_markdown())

    #plt.savefig("sumstats.png", bbox_inches="tight")
    return d_f["Close"].describe()


def dollars(value, _):
    """
    Format floats to dollars
    'The two args are the value and tick position'
    """
    return f"${value:.0f}"


def make_line_graph(d_f):
    """
    Create Line Graph of
    """
    _, axes = plt.subplots()
    d_f["Close"].plot()
    axes.set_xticks(d_f.index)
    plt.locator_params(axis="x", nbins=12)
    axes.set_title("SPY Closing Stock Price")
    axes.set_xlabel("Date")
    axes.set_ylabel("Closing Price")
    axes.xaxis.set_major_formatter(dates.DateFormatter("%m/%y"))
    axes.yaxis.set_major_formatter(FuncFormatter(dollars))
    plt.savefig("SPY_Closing.png")


def main():
    """
    Main function to perform actions
    """
    spy = readin()
    print(get_summ_stats(spy))
    #make_line_graph(spy)


if __name__ == "__main__":
    main()


