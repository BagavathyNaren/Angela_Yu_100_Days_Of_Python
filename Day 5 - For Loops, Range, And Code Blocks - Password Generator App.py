#import random
# fruits = ["Apple","Peach", "Pear"]
# for fruit in fruits:
#     print(f"Current fruit is: {fruit}")
#     print(f'{fruit} pie')

# student_scores = [180, 180, 124, 165, 173, 189, 169, 146]

# total_score = sum(student_scores)

# print("Sum using sum() function in python: "+ str(total_score))
# print("Max score using max() function in python: "+ str(max(student_scores)))

# sum = 0
# for student_score in student_scores:
#     sum += student_score

# print("Sum using For Each Loop: "+ str(sum))


# max_score = 0
# for studentScore in student_scores:
#     if (studentScore >= max_score):
#         max_score = studentScore

# print("Maximum score using for each loop in python: "+ str(max_score))

# print("Minimum score using min() function in python: "+ str(min(student_scores)))

# min_score = max(student_scores)
# for student_Score in student_scores:
#     if (student_Score <= min_score):
#         min_score = student_Score
# print("Minimum score using for each loop in python: "+ str(min_score))

# # range() function with for loop

# for number in range(1,9):
#     print(f'Print numbers from 1 to 8 sequentially: {number}')


# for number in range(1,9, 7):
#     print(f'Print numbers from 1 to 8 sequentially with adding 7: {number}')

# Gauss challenge - Print the total of first 100 numbers. 1 and 100 are both inclusive
# sum = 0
# for number in range(1,101):
#     sum += number
# print("Gauss challenge: The total of the first hundred numbers is "+str(sum))

# Fizz Buzz Game
# for number in range(1,101):
#     if(number % 15 == 0):
#         print("FizzBuzz")
#     elif(number % 3 == 0):
#         print("Fizz")
#     elif(number % 5 == 0):
#         print("Buzz")
#     else:
#         print(number)

# PyPassword Generator 

# Easy Level

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# user_letter_input = input("How many letters would you like in your password? \n")

# if user_letter_input.strip() == "":
#     print("Input letter is empty.")
# else:
#     try:
#         letter_input = int(user_letter_input)
#         if letter_input <= 0:
#             print("Please enter a positive number.")
#         else:
#             print(f"You chose {letter_input} letters for your password.")
#             random_letters = ""
#             for letterCount in range(1,letter_input+1):
#                 random_letters += random.choice(letters)
#             print("The random letters are: "+random_letters)
#             user_symbol_input = input("How many symbols would you like? \n")
#             if user_symbol_input.strip() == "":
#                     print("Input symbol is empty.")
#             else:
#                  try:
#                       symbol_input = int(user_symbol_input)
#                       if symbol_input <= 0:
#                             print("Please enter a positive number.")
#                       else:
#                             print(f"You chose {symbol_input} symbols for your password.")
#                             random_symbols = ""
#                             for symbolCount in range(1,symbol_input+1):
#                                  random_symbols += random.choice(symbols)
#                                  print("The random symbols are: "+random_symbols)
#                  except ValueError:
#                          print("Invalid symbol input. Please enter a valid number.")
#             user_number_input = input("How many numbers would you like? \n")
#             if user_number_input.strip() == "":
#                     print("Input number is empty.")
#             else:
#                  try:
#                       number_input = int(user_number_input)
#                       if number_input <= 0:
#                             print("Please enter a positive number.")
#                       else:
#                             print(f"You chose {number_input} numbers for your password.")
#                             random_numbers = ""
#                             for numberCount in range(1,number_input+1):
#                                  random_numbers += random.choice(numbers)
#                                  print("The random numbers are: "+random_numbers)
#                       password = random_letters+random_symbols+random_numbers
#                       print(f"Your password is {password}")
#                  except ValueError:
#                          print("Invalid number input. Please enter a valid number.")          
#     except ValueError:
#         print("Invalid number input. Please enter a valid number.")


# Hard Level


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")



