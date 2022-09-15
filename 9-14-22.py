
# name = "Blake"
# number = 2
# distance = 1.2
# finished = True

# print("Blake")
# print(name)



# if number > 10:
#     print("This is a thing")
# elif number < 10:
#     print("this thing")
# else:
#     print("This is not a thing")

# if number > 10:
#     print("Lol")
# if number < 10:
#     print("naa")



# while number <= 10:
#     print(number)
#     number += 1



# # Write a script that keeps asking the user for a number and check if the number is even or odd. Let the user know what it is. If they enter the number 0 stop asking for numbers.

# user = int(input("Please Enter your number: "))
# while user != 0:
#     if user % 2 == 0:
#         print("This number is even")
#     elif user % 2 != 0:
#         print("This number is odd")
#     else:
#         print("This entry is not valid")
#     user = int(input("Please pick another number, or enter '0' to stop: "))
# Create a script that asks the user for their name and income. let the user know how much money they would have if they don't spend any money in 20 years/

# Hey _name_, you make _income_ a year!
# This is how much money you would have in 20 years
# 40000 year 1
# 80000 year 2
# ...... year 20

# name = str(input("What's your name: "))
# income = int(input("How much do you make in a year: "))
# years = 0
# money = 0
# print("Hey", name, "you make", income, "a Year!")
# print("This is how much money you would have in 20 years")
# while years != 20:
#     years += 1
#     money += income
#     print("$" + str(money), "year", years)

# let the user know how many years until they save $10,000

name = str(input("What's your name: "))
income = int(input("How much do you make in a year: "))
years = 0
money = 0
print("Hey", name, "you make", income, "a Year!")
while money < 10000:
    years += 1
    money += income
    print("Hey", name, "it will take you", years, "years to save $10,000")