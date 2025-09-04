import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",verify=False, params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
#print(sunrise.split("T")[1].split(":")[0])




print(sunrise)
print(sunset)


time_now = datetime.now()
print(time_now)
print(time_now.hour)