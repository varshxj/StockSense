import pandas as pd


def detect_trend(df):

    df["Trend"] = "Sideways"

    df.loc[df["MA_7"] > df["MA_30"], "Trend"] = "Bullish"

    df.loc[df["MA_7"] < df["MA_30"], "Trend"] = "Bearish"

    return df

def generate_insights(df):

    insights = []

    for _, row in df.iterrows():

        stock_insights = []

        if row["Trend"] == "Bullish":
            stock_insights.append("Strong upward trend")

        elif row["Trend"] == "Bearish":
            stock_insights.append("Downward trend")

        if row["Daily_Return"] > 2:
            stock_insights.append("Price gained more than 2% today")

        elif row["Daily_Return"] < -2:
            stock_insights.append("Price dropped more than 2% today")

        if row["Volatility"] > 10:
            stock_insights.append("High volatility")

        if row["Volume"] > row["Volume_MA30"]:
            stock_insights.append("Higher than average trading volume")

        insights.append(", ".join(stock_insights))

    df["Insights"] = insights

def calculate_stocksense_score(df):

    df["StockSense_Score"] = 50

    average_volume = df["Volume"].mean()
    average_volatility = df["Volatility"].mean()

        # Trend
    df.loc[df["Trend"] == "Bullish", "StockSense_Score"] += 20
    df.loc[df["Trend"] == "Bearish", "StockSense_Score"] -= 20

    # Daily Return
    df.loc[df["Daily_Return"] > 0, "StockSense_Score"] += 10
    df.loc[df["Daily_Return"] <= 0, "StockSense_Score"] -= 10

    # Monthly Return
    df.loc[df["Monthly_Return"] > 0, "StockSense_Score"] += 10
    df.loc[df["Monthly_Return"] <= 0, "StockSense_Score"] -= 10

    # Volume
    df.loc[
        df["Volume"] > df["Volume_MA30"],
        "StockSense_Score"
    ] += 5

    df.loc[
        df["Volume"] <= df["Volume_MA30"],
        "StockSense_Score"
    ] -= 5

    # Volatility
    df.loc[
        df["Volatility"] < average_volatility,
        "StockSense_Score"
    ] += 5

    df.loc[
        df["Volatility"] >= average_volatility,
        "StockSense_Score"
    ] -= 5
    
    return df

def generate_explanation(df):

    explanations = []

    for _, row in df.iterrows():

        reason = []

        if row["Trend"] == "Bullish":
            reason.append("Bullish Trend")
        else:
            reason.append("Bearish Trend")

        if row["Daily_Return"] > 0:
            reason.append("Positive Daily Return")
        else:
            reason.append("Negative Daily Return")

        if row["Monthly_Return"] > 0:
            reason.append("Positive Monthly Return")
        else:
            reason.append("Negative Monthly Return")

        if row["Volume"] > row["Volume_MA30"]:
            reason.append("High Trading Volume")
        else:
            reason.append("Normal Trading Volume")

        if row["Volatility"] < df["Volatility"].mean():
            reason.append("Low Volatility")
        else:
            reason.append("High Volatility")

        explanations.append(", ".join(reason))

    df["Explanation"] = explanations

    return df

def assign_rating(df):

    df["Rating"] = "Moderate"

    df.loc[df["StockSense_Score"] >= 90, "Rating"] = "Excellent"

    df.loc[
        (df["StockSense_Score"] >= 75) &
        (df["StockSense_Score"] < 90),
        "Rating"
    ] = "Strong"

    df.loc[
        (df["StockSense_Score"] >= 60) &
        (df["StockSense_Score"] < 75),
        "Rating"
    ] = "Moderate"

    df.loc[
        (df["StockSense_Score"] >= 40) &
        (df["StockSense_Score"] < 60),
        "Rating"
    ] = "Weak"

    df.loc[df["StockSense_Score"] < 40, "Rating"] = "High Risk"

    return df

def calculate_indicators(df):

    # Returns
    df["Daily_Return"] = df["Close"].pct_change() * 100
    df["Weekly_Return"] = df["Close"].pct_change(periods=5) * 100
    df["Monthly_Return"] = df["Close"].pct_change(periods=21) * 100

    # Moving Averages
    df["MA_7"] = df["Close"].rolling(7).mean()
    df["MA_30"] = df["Close"].rolling(30).mean()
    df["Volume_MA30"] = df["Volume"].rolling(30).mean()

    # Risk
    df["Volatility"] = df["Close"].rolling(30).std()

    # Price Movement
    df["Price_Change"] = df["Close"].diff()
    df["High_Low_Diff"] = df["High"] - df["Low"]
    df["Open_Close_Diff"] = df["Close"] - df["Open"]
    df["Intraday_Return"] = (
        (df["Close"] - df["Open"]) / df["Open"]
    ) * 100


    # Call another function
    df = detect_trend(df)

    df = calculate_stocksense_score(df)

    df = generate_explanation(df)

    df = detect_trend(df)

    df = assign_rating(df)


    return df