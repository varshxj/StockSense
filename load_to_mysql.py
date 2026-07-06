import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv("stock_data.csv")
df = df.where(pd.notna(df), None)

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="stocksense"
)

cursor = conn.cursor()

query = """
    INSERT INTO stock_prices
    (
    trade_date,
    ticker,
    open_price,
    high_price,
    low_price,
    close_price,
    volume,
    daily_return,
    weekly_return,
    monthly_return,
    ma7,
    ma30,
    volume_ma30,
    volatility,
    price_change,
    high_low_diff,
    open_close_diff,
    intraday_return,
    trend,
    stocksense_score,
    rating,
    explanation
    )
    VALUES
    (
    %s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s
    )
"""

for _, row in df.iterrows():

    values = (
    row["Date"][:10],
    row["Ticker"],
    row["Open"],
    row["High"],
    row["Low"],
    row["Close"],
    int(row["Volume"]),

    row["Daily_Return"],
    row["Weekly_Return"],
    row["Monthly_Return"],

    row["MA_7"],
    row["MA_30"],
    row["Volume_MA30"],

    row["Volatility"],

    row["Price_Change"],
    row["High_Low_Diff"],
    row["Open_Close_Diff"],
    row["Intraday_Return"],

    row["Trend"],
    int(row["StockSense_Score"]),
    row["Rating"],
    row["Explanation"]
)

    cursor.execute(query, values)

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()