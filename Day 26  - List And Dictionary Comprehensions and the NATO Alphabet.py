# Without List Comprehension

numbers = [1, 2, 3]
# numbers_list = []
# for number in numbers:
#     number += 1
#     numbers_list.append(number)

# print(numbers_list)

# List Comprehension - Python

# new_list = [number + 1 for number in numbers]
# print(new_list)

# name = "Naren Bagavathy"

# letters_list = [letter for letter in name]
# print(letters_list)


# double_number_list = [number*2 for number in range(1,5)]
# print(double_number_list)


# # Conditional List Comprehension

# names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]

# short_names = [short_name for short_name in names if len(short_name) < 5] 

# print(short_names)


# fancy_names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]

# long_names = [long_name.upper() for long_name in fancy_names if len(long_name) > 5 ] 

# print(long_names)


# # TODO - CHALLENGE 1 

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number * number for number in numbers]
# print(squared_numbers)


# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(number) for number in list_of_strings]
# result = [even_number for even_number in numbers if even_number % 2 == 0]
# print(result)


# # TODO - CHALLENGE 2

# with open("file1.txt") as file_one:
#     number_list_one = [int(number.strip()) for number in file_one.readlines()]

# with open("file2.txt") as file_two:
#     number_list_two = [int(number.strip()) for number in file_two.readlines()]

# print(number_list_one)
# print(number_list_two)
  
# result = [num for num in number_list_one if num in number_list_two]

# print(result)

"""

list

range

string

tuple  are sequences. They have a specific order.


"""


"""         DICTIONARY COMPREHENSION                  """

# import random

# names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]

# students_scores = {student:random.randint(1,100) for student in names}

# print(students_scores)

# passed_students = {student:score for (student, score) in students_scores.items() if int(score) >= 60 }

# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = { word:len(word) for word in sentence.split() if " " not in word }
# print(result)


# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {day:(temperature * 9/5 + 32) for (day, temperature) in weather_c.items()}

# print(weather_f)



#   How to iterate over a Pandas DataFrame  #

student_dict = {
    "student": ["Angela","James","Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries 
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
