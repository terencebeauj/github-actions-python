"""This file is used to generate the Binance class"""

import typing

import requests
import pandas as pd


class Binance:
    """Class to work with Binance exchange"""

    def __init__(self) -> None:
        self.base_url = "https://api.binance.com"
        self.markets = self.get_markets()
        self.candles = {}

    def get_markets(self) -> typing.List:
        """Get all the pairs

        Returns:
            typing.List: Array with the pairs
        """
        endpoint = "/api/v3/exchangeInfo"
        response = requests.get(url=self.base_url + endpoint, timeout=5)
        symbols = []
        if response.status_code == 200:
            data = response.json()
            for symbol in data["symbols"]:
                symbols.append(symbol["symbol"])
            return symbols
        response.raise_for_status()
        return None

    def get_candles(
        self, symbol: str, interval: str = "1m", limit: int = 1000
    ) -> typing.Dict:
        """Get 1000 last candles for a symbol and a particular timeframe

        Args:
            symbol (str): symbol should be in binance pairs
            interval (str, optional): timeframe. Defaults to "1m".
            limit (int, optional): how many candles to retrieve, max 1000. Defaults to 1000.

        Raises:
            Exception: Raise Exception if we pass an unknown pair

        Returns:
            typing.Dict: Dictionnary of candles for the symbol
        """
        if (symbol.upper() or symbol) in self.markets:
            endpoint = "/api/v3/klines"
            params = {}
            params["symbol"] = symbol.upper()
            params["interval"] = interval
            params["limit"] = limit

            response = requests.get(
                url=self.base_url + endpoint, params=params, timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                candles = {
                    "time": [],
                    "open": [],
                    "high": [],
                    "low": [],
                    "close": [],
                    "volume": [],
                }
                for candle in data:
                    candles["time"].append(candle[0])
                    candles["open"].append(float(candle[1]))
                    candles["high"].append(float(candle[2]))
                    candles["low"].append(float(candle[3]))
                    candles["close"].append(float(candle[4]))
                    candles["volume"].append(float(candle[5]))
                return candles
            response.raise_for_status()
        raise Exception(f"{symbol} not in binance pairs")

    def candles_to_df(
        self, candles: typing.Dict, symbol: str, interval: str = "1m", limit: int = 1000
    ) -> pd.DataFrame:
        """Convert candles to DataFrame object

        Args:
            candles (typing.Dict): List of candles
            symbol (str): Symbol
            interval (str, optional): Timeframe. Defaults to "1m".
            limit (int, optional): How many candles to retrieve, max 1000. Defaults to 1000.

        Returns:
            _type_: None
        """
        candles = self.get_candles(symbol, interval, limit)
        df = pd.DataFrame(candles)
        df.set_index("time", drop=True, inplace=True)
        df["datetime"] = pd.to_datetime(df.index, unit="ms")
        self.candles[symbol] = df
        return df