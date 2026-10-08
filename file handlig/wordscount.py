f = open("students.txt", "r")

word = input("Enter word: ")

data = f.read()

count = data.count(word)

print("Word occurs", count, "times")

f.close()