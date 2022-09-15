from itertools import count
from random import randint


name = "Blake"
# number = 5
# number2 = 2345.343

# print("Blake was here")
# print(name,number)

number = 1
if number == 10:
    print("This number 10")
elif number > 10:
    print("This number is greater than 10")
else:
    print("That makes no sense")

print("Naaa")


# Create a script that asks the user for their income. If the income is greater than 450000 say "Damn u rich", if they make less say "You got it"

# salary = float(input("What's your salary? ")) # asks for user salary and stores it
# if salary > 450000: # checks user input against our own variable
#     print("Damn you rich")
# elif salary <= 450000:
#     print("You got it")
# else:
#     print("You fucked up")

while number <= 10 or number == 50:
    print(number)
    number = number + 1



# creat a guessing game. Give the user 3 chances, If they git it right print("YAY"). if not make a custom message.

count = 0
number = randint(1,10)
user = int(input("The number is between 1 & 10. What's your guess? "))
while True:
    count += 1
    if user == number:
        print("YAY")
        break
    elif count == 3:
        print("Sorry you ran out of guesses. Better luck next time")
        break
    user = int(input("Sorry try again "))

