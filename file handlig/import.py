while True:
    print("\n1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Exit")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        f = open("students.txt", "a")

        name = input("Enter the name: ")
        age = input("Enter the age: ")
        dept = input("Enter the dept: ")

        f.write(name + "," + age + "," + dept + "\n")
        f.close()

    elif choice == 2:
        f = open("students.txt", "r")
        print("Student details:")

        for line in f:
            print(line, end="")

        f.close()

    elif choice == 3:
        search = input("Enter the name to search: ")

        f = open("students.txt", "r")
        found = False

        for line in f:
            data = line.strip().split(",")

            if data[0] == search:
                print("Name:", data[0])
                print("Age:", data[1])
                print("Dept:", data[2])
                found = True

        f.close()

        if not found:
            print("Not found")

    elif choice == 4:
        print("Exit")
        break

    else:
        print("Invalid choice")