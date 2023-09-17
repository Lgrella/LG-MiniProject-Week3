"""
Created on Fri Sep 15 15:03:11 2023
@author: lillygrella
"""
import polars as pl
from matplotlib import pyplot as plt, dates
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import plotly.express as px


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
    d_f["Close"].describe().write_csv("sumstats.csv")
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
    px.line(x=d_f["Date"], y=d_f["Close"])


def main():
    """
    Main function to perform actions
    """
    spy = readin()
    get_summ_stats(spy)
    make_line_graph(spy)


if __name__ == "__main__":
    main()


