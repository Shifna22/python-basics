# Create a banking system using Encapsulation, Abstraction, Inheritance, and
# Polymorphism. Create a parent BankAccount class with private balance and
# common methods like deposit and balance checking.
# Create SavingsAccount and CurrentAccount as child classes and
# implement withdraw() differently for each account type.



class bankac:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance

    def display(self):
        print("name",self.name)
        print("balance",self.balance)
    def deposit(self,amount):
        amount=self.balance+amount
        print("balance:",amount)
    def check_balance(self):
        print("balance:",self.balance)
    def get_balance(self):
        return self.balance

class savingac(bankac):
    def withdraw (self,amount):
        if amount<=self.get_balance():
            print("withdraw:",amount)
        else:
            print("inneficient balance")
class currentac(bankac):
    def withdraw(self,amount):
        if amount<=self.balance+5000:
            print("current withdraw:",amount)
        else:
            print("limit exceeded")
saving=savingac("shifna",10000)
current=currentac("fathima",10000)

print("Savings Account")
saving.deposit(2000)
saving.withdraw(5000)
saving.check_balance()

print("Current Account")
current.deposit(3000)
current.withdraw(15000)
current.check_balance()


