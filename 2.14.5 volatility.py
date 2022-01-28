import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.

    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']

    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """

    # format dataset
    df = prices.pivot(index='date', columns='ticker', values='price')
    print(df.head())

    # separate A and B subsets
    a = df['A']
    b = df['B']
    print(a.head())

    # calculate log prices
    al = np.log(a)
    bl = np.log(b)
    print(al.head())

    # calculate log returns
    alr = al - al.shift(1)
    blr = bl - bl.shift(1)
    print(alr.head())

    # calculate standard deviation of log returns
    alr_std = np.std(alr)
    blr_std = np.std(blr)
    print(alr_std)
    print(blr_std)

    if (alr_std > blr_std):
        return 'A'
    return 'B'


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
