from math import floor
# # name = "Blake"
# # lastname = "Johnson"

# # print("Blake")
# # print(name)


# # name = "B"


# # coolname = "Lol"
# # print(coolname)

# # age = 26

# # print(type(age))


# # distance = 34.5

# # print(type(distance))

# # print(age + distance)

# # Lab 2 part 1

dog_years = 7

# # Create a variable to stroe the humans age
human_age = float(input("How old are you: "))
# # Calculate how old is the human in dog years
dog_age_years = dog_years*human_age
dog_age_years_r = dog_years%human_age
dog_age_months = dog_age_years_r*12
dog_age_months_r = dog_age_months%1
dog_age_days = dog_age_months_r*31
# print(floor(dog_age_years))
# print(floor(dog_age_months))
# print(dog_age_months_r)
print(round(dog_age_days))
print("An age", human_age, "human should be", floor(dog_age_years), "years, and", floor(dog_age_months), "months, and", round(dog_age_days), "dyas in dog age.")


# # Create a script that asks the user for name,lastname and age. Print out the info as follows
# # Hi Kendrick Morales, You're 23 years old, damn.

# name = input("What's your first name? ")
# lastname = input("What's your last name? ")
# age = int(input("How old are you? "))

# print("Hi", name, lastname +",", "You're", age, "years old, Damn.")

# # human_age = float(input("How old are you? "))
# Horse_age = 3 * ((((human_age**2)-47)/7)+12)

# print("An age", human_age, "human should be about", Horse_age, "in horse age.")

# # To calculate a humans height you do the following: age^2

# # Print out the humans age and estimated height

# # human_age = int(input("How old are you: ")) # taking the age of the person
# height = human_age**2 # Calculates and stores height estimate

# print("Someone that is", human_age, "years old, should be around", height, "tall.")