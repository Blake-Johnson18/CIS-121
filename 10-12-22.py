# write a function that creates two lists of random values. the user should send as a parameter how mnay elements the list should have


from random import randint
from statistics import mean
def main():
    # createList(6)
    # print(AUfinder('abundance'))
    # print(bestMile())
    print(dictCreate(list1,list2))

def createList(amount):
    list1 = []
    list2 = []
    for x in range(amount):
        y = randint(1,100)
        z = randint(1,100)
        list1.append(y)
        list2.append(z)
    print(list1)
    print(list2)

# wtrie a function that can find how many times the letters "a" and 'u' appear in a word. return a dictionary with each amount

def AUfinder(word):
    dict = {
        'a' : 0,
        'u' : 0
    }
    Lword = word.lower()
    for ch in Lword:
        if ch in dict:
            dict[ch] += 1
    return dict

# wtite a function that ask the user for his 10 best 4 mile run times. calculate the avg.

# Store the 10 times, the avg and the seperate the best and worst times in a dictionary

def bestMile():
    info = {
        "Times":[],
        'Avg': 0,
        'best time': 0,
        'worst time': 0
        }
    for i in range(10):
        user = int(input("Please enter a time: "))
        info['Times'].append(user)
        if user > info['worst time']:
            info['worst time'] = user
        if user < info['best time'] or info['best time'] == 0:
            info['best time'] = user
    info['Avg'] = mean(info['Times'])
    return info

# write a function that thatkes two lists and generates a dictionary.

# then mulitply all the values by 5 and create a new key for each mulitplication
list1 = ['num 1','num 2','num 3']
list2 = [1,2,3]
def dictCreate(list1, list2):
    dict = {}
    for x in range(len(list1)):
        dict[list1[x]] = list2[x]
    for x in range(len(list1)):
        dict[f'num {x+len(list1)+1}'] = int(list2[x])*5
    return dict

if __name__ == '__main__':
    main()