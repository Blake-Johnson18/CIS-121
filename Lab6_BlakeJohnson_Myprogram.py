import Lab6_BlakeJohnson_Stats as lab6
file = open("500DayFruitData.txt", 'r')

# Getting the lines and seperating them by \n
data = file.read().splitlines()
data.pop(0)
apples = []
strawberries = []
bananas = []

for item in data: # checks each item and adds the quantity to the correct list
    temp = item.split()
    if temp[1] == 'apple':
        apples.append(int(temp[2]))
    elif temp[1] == 'strawberry':
        strawberries.append(int(temp[2]))
    elif temp[1] == 'banana':
        bananas.append(int(temp[2]))

aMean = round(lab6.mean(apples))
aMedian = round(lab6.median(apples))
sMean = round(lab6.mean(strawberries))
sMedian = round(lab6.median(strawberries))
bMean = round(lab6.mean(bananas))
bMedian = round(lab6.median(bananas))
# print("The mean number of apples eaten is", mean)
# print("The median number of apples eaten is", median)

# creating a new file
with open("Blake_Johnson_Output.txt",'w') as f:
    f.write("# Apples \n" + "The mean number of Apples eaten is " + str(aMean) + "\n" + "The median number of Apples eaten is " + str(aMedian) + "\n\n" + "# Strawberries \n" + "The mean number of Strawberries eaten is " + str(sMean) + "\n" + "The median number of Strawberries eaten is " + str(sMedian) + "\n\n" + "# Bananas \n" + "The mean number of Bananas eaten is " + str(bMean) + "\n" + "The median number of Bananas eaten is " + str(bMedian) + "\n\n")