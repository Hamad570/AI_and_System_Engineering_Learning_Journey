import os

FILE_NAME = "students.txt"

def add_student():

    print("\n--- Add Student ---")
    roll_no = input("Enter Roll Number: ")

    if os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "r")
        for line in file:
            # Har line ka pehla hissa (roll number) nikaal kar check karna
            existing_roll = line.strip().split(",")[0]
            if existing_roll == roll_no:
                print("Error: This Roll Number already exists!")
                file.close()
                return  # Return karne se function yahin ruk jayega aur data save nahi hoga
        file.close()
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    
    # Data ko comma se separate karke file mein save karna
    file = open(FILE_NAME, "a")
    file.write(roll_no + "," + name + "," + age + "," + grade + "\n")
    file.close()
    print("Record added successfully!")

def view_students():
    print("\n--- Student Records ---")
    if not os.path.exists(FILE_NAME):
        print("No records found. Database is empty.")
        return
        
    file = open(FILE_NAME, "r")
    for line in file:
        # Comma ke zariye data ko alag alag karna
        roll_no, name, age, grade = line.strip().split(",")
        print("Roll No:", roll_no, "| Name:", name, "| Age:", age, "| Grade:", grade)
    file.close()

def search_student():
    print("\n--- Search Student ---")
    if not os.path.exists(FILE_NAME):
        print("Database is empty.")
        return
        
    search_roll = input("Enter Roll Number to search: ")
    found = False
    
    file = open(FILE_NAME, "r")
    for line in file:
        roll_no, name, age, grade = line.strip().split(",")
        if roll_no == search_roll:
            print("\nStudent Found:")
            print("Roll No:", roll_no)
            print("Name:", name)
            print("Age:", age)
            print("Grade:", grade)
            found = True
            break
    file.close()
    
    if found == False:
        print("Student record not found.")

# --- Main Program Loop ---
while True:
    print("\n=== STUDENT DATABASE ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")