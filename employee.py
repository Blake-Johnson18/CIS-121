class employee:
    def __init__(self,hourlyWage,weeklyHours,position,name):
        self.wage = hourlyWage
        self.position = position
        self.hours = weeklyHours
        self.name = name
    def yearlySalary(self):
        weekly = self.wage*self.hours
        yearly = weekly*52
        if yearly > 999:
            x = str(round(yearly))
            if yearly > 99999:
                x = x[:3] + ',' + x[3:]
            elif yearly > 9999:
                x = x[:2] + ',' + x[2:]
            else:
                x = x[:1]+','+x[1:]
        return f'You make ${x} a year.'
    def __str__(self) -> str:
        print('===Employee Info===')
        print(f'Name: {self.name}')
        print(f'Hours worked in a week {self.hours}')
        print(f'Position: {self.position}')
        print(f'Hourly Wage: {self.wage}')
        print(f'Yearly Salary: {self.yearlySalary()}')
        return ""
    def change(self,ChangeToBeMade,changeTo):
        x = ChangeToBeMade.lower()
        if x == 'wage':
            self.wage = float(changeTo)
        elif x == 'hours':
            self.hours = int(changeTo)
        elif x == 'position':
            self.position = changeTo
        elif x == 'name':
            self.name = changeTo
        