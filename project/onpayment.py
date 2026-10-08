# Create an online payment system using Encapsulation, Abstraction, Inheritance,
# and Polymorphism. Create a parent Payment class with a common pay() operation.
# Create UPI, CreditCard, and CashPayment child classes. Each payment type should
# implement pay() differently. Keep important payment information protected.

class payment:
    def __init__(self,amount):
          self.amount=amount
    def pay(self):
         return self.amount
    def payment_method(self):
         print("payment method:") 

class cash(payment):
     def payment_method(self):
          print("payment:",self.pay())
class upi(payment):
     def payment_method(self):
          print("payment:",self.pay())
class creditcard(payment):
     def payment_method(self):
          print("payment:",self.pay())

cash=cash(10000)
upi=upi(1100)
creditcard=creditcard(1100)

cash.payment_method()
upi.payment_method()
creditcard.payment_method()

     
