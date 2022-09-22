



# number = 1


# # # for loop



#         ######
# for number in range(1,11):
#     print(number)


# for number in range(1,11):
#     if number % 2 == 0:
#         print(number)



# def askUserForName():
#     name = input("Please enter your name:")
#     return name



# name = askUserForName()
# print(name)
# name2 = askUserForName()
# print(name2)
# #   #   # Create a function that ask the user for their age. Then use that value to print out the next 20 years (use a for loop)

# def askUserForAge():
#     age = int(input("Please enter your age:"))
#     return age

# age = askUserForAge()

# for i in range(21):
#     print(age)
#     age += 1



# name = "Blake"

# ## string manipulation
# print(name[0:3])



# for letter in name:
#     print(letter)

import abc
from ast import Num
from tkinter.messagebox import YES


def userNum():
    num = int(input("Enter a number:"))
    return num

def problem1():
    Sum = 0
    for x in range(6):
        num = userNum()
        Sum += num
    for y in range(Sum,2001):
        if y % 2 != 0:
            print(y)
        if 96 % y == 0:
            print("Found One!")

def problem2():
    cost = 3
    DVDs = int(input("How many DVDs did you buy: "))
    total = cost * DVDs
    if total >= 30:
        total *= .9
        print(total)
    elif total >= 50:
        total *= .8
        print(total)
    else:
        print(total)

# problem2()

def problem3():
    for a in range(1,6):
        for b in range(1,a):
            print(b,end=" ")
        print(" ")



problem3()