# import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get("EMAIL")
my_password = os.environ.get("PASSWORD")

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password) # type: ignore
#     connection.sendmail(from_addr=my_email, # type: ignore
#                          to_addrs=my_email, # type: ignore
#                          msg="Subject:Happy Birthday!\n\nWishing you a day filled with love and cheer!") 

# import datetime as dt
# from zoneinfo import ZoneInfo

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# print(now)
# print(year)
# print(month)
# print(day_of_week)

# date_of_birth = dt.datetime(year= 1995, month=6,day=21, hour=17, minute=15, tzinfo=ZoneInfo("Asia/Kolkata") )
# print(date_of_birth)
# print(date_of_birth.strftime('%Y-%m-%d %I:%M %p %Z'))  # Format with AM/PM and timezone name

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        random_quote = random.choice(all_quotes)

    print(random_quote)
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                         to_addrs=my_email,
                         msg=f"Subject:Sunday Motivation\n\n{random_quote}")
    connection.close()
