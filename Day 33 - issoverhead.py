import requests
from datetime import datetime, time
import smtplib


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get("EMAIL")
my_password = os.environ.get("PASSWORD")

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night_time():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now > = sunset and time_now < = sunrise:
        # It's dark
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night_time():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs="narenbagavathye5@gmail.com",
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
        )
    else:
        print("The ISS is not overhead or it's not night.")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



