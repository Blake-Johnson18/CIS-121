# Write a dunction that creates a file with 300 random numbers from 1-2000
from random import randint
from re import I
file = '10-17-22.txt'
def numGen(file):
    with open(file,'w') as f:
        for x in range(300):
            num = randint(1,2000)
            f.write(f'{str(num)}\n')
# Write a function that takes the file created before and determine how many times you can find the numbers 10,24,7,11
def numFind(file):
    dict ={
        '10':0,
        '24':0,
        '7':0,
        '11':0
    }
    with open(file,'r') as f:
        nums = f.read().splitlines()
        for x in nums:
            if x in dict:
                dict[x] += 1
    return dict

# Write a fucntion that looks at 2 dictinoaries and checks if they have similar keys. return only one dictionary that has all the values for a given key
dict1 ={
    'Data': [0],
    'Info': "NA"
}
dict2 = {
    'Data': [3],
    'Stats': "NA",
    'Info': "NA"
}
def dictCompile(dict1,dict2):
    newDict = {}
    for item in dict1:
        newDict[item] = [dict1[item]]
    for item in dict2:
        if item not in newDict:
            newDict[item] = [dict2[item]]
        else:
            newDict[item].append(dict2[item])
    return newDict

# Write a function that takes the file created in problem 1 and adss the words (even or odd) next to the numbers.
def overwrite(file):
    with open(file,'r') as f:
        numbers = f.read().splitlines()
        with open(file,'w') as w:
            for num in numbers:
                if int(num) % 2 == 0:
                    num = f'{num} Even\n'
                else:
                    num = f'{num} Odd\n'
                w.write(num)

if __name__ == '__main__':
    numGen(file)
    # print(numFind(file))
    # print(dictCompile(dict1,dict2))
    overwrite(file)
