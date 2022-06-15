logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
  return n1+n2

def substract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2


operation = {}
operation['+'] = add
operation['-'] = substract
operation['*'] = multiply
operation['/'] = divide


def calculator():

  num1 = float(input("what's the first number:   "))
  
  stop_calculation = False
  
  while not stop_calculation:
    user_choice = input('pick an operation +/*- ' )
  
    num2 = float(input("what's the next number: "))
  
    for key,value in operation.items():
      if key == user_choice:
        function = operation[key]
        answer = function(num1,num2)
        print(f"{num1} {key} {num2} = {answer}")
  
    quit = input('Enter y to continue or n to start a new calculation: ')
    if quit == 'n':
      stop_calculation = True
      calculator()
    elif quit == 'y':
      num1 = answer
      stop_calculation = False
    
    

  
calculator()  



