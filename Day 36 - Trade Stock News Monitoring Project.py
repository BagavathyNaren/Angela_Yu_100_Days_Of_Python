import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from types import NoneType
import requests
from dotenv import load_dotenv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_ACCOUNT_SID = "AC4162600d85bbb14581b6ce48a3505b09"
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")  
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")
# ALPHA_VANTAGE_STOCK_API_KEY = os.environ.get("ALPHA_VANTAGE_STOCK_API_KEY")
# ALPHA_VANTAGE_STOCK_API_KEY = str(ALPHA_VANTAGE_STOCK_API_KEY)

print("=== DEBUG INFO ===")
print(f"SID: {repr(TWILIO_ACCOUNT_SID)}")
print(f"Token: {repr(TWILIO_AUTH_TOKEN)}")
print(f"SID type: {type(TWILIO_ACCOUNT_SID)}")
print(f"Token type: {type(TWILIO_AUTH_TOKEN)}")
print("================")

ALPHA_VANTAGE_STOCK_API_KEY = "8FGDPQ62YFQP6BHX"
NEWS_API_KEY = "ac71d3a3eb2d42b183fed5cace51e56e"


STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, verify=False, params=STOCK_PARAMS)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference = round((difference / float(day_before_yesterday_closing_price)) * 100)

if abs(percentage_difference) > 1:
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, verify=False, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
          truncated_article = article[:157] + "..." if len(article) > 160 else article

          print(f"Original length: {len(article)}")
          print(f"Truncated length: {len(truncated_article)}")
          try:
              message = client.messages.create(
              to=MY_PHONE_NUMBER,  # Fixed: removed dash
              from_=TWILIO_PHONE_NUMBER,
              body=truncated_article
              )
              print(f"Message sent! SID: {message.sid}")
          except TwilioRestException as e:
             print(f"Twilio Error: {e.status} - {e.code} - {e.msg}")