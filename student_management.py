student = {}
while True:    
    print("""
      1. Add Student
      2. View Students
      3. Search Student
      4. Calculate Average Marks
      5. Find Topper
      6. Delete Student
      7. Exit
      """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        course = input("Enter course name: ")
        marks = float(input("Enter marks: "))
        student[name] = [course, marks]
        print("Student added successfully!")
    elif choice == 2:
        print("Viewing all students...")
        print("Student Name | Course | Marks")
        print("-------------------------------")
        for i in student:
            print(i, "|", student[i][0], "|", student[i][1])
    elif choice == 3:
        search_name = input("Enter student name to search: ")
        if search_name in student:
            print("Student found!")
            print("Name:", search_name)
            print("Course:", student[search_name][0])
            print("Marks:", student[search_name][1])
        else:
            print("Student not found.")
    elif choice == 4:
        print("Displaying average marks of all students")
        if student:
            total_marks = sum(student[i][1] for i in student)
            average_marks = total_marks / len(student)
            print("Average Marks:", average_marks)
        else:
            print("No students available to calculate average marks.")
    elif choice == 5:
        print("Finding the topper...")
        if student:
            topper = max(student, key=lambda x: student[x][1])
            print("Topper is:", topper)
            print("Course:", student[topper][0])
            print("Marks:", student[topper][1])
        else:
            print("No students available to find the topper.")
    elif choice == 6:
        delete_name = input("Enter student name to delete: ")
        if delete_name in student:
            del student[delete_name]
            print("Student deleted successfully!")
        else:
            print("Student not found.")
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")