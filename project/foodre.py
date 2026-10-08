from abc import ABC, abstractmethod


# Parent class
class User:
    def __init__(self, name):
        self.name = name


# Inheritance
class Customer(User):
    def order_food(self):
        print(self.name, "placed an order")


class DeliveryPartner(User):
    def deliver(self):
        print(self.name, "is delivering the order")


# Food class
class Food:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price


# Restaurant class
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.food = []

    def add_food(self, food):
        self.food.append(food)

    def show_food(self):
        print("\nRestaurant:", self.name)

        for item in self.food:
            print(item.name, "- ₹", item.get_price())


# Order class
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, food, quantity):
        self.items.append((food, quantity))

    def total(self):
        total = 0

        for food, quantity in self.items:
            total = total + food.get_price() * quantity

        return total


# Abstract Payment class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Polymorphism
class UPI(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class Card(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Card")


# Create objects
customer = Customer("Shifna")

restaurant = Restaurant("Food Palace")

burger = Food("Burger", 150)
pizza = Food("Pizza", 300)

restaurant.add_food(burger)
restaurant.add_food(pizza)


# Show food
restaurant.show_food()


# Create order
order = Order()

order.add_item(burger, 2)
order.add_item(pizza, 1)


# Calculate total
amount = order.total()

print("\nOrder Total:", amount)


# Payment
payment = UPI()
payment.pay(amount)


# Delivery
delivery = DeliveryPartner("Rahul")
delivery.deliver()