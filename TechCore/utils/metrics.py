import pandas as pd


def maximum_drawdown(pnl, window=252):
    Roll_Max = pnl.rolling(window, min_periods=1).max()
    Daily_Drawdown = pnl/Roll_Max - 1.0

    # Next we calculate the minimum (negative) daily drawdown in that window.
    # Again, use min_periods=1 if you want to allow the expanding window
    Max_Daily_Drawdown = Daily_Drawdown.rolling(window, min_periods=1).min()
    return Max_Daily_Drawdown


def portfolio_value(pnl):
    return pnl


def relative_return(pnl, window=252):
    daily_pnl = pnl.diff()
    return daily_pnl.rolling(window).mean()


def sharpe_ratio(pnl):
    daily_pnl = pnl.diff()
    return daily_pnl.mean() / daily_pnl.std()


def get_mertics(pnl, logs=False):
    mdd = maximum_drawdown(pnl)
    pv = portfolio_value(pnl)
    rr = relative_return(pnl)
    sr = sharpe_ratio(pnl)

    if logs:
        return {
            'maximum_drawdown': mdd,
            'portfolio_value': pv,
            'relative_return': rr
        }
    else:
        return {
            'maximum_drawdown': mdd.min(),
            'portfolio_value': pv.iloc[-1],
            'relative_return': rr.sum(),
            'sharpe_ratio': sr
        }