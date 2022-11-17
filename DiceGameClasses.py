from random import randint
from turtle import hideturtle


class die:
    def __init__(self,sides,faceUpValue=1):
        self.sides = sides
        self.face = faceUpValue
    def roll(self,numOfSides):
        roll = randint(1,numOfSides)
        return roll
    def getValue(self,roll=False):
        if roll == True:
            self.face = self.roll(self.sides)
        return self.face
    def __str__(self):
        print(self.getValue())
        return ""
    def _add_(self,die1,die2):
        total = die1 + die2
        return total
    def _gt_(self,roll1,roll2):
        if roll1 > roll2:
            return roll1
        if roll2 > roll1:
            return roll2
        else:
            return 'Tie'



class player:
    def __init__(self,name,die1,die2):
        self.name = name
        self.die1 = die1
        self.die2 = die2
    def rollDice(self):
        roll1 = self.die1.getValue(True)
        roll2 = self.die2.getValue(True)
        total = self.die1._add_(roll1,roll2)
        return total
    def getDiceValue(self):
        value = self.rollDice()
        return value
    def __str__(self) -> str:
        print(self.getDiceValue())
        return ""

class HighTwoGame:
    def __init__(self,Player1,Player2):
        self.p1 = player(Player1,d6,d10)
        self.p2 = player(Player2,d6,d10)
    def playOneGame(self):
        p1Roll = self.p1.getDiceValue()
        p2Roll = self.p2.getDiceValue()
        print(f"{self.p1.name} rolled {p1Roll}")
        print(f"{self.p2.name} rolled {p2Roll}")
        decison = self.p1.die1._gt_(p1Roll,p2Roll)
        if decison == 'Tie':
            print("Tie")
        elif decison == p1Roll:
            print(f"{self.p1.name} wins!")
        else:
            print(f"{self.p2.name} wins!")

    def playManyGames(self,numOfGames=2):
        for x in range(numOfGames):
            p1Roll = self.p1.getDiceValue()
            p2Roll = self.p2.getDiceValue()
            print(f"Game {x+1}")
            print(f"{self.p1.name} rolled {p1Roll}")
            print(f"{self.p2.name} rolled {p2Roll}")
            decison = self.p1.die1._gt_(p1Roll,p2Roll)
            if decison == 'Tie':
                print("Tie")
            elif decison == p1Roll:
                print(f"{self.p1.name} wins!")
            else:
                print(f"{self.p2.name} wins!")
    def __str__(self,games=1) -> str:
        if games == 1:
            self.playOneGame()
        else:
            self.playManyGames(games)
        return ""

d6 = die(6)
d10 = die(10)
if __name__ == "__main__":
    print(HighTwoGame("Bob","Rob"))

