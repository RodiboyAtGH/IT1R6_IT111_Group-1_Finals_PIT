import hashlib
import os

print("======== STUDENT RECORD SYSTEM ========")
print("\nHello Rhuddens!\n\nWelcome to Cagatan University Student Record System!\n")

#menu option
def main_menu():
    print("======================================")
    print("Please select an option:")
    print("1. Add Student")
    print("2. View Student Records")
    print("3. Search Student Record")
    print("4. Delete Student Record")
    print("5. Update Student Record")
    print("6. Exit")
    print("======================================")  

#add student option
file_name = "students.txt"

def hash_id(student_ID):
    return hashlib.sha256(student_ID.encode()).hexdigest()

def add_student():
    print("\n===== ADD STUDENT =====\n")
    print("Note: Please fill out the following information: \n")
    
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    student_ID = input("Enter Student ID: ")
    password = input("Enter Password: ")
    section = input("Enter Section: ")
    year_level = input("Enter Year Level: ")
    course = input("Enter Course: ")
    
    hashed_id = hash_id(student_ID)
    
    #check duplicates
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            records = file.readlines()

            for record in records:
                data = record.strip().split("|")
        
                if data[0] == hashed_id:
                    print("Student ID already exists!")
                    return
                
    with open(file_name, "a") as file:
        file.write(
            f"{hashed_id}|{name}|{age}|{student_ID}|"
            f"{password}|{section}|{year_level}|{course}\n"
                )
                            
    print("\n\nSTUDENT RECORD ADDED SUCESSFULLY!")

#view student records
def view_students():

    print("\n======== STUDENT RECORDS ========\n")

    if not os.path.exists(file_name):
        print("Error. No student records found!\n")
        return
    
    with open(file_name, "r") as file:
        records = file.readlines()


        for record in records:
            data = record.strip().split("|")

            print(
                f"Name: {data[1]}  | "
                f"Age: {data[2]} | "
                f"Course: {data[7]} | "
                f"Section: {data[5]} | "
                f"ID: {data[3]}"
            )


#Search student record
def search_student():
    print("\n======== SEARCH STUDENT RECORD ========\n")
    search_id = input("Enter Student ID to search: ")
    hashed_search_id = hash_id(search_id)

    if not os.path.exists(file_name):
        print("Error. No student records found!\n")
        return
    
    with open(file_name, "r") as file:
        records = file.readlines()

        for record in records:
            data = record.strip().split("|")

            if data[3] == search_id:
                print("\nStudent Found!")
                print("--------------------------")
                print(f"Name        : {data[1]}")
                print(f"Age         : {data[2]}")
                print(f"Student ID  : {data[3]}")
                print(f"Password    : {data[4]}")
                print(f"Section     : {data[5]}")
                print(f"Year Level  : {data[6]}")
                print(f"Course      : {data[7]}")
                print("--------------------------")
                return
        
        print("Student record not found.")

#Delete student record
def delete_student():
    print("\n======== DELETE STUDENT RECORD ========\n")
    delete_id = input("Enter Student ID to delete: ")
    hashed_delete_id = hash_id(delete_id)

    if not os.path.exists(file_name):
        print("Error. No student records found!\n")
        return
    
    with open(file_name, "r") as file:
        records = file.readlines()

    with open(file_name, "w") as file:
        for record in records:
            data = record.strip().split("|")

            if data[0] != hashed_delete_id:
                file.write(record)
            else:
                print("Student record deleted successfully.")

            
#Update or edit student record
def update_student():
    print("\n======== UPDATE STUDENT RECORD ========\n")
    update_id = input("Enter Student ID to update: ")
    hashed_update_id = hash_id(update_id)

    if not os.path.exists(file_name):
        print("Error. No student records found!\n")
        return
    
    with open(file_name, "r") as file:
        records = file.readlines()

    with open(file_name, "w") as file:
        for record in records:
            data = record.strip().split("|")

            if data[0] == hashed_update_id:
                print("Enter new details (leave blank to keep current value):")
                name = input(f"Name ({data[1]}): ") or data[1]
                age = input(f"Age ({data[2]}): ") or data[2]
                section = input(f"Section ({data[5]}): ") or data[5]
                year_level = input(f"Year Level ({data[6]}): ") or data[6]
                course = input(f"Course ({data[7]}): ") or data[7]

                file.write(
                    f"{hashed_update_id}|{name}|{age}|{data[3]}|"
                    f"{data[4]}|{section}|{year_level}|{course}\n"
                )
                print("Student record updated successfully.")
            else:
                file.write(record)

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Exiting program. Goodbye Rhuddens!")
            break
        else:
            print("Invalid. Please try again.")

#calling area
main()
      

    


# NOT YET EDITED
print("Please Login:")
id_number = input("ID Number: ")
password = input("Password: ")

if id_number == "2025010203" and password == "gwaposirhuddomg":
    print("\nLogin Successful! Welcome Rhuddens!")
    print("Coming Soon pa ang features mwehehehe")

else:
    print("Gagi ka! Wrong ID Number or Password! Try Again!")
