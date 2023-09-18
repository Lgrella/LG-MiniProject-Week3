# test test_main.py
from main import readin, get_summ_stats


def test_sumstats():
    """
    confirms summary stats are being calculated correctly
    """
    spy = readin()
    series = get_summ_stats(spy)
    data = spy.to_pandas()
    #print(spy["Close"].median())

    print(spy["Close"].median())
    print(series[6]['value'][0])

    assert data["Close"].mean().round(2) == round(series[2]['value'][0],2)
    assert data["Close"].count() == series[0]['value'][0]
    assert data["Close"].std().round(2) == round(series[3]['value'][0],2)


if __name__ == "__main__":
    test_sumstats()
