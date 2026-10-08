from abc import ABC, abstractmethod

class user:
      def __init__(self,name):
           self.name=name
class customer(user):
     def food_order(self):
          print(self.name,"placed order")
class delivery(user):
     def food_deliver(self):
          print(self.name,"deliver your food")

class food:
    def __init__(self,name,price):
          self.name=name
          self.price=price
          
    def get_price(self):
      
      print(self.price,"price of food")

class hotel:
       def __init__(self,name):
            self.name=name
            self.food=[]
       def add_food(self,food):
            self.food.append(food)
       def show_food(self):
            print("hotel:",self.name)
            for item in self.food:
              print(item.name, "-/", item.get_price())

class order:
     def __init__(self):
          self.items=[]
     def add_food(self,food,quantity):
          self.items.append(food,quantity)
     def total(self):
          total=0
          for food,quantity in self.items:
               total=total+food.get_price()*quantity
               return total()
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class upi(Payment):
     def pay(self,amount):
          print("payment done...!",amount,"using upi")
class card(Payment):
     def pay(self,amount):
          print("payment done...!",amount,"using card")

print("--------hotel----------")
customer=customer("shifna")
hotel=hotel("kv hotel")

biriyani=food("biriyani","120")
chapathicombo=food("chapathicombo","30")
porattacombo=food("porattacombo","30")

hotel.add_food("biriyani")
hotel.add_food("chappathicombo")
hotel.add_food("porattacombo")


hotel.show_food()

print("-------------order--------------")
order=order()
order.add_item("chapathicombo","2")
order.add_item("biriyani","2")

print("-----------billing---------------")
amount=order.total()
print("pay:",amount)
print("------------payment--------------")
payment=upi()
payment.pay(amount)

print("------------delivery---------------")
delivery1=delivery("rahul")
delivery.get_food()















          
     


               

     
     
          
          
          
    

          
            

        

















     

    
    
          
    