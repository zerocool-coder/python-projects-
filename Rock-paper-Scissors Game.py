import random
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
art_Images = [rock,paper,scissors]
choice = int(input("what do you choose?\n Type 0 for Rock,1 for paper or 2 for Scissors\n"))
if choice >=3 or choice < 0 :  
  print("you typed an invalid number, you lose!")
else :
  print(art_Images[choice])
pc_choice = random.randint(0,2)
print("computer chose:"+art_Images[pc_choice])
if choice == 0 and pc_choice == 2:  
  print("you win")
elif pc_choice == 0 and choice == 2:  
  print("you lose!")
elif pc_choice > choice :
  print("computer wins!")
elif choice > pc_choice  :
  print("you win the Game!")
elif  pc_choice == choice:
  print("it's a draw")

