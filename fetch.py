import yfinance as yf
import pandas as pd
from analytics import calculate_indicators

tickers = ["AAPL","MSFT", "NVDA", "AMZN","TSLA"]
all_data = []
for ticker in tickers:
    stock = yf.Ticker(ticker)
    df=stock.history(period = '1y')

    df = calculate_indicators(df)

    df["Ticker"] = ticker

    df.reset_index(inplace= True)
    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)

final_df = final_df[[
    "Date",
    "Ticker",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",

    "Daily_Return",
    "Weekly_Return",
    "Monthly_Return",

    "MA_7",
    "MA_30",
    "Volume_MA30",

    "Volatility",

    "Price_Change",
    "High_Low_Diff",
    "Open_Close_Diff",
    "Intraday_Return",

    "Trend",
    "StockSense_Score",
    "Explanation",
    "Rating"
]]

print(
    final_df[
        [
            "Ticker",
            "Daily_Return",
            "Monthly_Return",
            "Trend",
            "StockSense_Score",
            "Rating",
            "Explanation"
        ]
    ].tail(20)
)

final_df.to_csv("stock_data.csv", index=False)

print("\n CSV Saved Sucessfully!")