import random
from replit import clear
from art import logo
def deal_card():
  """ returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def calculate_score(cards):
  """takes a list of cards and return their sum"""
  if sum(cards) == 21 and len(cards)==2:
    return 0
  return sum( cards)
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare_score(user_score,computer_score):
  if user_score == computer_score:
    return "Draw 👻"
  elif computer_score == 0:
    return "Lose,your opponent has a blackjack"
  elif user_score == 0:
    return " win with a blackjack 😉"
  elif user_score > 21:
    return " opponent went over.you lose"
  elif computer_score > 21:
    return"opponent went over, you win"
  elif user_score > computer_score:
    return " you win"
  else:
    return "you lose"
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"your cards: { user_cards},current score : {user_score}")
    print(f"computer first card : {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      check_userdeal = input("Type 'y' to get another card or Type 'n' to pass: ")
    if check_userdeal == "y":
          user_cards.append(deal_card())
    else:
     is_game_over = True
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score (computer_cards)
  print(compare_score(user_score,computer_score))   
while input("Do you want to play the Game again ? Type 'y' or 'n' : ") == "y":
  clear()
  play_game()