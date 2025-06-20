# with open("weather_data.csv") as csv_file:
#     data = csv_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))

#print(data)
# print(type(data["temp"]))

# data_dict = data.to_dict()

# print(data_dict)

# temperature_list = data["temp"].to_list()
# print(temperature_list)
# print(len(temperature_list))

# Sum = sum(temperature_list)

# Average_Temperature = Sum / len(temperature_list)

# print(round(Average_Temperature,2))

# print(data["temp"].mean())

# print(data["temp"].max())

# print(data["condition"])

# print(data.day)

# Get data in row

# print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])

# Monday_Temperature =data["temp"][data.day == 'Monday']

# print(Monday_Temperature)

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32 
# print(monday_temp_F)


# Create a DataFrame from scratch

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Pandas_Dictionary_DataFrame.csv")

"""

The two primary data structures of pandas, Series [1-dimensional] and DataFrame [2-dimensional]],
handle the vast majority of typical use cases in finance, statistics, social science, and many areas
of engineering.

"""