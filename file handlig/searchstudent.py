
f = open("students.txt", "w")

for i in range(2):
    name = input("Enter student name: ")
    f.write(name + "\n")

f.close()


f = open("students.txt", "r")
search_name = input("Enter name to search: ")
students = f.readlines()
found = False

for name in students:
    if name.strip() == search_name:
        found = True
        break

if found:
    print("Student found")
else:
    print("Student not found")

f.close()



    
    



