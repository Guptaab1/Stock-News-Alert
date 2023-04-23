# print("Welcome to day 36.")

import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "0HCSEG2IMEV0HQWF"
NEWS_API_KEY = "c79e4ef26de34350b01fa7a764096cb0"

stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": STOCK_API_KEY,
}

# Get yesterday's closing price

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (60min)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get day before yesterday's data

day_before_yesterday_data = data_list[16]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Difference between yesterday's data and day before yesterday's data

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "▲"
else:
    up_down = "▼"

difference_percent = difference / float(yesterday_closing_price) * 100

if difference_percent > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # print(articles)

    three_article = articles[:3]
    # print(three_article)

    formatted_articles = [f"{STOCK_NAME}: {up_down} {difference_percent}\nHeadline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_article]
    # formatted_articles = [f"Headline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_article]
    for articles in formatted_articles:
        print(articles)
