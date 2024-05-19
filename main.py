#Number Guessing Game Objectives:
from random import randint
from logo import art
Easy_level_turns = 10
Hard_level_turns = 5
def check_answer(guess, answer,turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
      print("Too low")
      return turns - 1

  else:
   print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return Easy_level_turns
  else:
    return  Hard_level_turns
def game():
 print(art)
 print("welcome to the number Guessing Game")
print("I am thinking of a number between 1 and 100")
answer = randint(1,100)
guess = 0 
while guess != answer:
  print(f"You have {turns} attempts remaining to guess the number.")
 guess = int(input("Make a guess: "))
check_answer(guess,answer,turns)
if turns == 0:
  print("You've run out of guesses, you lose.")
  return
turns = set_difficulty()
game()




  
  

  

 