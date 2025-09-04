import pandas as pd

df = pd.DataFrame({
    "Open": [100, 102, 105],
    "Close": [102, 101, 107]
})

# Function takes 2 arguments (from DataFrame columns)
def price_change(open_price, close_price):
    return close_price - open_price

# https://www.dataquest.io/blog/tutorial-how-to-use-the-apply-method-in-pandas/
df["Change"] = df.apply(lambda row: price_change(row["Open"], row["Close"]), axis=1)

print(df)
