class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position
    def display_info(self):
        return f"Employee ID: {self.employee_id}, Position: {self.position}"
class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department
    def display_info(self):
        person_info = Person.display_info(self)
        employee_info = Employee.display_info(self)
        return f"{person_info}, {employee_info}, Department: {self.department}"
    def additional_info(self):
        return f"Department: {self.department}"

def read_employees_from_file(filename):
    try:
        with open(filename, 'r') as file:
            employees = file.readlines()
        return employees
    except FileNotFoundError:
        print("File not found. Returning an empty list.")
        return []

def save_employee_to_file(filename,staff_member):
    with open(filename, 'a') as file:
        file.write(f"{staff_member.name}, {staff_member.age}, {staff_member.employee_id}, {staff_member.position}, {staff_member.department}\n")
def add_new_employee(filename):
    name = input("Enter employee's name: ")
    age = input("Enter employee's age: ")
    employee_id = input("Enter employee's ID: ")
    position = input("Enter employee's position: ")
    department = input("Enter employee's department: ")

    new_staff = Staff(name,age,employee_id,osition,department)
    save_employee_to_file(filename, new_staff)
    print("Employee added successfully.")
def display_employees_from_file(filename):
    employees = read_employees_from_file(filename)
    if employees:
        for employee in employees:
            print(employee.strip())
    else:
        print("No employees found in the file.")
def main():
    filename = "employees.txt"
    
    while True:
        print("\nMenu:")
        print("1. Add new employee")
        print("2. Display all employees")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_new_employee(filename)
        elif choice == '2':
            display_employees_from_file(filename)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
