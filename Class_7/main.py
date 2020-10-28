from book import Book

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


##============= Built-in Instance Methods

print("Does price exist in b1?", hasattr(b1,"price"))

##============= Build-in Class methods 

print("Book Doc", Book.__doc__)




