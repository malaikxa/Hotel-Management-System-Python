# from types import new_class
#
students = []

while True:
    # print("\n----- Student Management -----")
    print("1. Add student")
    print("2. Update student")
    print("3. Remove student")
    print("4. Display all students")
    print("5. Search student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        students.append(name)
        print(name, "added successfully.")

    elif choice == 2:
        old = input("Enter the name you want to update: ")
        if old in students:
            new = input("Enter new name: ")
            index = students.index(old)
            students[index] = new
            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == 3:
        name = input("Enter the name you want to remove: ")
        if name in students:
            students.remove(name)
            print(name, "removed successfully.")
        else:
            print("Student not found.")

    elif choice == 4:
        if students:
            print("Student List:", students)
        else:
            print("No students to display.")

    elif choice == 5:
        name = input("Enter student name to search: ")
        if name in students:
            print(name, "is in the list.")
        else:
            print(name, "not found.")

    elif choice == 6:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")






