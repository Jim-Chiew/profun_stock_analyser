# Import packages
# Resources: https://blog.quantinsti.com/stock-market-data-analysis-python/
# https://plotly.com/python/candlestick-charts/
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# _______________________________________ Individual Searches __________________________________________________
# Set the start and end date
start_date = '1990-01-01' 
end_date = '2024-08-1'

# Set the ticker
tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT', 'AMZN']

# Get the data
data_all = None
for ticker in tickers_list:
    data = yf.download(ticker, start_date, end_date, group_by=ticker, auto_adjust=False)[ticker]
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html
    data = data.reset_index()  # DataFrame has a MultiIndex, this method can remove the levels to only a single column.
    data['ticker'] = ticker  # Sets all data to have ticker:ticker_value in the dataframe
    data_all = pd.concat([data_all, data], axis=0, ignore_index=True)

print(data_all.tail())

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])
fig.show()
