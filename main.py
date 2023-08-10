from datetime import datetime
import helper.technical_analysis as ta


def main():
    try:
        # TODO: add future testing
        # downloadYahooHistoricTest()
        # downloadBinanceHistoricTest()
        from_date = "2022-01-01"
        to_date = "2022-02-15"
        start_time = ta.dateToMs(from_date)
        stop_time = ta.dateToMs(to_date)
        symbol = "BTCUSDT"
        interval = "15m"
        print(f"Backtesting {symbol} on {interval} for dates from {from_date} to {to_date}")

        price_data = ta.getBinanceHistoricFull(symbol, startTime=start_time, endTime=stop_time, interval=interval)
        print(price_data)



    except Exception as e:
        print(f"Error while running script: {str(e)}")


def downloadYahooHistoricTest():
    # Example usage of getYfinanceHistoric function
    start_time = "2023-01-01"
    end_time = datetime.now()
    symbol = "AAPL"
    interval = "1d"
    try:
        price_data = ta.getYfinanceHistoric(symbol, startTime=start_time, endTime=end_time, interval=interval)
        print(f"Prices of {symbol}\n")
        print(price_data)
    except Exception as e:
        errMsg = f"Error getting historic prices for {symbol}: {str(e)}"
        raise Exception(errMsg)

def downloadBinanceHistoricTest():
    # Example usage of getBinanceHistoric function
    start_time = ta.dateToMs("2023-01-01")
    stop_time = ta.dateToMs("2023-12-31")
    symbol = "BTCUSDT"
    interval = "15m"
    try:
        price_data = ta.getBinanceHistoric(symbol, startTime=start_time, endTime=stop_time, interval=interval)
        print(price_data)
    except Exception as e:
        errMsg = f"Error getting historic prices for {symbol}: {str(e)}"
        raise Exception(errMsg)

if __name__ == '__main__':
    main()
