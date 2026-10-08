# Create a Camera class with a take_photo() method and a Phone class with
# a make_call() method. Create a Smartphone class that inherits from both classes.
# Create an object and use both methods

class camera:
    def take_photo():
        print("taking photo")

class phone:
    def make_call():
        print("making call")

class smartphone(camera,phone):
    pass

smartphone=smartphone()
camera.take_photo()
phone.make_call()

