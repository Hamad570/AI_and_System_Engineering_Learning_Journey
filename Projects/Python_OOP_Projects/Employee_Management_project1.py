# Project on Employee Management
#git add .
#git commit -m "refactor: major overhaul of project structure and file updates" -m "Restructured repository hierarchy, created subfolders, performed massive cleanup, and updated source files with new code modifications."
class Employee:
    def __init__(self, emp_id, name, salary, role):
        self.emp_id = emp_id          
        self.name = name              
        self.__salary = salary        
        self.__role = role            

    def get_salary(self, requester_id, requester_role):
        """
        Sirf HR ya woh Employee khud apni salary dekh sakta hai.
        """
        if requester_role == "HR" or requester_id == self.emp_id:
            return f"Rs. {self.__salary}"
        else:
            return "ACCESS DENIED: Aapko is employee ki salary dekhne ki ijazat nahi hai."


    def apply_increment(self, percentage, requester_role):
        """
        Sirf HR salary barha sakta hai, aur increment 0% se 50% ke darmiyan hona chahiye.
        """

        if requester_role != "HR":
            return "ERROR: Sirf HR department salary modify kar sakta hai!"
        

        if 0 < percentage <= 50:
            old_salary = self.__salary
            self.__salary += (self.__salary * percentage / 100)
            return f"SUCCESS: {self.name} ki salary Rs. {old_salary} se barha kar Rs. {self.__salary} kar di gayi hai."
        else:
            return "ERROR: Invalid Percentage! Increment 1% se 50% ke darmiyan hona chahiye."

    def get_role(self):
        return self.__role

    def promote_employee(self, new_role, requester_role):
        if requester_role == "HR" or requester_role == "Manager":
            self.__role = new_role
            return f"SUCCESS: {self.name} ko promote kar ke '{new_role}' bana diya gaya hai."
        return "ERROR: Sirf HR ya Manager hi promotion de sakte haen."


if __name__ == "__main__":
    print("--- Creating Employees ---")
    emp1 = Employee(emp_id=101, name="Ali", salary=60000, role="Intern")
    emp2 = Employee(emp_id=102, name="Ayesha", salary=150000, role="HR")

    print("\n--- Scenario 1: Salary Checking Tests ---")
    print(f"Ali checking his own salary: {emp1.get_salary(requester_id=101, requester_role='Intern')}")
    
    # Case B: Ali chori se HR (Ayesha) ki salary dekhna chahta hai (Denied)
    print(f"Ali trying to check Ayesha's salary: {emp2.get_salary(requester_id=101, requester_role='Intern')}")
    
    # Case C: HR (Ayesha) Ali ki salary dekhna chahti hai (Allowed)
    print(f"HR checking Ali's salary: {emp1.get_salary(requester_id=102, requester_role='HR')}")


    print("\n--- Scenario 2: Salary Increment Tests (Data Modification) ---")
    # Case A: Ali khud apni salary 50% barhane ki koshish karta hai (Denied)
    print(f"Ali trying to give himself an increment: {emp1.apply_increment(50, requester_role='Intern')}")
    
    # Case B: HR Ali ko illegal (100%) increment dene ki koshish karti hai (Validation Fails)
    print(f"HR trying to give 100% increment: {emp1.apply_increment(100, requester_role='HR')}")
    
    # Case C: HR Ali ko valid (15%) increment deti hai (Allowed)
    print(f"HR giving valid 15% increment: {emp1.apply_increment(15, requester_role='HR')}")


    print("\n--- Scenario 3: Direct Access Attempt (The Ultimate Test) ---")
    # Kya hum direct variable change kar sakte haen?
    # emp1.__salary = 999999  <-- Yeh line Python mein error nahi degi, lekin aik naya variable bana degi. Original private variable safe rahega.
    print(f"Verifying original salary after direct bypass attempt: {emp1.get_salary(101, 'Intern')}")