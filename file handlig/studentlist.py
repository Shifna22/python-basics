f= open("students.txt", "a")
for i in range(2):
    name = input("Enter student name: ")
    f.write(name + "\n")
f.close()

print("Students added successfully")