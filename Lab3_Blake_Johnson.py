"""
Your Name: Blake Johnson
Date: 9/8/2022

Description of what this program does
"""
from asyncore import poll3
import sys


taxes = 0.0

Income = float(input("Enter the amount of income you earned in 2021: "))
if Income < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
Status = input("Type m for married and s for single: ") # Takes in the Marital Status of the Individual


#Ensures you have a valid marital status
while Status != "m" and Status != "s":
	print("you entered an invalid marital status")
	Status = input("Type m for married and s for single: ")




# Your code goes here
# Created variables for the 3 tax rates
lvl1 = .1   # Single Range = $0-$9,950 /// Married Range = $0-$19,900
lvl2 = .12  # Single Range = $9,951-$40,525 /// Married Range = $19,901-$81,050
lvl3 = .22  # Single Range = $40,526-$86,375 /// Married Range = $81,051-$172,750

# Created variables for the amount for the first 2 brackets
m1 = 19900 # Gotten from the max value from bracket 1 from the married bracket
m2 = 61150 # Gotten from the max value in bracket 2 minus the max value in bracket 1 Both from the married bracket
s1 = 9950  # Gotten from the max value from bracket 1 from the single bracket
s2 = 30575 # # Gotten from the max value in bracket 2 minus the max value in bracket 1 Both from the single bracket

if Status == "m":
	if Income <= 19900:  			# Takes in the income and checks it against first bracket range
		taxes = lvl1 * Income  		# Takes thier income and multiplies it with the corresponding tax percentage.
		print("This year you owe", taxes, "in taxes")
	elif 19901 <= Income <= 81050:  # Takes in the income and checks it against second bracket range
		Income -= m1            # Takes out the part for the first bracket
		p1 = m1 * lvl1          # Takes the first braket value and multiplies it to get the tax for the part of the income
		p2 = Income * lvl2  		# Takes the remainder and multiplies it against the second braket
		taxes = p1 + p2				# Adds all the parts together
		print("This year you owe", taxes, "in taxes")
	elif 81051 <= Income <= 172750: # Takes in the income and checks it against third bracket range
		Income -= m1 + m2   		# Takes out the part from the first 2 brackets
		p1 = m1 * lvl1				# Takes the first bracket max value and mulitplies it to get the tax for that part of the income
		p2 = m2 * lvl2				# Takes the second bracket max value and mulitplies it to get the tax for that part of the income
		p3 = Income * lvl3			# Takes the remainder and multiples it against the third bracket
		taxes = p1 + p2 + p3  		# adds all the parts together
		print("This year you owe", taxes, "in taxes")
	else: 						 	# For everything above the brackets we were given
		print("You made too much for this calculator. Hurray!")
elif Status == "s":
	if Income <= 9950:  			# Takes in the income and checks it against third bracket range
		taxes = lvl1 * Income  		# Takes thier income and multiplies it with the corresponding tax percentage.
		print("This year you owe", taxes, "in taxes")
	elif 9951 <= Income <= 40525:  	# Takes in the income and checks it against third bracket range
		Income -= s1            	# Takes out the part for the first bracket
		p1 = s1 * lvl1          # Takes the first braket value and multiplies it to get the tax for the part of the income
		p2 = Income * lvl2  		# Takes the remainder and multiplies it against the second braket
		taxes = p1 + p2				# Adds all the parts together
		print("This year you owe", taxes, "in taxes")
	elif 40526 <= Income <= 86375:  # Takes in the income and checks it against third bracket range
		Income -= s1 + s2   # Takes out the part from the first 2 brackets
		p1 = s1 * lvl1			# Takes the first bracket max value and mulitplies it to get the tax for that part of the income
		p2 = s2 * lvl2			# Takes the second bracket max value and mulitplies it to get the tax for that part of the income
		p3 = Income * lvl3			# Takes the remainder and multiples it against the third bracket
		taxes = p1 + p2 + p3  		# adds all the parts together
		print("This year you owe", taxes, "in taxes")
	else:  							# For everything above the brackets we were given
		print("You made too much for this calculator. Hurray!")



