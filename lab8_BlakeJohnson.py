def main():
    file = 'randomValues.txt'
    numData = openFileNum(file)
    # print(data)
    print(findMin(numData,0,numData[0]))
    print(findMax(numData,0,numData[0]))
    Extrema(numData,False)

def openFileNum(fileName):
    list = []
    with open(fileName,'r') as r:
        lines = r.read().splitlines()
        for line in lines:
            if line.isdigit():
                list.append(int(line))
    return list
def findMin(data,index,Cmin):
    if len(data) == 0:
        print("Empty list can't be worked on")
    if len(data) == 1:
        return data[0]
    Min = data[index]
    if Min <= Cmin:
        Cmin = Min
    if index >= len(data)-1:
        return Cmin
    else:
        return findMin(data,index+1,Cmin)
def findMax(data,index,Cmax):
    if len(data) == 0:
        print("Empty list can't be worked on")
    if len(data) == 1:
        return data[0]
    Max = data[index]
    if Max >= Cmax:
        Cmax = Max
    if index >= len(data)-1:
        return Cmax
    else:
        return findMax(data,index+1,Cmax)
def Extrema(data,Min=True,Max=True):
    if Min == True and Max == True:
        print(findMin(data,0,data[0]))
        print(findMax(data,0,data[0]))
    elif Min == False and Max == True:
        print(findMax(data,0,data[0]))
    elif Min == False and Max == False:
        print("Nothing")



if __name__=='__main__':
    main()