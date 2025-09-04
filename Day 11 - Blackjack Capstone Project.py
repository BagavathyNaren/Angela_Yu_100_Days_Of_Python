from BlackJack_Game_Art import logo
import os
import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(u_score,com_score):
     """Compares the user score and the computer score"""
     if u_score > 21 and com_score > 21:
        return "You and computer went over. Both of them are losers  😤"
     if u_score == com_score:
          return "It's a draw. 🙃"
     elif com_score == 0:
          return "You lose because the computer has a blackjack. 😱"
     elif u_score == 0:
          return "You win because you have a blackjack. 😎"
     elif u_score > 21:
          return "You lose because your score is over 21. You lose 😭"
     elif com_score > 21:
          return "Computer lose because computer score is over 21. You lose 😭"
     elif u_score > com_score:
          return "You win because your score is greater than the computer score. 😃"
     else:
          return "Yoe lose 😤"
     
def play_blackjack():
     """ Play the blackjack game"""

     print(logo)
     user_cards = []
     computer_cards = []
     user_score = -1
     computer_score = -1
     isBlackJackGameOver = False

     for _ in range(2):
          user_cards.append(deal_card())
          computer_cards.append(deal_card())


     while not isBlackJackGameOver:
        user_score = calculate_score(user_cards)
        computer_score  = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isBlackJackGameOver = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                isBlackJackGameOver = True

     while computer_score != 0  and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

     print(f"Your final hand: {user_cards}, final score: {user_score}")
     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
     print(compare_score(user_score,computer_score))

while input("Do you want to play the game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    play_blackjack()


     
