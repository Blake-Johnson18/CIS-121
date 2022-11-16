class Document:
    def __init__(self,authors=[],date='') -> None:
        self.authors = authors
        self.date = date
    
    def getAuthors(self):
        return self.authors
    def getDate(self):
        return self.date
    def addAuthor(self,name):
        if type(name) == str:
            self.authors.append(name)

class Book(Document):
    def __init__(self, authors=[], date='',title='') -> None:
        super().__init__(authors, date)
        self.title = title
    def getTitle(self):
        return self.title
    def __str__(self):
        print("=====Book information=====")
        print(f'Authors - {self.getAuthors()}')
        print(f' Date - {self.getDate()}')
        return f'Title - {self.getTitle()}'

class EMail(Document):
    def __init__(self, authors=[], date='',subject='',to=[]) -> None:
        super().__init__(authors, date)
        self.subject = subject
        self.to = to
    def getSubject(self):
        return self.subject
    def getTo(self):
        return self.to
    def __str__(self):
        print("=====Email information=====")
        print(f'Authors - {self.getAuthors()}')
        print(f'Date - {self.getDate()}')
        print(f'Subject - {self.getSubject()}')
        return f'To - {self.getTo()}'

email1 = EMail(['Blake'],'11/16/2022',"What's the plan?",['Codi','Ezekiel','Jacob'])
book1 = Book(['Blake'],'11/16/2022','How to code objects')

print(email1)
print(book1)