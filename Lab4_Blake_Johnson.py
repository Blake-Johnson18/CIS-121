# Blake Johnson

# proper divisor
# Perfect number
# abundant number
# deficient number

bound = int(input("Enter an upper bound for a check: ")) # Gets upper bound from the user

holder = True       # set to help end the loop
num = 2         # variable to check against
perfect = 0     # variable to count the number of perfect numbers
abundant = 0    # variable to count the number of proper divisors
deficient = 0   # variable to count the number of proper divisors 
while holder == True:
    proper = 0      # variable to count the sum of the proper divisors
    count = 1       # variable to count up to the bound
    if num <= bound:
        while count < num:
            if num % count == 0:  # checks to see if the current count number is a proper divisor of the num variable
                proper += count
            count += 1
    elif num > bound:        # Ends the loop once num becomes larger than the bound
        holder = False
    if proper < num: # checks to see if the num is deficient
        deficient += 1
    elif proper > num: # checks to see if the num is abundant
        abundant += 1
    elif proper == num:   # checks to see if the num is perfect
        perfect += 1
    num += 1 
print("Between 1 and", bound, "there are")
print(deficient, "deficient numbers")
print(perfect, "perfect numbers")
print(abundant, "abundant numbers")

