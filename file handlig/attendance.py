
f = open("attendance.txt", "w")

for i in range(2):
    print("\nEnter details:", i + 1)

    name = input("Enter name : ")
    attendance = input("Enter attendance: ")
    marks = input("Enter marks: ")
    f.write("Name: " + name + "\n")
    f.write("Attendance: " + attendance + "\n")
    f.write("marks:" + marks + "\n")
    f.write("\n")

f.close()



f = open("attendance.txt", "r")

print("\nAttendance List:")

lines = f.readlines()

for line in lines:
    print(line, end="")

f.close()


f = open("attendance.txt", "a")

print("\nAdd another student")

name = input("Enter name: ")
attendance = input("Enter attendance: ")
marks = input("Enter marks: ")

f.write("\nName: " + name + "\n")
f.write("Attendance: " + attendance + "\n")
f.write("marks:" + marks + "\n")

f.close()

print("\nStudent added successfully")