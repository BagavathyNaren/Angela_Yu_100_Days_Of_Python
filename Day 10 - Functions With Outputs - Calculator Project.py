# def format_name(f_name,l_name):
#     Formatted_First_Name = f_name.title()
#     Formatted_Last_Name = l_name.title()
#     #Formatted_Full_Name = 
#     return f"{Formatted_First_Name} {Formatted_Last_Name}"


# # output = format_name("Naren","Bagavathy")
# # print(output)

# print(format_name("Naren","Bagavathy"))


# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output = function_2(function_1("hello"))
# print(output)



"""    Leap Year

This is how you work out whether if a particular year is a leap year. 

- on every year that is divisible by 4 with no remainder

- except every year that is evenly divisible by 100 with no remainder 

- unless the year is also divisible by 400 with no remainder   

e.g. The year 2000: 

2000 ÷ 4 = 500 (Leap)  
2000 ÷ 100 = 20 (Not Leap)  
2000 ÷ 400 = 5 (Leap!)  
So the year 2000 is a leap year. 



But the year 2100 is not a leap year because: 

2100 ÷ 4 = 525 (Leap)  
2100 ÷ 100 = 21 (Not Leap)  
2100 ÷ 400 = 5.25 (Not Leap)  


Warning

Your return should be a boolean and match the Example Output format exactly, including spelling and punctuation. 



Example Input 1

2400

Example Return 1

True



Example Input 2

1989

Example Return 2

False





How to test your code and see your output?



Udemy coding exercises do not have a console, so you cannot use the input() function. 

You will need to call your function with hard-coded values like so:



def is_leap_year(year):
  # your code here
 
# Call your function with hard coded values
is_leap_year(2024)


"""
# def is_leap_year(year):
#     """ This function checks whether the given year is a leap year or not """
#     if ( year % 4 == 0 ):
#         if ( year % 100 == 0 ):
#             if ( year % 400 == 0 ):
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
                
# print(is_leap_year.__doc__)   
# print(is_leap_year(2024))


# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))



'''            Calculator Project                       '''
from Calculator_Art import logo
import os

#ADD
def add(n1, n2):
    return n1 + n2

#SUBTRACT
def subtract(n1, n2):
    return n1 - n2

#MULTIPLY
def multiply(n1, n2):
    return n1 * n2

#DIVIDE
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
    
def calculator():

    print(logo)

    first_number = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    isCalculatorOn = False

    while not isCalculatorOn:

        choose_arithmetic_operation = input("Pick an operation: ")
        next_number = int(input("What's the next number?: "))
        answer = operations[choose_arithmetic_operation](first_number, next_number)
        print(f"{first_number} {choose_arithmetic_operation} {next_number} = {answer}")
        continue_calculation_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        
        if "y" in continue_calculation_input:
            first_number = answer
        else:
             isCalculatorOn = False
             os.system('cls')
             calculator()

calculator()

