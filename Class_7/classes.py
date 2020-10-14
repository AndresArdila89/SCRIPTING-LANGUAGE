class Book:

    ## Class Level Variables
    seqNumber = 1000

    def __init__(self,title,author,editor,price):

        ##Instance Variables
        self.title = title
        self.author = author
        self.editor = editor
        self.price = price
        self.bookId = Book.seqNumber
        Book.seqNumber += 1


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
print(b2.title)
print(b2.author)
print(b2.editor)
print(b2.price)
print(b2.bookId)

print("================================================")