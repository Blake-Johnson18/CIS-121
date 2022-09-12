# Blake J.
# Exam 1

# Part 1

# A. True
# B. False kjsdhfkjsdfh


# Promlem2


# name = "Blake"
# number = 12
# distance = 1.23

# if name == "Blake":
#     print("Hello Blake")
# elif name == "Bob":
#     pinrt("Hello Bob")
# else:
#     print("Hello", name)

# winner = 0
# tries = 0

# while winner != 1 and tries < 3:
    









# Write a small script that asks the user for a number between 35-1000. When the user enters the number your program should print the numbers from that x number to 100.

# But if the number goes over 100. just print the 100 by itself.

from pickle import FALSE, TRUE


num = int(input("Enter a number between 35 & 1000: "))


if 35 <= num <=1000:
    while 35 <= num <= 99:
        even = num % 2
        if even == 0:
            print(num)
            num += 1
        else:
            num +=1
    while num >= 100:
        print(100)
        break
else:
    print("The number needs to be between 35 & 1000")

# Boolean
winner = True
loser = False

