while True:
  
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Note")
    print("4. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        note = input("Enter your note: ")

        f = open("notes.txt", "a")
        f.write(note + "\n")
        f.close()

        print("Note added successfully!")

    
    elif choice == "2":
        try:
            f = open("notes.txt", "r")

            notes = f.readlines()
            f.close()

            if len(notes) == 0:
                print("No notes found.")
            else:
                for i, note in enumerate(notes, 1):
                    print(i, ".", note.strip())

        except FileNotFoundError:
            print("No notes found.")

    
    elif choice == "3":
        search = input("Enter word to search: ")

        try:
            f = open("notes.txt", "r")
            notes = f.readlines()
            f.close()

            found = False

            for note in notes:
                if search.lower() in note.lower():
                    print("Found:", note.strip())
                    found = True

            if not found:
                print("Note not found.")

        except FileNotFoundError:
            print("No notes found.")

    
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")