class Book:
    def read(self):
        self.name=input()
        self.author=input()
        self.price=int(input())
    def display(self):
        print("---Book Details---")
        print("Book Name: ",self.name)
        print("Book Author: ",self.author)
        print("Book Price: ",self.price)
        
b1=Book()
b1.read()
b1.display()