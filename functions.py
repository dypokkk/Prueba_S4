#Print all list
def ShowStudents(students):
    if students == {}:
        print("Not have data yet")
    else:
        for i, e in enumerate(students):
            print(f"ID: {e['ID']}. Name: {e['Name']}. Age: {e['Age']} Program: {e['Program']}. State: {e['State']}.")
#Just for options
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
#If press return don't crash the code
    except ValueError:
        print("Escoge una opción válida")
        Option(option)
    return option
#add student for the list
def addToStudent(students, id, name, age, program, state):
    id += 1
    students.append({"ID":id, "Name":name, "Age":age, "Program":program, "State":state})
    print("Student added succesfully!")
    return students, id
#inputs of the student the first time
def AddStudent():
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
    return name, age, program, state
#inputs for the update function
def AddNewStudent():
    program = input("Put the new program of the student.").lstrip().lower()
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
            age = int(input("Write the new age of the student."))
        except ValueError:
            print("Write a valid number.")
            if age <= 0:
                print("Write a valid number.")
    return age, program, state
#search the student
def search_student(students, s_option):
    while s_option == 0:
            #No error for input string
            try:
                s_option = int(input("Write if you want search by:\n1. ID\n2. Name"))
            except ValueError:
                print("Write a valid number.")
    if s_option == 1:
        l_id = int(input("Write the id that you wanna search"))
        for e in students:
            if e["ID"] == l_id:
                return e
        
    if s_option == 2:
        l_name = input("Write the name that you wanna search")
        for e in students:
            if e["Name"].lower() == l_name.lower():
                return e
    return None
#Update the student using search function
def update_student(students, s_option, name, new_age=None, new_program=None, new_state=None):
    e = search_student(students, s_option)
    if e:
        if new_age is not None: e["Age"] = int(new_age)
        if new_program is not None: e["Program"] = new_program
        if new_state is not None: e["State"] = new_state
        print(f"Estudiante '{name}' actualizado.")
        return True
    return False
#remove student with remove function
def remove_student(students, s_option):
    e = search_student(students, s_option)
    students.remove(e)
    print(f"remove succesfully")