


f = open("application.txt", "w")

for i in range(2):
    print("Activity", i + 1)

    activity = input("Enter the activity: ")

    f.write("Activity: " + activity + "\n")
    f.write("\n")

f.close()


f = open("application.txt", "r")

lines = f.readlines()

for line in lines:
    print(line, end="")

f.close() 


