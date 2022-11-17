class employee:
    def __init__(self,ID,name):
        self.id = ID
        self.name = name

class salaryEmployee(employee):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.weekly = 600
    def calculatePayroll(self,):
        pay = self.weekly*52
        return f'{self.name} makes ${pay} a year'
    def printInfo(self):
        return f"==========Employee Info==========\nName: {self.name}\nID: {self.id}\nWeekly pay: {self.weekly}\nTotal Salary this week: {self.calculatePayroll()} "

class commissionEmployee(salaryEmployee):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.weekly = 600
        self.commision = 25
        self.wage = 100
    def calculatePayroll(self):
        pay = self.wage*self.commision+self.weekly
        return f'{self.name} makes ${pay} a year'
    def printInfo(self):
        return f"==========Employee Info==========\nName: {self.name}\nID: {self.id}\nWeekly pay: {self.weekly}\nComission: {self.commision}\nTotal Salary this week: {self.calculatePayroll()}"

class hourlyEmployee(employee):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.hours = 48
        self.wage = 25.50
    def calculatePayroll(self):
        pay = (self.hours*self.wage)*52
        return f'{self.name} makes ${pay} a year'
    def printInfo(self):
        return f"==========Employee Info==========\nName: {self.name}\nID: {self.id}\nHours Worked: {self.hours}\nHourly wage: {self.wage}\nTotal Salary this week: {self.calculatePayroll()}"
        
if __name__ == '__main__':
    bobH = hourlyEmployee(5648,"Bob")
    TonyS = salaryEmployee(9758,'Tony')
    SteveC = commissionEmployee(3458,'Steve')

    print(bobH.printInfo())
    print(TonyS.printInfo())
    print(SteveC.printInfo())