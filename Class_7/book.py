class Book:

    ## Class Level Variables
    seqNumber = 1000
    bookCounter = 1

    def __init__(self,title,author,editor,price):

        ##Instance Variables
        self.title = title
        self.author = author
        self.editor = editor
        self.price = price
        self.bookId = Book.seqNumber
        Book.seqNumber += 1
        Book.bookCounter += 1

    ###==================Getters and Setters
    @property ###decoratior
    def getTitle(self):
        return self.title

    @property
    def getAuthor(self):
        return self.author

    @property
    def getEditor(self):
        return self.author

    @getEditor.setter
    def setEditor(self, newEditor):
        self.editor = newEditor

    @property
    def getBookID(self):
        return self.bookId

    @property
    def getPrice(self):
        return self.price

    @getPrice.setter
    def setPrice(self, newPrice):
        if newPrice < 0:
            self.price = 0 
            print("not a valid price")
        else:
            self.price = newPrice

    ###========== class level method
    ##            1- When you are working on Class level Attributes
    ##            2- Factory Method
    ##                      

    @classmethod
    def getNbOfBooks(cls):
        print(f"The total number of books are {cls.bookCounter}")

    @classmethod ## factory method
    def createdABook(cls,title,author,price):
        return cls(title,author,author,price)

    @classmethod
    def createABookByBook(cls, myBook):
        return cls(myBook.title,myBook.author, myBook.editor, myBook.price)

    ##=================Static Method
    @staticmethod
    def sayHello():
        print(f"Hello from Static Method")
    
    
##================================Display 
b1 = Book("Red Rose","Walter Abish","Marc London", 169.99)
print(b1)
print(b1.title)
print(b1.author)
print(b1.editor)
print(b1.price)
print(b1.bookId)

print("================================================")

b2 = Book("Davinci","some body","Langdon", 99.99)
print(b2)
print(b2.getTitle)
print(b2.getAuthor)
print(b2.getEditor)
b2.setPrice = 100
print(b2.getPrice)
print(b2.getBookID)

print("================================================")