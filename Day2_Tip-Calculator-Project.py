#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip Calculator")
bill = float(input('What was the total bill? $'))
tip = float(input('How much tip would you like to give? '))
split_bill = float(input('How many people to split the bill ?'))

total_tip_amount = (tip+ 100)/100


bill_per_person = round((bill/split_bill)*(total_tip_amount),2)

print(f"Each person should pay: %.2f" % bill_per_person )


