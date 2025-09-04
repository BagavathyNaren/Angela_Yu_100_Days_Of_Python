# enemies = 1

# def increare_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")

# increare_enemies()
# print(f'enemies outside function: {enemies}')

# def is_prime(num):
#     if (num > 1):
#         for i in range(2,num):
#             if (num % i == 0):
#                 print(str(i) + " times " + str(num//i) + " is "+ str(num))
#                 return False
#                 break
#         else:
#             return True
#     elif(num == 1):
#         return False
    
# print(is_prime(75))  


# enemies = 1

# def increare_enemies():
#     global enemies
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")

# increare_enemies()
# print(f'enemies outside function: {enemies}')

# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
 
# a_function(10)
# print(a_variable)

# def bar():
#     my_variable = 9
 
#     if 16 > 9:
#       my_variable = 16
 
#     print(my_variable)
 
# bar()
import random

from Number_Guessing_Game_Art import logo



EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
   
 
   
"""    
    
    # Too high.
    # Guess again.
    # You have 3 attempts remaining to guess the number.
    # Make a guess: 
    # You've run out of guesses. Refresh the page to run again.
    
    # Make a guess: 
    # You got it! The answer was 16.

      import random

from Number_Guessing_Game_Art import logo

print(logo)



EASY_LEVEL_NO_OF_ATTEMPTS = 10

HARD_LEVEL_NO_OF_ATTEMPTS = 5

print("Welcome to the Number Guessing Game!")
print('I\'m thinking of a number between 1 and 100.')
correct_number = random.randint(1,100)
print(f'The correct number is {correct_number}')

difficulty_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if 'easy' in difficulty_input:

    
    isNumberGuessingGameOn = False

    while not isNumberGuessingGameOn:
            
            print(f'You have {EASY_LEVEL_NO_OF_ATTEMPTS} attempts remaining to guess the number.')

            user_guess_number = int(input("Make a guess: "))
  
            if(user_guess_number < correct_number):
                   print("Too Low")
                   print("Guess again.")
                   EASY_LEVEL_NO_OF_ATTEMPTS -= 1
            elif(user_guess_number > correct_number):
                   print("Too high")
                   print("Guess again.")
                   EASY_LEVEL_NO_OF_ATTEMPTS -= 1
            elif(user_guess_number == correct_number):
                   print(f"You got it! The answer was {correct_number}.")

            if EASY_LEVEL_NO_OF_ATTEMPTS == 0:
                   print("You've run out of guesses. Refresh the page to run again.")
                   isNumberGuessingGameOn = True
            
   

"""