class employee:
    def __init__(self,id_,name):
        self.id = id_
        self.name = name

class salaryEmployee(employee):
    def __init__(self, id_, name):
        super().__init__(id_, name)
    def calculatePayroll(self,weeklyPay):
        pay = weeklyPay*52
        return f'{self.name} makes ${pay} a year'

class commissionEmployee(salaryEmployee):
    def __init__(self, id_, name):
        super().__init__(id_, name)
    def calculatePayroll(self,wage):
        commision = 25
        pay = wage*commision
        return f'{self.name} makes ${pay} a year'

class hourlyEmployee(employee):
    def __init__(self, id_, name):
        super().__init__(id_, name)
    def calculatePayroll(self,hoursWorked,wage):
        pay = (hoursWorked*wage)*52
        return f'{self.name} makes ${pay} a year'
        
if __name__ == '__main__':
    bob = hourlyEmployee(5648,"Bob")
    Tony = salaryEmployee(9758,'Tony')
    steve = commissionEmployee(3458,'Steve')

    print(bob.calculatePayroll(38,24))
    print(Tony.calculatePayroll(1657))
    print(steve.calculatePayroll(600))