class Bank:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance not worked")

    def check_balance(self):
        print("Balance:", self.__balance)

    def display(self):
        print("Name:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.__balance)


name = input("Enter name: ")
account_no = input("Enter account number: ")
balance = int(input("Enter initial balance: "))

account = Bank(name, account_no, balance)

while True:
    print("\n-management system")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter deposit amount:"))
        account.deposit(amount)

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        account.display()

    elif choice == 5:
        print("thanks")
        break

    else:
        print("Invalid choice")