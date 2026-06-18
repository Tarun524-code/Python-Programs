class Book:
    def __init__(self, title, author, publisher, price):
        self.__title = title
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
        return [self.__title, self.__author, f"{self.__price:.0f}", str(self.copies), discount, f"{self.total:.0f}"]



print("Enter purchase details for multiple books")
while True:
    try:
        n = int(input("Number of books: ").strip())
        if n > 0:
            break
        print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")

books = []
for index in range(1, n + 1):
    print(f"\nBook {index}")
    title = input("Book Name: ").strip()
    author = input("Author: ").strip()
    publisher = input("Publisher: ").strip()
    price = input("Price: ").strip()
    copies = input("Number of copies: ").strip()

    book = Book(title, author, publisher, price)
    book.purchase(copies)
    books.append(book)

header = "                purchase of book details"
separator = "---------------------------------------------------------------"
print("\n" + header)
print(separator)
print(f"{'Book Name':<15}{'Author':<12}{'Price':<10}{'noc':<6}{'discount':<14}{'total'}")
print(separator)
for book in books:
    title, author, price, copies, discount, total = book.display()
    print(f"{title:<15}{author:<12}{price:<10}{copies:<6}{discount:<14}{total}")
