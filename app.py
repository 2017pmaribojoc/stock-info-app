# app.py
from flask import Flask, request

from yfinance_client import get_stock_info

app = Flask(__name__)

@app.route("/health")
def hello():
    return "Up and running!"

@app.route("/stock/<ticker>")
def data(ticker):
    ticker == request.view_args['ticker']
    return get_stock_info(ticker)
