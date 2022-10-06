# names = ['Blake',2,3.45,23]



# print(names[2])


# # Empty dict
# info = {}

# info = {
#     "Patient 0": ["Blake","Johnson",26],
#     "Patient 1": 23,
#     "Patient 2": ['Bob','Builder',134]
# }

# # how to add values to dict
# info["Patient 3"] = ['Roger','NA','NA']

# print(info)

# # create a script that ask the user for their name, lastname and age. keep this info stored on a dict and then print out the values

# firstName = str(input("Enter your first name: "))
# lastName = str(input("Enter your last name: "))
# age = int(input("Enter your age: "))

# dict = {
#     firstName : [firstName, lastName, age]
# }

# print(f'Hi! your name is {dict[firstName[0]]} {dict[firstName[1]]} and you are {dict[firstName[2]]} years old')


# # create a script that ask the user for 5 soccer players and how many goals they made this season (in a dictionary). Calculate the avg in a seperate funtion.
# dict = {}
# for x in range(5):
#     player = str(input("Enter a soccer player's name: "))
#     goals = int(input(f"How many goals did {player} score: "))
#     dict[player] = [goals]
# def goalAvg(players):
#     total = 0
#     for player in players:
#         total += players[player]
#     return total/len(players)
# print(goalAvg(dict))

# create a function that is capable of verifying if a key already exist in your dictionary

dict = {
    "Blake" : ['Blake'],
    "Codi" : ['Codi'],
    'Honey' : ['Honey'],
    'Jacob': ['jacob']
}

def check(dict,name):
    if name in dict:
        return 'That name is already there'
    else:
        return 'That name has not been added yet'
# print(check(dict,"Ken"))


# create a function that takes this two dict and add the values of the same index together. print out the resulting list
info1 = {
    'data' : [1,2,3,4,5]
}

info2 = {
    'data' : [6,7,8,9,10]
}

def addition(list1,list2):
    list = []
    for x in range(len(list1['data'])):
        sum = 0
        sum += list1['data'][x] + list2['data'][x]
        list.append(sum)
    print(list)

addition(info1,info2)