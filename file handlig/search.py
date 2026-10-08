f = open("students.txt", "r")

word = input("Enter word to search: ")

data = f.read()

if word in data:
    print("Word found")
else:
    print("Word not found")

f.close()