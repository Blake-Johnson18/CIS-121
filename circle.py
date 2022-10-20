from math import pi
import re


class circle:
    def __init__(self,radius):
        self.r = radius
    
    def area(self):
        area = pi*(self.r**2)
        return round(area,2)
    def perimeter(self):
        p = 2*pi*self.r
        return round(p,2)
    def __str__(self):
        print(f"===Circle Info===\nRadius: {self.r}\nArea: {self.area()}\nPerimeter: {self.perimeter()}")
        return ""