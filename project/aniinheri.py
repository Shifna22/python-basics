# Create an Animal parent class with a method eat(). Create a Dog child class that
# inherits from Animal and has its own method bark(). Create a Dog object and call
# both method


class animal:
    def dogeat():
        print("dog eat bones")
class dog(animal):
    def dogbark():
        print("dog bark")
animal.dogeat()
dog.dogbark()