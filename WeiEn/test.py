from ipywidgets import interact_manual

@interact_manual(period=['1mo', '3mo', '6mo'], interval=['1d', '1h'])
def interactive_amzn(period='1mo', interval='1d'):
    prices, dates = get_stock_prices('AAPL', period, interval)
    trade = best_time_to_buy_and_sell(prices)
    plot_prices_with_trade(prices, dates, trade, 'AAPL')
#testing commit