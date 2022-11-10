"""
Company:
    -name: str
    -year: int

Car:
    self.wheels: int
    self.company: Comapany
    self.color: str
    self.miles: int
    self.status: str
    self.speed: int

    -accelerate(amount):
    -stop():
    -decrease(20):
"""
from random import randint

class company:
    def __init__(self,name,year) -> None:
        self.name = name
        self.year = year

class car:
    def __init__(self,wheels,company,color,miles,speed) -> None:
        self.wheels = wheels
        self.company = company
        self.color = color
        self.miles = miles
        self.status = 'stopped'
        self.speed = speed
    def accelerate(self,amount):
        self.status = 'accelerating'
        self.speed = amount
        self.updatemiles(amount)
    def stop(self):
        self.status = 'stopped'
        self.speed = 0
    def decrease(self):
        self.speed -= 20
        if self.speed < 0:
            self.speed = 0
        self.status = 'slowing down'
    def updatemiles(self,miles):
        self.miles += miles


def oneToSixty(car):
    seconds = 0
    speed = car.speed
    while speed < 60:
        speed += car.accelerate(randint(1,25))
        seconds += 1

    print('==========Car Info==========')
    print(f"It took {seconds} seconds for you car to reach 60 mph.")
    return f"The car drove {car.miles}"





toyota = company('Toyota',1996)

Supra = car(4,toyota,'blue',1000,16)

print(oneToSixty('Supra'))

"""
add checks for 0-100 and 0-250
add 5 cars
"""