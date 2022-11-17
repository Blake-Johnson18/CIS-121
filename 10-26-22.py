from random import randint

# parent class
class student:
    def __init__(self,name,lastname) -> None:
        self.name = name
        self.last = lastname
        self.__ssn = randint(100000000,999999999)
    def desplayInfo(self):
        print(f"Name: {self.name} ")
        print(f"Lastname: {self.last} ")
        print(f"SSN: {self.__ssn} ")
    def getSSN(self):
        return self.__ssn
    
# Child class
class HighSchoolStudent(student):
    def __init__(self, name, lastname,grade) -> None:
        super().__init__(name, lastname)
        self.grade = grade
    def displayInfo(self):
        print(f"Name: {self.name} ")
        print(f"Lastname: {self.last} ")
        print(f"SSN: {self.getSSN} ")
        print(f"Grade: {self.grade} ")


student = student('Bob','Saget')

# create a class that manages an account
# Client class
# username, password, recovery phrase
# method to change username
# mehtod to change __password
# protected value __password
# protected value __username

class client:
    def __init__(self,username,password,recovery) -> None:
        self.__user = username
        self.__pass = password
        self.rec = recovery

    def changeusername(self,newUsername):
        self.__user = newUsername
    def changepassword(self,newPassword):
        self.__pass = newPassword

class UpdateUser(client):
    def __init__(self, username, password, recovery,newUsername,newPassword) -> None:
        super().__init__(username, password, recovery)
        self.__nuser = newUsername
        self.__npass = newPassword
    def update(self):
        if self.rec == 'Recovery':
            self.changeusername(self.__nuser)
            self.changepassword(self.__npass)
        else:
            print("Incorrect recovery phrase")
