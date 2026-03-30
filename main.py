from functions import *

students = []
option = 1
id = 0

option = Option(option)

while option != 0:
    if option > 5:
        print("Write a valid number for execute the program. (1-6)")
        option = Option(option)
    elif option == 1:
        students, id = AddStudent(students, id)
        option = Option(option)
        
    elif option == 2:
        ShowStudents(students)
        option = Option(option)
    elif option == 3:
        print("Search student")
        Looking_for = 0
        while Looking_for < 2 and Looking_for < 1:
            try:
                Looking_for = int(input("How do you like to search student.\n1. ID\n2. Name"))
            except ValueError:
                print("Write a valid number")
            if Looking_for == 1:
                print("ID")
            elif Looking_for == 2:
                print("Name")
    elif option == 4:
        print("Update student")
    elif option == 5:
        print("Remove student")
    elif option == 0:
        print("Exit")
