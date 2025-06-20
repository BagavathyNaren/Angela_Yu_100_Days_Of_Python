"""

For & While Loops

IF / ELSE

Lists

Strings

Range 

Modules


"""
import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

random_index_of_word = random.randint(0,len(word_list)-1)
chosen_word = word_list[random_index_of_word]
print("Word chosen from the input list: \n"+chosen_word)

placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: "+placeholder)

no_of_lives = 6
correct_letters = []
game_over = False

while not game_over:
    
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")   
    
    display = "" 

    for letter in chosen_word:
       if letter == guess:
          display  += letter
          correct_letters.append(guess)
       elif letter in correct_letters:
          display += letter     
       else:
          display += "_"
    
    print(display)

    if guess not in chosen_word:
          no_of_lives -= 1
          print(f'You guessed {guess}, that\'s not in the word. You lose a life')
          if no_of_lives == 0:
              game_over = True
              print(f"****************************************IT WAS {chosen_word}! YOU LOSE*****************************************")
          
         
    if "_" not in display:
       game_over = True        
       print("*************************************YOU WIN******************************************")

    print(stages[no_of_lives])
    print(f"***************************************************{no_of_lives}/6 LIVES LEFT*********************************************************") 

