from random import randint


def main():
    list1 = []
    for x in range(50):
        list1.append(randint(1,100)) # Generates a list of 50 numbers for me
    evenOddOutput(list1)
    duplicates()
    fitness()
    Bonus(5,list1)

def evenOddOutput(list): # Problem 1
    dict = {
        'Even':[],
        'Odd':[]
    }
    for num in list:
        if num % 2 == 0: # checks if the number is even
            dict['Even'].append(num)
        else:
            dict['Odd'].append(num)
        with open('evenOdd.txt','w') as f: # creates output file
            f.write('Even: ')
            for E in dict['Even']:
                f.write(f'{E}, ')
            f.write('\nOdd: ')
            for O in dict['Odd']:
                f.write(f'{O}, ')
def duplicates(): # Problem 2
    list1 = []
    list2 = []
    dict = {}
    for x in range(200):
        list1.append(randint(1,100))
        list2.append(randint(1,100))
    for y in list1:
        if y not in dict:
            dict[y] = 1
        else:
            dict[y] += 1
    for z in list2:
        if z not in dict:
            dict[z] = 1
        else:
            dict[z] += 1
    with open('RESULTS4.txt','w') as f:
        for b in dict:
            if dict[b] > 1:
                f.write(f'{b}: {dict[b]} Times\n')
def fitness(): # Problem 3
    file = 'steps.txt'
    outfile = 'month.txt'
    with open(file,'r') as f:
        with open(outfile,'w') as o:
            lines = f.read().splitlines()
            Jan = lines[0:31] # 31   # split the values into the correct month
            Feb = lines[31:59] # 28
            Mar = lines[59:90] # 31
            Apr = lines[90:120] # 30
            May = lines[120:151] # 31
            Jun = lines[151:181] # 30
            Jul = lines[181:212] # 31
            Aug = lines[212:243] # 31
            Sep = lines[243:273] # 30
            Oct = lines[273:304] # 31
            Nov = lines[304:334] # 30
            Dec = lines[334:365] # 31
            Months = {
                'January':0,
                'Febuary':0,
                'March':0,
                'April':0,
                'May':0,
                'June':0,
                'July':0,
                'August':0,
                'September':0,
                'October':0,
                'November':0,
                'December':0
            }
            for x in Jan:  # Sums up each month and then divides it by the length of the coresponding Month
                Months['January'] += int(x)
            Months['January'] /= len(Jan)
            for x in Feb:
                Months['Febuary'] += int(x)
            Months['Febuary'] /= len(Feb)
            for x in Mar:
                Months['March'] += int(x)
            Months['March'] /= len(Mar)
            for x in Apr:
                Months['April'] += int(x)
            Months['April'] /= len(Apr)
            for x in May:
                Months['May'] += int(x)
            Months['May'] /= len(May)
            for x in Jun:
                Months['June'] += int(x)
            Months['June'] /= len(Jun)
            for x in Jul:
                Months['July'] += int(x)
            Months['July'] /= len(Jul)
            for x in Aug:
                Months['August'] += int(x)
            Months['August'] /= len(Aug)
            for x in Sep:
                Months['September'] += int(x)
            Months['September'] /= len(Sep)
            for x in Oct:
                Months['October'] += int(x)
            Months['October'] /= len(Oct)
            for x in Nov:
                Months['November'] += int(x)
            Months['November'] /= len(Nov)
            for x in Dec:
                Months['December'] += int(x)
            Months['December'] /= len(Dec)
            o.write(f'Month     |    Average\n')
            for x in Months:
                o.write('{}   |     {}\n'.format(x,round(Months[x],1)))
def Bonus(num, list, index=0): # Bonus question
    if index >= len(list):
        print(f'The number {num} is not in the list!')
    elif num == list[index]:
        print(f"The number {num} is in the list!")
    else:
        index += 1
        Bonus(num, list, index)


if __name__=='__main__':
    main()