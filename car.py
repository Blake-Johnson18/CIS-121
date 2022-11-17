class Car:
    def __init__(self,numberOfWheels,engine,model,year):
        self.numWheels = numberOfWheels
        self.engine = engine
        self.model = model
        self.year = year
    def __str__(self):
        ## make it display the car info necely
        print(f'===Car Info===\nNumber of Wheels: {self.numWheels}\nEngine: {self.engine}\nCar Model: {self.model}\nCar Year: {self.year}')
        return ""
    def changeYear(self,newYear):
        self.year = newYear
    def changeEngine(self,newEngine):
        self.engine = newEngine
    
        