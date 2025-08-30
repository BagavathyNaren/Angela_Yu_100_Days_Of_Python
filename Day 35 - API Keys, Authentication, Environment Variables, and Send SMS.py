import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

weather_parameters = {
    "lat": 8.7333,
    "lon": 77.7,
    "appid": OPEN_WEATHER_API_KEY,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", verify=False,params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["description"])
# print(weather_data["list"][0]["weather"][0]["id"])

#hour_weather_data = [weather_data["list"][i]["weather"][0]["description"] for i in range(4)]

will_rain = False

for hour_weather_data in weather_data["list"]:
    condition_code = hour_weather_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to take an umbrella!",
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )
    print(message.status)
    