# 📈 StockSense - Stock Market Analytics Dashboard

An end-to-end stock market analytics project that collects historical stock data using Python, performs financial analysis, stores processed data in MySQL, and visualizes insights through an interactive Power BI dashboard.

---

## 🚀 Features

- Fetches one year of historical stock data using Yahoo Finance
- Calculates financial indicators:
  - Daily Return
  - Weekly Return
  - Monthly Return
  - 7-Day Moving Average (MA7)
  - 30-Day Moving Average (MA30)
  - Volume Moving Average
  - Volatility
  - Price Change
  - Intraday Return
- Detects market trends (Bullish / Bearish)
- Generates a custom **StockSense Score**
- Assigns stock ratings
- Generates stock insights
- Stores processed data in MySQL
- Visualizes results using Power BI

---

## 🛠 Technologies Used

- Python
- Pandas
- Yahoo Finance API (yfinance)
- MySQL
- SQL
- Power BI

---

## 📂 Project Structure

```
StockSense/
│
├── analytics.py
├── fetch.py
├── load_to_mysql.py
├── stock_data.csv
├── requirements.txt
├── README.md
│
├── dashboard/
│   └── StockSense.pbix
│
└── screenshots/
```

---

## 📊 Dashboard Pages

### 📈 Executive Dashboard
Provides an overview of stock performance, market trends, StockSense Score, ratings, and key performance indicators.

### 🏢 Company Analysis
Interactive analysis of individual companies using price trends, moving averages, returns, ratings, and insights.

### ⚠ Risk & Performance Analysis
Compares volatility, returns, and trading volume across companies.

### 🧠 StockSense Intelligence
Displays StockSense Scores, ratings, market trends, and generated insights.

---

## 🔄 Project Workflow

```
Yahoo Finance API
        │
        ▼
   Fetch Stock Data
        │
        ▼
 Calculate Indicators
        │
        ▼
 Generate StockSense Score
        │
        ▼
 Store Data (CSV & MySQL)
        │
        ▼
   Power BI Dashboard
```

---

## 📸 Dashboard Preview

Dashboard screenshots will be added soon.

---

## 🚀 Future Improvements

- Real-time stock monitoring
- Portfolio analysis
- Machine Learning-based price prediction
- News sentiment analysis
- Email alerts
- Stock recommendation engine

---

## 👩‍💻 Author

**Varshini J**

Bachelor of Engineering – Electronics and Communication Engineering

Python | SQL | MySQL | Power BI | Data Analytics
