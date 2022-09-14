# Price predictor
This simple application is going to return the prediction for any symbol on the binance spot exchange at the actual candle, you can compare the prediction with the actual price of the candle (on the 1m timeframe).
I've used a naive random forest model algorithm to make the predictions.
I'm going to improve it in the future, it was a quick project for me to setup a complete workflow with github actions.

## Installation

1. Clone the project

2. Create a virtual environnement

        python -m venv venv

3. Install dependancies:

        pip install -r requirements.txt

## Launching the app
I have created the app using FastAPI. To run the server, launch the command:

        uvicorn src.main:app --reload

Then, you will be able to access the API on your machine at this location `localhost:8000`

## Tests
I'm using the pytest libray for testing, to run the tests launch the command:

        pytest -s -v

## CI
I'm using Github Actions for the CI workflow, you can access the details at this location `.github/workflows`





