import requests
from datetime import datetime, timedelta

STOCK = "IBM"
TIME_FRAME = "TIME_SERIES_DAILY"
API_KEY = "demo"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = "b31f71d3a9cf4f2e8bc2ebea16e3dddf"

daily_data_endpoint = "https://www.alphavantage.co/query"


def start_app():
    ## STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday_datetime and the day before yesterday_datetime then print("Get News").
    params = {
        "function": TIME_FRAME,
        "symbol": STOCK,
        "apikey": API_KEY,
    }
    response = requests.get(daily_data_endpoint, params=params)
    response.raise_for_status()
    data = response.json()

    print(data)

    today = datetime.now()
    yesterday_datetime = today - timedelta(days=1)
    yesterday = str(yesterday_datetime).split(" ")[0]
    print(yesterday)
    day_before_yesterday_datetime = yesterday_datetime - timedelta(days=1)
    d_b_yesterday = str(day_before_yesterday_datetime).split(" ")[0]
    print(d_b_yesterday)

    y_open_price = float(data["Time Series (Daily)"][yesterday]["1. open"])
    d_b_y_open_price = float(data["Time Series (Daily)"][d_b_yesterday]["1. open"])
    print(f"Yesterday market open price: {y_open_price}")
    print(f"Day before yesterday market open price: {d_b_y_open_price}")

    news_params = {
        "q": STOCK,
        "from": d_b_yesterday,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }
    news_endpoint = "https://newsapi.org/v2/everything?q=tesla&from=2025-04-08&sortBy=publishedAt&apiKey=b31f71d3a9cf4f2e8bc2ebea16e3dddf"
    news_response = requests.get(news_endpoint, news_params)
    print(news_response.json())
    if d_b_y_open_price - y_open_price > d_b_y_open_price * 0.05:
        print("Get News")

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.


    #Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """


if __name__ == "__main__":
    start_app()
