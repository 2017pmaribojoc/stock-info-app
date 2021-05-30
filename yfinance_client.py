import yfinance


def get_stock_info(ticker):
    response = {}

    try:

        stock_info = yfinance.Ticker(ticker=ticker).history(period="1wk", interval="1d")
        stock_info['id'] = range(0, 0 + len(stock_info))
        stock_info.insert(loc=1, column='date', value=stock_info.index)
        stock_info = stock_info.set_index('id')
        stock_info.columns = stock_info.columns.str.lower()

        response['performance'] = stock_info.to_dict(orient='records')


    except Exception as e:
        print(e)
        response['error'] = 'Error retrieving stock information'
    return response