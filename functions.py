def register_student(list_student):
    keep_register = "yes"  # control loop to keep adding students
    while keep_register == "yes":  
        try:
            student_ID = 0
            # loop until a valid positive ID is entered
            while student_ID <= 0 :
                try:
                    student_ID = int(input("\nEnter an ID: ")) 
                    print("-" * 40 )
                    if student_ID <= 0:
                        print ("Error, the ID must be a positive integer")
                        print("-" * 40)
                        continue
                except ValueError:
                    print("Error, the ID must be a numeric data")
                    print("-" * 40) 
                    continue
#---------------------------------------------------------------------------------
            # loop until name is not empty
            a = True
            while a:
                student_name = input("\nenter the student name: ").lower().strip()
                print("-" * 40)
                if not student_name:
                    print("Try again, enter a name please.")
                    print("-" * 40)
                    continue
                else:
                    break
#---------------------------------------------------------------------------------
            # loop until valid positive age
            b = True
            while b:
                try:
                    age = int(input("\nenter your age: "))
                    print("-" * 40)
                    if age <= 0:
                        print("Error, enter age invalide")
                        print("-" * 40)
                        continue 
                    else:
                        break
                except ValueError:
                    print("Error, enter a number")
                    print("-" * 40)
            
#--------------------------------------------------------------------------------- 
            # loop until course is between 1 and 11
            c = True
            while c:
                try:
                    course = int(input("\nenter your course: "))
                    print("-" * 40)
                    if 1 <= course <= 11:
                        break
                    else:
                        print("Error, enter a grade (1-11)")
                        continue 
                except ValueError:
                    print("Error, enter a number")
                    print("-" * 40)
                    continue
#---------------------------------------------------------------------------------
            # loop until status is valid
            d = True
            while d:
                status = input("\nWhat is the student's status? active/inactive: ").lower().strip()
                print("-" * 40)
                if status == "active": 
                    break
                elif status == "inactive":
                    break
                else:
                    print("enter status valide")
                    print("-" * 40)
                    continue
#---------------------------------------------------------------------------------
            # create dictionary with student data
            inf_students= {
                "id":student_ID,
                "name": student_name,
                "age":age,
                "course":course,
                "status":status
            }

            # add student to list
            list_student.append(inf_students)

            # ask if user wants to continue
            keep_register = input("Do you want to register another student? yes/no ").lower().strip()
            
            # validate answer
            if keep_register not in ["yes", "no"]:
                print("invalid option, try again")
                keep_register = "yes"
        
        except Exception:
            print("enter input invalide :/")
            print("-" * 40)
            continue

    return list_student

#-----------------------------------------------------------------------------------
def consult_list(list_student):
    print("""╔════════════════════════════╗
       LIST OF STUDENTS 
╚════════════════════════════╝\n""".center(60))  # title
    print("student name:\n")
    for student in list_student:
        print(student["name"])  # print only names

#-----------------------------------------------------------------------------------
def show_inf(list_student): 
    print("-"*40)
    print("\nSTUDENT INFORMATION LIST:".center(30))  # title
    print("-"*40)
    for student in list_student:
        print("ID:", student["id"])
        print("name:", student["name"])
        print("age:", student["age"])
        print("course:", student["course"])
        print("status:", student["status"])
        print("-" * 40)  # separator

#-----------------------------------------------------------------------------------

def update_student(list_student):

    # check if list is empty
    if len(list_student) == 0:
        print("list empty :/")
        print("-" * 40)
        return
    
    # get student ID
    try:
        ask_student = int(input("enter student ID: ")) 
    except ValueError:
        print("Invalid ID :/")
        print("-" * 40)
        return

    # ask what to update
    data = input("what do you want to update (age, course, status): ").lower().strip()

    # search student by ID
    for student in list_student:
        if student["id"] == ask_student: 

            # update age
            if data == "age":
                try:
                    new_data = int(input("enter new age: "))
                    student["age"] = new_data
                except ValueError:
                    print("invalid age :/")
                    return

            # update course
            elif data == "course":
                try:
                    new_data = int(input("enter update course: "))
                    student["course"] = new_data
                except ValueError:
                    print("invalid course :/")
                    return

            # update status
            elif data == "status":
                new_data = input("enter status: ").lower().strip()
                if new_data in ["active", "inactive"]:
                    student["status"] = new_data
                else:
                    print("invalid status :/")
                    return
            else:
                print("invalid field :/")
                return

            print("updated successfully")
            return

    # if not found
    print("student not found :/")

#-----------------------------------------------------------------------------------

def delete_student(list_student):
    # get student name
    name = input("\nEnter the name of the student to delete: ").lower().strip()

    # search by name
    for student in list_student:
        if student["name"].lower() == name:

            # confirm deletion
            confirm = input(f"Are you sure you want to delete '{student['name']}'? (yes/no): ").lower().strip()
            if confirm == "yes":
                list_student.remove(student)
                print(f"student '{name}' deleted successfully!\n")
            else:
                print("Deletion cancelled.\n")
            return

    # if not found
    print(f"student '{name}' not found :/\n")