import hashlib
import os

print("======== STUDENT RECORD SYSTEM ========")
print("\nHello Rhuddens! Welcome to Cagatan University Student Record System!\n")

file_name = "students.txt"

def hash_id(student_ID):
    return hashlib.shan256(student_ID.encode()).hexdigest()

def add student():
    print("\n===== ADD STUDENT =====\n")
    print("Note: Please fill out the following information: /n")

name = input("Enter Name: ")
    age = input("Enter Age: ")
    student_ID = input("Enter Student ID: ")
    password = input("Enter Password: ")
    section = input("Enter Section: ")
    year_level = input("Enter Year Level: ")
    course = input("Enter Course: ")

hash_id = hash_id(student_ID)

if os.path.exist(file_name):
    with open(file_name, "r") as file:
        records = file.readlines()

    for record in records;
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


      

    


# NOT YET EDITED
print("Please Login:")
id_number = input("ID Number: ")
password = input("Password: ")

if id_number == "2025010203" and password == "gwaposirhuddomg":
    print("\nLogin Successful! Welcome Rhuddens!")
    print("Coming Soon pa ang features mwehehehe")

else:
    print("Gagi ka! Wrong ID Number or Password! Try Again!")
