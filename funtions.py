

def register_student(list_student):
    keep_register = "yes"
    while keep_register:
        try:
            student_ID = 0
            while student_ID <= 0 :
                    
                try:
                    student_ID = int(input("Enter an ID: "))   

                    if student_ID <= 0:
                        print ("Error, the ID must be a positive integer")
                        continue
                except ValueError:
                    print("Error, the ID must be a numeric data")
                    
        

            a = True
            while a:
                    
                    student_name = input("enter the student name: ")
                    if not student_name:
                        print("Try again, enter a name please.")
                        continue
                    else:
                        a = False


            b = True
            while b:
                try:
                    age = int(input("enter your age: "))
                    if age <= 0:
                        print("Error, enter age invalide")
                        continue 
                    else:
                        break
                except ValueError:
                    print("Error, enter a number")
            
            c = True
            while c:
                try:
                    course = int(input("enter your course 1-11: "))
                    if 1 <= course <= 11:
                        break

                    else:
                        print("Error, enter a grade 1-11")
                        continue 

                except ValueError:
                    print("Error, enter a number")

            d = True
            while d:
                try:
                    status = input("What is the student's status? active/inactive: ").lower().strip()
                    if status == "active":
                        break
                    elif status == "inactive":
                        break
                    else:
                        print("enter status valide")
                        continue

                except TypeError:
                    print("enter a status valide.")

                
            inf_students= {
                "id":student_ID,
                "name": student_name,
                "age":age,
                "course":course,
                "status":status
                }
            list_student.append(inf_students)

       

            keep_register = input("Do you want to register another student? yes/no ").lower()
            if keep_register == "yes":
                continue
            elif keep_register == "no":
                break
            else: 
                print("try again")
                continue
        
            
        except TypeError:
            print("enter input invalide")


    keep_register = False
    return list_student

def consult_list(list_student):
    print("\n")
    print("list students:".center(60, "-"))
    for i in list_student:
       
        print("name:", i["name"])
        print("\n")
     
def show_inf(list_student): 
    print("list information students:".center(60, "-"))
    for i in list_student:
        print("ID:", i["id"])
        print("name:", i["name"])
        print("age:", i["age"])
        print("course:", i["course"])
        print("status:", i["status"])
        print("-" * 40)

def update_student(list_student):

    if len(list_student) == 0:
        print("list empty")
        return
    
    ask_student = input("enter  student ID:  ").strip()
    data = input("what do you want to update (age, course,status): ").lower()

    for student in list_student:
        a = True
        while a:
            if student["id"] == ask_student:

                for est in list_student:

                    if data in est["age"]:
                        new_data = input("enter     new age: ")

                        student[data] = new_data
                        print("updated successfully")

                
                    elif data in est["course"]:
                        new_data = int(input("enter update course: "))
                        student[data] = new_data
                        print("updated successfully")


                            
                    elif data in est["status"]:
                        new_data = input("enter status: ")
                        student[data] = new_data
                        print("updated successfully")
            

            return

    print("student not found")

          
        

    # If student is not found
    print("student not found")
    
def delete_student(list_student):
    name =input ("\nEnter the name of the student to delete: ").lower()

    for student in list_student:
        if student["name"].lower() == name:
            

            confirm = input(f"  Are you sure you want to delete '{list_student['name']}'? (yes/no): ").lower()
            if confirm == "yes":
                list_student.remove(student)
                print(f"  student '{name}' deleted successfully!\n")
            else:
                print(" Deletion cancelled.\n")
            return

    print(f" student '{name}' not found.\n")

        