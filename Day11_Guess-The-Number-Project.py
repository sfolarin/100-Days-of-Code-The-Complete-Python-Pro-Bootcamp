#Number Guessing Game Objectives:
import numpy as np
import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print("Welcom to guessing game")
print("I am thinking of a number between 1 and 100")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def difficulty_level():
  level = input('You want to play easy or hard: ').lower()
  if level =='easy':
    return EASY_LEVEL_TURNS
  elif level == 'hard':
    return HARD_LEVEL_TURNS

def comparison(user, actual_answers, count):
    
      if user < actual_answers:
        print("Too low")
        return count-1
      
      elif user > actual_answers:
        print("Too High")
        return count-1
      
      elif user == actual_answers:
        print("You Got it, The actual answer is {}".format(actual_answers))
        return count-1

    

def game():
 # print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  actual_answers = random.randint(1, 100)
  print(f"Pssst, the correct answer is {actual_answers}") 

  turns = difficulty_level()
  #Repeat the guessing functionality if they get it wrong.
  user = 0
  while user != actual_answers:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    user = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = comparison(user, actual_answers, turns)
  
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif user != actual_answers:
      print("Guess again.")


game()