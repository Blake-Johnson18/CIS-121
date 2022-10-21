"""
#Name Blake Johnson
#Date 10/20/2022

This implements the RoboFriend class.
"""

class RoboFriend:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def stateName(self):
        return f"Hello. My name is {self.name}."
    def stateAge(self):
        return f"I'm {self.age} years old."
    def __str__(self):
        print(self.stateName())
        print(self.stateAge())
        return ""