# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# screen.listen()
# screen.onkey(key="space",fun=move_forwards)
# screen.exitonclick()


"""

Higher Order Function is a function that can work with other functions

def add(n1,n2):
    return n1 + n2 
    
def subtract(n1,n2):
    return n1 - n2 
    
def multiply(n1,n2):
    return n1 * n2 
    
def divide(n1,n2):
    return n1 / n2 
    
def calculator(n1,n2,func):
    return func(n1,n2) 

result = calculator(2,2,multiply)
print(result)

calculator() is the higher order function
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")

screen.exitonclick()