class animal:
    def __init__(self,name):
        self.name = name
    def displayInfo(self):
        print(f"===Animal===")
        print(f'Name: {self.name}')
        
class Dog(animal):
    def __init__(self, name,color,eyeColor,height,length,weight):
        super().__init__(name)
        self.color = color
        self.eye = eyeColor
        self.height = height
        self.length = length
        self.weight = weight
    def sit(self):
        print("I'm sitting!")
    def layDown(self):
        print("I'm laying down!")
    def shake(self):
        print("I'm shaking!")
    def come(self):
        print("I'm running to you!")
    def __str__(self):
        return f"Name: {self.name}\nColor: {self.color}\nEye Color: {self.eye}\nHeight: {self.height}\nLength: {self.length}\nWeight: {self.weight}\n"

class Cat(animal):
    def __init__(self, name):
        super().__init__(name)

# Dog - layer 1
# Color - layer 2
# Eye Color - layer 2
# Height - layer 2
# Length - layer 2
# Weight - layer 2
# sit() - layer 3
# layDown() - layer 3
# shake() - layer 3
# come() - layer 3



if __name__ == '__main__':
    Bobby = Dog('Bobby','Yellow','Brown','17 in','35 in','24 pounds')
    Bobby.come()
    print(Bobby)
    test = Cat('test')
    test.displayInfo()