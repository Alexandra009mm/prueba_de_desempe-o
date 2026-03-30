from funtions import  * #Here, the import function is for registering students.
list_student = []#this list is for saveing study information 
keep_registe = "yes"
while keep_registe == "yes":
    try:
        option= (input(f"""
            ╔════════════════════════════════════════════════════════════╗
                    WELCOME TO THE SALES RECORD RIWI STORE!!             
            ╚════════════════════════════════════════════════════════════╝
                        ╔════════════════════════════╗
            ------------------------sistem students ---------------------------------
                        ╚════════════════════════════╝
            1. Add students.
            2. show list students.
            3. show total information students.
            4. update information.
            5. remove student. 
            6. exit.
            --------------------------------------------------------------                   
            enter a option => """)).strip()
                
        if option =="1":
            register_student(list_student)

        elif option == "2":
            consult_list(list_student)

        elif option == "3":
            show_inf(list_student)

        elif option == "4":
            update_student(list_student)

       
        elif option == "5":
            delete_student(list_student)

        elif option == "6":

            print ("Exting...")
            print()
        
            keep_register = "no"
            break


    except ValueError:
        print("Error, enter option invalide")



