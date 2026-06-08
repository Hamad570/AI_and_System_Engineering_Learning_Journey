import os

FILE_NAME = "notes.txt"

def create_note():
    print("\n--- Create New Note ---")
    title = input("Enter Note Title: ")
    
    # Check karna k is title ka note pehle se toh nahi bana hua
    if os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "r")
        for line in file:
            existing_title = line.strip().split(",")[0]
            if existing_title == title:
                print("Error: This note title already exists!")
                file.close()
                return
        file.close()

    content = input("Enter Note Content: ")
    
    # Note ko title aur content ke sath save karna
    file = open(FILE_NAME, "a")
    file.write(title + "," + content + "\n")
    file.close()
    print("Note saved successfully!")

def view_all_notes():
    print("\n--- All Notes ---")
    if not os.path.exists(FILE_NAME):
        print("No notes found. Notes file is empty.")
        return
        
    file = open(FILE_NAME, "r")
    for line in file:
        title, content = line.strip().split(",")
        print("Title:", title, "| Content:", content)
    file.close()

def delete_all_notes():
    print("\n--- Delete All Notes ---")
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME) # Poori file hi delete kar di
        print("All notes deleted successfully!")
    else:
        print("No notes file exists to delete.")

# --- Main Program Loop ---
while True:
    print("\n=== NOTES MANAGER ===")
    print("1. Create New Note")
    print("2. View All Notes")
    print("3. Delete All Notes")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == '1':
        create_note()
    elif choice == '2':
        view_all_notes()
    elif choice == '3':
        delete_all_notes()
    elif choice == '4':
        print("Exiting Notes Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")