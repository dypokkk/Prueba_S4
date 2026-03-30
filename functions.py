def ShowStudents(students):
    for i, e in enumerate(students):
        print(f"{e['ID']}. Name: {e['Name']}. Age: {e['Age']} Program: {e['Program']}. State: {e['State']}.")

def Option(option):
    try:
        option = int(input("""       Hi!, Welcome.
¿what do you like to do today?
1. Add student.
2. Show student list.
3. Search student.
4. Update student.
5. Remove student.
0. Exit
Write the option you choose: """))
    except ValueError:
        print("Escoge una opción válida")
        Option(option)
    return option

def AddStudent(students, id):
    name = input("Put the name of the student.").lstrip().lower()
    program = input("Put the program of the student.").lstrip().lower()
    state = ""
    age = 0
    while state != "active" or state != "inactive":
        state = input("Which is the state of the student (Active/Inactive)").lstrip().lower()
        if state == "active" or state == "inactive":
            break
        else:
            print("Invalid input, please write if the student are inactive or active.")
        
    while age <= 0:
        try:
            age = int(input("Write the age of the student."))
        except ValueError:
            print("Write a valid number.")
            if age <= 0:
                print("Write a valid number.")
    id += 1  
    students.append({"ID":id, "Name":name, "Age":age, "Program":program, "State":state})
    print("Student added succesfully!")
    return students, id

def SearchStudent(students):
    Looking_for = 0
    while Looking_for < 3 and Looking_for < 1:
            try:
                Looking_for = int(input("How do you like to search student.\n1. ID\n2. Name\n3. Exit."))
            except ValueError:
                print("Write a valid number.")
                if Looking_for > 3 and Looking_for < 1:
                    print("Write a valid number.")
            if Looking_for == 1:
                try:
                    ID_Looking = int(input("Number of ID for the student."))
                    result = next((item for item in students if item.get("ID") == ID_Looking), "The student has not yet been created.")
                    print(result)
                    return result
                except ValueError:
                    print("Write a valid number.")
                except IndexError:
                    print("The student has not yet been created.")
                    
            elif Looking_for == 2:
                name_looking = ""
                    
                while name_looking == "":
                    try:
                        name_looking = input("Write the name of the student to search.").lstrip().lower()
                        result = next((item for item in students if item.get("Name") == name_looking), "The student has not yet been created.")
                        print(result)
                        return result
                    except IndexError:
                        print("The student has not yet been created.")
            elif Looking_for == 3:
                break
                
def UpdateStudents(students):
    return_ = SearchStudent(students)
    n_age = input()
    n_program = input()
    n_state = input()
    