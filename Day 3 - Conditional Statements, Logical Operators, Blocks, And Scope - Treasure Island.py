# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# print(10 % 3)

# input_number = int(input("Enter a number: \n"))
# if (input_number % 2 == 0):
#     print(f"{input_number} is even.")
# else:
#     print(f"{input_number} is odd.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if (12 >= age <= 18):
#         print("Please pay $7.")
#     elif (age < 12):
#         print("Please pay $5.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# print(10 % 3)
# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# print(bmi)

# # 🚨 Do not modify the values above
# # Write your code below 👇
# if (18.5 <= bmi < 25):
#     print("normal weight")
# elif (bmi < 18.5):
#     print("underweight")
# elif (bmi >= 25):
#     print("overweight")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if (12 >= age <= 18):
#         bill = 7
#         print("Youth tickets are $7.")
#     elif (age < 12):
#         bill = 5
#         print("Child tickets are $5.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#     want_photo = input("Do you want a photo taken? Y or N: ")
#     if want_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want to add pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want to add extra cheese? Y or N: ")

# small_pizza_cost = 15
# pepperoni_small_cost = 2
# pepperoni_medium_or_large_cost = 3
# medium_pizza_cost = 20
# large_pizza_cost = 25
# extra_cheese_cost = 1

# if(size == "S"):
#      bill = small_pizza_cost
# elif(size == "M"):
#     bill = medium_pizza_cost
# elif(size == "L"):
#     bill = large_pizza_cost
# else:
#     print("Invalid pizza size.")

# if(pepperoni == "Y" and size == "S"):
#         bill += pepperoni_small_cost
# else:
#         bill += pepperoni_medium_or_large_cost

# if(extra_cheese == "Y"):
#     bill += extra_cheese_cost

# print(f"Your final bill is ${bill}")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if (age < 12):
#         bill = 5
#         print("Child tickets are $5.")
#     elif (age <= 18):
#         bill = 7
#         print("Youth tickets are $7.")
#     elif (age <=45 and age <= 55):
#         print("Senior tickets are free.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#     want_photo = input("Do you want a photo taken? Y or N: ")
#     if want_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
""" Fall into a hole. Game Over."""
""" Attacked by trout. Game Over."""
""" Eaten by beasts. Game Over."""
""" Burned by fire. Game Over."""
""" Game Over. """
""" You Win! """
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_one = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right".\n').lower()
if (choice_one == 'left'):
    choice_two = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if(choice_two == 'wait'):
        choice_three = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if(choice_three == "yellow"):
            print("You found the treasure! You Win!")
        elif(choice_three == "red"):
            print("You are burned by fire. Game Over.")
        elif(choice_three == "blue"):
            print("You are eaten by beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")