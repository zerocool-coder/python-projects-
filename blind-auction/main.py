from art import logo
print(logo)
from replit import clear
bids = {}
finished_bid = False
def highest_Bid(bid_record):
  highest_Bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
  if bid_amount > highest_Bid:
     highest_Bid = bid_amount
     winner = bidder
     print(f"The winner is {winner} with a bid of ${highest_Bid}")

while not finished_bid:
  name = input("welcome to secret auction program .\n what is your name?")
  bid = int(input("what is your bid? $"))
  bids[name] = bid
  other = input("are there any other bidders Type yes or No \n")
  if other == "no":
    finished_bid = True
    highest_Bid(bids)
  elif other == "yes":
     clear()

  
  
  
  