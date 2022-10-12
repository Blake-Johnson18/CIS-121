

from random import randint


names = ['Blake']

info = {
    'Blake':26
}

# Create a function that takes 2 lists and makes them a dictionary
keys = ['number 1', 'number 2', 'number 3']
values = [1,2,3]

def dictMaker(keys_list,values_list):
    dict = {}
    for x in range(len(keys_list)):
        dict[keys_list[x]] = values_list[x]
    return dict
# print(dictMaker(keys,values))
        
# create a function that can mulitply all the numbers in a dictionary by a given number. make sure that these values are numeric
info = {
    'Num 1': '12',
    'num 2': 'abcs',
    'num 3': '56',
}
def dictMultiply(data, number):
    for key in data:
        if data[key].isdigit():
            return f'{data[key]} {number} {int(data[key])*number}'
# print(dictMultiply(info,2))

# create a function that can generates a dictionary with 5 numbers. then make another function that generates random numbers until it generates one inside the dictionary

def randomFind():
    dict = {}
    for x in range(5):
        dict[f'Num {x}'] = randint(1,1000)
    while True:
        num = randint(1,1000)
        for key in dict:
            if num == dict[key]:
                return f'I found {num} in your dictionary'
                break
print(randomFind())

