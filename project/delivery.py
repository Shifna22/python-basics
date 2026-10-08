from abc import ABC, abstractmethod

class User:
    def __init__(self, name):
        self.name = name


class Customer(User):
    def food_order(self):
        print(self.name, "placed order")


class Delivery(User):
    def food_deliver(self):
        print(self.name, "delivers your food")


class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class Hotel:
    def __init__(self, name):
        self.name = name
        self.food = []

    def add_food(self, food):
        self.food.append(food)

    def show_food(self):
        print("Hotel:", self.name)

        for item in self.food:
            print(item.name, "- ₹", item.get_price())


class Order:
    def __init__(self):
        self.items = []

    def add_food(self, food, quantity):
        self.items.append((food, quantity))

    def total(self):
        total = 0

        for food, quantity in self.items:
            total = total + food.get_price() * quantity

        return total


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print("Payment done:", amount, "using UPI")


class Card(Payment):
    def pay(self, amount):
        print("Payment done:", amount, "using Card")


# ---------------- MAIN PROGRAM ----------------

print("---------- HOTEL ----------")

customer1 = Customer("Shifna")

hotel1 = Hotel("KV Hotel")

biriyani = Food("Biriyani", 120)
chapathi_combo = Food("Chapathi Combo", 30)
porotta_combo = Food("Porotta Combo", 30)

hotel1.add_food(biriyani)
hotel1.add_food(chapathi_combo)
hotel1.add_food(porotta_combo)

hotel1.show_food()


print("\n---------- ORDER ----------")

order1 = Order()

order1.add_food(chapathi_combo, 2)
order1.add_food(biriyani, 2)

customer1.food_order()


print("\n---------- BILLING ----------")

amount = order1.total()

print("Total amount:", amount)


print("\n---------- PAYMENT ----------")

payment = UPI()

payment.pay(amount)


print("\n---------- DELIVERY ----------")

delivery1 = Delivery("Rahul")

delivery1.food_deliver()