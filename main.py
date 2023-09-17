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
    return d_f


def get_summ_stats(d_f):
    """
    Return Summary Stats
    """
    stats = d_f['Close'].describe()
    return stats

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
    d = d_f.to_pandas()
    _, axes = plt.subplots()
    d["Close"].plot()
    axes.set_xticks(d.index)
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
    stats = get_summ_stats(spy)

    make_line_graph(spy)

    string = f'''
    # This is the generated report for [SPY.csv](https://github.com/nogibjj/LG-Week2-Pandas/blob/main/SPY.csv).
    #It includes both summary statistics and data visualizations

    ## Summary statistics for the Close Variable

    {stats.to_pandas().to_markdown()}

    ## Data Visualization

    ### Boxplots of each variable
    ![LineGraph](SPY_Closing.png)

    '''

    # Specify the file path where you want to create the Markdown file
    filepath = "Generated Report.md"

    # 
    with open(filepath, "w", encoding="utf-8") as md_file:
        md_file.write(string)


if __name__ == "__main__":
    main()


