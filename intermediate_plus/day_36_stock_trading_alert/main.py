import os
from email.mime.text import MIMEText

import requests
from datetime import datetime, timedelta
import smtplib

from dotenv import load_dotenv

# Stocks API Data
STOCK = "IBM"
TIME_FRAME = "TIME_SERIES_DAILY"
STOCKS_API_KEY = "demo"
daily_data_endpoint = "https://www.alphavantage.co/query"

# News API Data
NEWS_API_KEY = "b31f71d3a9cf4f2e8bc2ebea16e3dddf"
news_endpoint = "https://newsapi.org/v2/everything"

# SMTP Data
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("APP_PASSWORD")
ADDR_TO = os.getenv("ADDR_TO")
mail_host = "smtp.gmail.com"
mail_port = 587


def collect_stock_data():
    ## STEP 1: Use https://www.alphavantage.co - DONE
    # When STOCK price increase/decreases by 5% between yesterday_datetime and the day before yesterday_datetime then print("Get News").
    params = {
        "function": TIME_FRAME,
        "symbol": STOCK,
        "apikey": STOCKS_API_KEY,
    }
    response = requests.get(daily_data_endpoint, params=params)
    response.raise_for_status()
    data = response.json()

    today = datetime.now()
    yesterday_datetime = today - timedelta(days=1)
    yesterday = str(yesterday_datetime).split(" ")[0]
    # print(yesterday)
    day_before_yesterday_datetime = yesterday_datetime - timedelta(days=1)
    d_b_yesterday = str(day_before_yesterday_datetime).split(" ")[0]
    # print(d_b_yesterday)

    y_open_price = float(data["Time Series (Daily)"][yesterday]["1. open"])
    d_b_y_open_price = float(data["Time Series (Daily)"][d_b_yesterday]["1. open"])
    # print(f"Yesterday market open price: {y_open_price}")
    # print(f"Day before yesterday market open price: {d_b_y_open_price}")

    ## STEP 2: Use https://newsapi.org - DONE
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "q": STOCK,
        "from": d_b_yesterday,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
        "language": 'en',
        "pageSize": 3,
        "page": 1,
    }

    price_increase = y_open_price - d_b_y_open_price
    percent_price_change_abs = f"{abs(round(price_increase / d_b_y_open_price * 100, 2))}%"

    if abs(price_increase) > d_b_y_open_price * 0.005:
        news_response = requests.get(news_endpoint, news_params)
        # Optional: Format the SMS message like this: - DONE
        if price_increase > 0:
            sign = f"🔺"
        else:
            sign = f"🔻"
        for article in news_response.json()["articles"]:
            print(f"{STOCK}: {percent_price_change_abs}")
            print(f"Headline: {article["title"]}")
            print(f"Brief: {article["description"]}\n")

            ## STEP 3: Send a message with the percentage change and each article's title and description
            message = f"{STOCK}: {sign}\nHeadline: {article["title"]}\nBrief: {article["description"]}\n\n"
            send_email(ADDR_TO, message)



def send_email(to_addrs: str, message: str):
    mime_message = MIMEText(message, _charset="utf-8").as_string()
    with smtplib.SMTP(mail_host, port=mail_port) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=to_addrs,
            msg=mime_message
        )


if __name__ == "__main__":
    collect_stock_data()
