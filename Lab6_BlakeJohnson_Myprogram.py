import Lab6_BlakeJohnson_Stats as lab6
file = open("500DayFruitData.txt", 'r')

# Getting the lines and seperating them by \n
data = file.read().splitlines()
data.pop(0)
apples = []

for item in data:
    temp = item.split()
    if temp[1] == 'apple':
        apples.append(int(temp[2]))

mean = lab6.mean(apples)
median = lab6.median(apples)
print("The mean number of apples eaten is", mean)
print("The meidan number of apples eaten is", median)

with open("Blake_Johnson_Output.txt",'w') as f:
    f.write("The mean number of apples eaten is " + str(mean) + "\n" + "The meidan number of apples eaten is " + str(median))