## ********Day 54 Start**********
## Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)

# result = calculate(add, 2, 3)
# print(result)

##Functions can be nested in other functions

# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     nested_function()

# outer_function()

## Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     return nested_function

# inner_function = outer_function()
# inner_function()


## Simple Python Decorator Functions
# import time

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print("Hello")

# #With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")

# #Without the @ syntactic sugar
# def say_greeting():
#     print("How are you?")
# decorated_function = delay_decorator(say_greeting)
# decorated_function()

import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

# Write your code below 👇
def speed_calc_decorator(func):
    """
    Decorator that measures and prints the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        # Record start time
        start_time = time.time()
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        # Record end time
        end_time = time.time()
        
        # Calculate execution time
        execution_time = end_time - start_time
        
        # Print the execution time
        print(f"{func.__name__} run speed: {execution_time}s")
        
        # Return the original function's result
        return result
    
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator       
def slow_function():
    for i in range(10000000):
        i * i

# Test the decorated functions
fast_function()
slow_function()
"""

Create Your Own Python Decorator

Objective Create your own decorator function to measure the amount of seconds that a function takes to execute.

Expected Output

1695050908.1985211
fast_function run speed: 0.33974480628967285s
slow_function run speed: 2.9590742588043213s
   

Calculating Time   

time.time() will return the current time in seconds since January 1, 1970, 00:00:00.



Try running the starting code to see the current time printed. 



If you run the code after a while, you'll see a new time printed.

e.g. first run:  1598524371.736911 

second run:  1598524436.357875 

The time difference = second run - first run  64.62096405029297  (approx 1 minute) 



Given the above information, complete the code exercise by printing out the time it takes to
 run the fast_function() vs the slow_function().



You will need to complete the speed_calc_decorator() function. 

"""