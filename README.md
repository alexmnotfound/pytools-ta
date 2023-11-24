# Python for Technical Analysis and Trading Strategies (WIP)
![img.png](img.png)
## Purpose
This repository provides a comprehensive set of tools for traders and investors to perform technical analysis of financial markets using Python.

---

The repository is a collection of Python scripts and modules designed to perform technical analysis of financial markets. Technical analysis is a method used by traders and investors to analyze market data, such as price and volume, to identify trends, patterns, and potential trading opportunities.

The repository includes tools for data retrieval, data preprocessing, and technical analysis. The data retrieval tools enable users to retrieve market data from various sources, such as APIs, CSV files, and databases. The data preprocessing tools are designed to clean, normalize, and transform the data into a format suitable for technical analysis.

The technical analysis tools include a wide range of indicators, such as moving averages, Bollinger Bands, Relative Strength Index (RSI), MACD, and many more. These indicators are used to identify trends, momentum, and overbought/oversold conditions in the market.

The repository also includes modules for backtesting trading strategies and evaluating their performance. These modules allow users to simulate trading strategies using historical market data and evaluate their profitability and risk metrics.


---


## How to run it
I personally recommend it to run it in a virtual environment, as follows:
1. Open a command prompt or terminal window.
2. Navigate to the directory where you want to create the virtual environment. You can use the `cd` command to change directories.
3. Enter the following command to create a new virtual environment: `python3 -m venv myenv`, replacing "myenv" with the name you want to give to your virtual environment.
4. Activate the virtual environment by entering the following command (Linux environments): `source myenv/bin/activate`
5. Once the virtual environment is activated, you can install Python packages using `pip` as usual. For example, to install the all the packages, 
you can enter the following command: `pip3 install -r requirements.txt`
6. Assuming you're on the project's folder, now you can run `python3 main.py`
7. When you're done using the virtual environment, you can deactivate it by entering the following command: `deactivate`


## Functions definitions
### `getYfinanceHistoric`
This function downloads historic price data for a specified ticker `symbol` from Yahoo Finance using the `yfinance` library. 
The data is returned as a Pandas dataframe with columns for open, high, low, close, and volume. 
The function takes optional arguments for `start time`, `end time`, and `interval`.
### `getBinanceHistoric`
This function downloads historic price data for a specified ticker `symbol` from the Binance API. 
The data is returned as a Pandas dataframe with columns for open, high, low, close, and volume. 
The function takes optional arguments for `start time`, `end time`, `interval`, and `row limit`. 
Note that the `startTime` and `endTime` arguments are specified in **milliseconds since epoch**.
### `dateToMs`
This function converts a date string in the format `"YYYY-MM-DD"` to **milliseconds since epoch**. 
This conversion is used in the `getBinanceHistoric` function to specify start and end times in the API request.


## Aknowledgements
We would like to acknowledge the work done by Juan Pablo Pisano, ownser of [this repository](https://github.com/gauss314).
Their open-source project has provided valuable resources and tools for backtesting trading algorithms and has inspired the development of many other similar projects. 
I used his code as a reference while developing some of the tools in this repository, and I'm grateful for their contributions to the community.
