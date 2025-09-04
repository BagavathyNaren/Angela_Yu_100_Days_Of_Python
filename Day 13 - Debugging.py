# year = int(input("What's your date of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif (year >= 1994):
#     print("You are a Gen Z.")

# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("You've entered an invalid number. Please try again with a numerical respnse such as 15.")
#     age = int(input("How old are you?"))
    
# if (age > 18):
#    print(f"You can drive at age {age}.")

# import random

# import maths

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1,3)
#         new_item = maths.add(new_item,item)
#         b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz(26)


"""
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if ( number % 3 == 0 or number % 5 == 0):
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz(26)



def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = maths.add(new_item,item)
    b_list.append(new_item)
    print(b_list)

"""

