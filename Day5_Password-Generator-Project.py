#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def random_char(nr_letters):
       return ''.join(random.choice(letters) for x in range(nr_letters))

random_character = random_char(nr_letters)

def random_numbers(nr_numbers):
       return ''.join(random.choice(numbers) for x in range(nr_numbers))

random_number = random_numbers(nr_numbers)
def random_symbols(nr_symbols):
       return ''.join(random.choice(symbols) for x in range(nr_symbols))

random_symbol = random_symbols(nr_symbols)

password = random_character + random_symbol+random_number #Concatenate
l = list(password) # Split into a list and reshuffle
random.shuffle(l)
randomize_password = ''.join(l)
print(randomize_password)



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P