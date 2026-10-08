file = open("students.txt","w")

for i in range(3):
    name = input("Enter name: ")
    course = input("Enter course: ")
    college = input("Enter college: ")
    year = input("Enter year: ")

    file.write(name + "\n")
    file.write(course + "\n")
    file.write(college + "\n")
    file.write(year + "\n")
    file.write("\n")

file.close()

print("Students added successfully")