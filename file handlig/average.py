
f = open("students.txt", "w")

for i in range(5):
    name = input("Enter student name: ")
    mark = int(input("Enter mark: "))

    f.write(name + "," + str(mark) + "\n")

f.close()
f = open("students.txt", "r")

students = f.readlines()

total = 0
count = 0

print("\nStudent Details:")

for line in students:
    data = line.strip().split(",")

    name = data[0]
    mark = int(data[1])

    print(name, "-", mark)

    total = total + mark
    count = count + 1

f.close()

average = total / count
print("\nAverage mark:", average)

print("\nStudents above average:")

for line in students:
    data = line.strip().split(",")

    name = data[0]
    mark = int(data[1])

    if mark > average:
        print(name)