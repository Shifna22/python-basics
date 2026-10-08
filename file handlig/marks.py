f = open("attendance.txt", "r")

lines = f.readlines()

for i in range(0, len(lines), 4):
    name = lines[i]
    marks = lines[i + 2]

    if marks.strip() == "marks:":
        continue

    mark = int(marks.split(":")[1])

    if mark > 75:
        print(name, end="")

f.close()