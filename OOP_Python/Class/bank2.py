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
    
accounts = {}

while True:
    print("\nMenu :")
    print("1. Create new account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display")
    print("5. Check balance")
    print("6. Exit")
    choice = input("Enter choice: ").strip()

    if choice == '1':
        name = input("Enter person name: ")
        acc = Bank(name)
        accounts[acc.Account_num] = acc
        print(f"Account created successfully! Account Number: {acc.Account_num}")

    elif choice == '2':
        acc_no = int(input("Enter account no: "))
        if acc_no in accounts:
            amt = input("Enter amount: ")
            res = accounts[acc_no].deposit(amt)
            if res is not None:
                print("New balance:", res)
        else:
            print("Account not found!")

    elif choice == '3':
        acc_no = int(input("Enter account no: "))
        if acc_no in accounts:
            amt = input("Enter amount: ")
            res = accounts[acc_no].withdraw(amt)
            if res is not None:
                print("New balance:", res)
        else:
            print("Account not found!")

    elif choice == '4':
        if accounts:
            print("Accounts Created Upto Now:")
            for acc_no in accounts:
                print(acc_no, end=" ")
            print("\n")

            acc_no = int(input("Enter account no to display details: "))
            if acc_no in accounts:
                accounts[acc_no].display()
            else:
                print("Account not found!")
        else:
            print("No accounts created yet!")


    elif choice == '5':
        acc_no = int(input("Enter account no: "))
        if acc_no in accounts:
            accounts[acc_no].check_balance()
        else:
            print("Account not found!")

    elif choice == '6':
        print("Exiting.")
        break

    else:
        print("Invalid choice")