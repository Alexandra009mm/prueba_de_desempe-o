from functions import  * # Import all functions from the module "functions" to manage student operations

list_student = [] # This list will store all student information (each student is likely a dictionary)
keep_register = "yes" # Control variable to keep the program running in a loop
#----------------------------------------------------------------------------------------------------------
print(f"""\n
════════════════════════════════════════════════════════════
            WELCOME TO THE SISTEM STUDENTS!!             
════════════════════════════════════════════════════════════""")

#----------------------------------------------------------------------------------------------------------

while keep_register == "yes": # Main loop that keeps showing the menu until the user decides to exit
    option= (input(f"""
-------------------------------------------------------------
╔════════════════════════════╗
            MENU
╚════════════════════════════╝
1. Add students.
2. show list students.
3. show total information students.
4. update information.
5. remove student. 
6. exit.
--------------------------------------------------------------                   
enter a option => """)).strip() # Show menu and remove extra spaces from input

#----------------------------------------------------------------------------------------------------------               
    if option =="1":
        register_student(list_student) # Call function to add a new student to the list
#----------------------------------------------------------------------------------------------------------
    elif option == "2":
        consult_list(list_student) # Call function to display all students in the list
#----------------------------------------------------------------------------------------------------------
    elif option == "3":
        show_inf(list_student) # Call function to show detailed or summarized student information
#----------------------------------------------------------------------------------------------------------
    elif option == "4":
        update_student(list_student) # Call function to update an existing student's information
#----------------------------------------------------------------------------------------------------------       
    elif option == "5":
        delete_student(list_student) # Call function to remove a student from the list
#----------------------------------------------------------------------------------------------------------
    elif option == "6":

        # Display exit message
        print("closing the program...")
        print("\n")
        print ("Thank you for using the student system.")
        keep_register = "no" # Change control variable to stop the loop
            # Exit the loop immediately
#----------------------------------------------------------------------------------------------------------            
    else:
        print("Error, enter option invalide :/\n")
        continue
