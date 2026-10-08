# Create a vehicle management system using all four OOP concepts. Create a
# parent Vehicle class containing common vehicle information and a protected/private
# property. Create Car, Bike, and Bus child classes. Each class should have its
# # own start() or calculate_fare() behaviour


class vehicle:
    def __init__(self,name,no):
        self.name=name  
        self.no=no                                                                          
    def display(self):
        print("name",self.name)
        print("fare",self.no)
    def get_no(self):
        return self.no
    def start(self):
        print("start by:")

class car(vehicle):
    def start(self):
        print("start by key")
class bike(vehicle):
    def start(self):
        print("start by key")
class bus(vehicle):
    def calculate_fare(self,distance):
        return distance*5
bus=bus("benz","kl00231")
car=car("toyoto","kl00001")
bike=bike("passionpro","kl0034")

bike.display()
car.start()
bike.start()
print("bus fare:",bus.calculate_fare(5))



