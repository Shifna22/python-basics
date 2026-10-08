file = open("students.txt", "w")

for i in range(2):
    print("enter the details",i+1)
    name = input("Enter name: ")
    course = input("Enter course: ")
    college = input("Enter college: ")
    year = input("Enter year: ")

    file.write("name:" +name+ "\n")
    file.write("course:"+course+ "\n")
    file.write("college:" +college+ "\n")
    file.write("year:" +year+ "\n")
    file.write("\n")

file.close()

print("Students added successfully")
