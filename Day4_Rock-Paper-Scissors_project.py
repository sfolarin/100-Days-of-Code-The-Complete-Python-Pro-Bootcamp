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



#Write your code below this line 👇
mylist = [rock, paper, scissors]
Player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n" ))

Player_choice = mylist[Player]
print("User's Choice"+Player_choice)

Computer = random.randint(0,2)

Computer_choice = mylist[Computer]
print("Computer's Choice"+Computer_choice)


if Player >= 3 or Player < 0: 
  print("You typed an invalid number, you lose!") 
elif Player == 0 and Computer == 2:
  print("You win")
elif Computer_choice == 0 and Player_choice == 2:
  print("Computer win")
elif Computer > Player:
  print("You lose")
elif Player > Computer:
  print("You win!")
elif Computer == Player:
  print("It's a draw")
        
