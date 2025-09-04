# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()



# import turtle => Here import is the keyword turtle is the module name

# from turtle import Turtle => from is the keyword ; turtle is the module name;
#   import is the keyword; Turtle is the thing in module

# from turtle import * => here * means import everything

# import turtle as t =>  import is the keyword : turtle is the module name ; 
# keyword is as ; and t is the alias name


# for _ in range(4):
#     timmy_the_turtle.left(90)
#     timmy_the_turtle.forward(100)


# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('red')




# screen = Screen()
# screen.exitonclick()


# import heroes

# print(heroes.gen())

# import turtle as t

# tim = t.Turtle()

# for _ in range(15):
#     tim.forward(10)
#     tim.penup() # Move forward without drawing
#     tim.forward(10)
#     tim.pendown()


# from turtle import Turtle
# import random
# turtleObject = Turtle()

# colours = ["medium aquamarine", "DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]


# # TODO - 1 - Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

# # Angle of a Triagle => 360 / num_of_sides  = 120
# # square =>


# def draw_shape(no_of_sides):
#     num_of_sides=no_of_sides
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#        turtleObject.forward(100)
#        turtleObject.right(angle)

# for shape_n_size in range(3,11):
#     turtleObject.color(random.choice(colours))
#     draw_shape(shape_n_size)


# import turtle as t
# import random

# tommy = t.Turtle()
# t.colormode(255)

# #colours = ["CornflowerBlue", "DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

# # Directions => east north west south

# def random_color():
#   """Generates random color"""
#   r = random.randint(0,255)
#   g = random.randint(0,255)
#   b = random.randint(0,255)
#   random_color_tuple =(r,g,b)
#   return random_color_tuple
  

# directions = [0,90,180,270]
# tommy.pensize(15)
# tommy.speed("fastest")

# for _ in range(200):
#   tommy.color(random_color())
#   tommy.forward(30)
#   tommy.setheading(random.choice(directions))

# Tuple is a datatype in python  and it looks like (1,3,8) and list [1,3,8]
# You can't change the values in the tuple just as we do in list. Tuples are immutable



# my_tuple = (1,3,8)
# print(my_tuple[1])

# """ Convert a tuple into a list"""
# list(my_tuple)


# Draw a Spirograph


import turtle as t
import random

tommy = t.Turtle()
t.colormode(255)

#colours = ["CornflowerBlue", "DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

# Directions => east north west south

def random_color():
  """Generates random color"""
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  random_color_tuple =(r,g,b)
  return random_color_tuple

tommy.speed("fastest")
  

def draw_spirograph(size_of_gap):
   for _ in range(int(360 / size_of_gap)):
     tommy.color(random_color())
     tommy.circle(100)
     tommy.setheading(tommy.heading() + size_of_gap)

draw_spirograph(5)

screen =  t.Screen()
screen.exitonclick()


