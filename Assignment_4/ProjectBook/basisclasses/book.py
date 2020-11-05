class Book:

    idSequence = 1000
    bookCounter = 1

    def __init__(self,title,author,editor,price):

        self.title = title
        self.author = author
        self.editor = editor
        self.price = price
        Book.idSequence += 1
        Book.bookCounter += 1

    @property
    def getTitle(self):
        return self.title
    @property
    def getAuthor(self):
        return self.author
    @property
    def getEditor(self):
        return self.editor
    @property
    def getPrice(self):
        return self.price
    
    @getPrice.setter
    def setPrice(self, newPrice):
        if newPrice < 0:
            self.price = 0
        else:
            self.price = newPrice


    def __str__(self):
        return f"Book id:{Book.idSequence}, Author: {self.author}, Price:{self.price}"
    

    
