# Create a Person class with a show_person() method. Create a Student class that
# inherits from Person and has a show_student() method. Create
# a CollegeStudent class that inherits from Student and has
# a show_college() method. Create a CollegeStudent object and call all three
# methods

class person:
    def show_person():
        print("name is shifna")
class student(person):
    def show_student():
        print("shifna is student")
class collegestudent(student):
    def show_college():
        print("arts collecge")
collegestudent1=collegestudent()
person.show_person()
student.show_student()
collegestudent.show_college()