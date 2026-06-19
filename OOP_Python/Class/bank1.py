class Bank:
    Account_num = 100
    def __init__(self, name):
        self.__name = name
        self.__balance = 0
        Bank.Account_num += 1
        self.Account_num = Bank.Account_num
        
    def deposit(self, amount):
        amt = int(amount)
        self.__balance += amt
        return self.__balance
    
    def withdraw(self, amount):
        amt = int(amount)
        if amt > self.__balance:
            print("You dont have sufficient Funds for withdraw")
            return
        self.__balance -= amt
        return self.__balance

    def display(self):
        print("Account Number:", self.Account_num)
        print("Name:", self.__name)
        print("Balance:", self.__balance)

    def check_balance(self):
        print("Balance:", self.__balance)
        return self.__balance

print("Enter account details:")
name = input("Enter person name: ")
acc = Bank(name)
while True:
    print("\nMenu :")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display")
    print("4. Check balance")
    print("5. Exit")
    choice = input("Enter choice: ").strip()
        
    if choice == '1':
        amt = input("Enter amount: ")
        res = acc.deposit(amt)
        if res is not None:
            print("New balance:", res)
    elif choice == '2':
        amt = input("Enter amount: ")
        res = acc.withdraw(amt)
        if res is not None:
            print("New balance:", res)
    elif choice == '3':
        acc.display()
    elif choice == '4':
        acc.check_balance()
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid choice")



