class Book:
    def __init__(self, name, author, publisher, price):
        self.__name = name
        self.__author = author
        self.__publisher = publisher
        self.__price = float(price)

    def purchase(self, copies):
        self.copies = int(copies)
        subtotal = self.__price * self.copies

        if 101 <= self.copies <= 200:
            self.discount_percent = 10
        elif 201 <= self.copies <= 300:
            self.discount_percent = 20
        elif 301 <= self.copies <= 400:
            self.discount_percent = 40
        elif self.copies > 400:
            self.discount_percent = 50
        else:
            self.discount_percent = 0

        self.discount_amount = subtotal * self.discount_percent / 100
        self.total = subtotal - self.discount_amount

    def display(self):
        discount = f"{self.discount_percent}%" if self.discount_percent else "no discount"
        print("Book purchase details")
        print("----------------------")
        print(f"Book Name: {self.__name}")
        print(f"Author: {self.__author}")
        print(f"Publisher: {self.__publisher}")
        print(f"Price: {self.__price}")
        print(f"NOC: {self.copies}")
        print(f"Discount: {discount}")
        print(f"Total: {self.total}")


print("Enter details for a single book purchase")
title = input("Book Name: ").strip()
author = input("Author: ").strip()
publisher = input("Publisher: ").strip()
price = input("Price: ").strip()
copies = input("Number of copies: ").strip()

b = Book(title, author, publisher, price)
b.purchase(copies)
print()
b.display()
