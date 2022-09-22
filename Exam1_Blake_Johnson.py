# """
# BLake Johnson
# 9/22/2022
# """
# # Question 1
# # A. This code does not work because in line 8 there's a space between 'input' and the parentheses
# name = input("Please enter your name: ")
# age = input ("Please enter your age: ")

# random_number = 10/(age%23)

# # B. This code does not work because 'number' is not defined
# while number < 100:
#     print(number)

# # C. This one works
# number = 5

# if number < 3:
#     print("Less")
# elif number > 3:
#     print("greater")
# else:
#     print("SAME")

# # D. Improper indentation
# for i in range(1,10):
# print(i)

# # E. This one works
# user_number = 0
# while user_number != 5:
#     user_number = input("Please enter a number:")

# Question #2
# A. Milk - $2.00
# B. Eggs - $1.50
# C. Bacon - $3.00
milk = 0
eggs = 0
bacon = 0
costMilk = 2.00
costEggs = 1.50
costBacon = 3.00
total = 0
shopping = True
while shopping == True: # checks to see if they are done shopping
    item = str(input("Please add one item at a time to your cart, press enter to finish shopping: "))
    if item == 'milk': # checks what item is and adds the cost to total and counts the amount
        total += costMilk
        milk += 1
    elif item == 'eggs':
        total += costEggs
        eggs += 1
    elif item == 'bacon':
        total += costBacon
        bacon += 1
    elif item == '':
        shopping = False
    else:
        print("We do not sell that item. Sorry.")
total *= 1.11 # adds tax to the total
print("You bought", milk, "milk(s),", eggs, "eggs, and", bacon, "bacon")
print("Your total is $" + str(total))

# Question 3
def phoneNumber():
    number = str(input("Enter your phone number: "))
    formated = '('
    formated += number[:3]
    formated += ') '
    formated += number[3:6]
    formated += '-'
    formated += number[6:]
    print(formated)
phoneNumber()

# Question 4
from random import randint


def divisor():
    count = 0
    div = 60 # sets the divisor
    while count != 10:
        num = randint(1,60)
        if num % div == 0 and num % 2 == 0 and num >= 15:
            count += 1
            print("I generated the number", str(num) + ", randomly" )
        else:
            pass
divisor()