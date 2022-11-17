"""
Question 1: Give a brief explanation of what you can figure out by looking at diagram in figure 1.
    Every person has an address on file and from the person class you can create either a studen or a teacher.

Question 2: Determine what classes are either parent/child and explain why
    Address is a parent class to Person because every person needs to be given an address.
    Person is a parent class to both the Student and Teacher classes because they both need the info from person but are seperate because they need different information to be passed through

Question 3: Using the diagram from figure 1 develop a python script that represents the class structure. Make sure you create at least one instance of each class.

Bonus: Add a __str__ method to every class that can display the information associate to the class
"""

class address:
    def __init__(self,street='',city='',country='',zipcode=00000,state=''):
        self.street = street
        self.city = city
        self.country = country
        self.zipcode = zipcode
        self.state = state
    def getAddress(self):
        return f"{self.street}, {self.city} {self.state}, {self.country}, {self.zipcode}"
    def getCity(self):
        return self.city
    def getZipcode(self):
        return self.zipcode
    def getState(self):
        return self.state
    def getCountry(self):
        return self.country
    def __str__(self):
        print("=====Adress Information=====")
        print(f"Street: {self.street}")
        print(f"City: {self.getCity()}")
        print(f"State: {self.getState()}")
        print(f"Country: {self.getCountry()}")
        print(f"Zipcode: {self.getZipcode()}")
        return f"Address: {self.getAddress()}\n"

class person(address):
    def __init__(self, street='', city='', country='', zipcode=0, state='',name='',phoneNumber='',emailAddress=''):
        super().__init__(street, city, country, zipcode, state)
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
    def __str__(self):
        print(f"====={self.name}'s Personal Information=====")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phoneNumber}")
        print(f"Email: {self.emailAddress}")
        return super().__str__()

class student(person):
    def __init__(self, street='', city='', country='', zipcode=0, state='', name='', phoneNumber='', emailAddress='',studentNumber=000,gpa=0.00):
        super().__init__(street, city, country, zipcode, state, name, phoneNumber, emailAddress)
        self.studentNumber = studentNumber
        self.gpa = gpa
    def getGPA(self):
        return self.gpa
    def getStudentNumber(self):
        return self.studentNumber
    def __str__(self):
        print(f"====={self.name}'s Student Information=====")
        print(f"Student Number: {self.getStudentNumber()}")
        print(f"Student GPA: {self.getGPA()}")
        return super().__str__()

class teacher(person):
    def __init__(self, street='', city='', country='', zipcode=0, state='', name='', phoneNumber='', emailAddress='',teacherID=000,workHours=0,workRate=0,yearsOfService=0):
        super().__init__(street, city, country, zipcode, state, name, phoneNumber, emailAddress)
        self.teacherID = teacherID
        self.workhours = workHours
        self.workrate = workRate
        self.YOS = yearsOfService
    def getTeacherID(self):
        return self.teacherID
    def getWorkHours(self):
        return self.workhours
    def getWorkRate(self):
        return self.workrate
    def getYearsOfService(self):
        return self.YOS
    def calculateYearlySalary(self):
        salary = self.getWorkHours()*self.getWorkRate()
        return salary
    def __str__(self):
        print(f"====={self.name}'s Teacher Information=====")
        print(f"Teacher ID: {self.getTeacherID()}")
        print(f"Worked hours: {self.getWorkHours()}")
        print(f"Work Rate: {self.getWorkRate()}")
        print(f"Years of Service: {self.getYearsOfService()}")
        print(f"Salary: {self.calculateYearlySalary()}")
        return super().__str__()
    

Address = address('111 Washington Ave','Mankato','USA',56001,'MN')
Person = person('111 Washington Ave','Mankato','USA',56001,'MN','BOB','507-645-2684','Random123@gmail.com')
Student = student('111 Washington Ave','Mankato','USA',56001,'MN','BOB','507-645-2684','Random123@gmail.com',123,3.8)
Teahcer = teacher('111 Washington Ave','Mankato','USA',56001,'MN','BOB','507-645-2684','Random123@gmail.com',587,2100,25,5)


print(Address)
print(Person)
print(Student)
print(Teahcer)