# from flask import Flask
# app = Flask(__name__)


# print(__name__)

# def make_bold(func):
#     """
#     Decorator that makes the text bold.
#     """
#     def wrapper(*args, **kwargs):

#         result = f"<b>{func(*args, **kwargs)}</b>"
                
#         # Return the bold text
#         return result
    
#     return wrapper

# def make_emphasis(func):
#     """
#     Decorator that makes the emphasis text.
#     """
#     def wrapper(*args, **kwargs):

#         result = f"<em>{func(*args, **kwargs)}</em>"
                
#         # Return the emphasis text
#         return result
    
#     return wrapper

# def make_underlined(func):
#     """
#     Decorator that makes the underlined text.
#     """
#     def wrapper(*args, **kwargs):

#         result = f"<u>{func(*args, **kwargs)}</u>"
                
#         # Return the underlined text
#         return result
    
#     return wrapper

# @app.route('/')
# def hello_world():
#      return '<h1 style="text-align: center">Hello, World!</h1>'\
#             '<p>This is a paragraph.</p>'\
#             '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2txcmZwZzF0Z3pncDI5ZjZ1Z3RtdG1wa3dzZmlkYmltMDRyNHQ2diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/42YlR8u9gV5Cw/giphy.gif" alt="funny monkeys gif" width="250" height="250">'

# @app.route('/bye')
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#      return "Bye!"   


# @app.route('/username/<name>/<int:number>')
# def greet(name, number):
#      return f"<h1>Hello there, {name}, you are {number} years old!</h1>"

# if __name__ == "__main__":
#      app.run(debug=True)

""" Python Advanced Decorators """

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
    
# def is_user_authenticataed(function):
#     def wrapper(*args,**kwargs):
#          if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
    
# @is_user_authenticataed
# def create_blog_post(self):
#         print(f"This is {self.name}'s new blog post.")

# user = User("Naren Bagavathy")
# user.is_logged_in = True
# create_blog_post(user)



"""


Advanced Decorators

Create a logging_decorator() which is going to print the name of the function that was called, 

the arguments it was given and finally the returned output: 

You called a_function(1,2,3) 
It returned: 6 
The value 6 is the return value of the function.



Don't change the body of a_function. 



IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise. 




"""

# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        result = function(*args)
        print(f"You called {function.__name__}{args}")
        print(f"It returnded: {result}")
        return result
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)