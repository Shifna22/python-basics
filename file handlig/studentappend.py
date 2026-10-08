file = open("students.txt", "a")

name = input("Enter name: ")
course = input("Enter course: ")
college = input("Enter college: ")
year = input("Enter year: ")

file.write("Name: " + name + "\n")
file.write("Course: " + course + "\n")
file.write("College: " + college + "\n")
file.write("Year: " + year + "\n")

file.close()

print("Student added successfully")