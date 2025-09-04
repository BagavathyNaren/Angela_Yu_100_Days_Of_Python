##################### Extra Hard Starting Project ######################

import pandas
import datetime as dt
import os
import random
from dotenv import load_dotenv
import smtplib

letter_list = [1,2,3]

load_dotenv()

my_email = os.environ.get("EMAIL")
my_password = os.environ.get("PASSWORD")

# 1. Update the birthdays.csv

birthdays = pandas.read_csv("birthdays.csv")
print(birthdays)


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

for index, row in birthdays.iterrows():
    if row["day"] == day and row["month"] == month:
        print(f"Today is {row['name']}'s birthday!")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name 
# from birthdays.csv

        with open(f"letter_templates/letter_{random.choice(letter_list)}.txt") as letter_file:
           letter_contents = letter_file.read()
           new_letter = letter_contents.replace("[NAME]", row["name"])

# 4. Send the letter generated in step 3 to that person's email address.
           with smtplib.SMTP("smtp.gmail.com", 587) as connection:
               connection.starttls()
               connection.login(user=my_email, password=my_password)
               connection.sendmail(
                   from_addr=my_email,
                   to_addrs=row["email"],
                   msg=f"Subject:Happy Birthday!\n\n{new_letter}"
               )





