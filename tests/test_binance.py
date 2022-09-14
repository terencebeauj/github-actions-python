"""Tests for the Binance class
"""
from src.binance import *


binance = Binance()

def test_api():
    """Test the base API url
    """
    response = requests.get(url=binance.base_url, timeout=5)
    assert response.status_code == 200

def test_get_markets():
    """Test the get_markets() method
    """
    binance.get_markets()
    assert isinstance(binance.markets, list)

def test_get_candles():
    """Test the get_candles() method
    """
    candles = binance.get_candles(symbol="btcbusd", interval="5m")
    assert isinstance(candles, dict)

def test_convert_candles_to_df():
    """Test dataframe converter method
    """
    candles = binance.get_candles(symbol="btcusdt")
    df = binance.candles_to_df(candles=candles, symbol="btcusdt")
    assert isinstance(df, pd.DataFrame)
    assert df.isna().sum().sum() == 0

def test_modelling():
    """Test the naive model
    """
    price = binance.naive_modelling("btcbusd")
    assert isinstance(price, float)
