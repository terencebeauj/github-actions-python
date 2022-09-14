"""Module for the API
"""
from fastapi import FastAPI
from fastapi import HTTPException

from src.binance import Binance

app = FastAPI()

binance = Binance()


@app.get("/")
def read_root():
    """Root endpoint

    Returns:
        typing.Dict: Return the message 'Ok' if connected successfully
    """
    return {"status": "Ok"}

@app.get("/prediction/{symbol}")
def get_prediction(symbol: str):
    """Get the prediction for a particular symbol

    Args:
        symbol (str): symbol to get the prediction from

    Raises:
        HTTPException: raise an error if binance does not have support for this symbol

    Returns:
        typing.Dict: return the prediction
    """
    if symbol.upper() not in binance.markets:
        raise HTTPException(status_code=404, detail=f"{symbol} not in binance pairs")
    pred = binance.naive_modelling(symbol)
    return {"prediction": pred}
