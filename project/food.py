# Create a food ordering system using Encapsulation, Abstraction, Inheritance, and
# Polymorphism. Create a parent Food class with common food details and private
# price. Create Pizza, Burger, and Biryani child classes. Each child class should have
# its own calculate_price() or prepare() method with different behaviour


class food:
    def __init__(self, name, price):
        self.price = price
        self.name = name

    def display(self):
        print("name:", self.name)
        print("price:", self.price)

    def get_food(self):
        return self.price


class biriyani(food):
    def prepare(self):
        print("biriyani is preparing")


class burger(food):
    def calculate_price(self, quantity):
        print("price:", self.get_food() * quantity)


class pizza(food):
    def calculate_price(self, quantity):
        print("pizza price:", self.get_food() * quantity)


biriyani1 = biriyani("ckb", 200)
pizza1 = pizza("chicken", 300)
burger1 = burger("burgerbeef", 349)

biriyani1.display()
burger1.display()
pizza1.display()

pizza1.calculate_price(2)
burger1.calculate_price(1)











        
        
