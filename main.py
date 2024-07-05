
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """Returns random card from deck"""
  card = random.choice(cards)
  return card 

def blackjack():
  game_over = True

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    blackjack()
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, dealer_score, user_cards, dealer_cards):
  if user_score > 21 and dealer_score > 21:
    return "Bust! You lose."
  elif user_score == dealer_score:
    return "It is a Draw"
  elif dealer_score == 21 and len(dealer_cards) == 2:
    return "Dealer has Blackjack. You lose."
  elif user_score == 21 and len(user_cards) == 2:
    return "You win with a Blackjack!"
  elif user_score > 21:
    return "Bust! You lose."
  elif dealer_score > 21:
    return "Dealer bust! You win!"
  elif user_score > dealer_score:
    return "You win!" 
  else:
    return "You lose."

def play_game():
  print(logo)

  user_cards = []
  dealer_cards = []
  
  for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
  
  
  game_over = False
  while not game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f" Your cards: {user_cards}, Current Score: {user_score}")
    print(f" Dealer's First Card: {dealer_cards[0]}")
    if user_score == 21 or dealer_score == 21 or user_score > 21:
      game_over = True
    else:
      while True:
        deal_extra = input("Type 'y' to hit. Type 'n' to stand: ")
        if deal_extra == "y":
          user_cards.append(deal_card())
          break
        elif deal_extra == "n":
          game_over = True
          break
        else:
          print("Invalid response.")
  
  while dealer_score != 0 and dealer_score < 17 and user_score <= 21:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
  print(compare(user_score, dealer_score, user_cards, dealer_cards))

while True:
  if input("Type 'y' to start a new game: ") == "y":
      clear()
      play_game()
  else:
      print("Invalid response.")
    





  

  
