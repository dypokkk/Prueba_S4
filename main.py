from functions import *

students = []
option = 1
id = 0
s_option = 0

option = Option(option)

while option != 0:
    if option > 5:
        print("Write a valid number for execute the program. (1-6)")
        option = Option(option)
    elif option == 1:
        name, age, program, state = AddStudent()
        addToStudent(students, id, name, age, program, state)
        option = Option(option)
    elif option == 2:
        ShowStudents(students)
        option = Option(option)
    elif option == 3:
        search_student(students, s_option)
        option = Option(option)
    elif option == 4:
        print("First write datas and next search the student to update.")
        while s_option == 0:
            try:
                age, program, status = AddNewStudent()
                update_student(students, s_option, name,
                                    int(age) if age else None, 
                                    program if program else None,
                                    status if status else None)
                break
            except ValueError:
                print("Write a valid number.")
        
        option = Option(option)
    elif option == 5:
        remove_student(students, s_option)
        option = Option(option)

    elif option == 0:
        print("Exit")
