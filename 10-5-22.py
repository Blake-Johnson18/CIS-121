from random import randint


# names = ['Blake','Johnson']

# info = {
#     'Blake':26,
#     'Bob':3456
# }


# # open file
# file = open('data.txt','r')
# # get data from file
# data = file.read().splitlines()

# print(data)

# # create a function that takes a list of values in str and returns a new list with only int.

# def conversion():
#     file = 'data.txt'
#     intList = []
#     with open(f'{file}','r') as f:
#         for l in f:
#             intList.append(int(l))
#     return intList

# print(conversion())

# # create a function that takes the numbers and adds 5 to them

# def Listaddition():
#     list = conversion()
#     newList = []
#     for x in list:
#         y = x+5
#         newList.append(y)
#     return newList

# data = Listaddition()


# # write the results to a new file

# with open('results.txt', 'w') as f:
#     for number in data:
#         f.write(str(number)+'\n')

# # generate a rnadom number
# a = randint(1,100)

# generate a list with 100 random values. then write to a file called "RandomNumbersGenerated.txt"
with open("randomNumbersGenerated.txt",'w')as f:
    for x in range(100):
        f.write(f'{randint(1,100)}\n')

# Part2
# create a functino that counts how many times each number appears. use a dictionary to keep track.

def counter():
    dict = {}
    with open("randomNumbersGenerated.txt",'r') as r:
        list = r.read().splitlines()
        for x in list:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
    return dict
counter()


# write the info from dictionary to a file called "final.txt"
def dictFile():
    dict = counter()
    with open('final.txt','w') as w:
        for item in dict:
            w.write(f'{item} : {item[0]}\n')

dictFile()