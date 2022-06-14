from replit import clear
import numpy as np
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# Ask for name input
print(logo)
bids = {}
bidding_finished= False

while not bidding_finished:

  Name = input("Please enter your name: \n")
  # Ask for Bid Price
  Bid_Price = int(input("Enter your bid price: $"))
  # Add name and bid into a dictionary as key and value
  
  
  bids[Name] = Bid_Price
 
  # Ask if there other users who want to bid
  New_User = input('Any user still want to bid: Type Yes or No? ').lower()
  if New_User == 'no':
    bidding_finished = True
  elif New_User =='yes':
    clear()
    

highest_bidder = 0
for key,value in bids.items():
  if value > highest_bidder:
    highest_bidder = value
    winner = key
print(f"The highest bidder is {highest_bidder} and the winner is {winner}")
    




