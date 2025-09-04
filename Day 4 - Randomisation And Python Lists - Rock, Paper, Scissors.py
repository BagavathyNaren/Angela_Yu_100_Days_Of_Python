import random
#import my_module


# random_integer_from_one_to_hundred = random.randint(1, 100)
# print(random_integer_from_one_to_hundred)

#print(f'my_module favorite number: {my_module.my_fav_number}')

# random_floating_number = random.random()
# print(f'Random floating number: {random_floating_number}')


# random_floating_number_from_zero_to_ten = random.random() * 10
# print(f'Random floating number from zero to 10: {random_floating_number_from_zero_to_ten}')

# flip_coin_random_number = random.randint(0, 1)
# if flip_coin_random_number == 0:
#     print("Heads")
# else:
#     print("Tails")

# Creating a list in python
# fruits = ["Cherry","Apple","Pear"]

# print(fruits[2])

# states_of_america = [
#     "Alabama", "Alaska", "Arizona", "Arkansas", "California",
#     "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
#     "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
#     "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
#     "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
#     "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
#     "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
#     "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
#     "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
#     "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
# ]

# print(states_of_america)

# states_of_america.append("NarenLand")

# arizona_state = states_of_america[2]

# print(f"Get arizona state from the states_of_america list: {arizona_state}")

# print(states_of_america)

# friends = ["Alice","Bob","Charlie","David","Emanuel"]
# no_of_friends = len(friends)
# random_friend_name = random.randint(0,(no_of_friends-1))
# print("Random friend name: "+ friends[random_friend_name])

# print("Random name of a friend: "+random.choice(friends))

# fruits = ["Avocados","Sweet corn","Pineapples","Papayas","Mangoes","Honeydew melons","Kiwis","Cantaloupes"]

# vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes","Cabbages",
# "Onions","Asparagus","Eggplants","Broccoli","Cauliflower"]

# fruits_vegetables = [fruits,vegetables]

# print(fruits_vegetables)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 


# print(dirty_dozen)


# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])
# print(dirty_dozen[1][1])

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_choice  = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices  = [rock,paper,scissors]

if (player_choice == 0 or player_choice == 1 or player_choice == 2):
    print("You entered the valid input.")
    computer_choice = random.randint(0,2)
    if(player_choice == computer_choice):
        print(choices[player_choice])
        print("Computer Chose:")
        print(choices[computer_choice])
        print("It's a draw")       
    elif(player_choice == 0 and computer_choice == 2):
        print(choices[player_choice])
        print("Computer Chose:")
        print(choices[computer_choice])
        print("You won the game")         
    elif(player_choice == 2 and computer_choice == 1):
        print(choices[player_choice])
        print("Computer Chose:")
        print(choices[computer_choice])
        print("You won the game")    
    elif(player_choice == 1 and computer_choice == 0):
        print(choices[player_choice])
        print("Computer Chose:")
        print(choices[computer_choice])
        print("You won the game")
    else:
        print(choices[player_choice])
        print("Computer Chose:")
        print(choices[computer_choice])
        print("You lost the game")            
else:
    print("Invalid Input")
