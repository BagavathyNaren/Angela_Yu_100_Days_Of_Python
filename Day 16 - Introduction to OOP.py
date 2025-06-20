# import another_module

# print(another_module.another_variable)
# from turtle import Turtle, Screen

# timmy = Turtle() # timmy is the object and Turtle() is the class

# print(timmy)
# timmy.shape('turtle')
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()

# print(my_screen.canvheight)

# my_screen.exitonclick()


"""
PrettyTable 0.7.2

pip install PrettyTable

A simple python library for easily displaying tabular data in a visually appealing ASCII table format.

"""

# from prettytable import PrettyTable

# table = PrettyTable()

# table.field_names =["Pokemon Name","Type"]
# table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Charmander","Fire"]
#     ] 
# )
# table.align["Pokemon Name"] = "l"
# table.align["Type"] = "l"
# print(table)