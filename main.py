from datetime import datetime
from helper.technical_analysis import getYfinanceHistoric, getBinanceHistoric, dateToMs


def main():
    # Example usage of getYfinanceHistoric function
    start_time = "2023-01-01"
    end_time = datetime.now()
    symbol = "AAPL"
    interval = "1d"
    try:
        price_data = getYfinanceHistoric(symbol, startTime=start_time, endTime=end_time, interval=interval)
        print(f"Prices of {symbol}\n")
        print(price_data)
    except Exception as e:
        print(f"Error getting historic prices for {symbol}: {str(e)}")

    # Example usage of getBinanceHistoric function
    start_time = dateToMs("2023-01-01")
    stop_time = dateToMs("2023-01-31")
    symbol = "BTCUSDT"
    interval = "1d"
    try:
        price_data = getBinanceHistoric(symbol, startTime=start_time, endTime=stop_time, interval=interval)
        print(price_data)
    except Exception as e:
        print(f"Error getting historic prices for {symbol}: {str(e)}")


if __name__ == '__main__':
    main()
