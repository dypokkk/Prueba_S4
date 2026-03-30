from functions import *

students = []
option = 1
id = 0
result = {}

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
        SearchStudent(students)
        option = Option(option)
    elif option == 4:
        UpdateStudents(students)
    elif option == 5:
        print("Remove student")
    elif option == 0:
        print("Exit")
