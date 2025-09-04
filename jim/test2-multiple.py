# Import packages
# Resources: https://blog.quantinsti.com/stock-market-data-analysis-python/
# https://plotly.com/python/line-charts/
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# _______________________________________ Individual Searches __________________________________________________
# Set the start and end date
start_date = '1990-01-01'
end_date = '2024-08-1'

# Set the ticker
ticker = 'AMZN'

data = yf.download(ticker, start_date, end_date, group_by=ticker, auto_adjust=False)[ticker]
 # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html
data = data.reset_index()  # DataFrame has a MultiIndex, this method can remove the levels to only a single column.
data['ticker'] = ticker
fig = px.line(data, x='Date', y=['Open', 'High', 'Low', 'Close'])
fig.show()
