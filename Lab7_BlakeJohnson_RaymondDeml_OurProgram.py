import lab7_BlakeJohnson_RaymondDeml_Stats as lab7
file = open("50DayFruitData.txt", 'r')

# Getting the lines and seperating them by \n
data = file.read().splitlines()
data.pop(0)
apples = []
# strawberries = []
# bananas = []

for item in data: # checks each item and adds the quantity to the correct list
    temp = item.split()
    if temp[1] == 'apple':
        apples.append(int(temp[2]))

aMean = round(lab7.mean(apples))
aMedian = round(lab7.median(apples))
aMode = []
aMode.append(round(lab7.mode(apples)))

appleDict = {}
appleDict["Mean of Apples"] = aMean
appleDict["Median of Apples"] = aMedian
appleDict["Mode of Apples"] = aMode

# creating a new file
with open("Blake_Johnson_RaymondDeml_Output.txt",'w') as f:
    f.write(f"# Apples\nThe Mean of apples is {appleDict['Mean of Apples']}\nThe Median of apples is {appleDict['Median of Apples']}\nThe Mode of apples is {appleDict['Mode of Apples']}")