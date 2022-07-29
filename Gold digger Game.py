import colorama
from colorama import Fore
print('''
_____ ____ _____
  /    /      \    \
/____ /_________\____\
\    \          /    /
   \  \        /  /
      \ \    / /
        \ \/ /
          \/
''')
print("Gold digger Game ")
print("Your mission is to find the Gold box.")
status1= input('you are at the end of a closed road with 2 doors in the end.....Type "Right" or "Left"\n  ').lower()
if status1 == "right":
  status2=input("you will enter inside a mansion full of rooms..which door u want to open?\n  ").lower()
  if status2=="right":
     status3=input('there is a garden infront of u with several doors..type "Right" or "left" to enter').lower()
     if status3 == "right":
      input("Congratulations ...u won..There is a Box  with Gold bricks inside")
     else:
       print(Fore.RED+"u lose...Game over")
  if status2 =="left":
    input(Fore.RED+"u have entered a room full of beasts with no escape...Game over")
elif status1=="left":
      input("you will enter typing room...please wait to save your progress")
else:
  print("press esc to exit")
  
  

  
  
  

