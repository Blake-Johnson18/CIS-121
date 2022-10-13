# modules
import statistics

def autoMedian(data):
    result = statistics.median(data)
    return result
def autoMean(data):
    result = statistics.mean(data)
    return result
def autoMode(data):
    result = statistics.mode(data)
    return result
def mode(data):
    tempD = {}
    for x in data:
        if x not in tempD:
            tempD[x] = 1
        else: tempD[x] += 1
    mode = max(tempD, key=tempD.get)
    return mode
def mean(data):
    total = 0
    for num in data:
        total += num
    mean = total/len(data)
    return mean
def median(data):
    data.sort()
    while len(data) > 2:
        data.pop(0)
        data.pop(len(data)-1)
    if len(data) == 2:
        temp = 0
        for x in data:
            temp += x
        median = temp/2
    else:
        median = data[0]
    return median

def all():
    info = '[3, 1, 7, 1, 4, 10]' #input("Enter your list: ")
    if isinstance(info,str):
        List = info.split()
        trueInfo = []
        for x in range(len(List)):
            temp = ''
            for ch in List[x]:
                if ch.isdigit():
                    temp += ch
            trueInfo.append(int(temp))
        print(f'List: {trueInfo}')
        print(f'Mode: {mode(trueInfo)}')
        print(f'Auto Mode: {autoMode(trueInfo)}')
        print(f'Median: {median(trueInfo)}')
        print(f'Auto Median: {autoMedian(trueInfo)}')
        print(f'Mean: {mean(trueInfo)}')
        print(f'Auto Mean: {autoMean(trueInfo)}')
    else:
        print(f'List: {info}')
        print(f'Mode: {mode(info)}')
        print(f'Median: {median(info)}')
        print(f'Mean: {mean(info)}')
    
all()