import tkinter as tk
from tkinter import messagebox, simpledialog
import hashlib
import os
import re

# ================= FILE =================
file_name = "students.txt"

# ================= WINDOW =================
root = tk.Tk()
root.title("Student Record System")
root.geometry("1080x700")
root.configure(bg="lightblue")

# ================= FUNCTIONS =================
def hash_id(student_ID):
    return hashlib.sha256(student_ID.encode()).hexdigest()


def validate_password(password):
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"\d", password)
    has_symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    return has_upper and has_digit and has_symbol


# ================= ADD STUDENT =================
def add_student():

    add_window = tk.Toplevel(root)
    add_window.title("Add Student")
    add_window.geometry("400x500")
    add_window.configure(bg="lightblue")

    # Labels and Entries
    tk.Label(add_window, text="Name", bg="lightblue").pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    tk.Label(add_window, text="Age", bg="lightblue").pack()
    age_entry = tk.Entry(add_window)
    age_entry.pack()

    tk.Label(add_window, text="Student ID", bg="lightblue").pack()
    id_entry = tk.Entry(add_window)
    id_entry.pack()

    tk.Label(add_window, text="Password", bg="lightblue").pack()
    password_entry = tk.Entry(add_window, show="*")
    password_entry.pack()

    tk.Label(add_window, text="Section", bg="lightblue").pack()
    section_entry = tk.Entry(add_window)
    section_entry.pack()

    tk.Label(add_window, text="Year Level", bg="lightblue").pack()

    year_var = tk.StringVar()
    year_var.set("1st Year")

    year_menu = tk.OptionMenu(
        add_window,
        year_var,
        "1st Year",
        "2nd Year",
        "3rd Year",
        "4th Year"
    )
    year_menu.pack()

    tk.Label(add_window, text="Course", bg="lightblue").pack()
    course_entry = tk.Entry(add_window)
    course_entry.pack()

    # ================= SAVE FUNCTION =================
    def save_student():

        name = name_entry.get()
        age = age_entry.get()
        student_ID = id_entry.get()
        password = password_entry.get()
        section = section_entry.get()
        year_level = year_var.get()
        course = course_entry.get()

        # ================= EMPTY FIELD VALIDATION =================
        if name == "":
            messagebox.showerror(
                "Error",
                "Name field is required."
            )
            name_entry.focus()
            return

        if age == "":
            messagebox.showerror(
                "Error",
                "Age field is required."
            )
            age_entry.focus()
            return

        if student_ID == "":
            messagebox.showerror(
                "Error",
                "Student ID field is required."
            )
            id_entry.focus()
            return

        if password == "":
            messagebox.showerror(
                "Error",
                "Password field is required."
            )
            password_entry.focus()
            return

        if section == "":
            messagebox.showerror(
                "Error",
                "Section field is required."
            )
            section_entry.focus()
            return

        if course == "":
            messagebox.showerror(
                "Error",
                "Course field is required."
            )
            course_entry.focus()
            return

        # ================= ID VALIDATION =================
        if not student_ID.isdigit():
            messagebox.showerror(
                "Error",
                "Student ID must contain numbers only."
            )

            id_entry.delete(0, tk.END)
            id_entry.focus()

            return

        # ================= PASSWORD VALIDATION =================
        if not validate_password(password):
            messagebox.showerror(
                "Error",
                "Password must contain:\n"
                "- CAPITAL letter\n"
                "- NUMBER\n"
                "- SYMBOL"
            )

            password_entry.delete(0, tk.END)
            password_entry.focus()

            return

        hashed_id = hash_id(student_ID)

        # ================= DUPLICATE CHECK =================
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                records = file.readlines()

                for record in records:
                    data = record.strip().split("|")

                    if data[0] == hashed_id:
                        messagebox.showerror(
                            "Error",
                            "Student ID already exists!"
                        )

                        id_entry.delete(0, tk.END)
                        id_entry.focus()

                        return

        # ================= SAVE RECORD =================
        with open(file_name, "a") as file:
            file.write(
                f"{hashed_id}|{name}|{age}|{student_ID}|"
                f"{password}|{section}|{year_level}|{course}\n"
            )

        messagebox.showinfo(
            "Success",
            "Student record added successfully!"
        )

        add_window.destroy()

    tk.Button(
        add_window,
        text="Save Student",
        command=save_student,
        bg="green",
        fg="white",
        relief="flat",
        bd=0,
        font=("Arial", 10, "bold"),
        padx=10,
        pady=5
    ).pack(pady=15)


# ================= VIEW STUDENTS =================
def view_students():

    display.delete(1.0, tk.END)

    if not os.path.exists(file_name):
        display.insert(tk.END, "No student records found.\n")
        return

    with open(file_name, "r") as file:
        records = file.readlines()

        if not records:
            display.insert(tk.END, "No student records available.\n")
            return

        for record in records:
            data = record.strip().split("|")

            display.insert(
                tk.END,
                f"Name: {data[1]}\n"
                f"Age: {data[2]}\n"
                f"Student ID: {data[3]}\n"
                f"Section: {data[5]}\n"
                f"Year Level: {data[6]}\n"
                f"Course: {data[7]}\n"
                f"-----------------------------\n"
            )


# ================= SEARCH STUDENT =================
def search_student():

    search_id = simpledialog.askstring(
        "Search",
        "Enter Student ID:"
    )

    if not search_id:
        return

    hashed_search_id = hash_id(search_id)

    display.delete(1.0, tk.END)

    if not os.path.exists(file_name):
        display.insert(tk.END, "No student records found.\n")
        return

    with open(file_name, "r") as file:
        records = file.readlines()

        for record in records:
            data = record.strip().split("|")

            if data[0] == hashed_search_id:

                display.insert(
                    tk.END,
                    f"Student Found!\n\n"
                    f"Name: {data[1]}\n"
                    f"Age: {data[2]}\n"
                    f"Student ID: {data[3]}\n"
                    f"Password: {data[4]}\n"
                    f"Section: {data[5]}\n"
                    f"Year Level: {data[6]}\n"
                    f"Course: {data[7]}\n"
                )
                return

    display.insert(tk.END, "Student record not found.\n")


# ================= DELETE STUDENT =================
def delete_student():

    delete_id = simpledialog.askstring(
        "Delete",
        "Enter Student ID:"
    )

    if not delete_id:
        return

    hashed_delete_id = hash_id(delete_id)

    if not os.path.exists(file_name):
        messagebox.showerror(
            "Error",
            "No student records found."
        )
        return

    with open(file_name, "r") as file:
        records = file.readlines()

    found = False

    with open(file_name, "w") as file:

        for record in records:
            data = record.strip().split("|")

            if data[0] != hashed_delete_id:
                file.write(record)
            else:
                found = True

    if found:
        messagebox.showinfo(
            "Success",
            "Student record deleted successfully."
        )
    else:
        messagebox.showerror(
            "Error",
            "Student record not found."
        )


# ================= UPDATE STUDENT =================
def update_student():

    update_id = simpledialog.askstring(
        "Update",
        "Enter Student ID:"
    )

    if not update_id:
        return

    hashed_update_id = hash_id(update_id)

    if not os.path.exists(file_name):
        messagebox.showerror(
            "Error",
            "No student records found."
        )
        return

    with open(file_name, "r") as file:
        records = file.readlines()

    updated = False

    with open(file_name, "w") as file:

        for record in records:
            data = record.strip().split("|")

            if data[0] == hashed_update_id:

                new_name = simpledialog.askstring(
                    "Update",
                    "Enter New Name:",
                    initialvalue=data[1]
                )

                new_age = simpledialog.askstring(
                    "Update",
                    "Enter New Age:",
                    initialvalue=data[2]
                )

                new_section = simpledialog.askstring(
                    "Update",
                    "Enter New Section:",
                    initialvalue=data[5]
                )

                new_year = simpledialog.askstring(
                    "Update",
                    "Enter New Year Level:",
                    initialvalue=data[6]
                )

                new_course = simpledialog.askstring(
                    "Update",
                    "Enter New Course:",
                    initialvalue=data[7]
                )

                file.write(
                    f"{hashed_update_id}|{new_name}|{new_age}|"
                    f"{data[3]}|{data[4]}|"
                    f"{new_section}|{new_year}|{new_course}\n"
                )

                updated = True

            else:
                file.write(record)

    if updated:
        messagebox.showinfo(
            "Success",
            "Student record updated successfully."
        )
    else:
        messagebox.showerror(
            "Error",
            "Student record not found."
        )


# ================= TITLE =================
title = tk.Label(
    root,
    text="CAGATAN UNIVERSITY - STUDENT RECORD SYSTEM",
    font=("Times New Roman", 24, "bold"),
    bg="lightblue"
)

title.pack(pady=15)

# ================= MAIN FRAME =================
main_frame = tk.Frame(root, bg="lightblue")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# ================= LEFT FRAME =================
left_frame = tk.Frame(main_frame, bg="lightblue")
left_frame.pack(side="left", fill="y", padx=30)

# ================= RIGHT FRAME =================
right_frame = tk.Frame(main_frame, bg="lightblue")
right_frame.pack(side="right", fill="both", expand=True)

# ================= BUTTON STYLE =================
button_style = {
    "width": 20,
    "font": ("Arial", 11, "bold"),
    "bg": "white",
    "fg": "black",
    "relief": "flat",
    "bd": 0,
    "cursor": "hand2",
    "highlightthickness": 0,
    "pady": 10
}

# ================= BUTTONS =================
tk.Button(
    left_frame,
    text="Add Student",
    command=add_student,
    **button_style
).pack(pady=8)

tk.Button(
    left_frame,
    text="View Students",
    command=view_students,
    **button_style
).pack(pady=8)

tk.Button(
    left_frame,
    text="Search Student",
    command=search_student,
    **button_style
).pack(pady=8)

tk.Button(
    left_frame,
    text="Delete Student",
    command=delete_student,
    **button_style
).pack(pady=8)

tk.Button(
    left_frame,
    text="Update Student",
    command=update_student,
    **button_style
).pack(pady=8)

tk.Button(
    left_frame,
    text="Exit",
    command=root.quit,
    bg="red",
    fg="white",
    relief="flat",
    bd=0,
    width=20,
    font=("Arial", 11, "bold"),
    cursor="hand2",
    pady=10
).pack(pady=8)

# ================= DISPLAY AREA =================
display = tk.Text(
    right_frame,
    width=70,
    height=25,
    font=("Spectral", 15),
    relief="flat",
    bd=2
)

display.pack(fill="both", expand=True)

# ================= RUN =================
root.mainloop()
