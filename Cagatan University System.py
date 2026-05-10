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
    print("3. Exit")
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
                            
    print("STUDENT RECORD ADDED SUCESSFULLY!")

#view student records
def view_students():

    print("\n======== STUDENT RECORDS ========\n")

    if not os.path.exists(file_name):
        print("No student records found!!\n")
        return
    
    with open(file_name, "r") as file:
        records = file.readlines()


        for record in records:
            data = record.strip().split("|")

            print(
                f"Name: {data[1]} | "
                f"Age: {data[2]} | "
                f"Course: {data[7]} | "
                f"Section: {data[5]} | "
                f"ID: {data[3]}"
            )
        
def main():
    while True:
        main_menu()
        choice = input("Enter your choice: \n")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
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
