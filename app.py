# app.py
import yfinance
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/stock/<ticker>")
def data(ticker):
    ticker == request.view_args['ticker']
    try:

        print (yfinance.Ticker(ticker).history(period="5d", interval="1h"))
        return ticker
    except:
        return 'Invalid stock ticker'
