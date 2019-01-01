class Book():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages

    def read(self):
        return self.pages

    def __str__(self):
        return " book name {}".format(self.name)
    def __len__(self):
        return self.pages

b = Book("mybook", "sandeep", 50)
print(b)
print(len(b))

print(b.read())
print(b.name)
print(b.author)
print(b.pages)
del b
