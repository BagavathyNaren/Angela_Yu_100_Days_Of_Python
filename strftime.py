import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


"""

https://www.w3schools.com/python/python_datetime.asp


In the context of the strftime() method

 (which is used with datetime objects in many programming languages like Python, PHP, etc.),
  
    %B is a format code that stands for the full month name.

Here's what it means and how it works:

%B: When you use this format code, the strftime() method will replace it with the complete,

 un-abbreviated name of the month.

Example:

If you have a datetime object representing:

January 15, 2024, %B would output "January".

July 28, 2025, %B would output "July".

December 1, 2023, %B would output "December".

It's one of many format codes available to customize how date and time information is presented as a string. 

Other common ones include:

%b: Abbreviated month name (e.g., "Jan", "Jul", "Dec")

%m: Month as a zero-padded decimal number (e.g., "01", "07", "12")

%Y: Full year with century (e.g., "2024")

%y: Year without century (e.g., "24")

%d: Day of the month as a zero-padded decimal (e.g., "01", "28")

%A: Full weekday name (e.g., "Monday", "Sunday")

%a: Abbreviated weekday name (e.g., "Mon", "Sun")


"""