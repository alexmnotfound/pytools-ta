import pandas as pd
import requests
import yfinance as yf
from datetime import datetime


def getYfinanceHistoric(symbol, startTime='2000-01-01', interval='1d', endTime=None):
    """
    Download historic prices from Yahoo Finance

    :param symbol: str
        Ticker symbol to download.
    :param interval: str
        Valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo.
        Intraday data cannot extend last 60 days.
    :param startTime: str
        Download start date string (YYYY-MM-DD) or datetime object.
        Default is '2000-01-01'.
    :param endTime: str
        Download end date string (YYYY-MM-DD) or datetime object.
        Default is now.

    :return: pd.DataFrame
        Price data, with the following columns: ['Open', 'High', 'Low', 'Close', 'Volume'].
    """
    data = yf.download(symbol, start=startTime, end=endTime, interval=interval, auto_adjust=True)
    data.index.names = ['openTime']

    return data


def getBinanceHistoric(symbol, interval='1d', startTime=None, endTime=None, limit=1000):
    """
    Download historic price data from the Binance API.

    :param symbol: str
        Ticker symbol to download.
    :param interval: str
        Valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1w, 1M, 3M.
    :param startTime: str
        Milliseconds since epoch.
        Default is None.
    :param endTime: str
        Milliseconds since epoch.
        Default is None.
    :param limit: int
        Row limit (default is 1000).

    :return: pd.DataFrame
        Price data, with the following columns: ['Open', 'High', 'Low', 'Close', 'Volume'].
    """
    url = 'https://api.binance.com/api/v3/klines'

    params = {'symbol': symbol, 'interval': interval, 'startTime': startTime, 'endTime': endTime, 'limit': limit}

    r = requests.get(url, params=params)
    js = r.json()

    # Creating DataFrame
    cols = ['openTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'cTime',
            'qVolume', 'trades', 'takerBase', 'takerQuote', 'Ignore']

    df = pd.DataFrame(js, columns=cols)

    # Converting strings to numeric
    df = df.apply(pd.to_numeric)

    # Timestamp index handling
    df.index = pd.to_datetime(df.openTime, unit='ms')

    # Dropping unused columns
    df = df.drop(['openTime', 'cTime', 'takerBase', 'takerQuote', 'Ignore'], axis=1)
    df = df.drop(['trades', 'qVolume'], axis=1)

    return df


def dateToMs(dateStr):
    """
    Convert a date string to milliseconds since epoch.

    :param dateStr: str
        Date string in YYYY-MM-DD format.

    :return: int
        Milliseconds since epoch.
    """
    return int(datetime.strptime(dateStr, '%Y-%m-%d').timestamp()) * 1000
