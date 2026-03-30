def ShowStudents(students):
    for i, e in enumerate(students):
        print(f"{e['ID']}. Name: {e['Name']}. Age: {e['Age']} Program: {e['Program']}. State: {e['State']}.")

def Option(option):
    option = int(input("""       Hi!, Welcome.
¿what do you like to do today?
1. Add student.
2. Show student list.
3. Search student.
4. Update student.
5. Remove student.
0. Exit
Write the option you choose: """))
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