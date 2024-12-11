class Employee:
    def __init__(self,name,age,salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary
    def display_info(self):
        return f"Name: {self.__name}, Age: {self.__age}, Salary: {self.__salary}"

class Manager(Employee):
    def __init__(self,name,age,salary,department):
        super().__init__(name, age, salary)
        self.__department = department
    
    def get_department(self):
        return self.__department
    def set_department(self,department):
        self.__department = department
    def display_info(self):
        return f"{super().display_info()}, Department: {self.__department}"

class Worker(Employee):
    def __init__(self,name,age,salary,hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked
    def get_hours_worked(self):
        return self.__hours_worked
    def set_hours_worked(self,hours_worked):
        self.__hours_worked = hours_worked
    def display_info(self):
        return f"{super().display_info()}, Hours Worked: {self.__hours_worked}"
def save_employee_to_file(filename, employee):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if isinstance(employee, Manager):
            writer.writerow([employee.get_name(),employee.get_age(),employee.get_salary(),employee.get_department(), 'N/A'])
        elif isinstance(employee, Worker):
            writer.writerow([employee.get_name(),employee.get_age(),employee.get_salary(),'N/A',employee.get_hours_worked()])

def read_employees_from_file(filename):
    employees = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        print("File not found.")
    return employees
def update_employee_in_file(filename, name, updated_employee):
    employees = read_employees_from_file(filename)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for employee in employees:
            if employee[0] == name:
                if isinstance(updated_employee, Manager):
                    writer.writerow([updated_employee.get_name(), updated_employee.get_age(), updated_employee.get_salary(), updated_employee.get_department(), 'N/A'])
                elif isinstance(updated_employee, Worker):
                    writer.writerow([updated_employee.get_name(), updated_employee.get_age(), updated_employee.get_salary(), 'N/A', updated_employee.get_hours_worked()])
            else:
                writer.writerow(employee)
def delete_employee_from_file(filename, name):
    employees = read_employees_from_file(filename)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for employee in employees:
            if employee[0] != name:
                writer.writerow(employee)
def add_employee(filename):
    print("Adding a new employee:")
    employee_type = input("Enter employee type (manager/worker): ").lower()
    name = input("Enter name: ")
    age = input("Enter age: ")
    salary = input("Enter salary: ")
    if employee_type == "manager":
        department = input("Enter department: ")
        manager = Manager(name, age, salary, department)
        save_employee_to_file(filename, manager)
    elif employee_type == "worker":
        hours_worked = input("Enter hours worked: ")
        worker = Worker(name, age, salary, hours_worked)
        save_employee_to_file(filename, worker)
    else:
        print("Invalid employee type!")
def display_all_employees(filename):
    employees = read_employees_from_file(filename)
    print("Displaying all employees:")
    for employee in employees:
        print(f"Name: {employee[0]}, Age: {employee[1]}, Salary: {employee[2]}, Department: {employee[3]}, Hours Worked: {employee[4]}")
def update_employee(filename):
    name = input("Enter the name of the employee to update: ")
    employees = read_employees_from_file(filename)
    found = False
    for employee in employees:
        if employee[0] == name:
            found = True
            employee_type = input("Enter new employee type (manager/worker): ").lower()
            if employee_type == "manager":
                department = input("Enter new department: ")
                updated_manager = Manager(employee[0], employee[1], employee[2], department)
                update_employee_in_file(filename, name, updated_manager)
            elif employee_type == "worker":
                hours_worked = input("Enter new hours worked: ")
                updated_worker = Worker(employee[0], employee[1], employee[2], hours_worked)
                update_employee_in_file(filename, name, updated_worker)
            else:
                print("Invalid employee type!")
            break
    if not found:
        print("Employee not found!")
def delete_employee(filename):
    name = input("Enter the name of the employee to delete: ")
    delete_employee_from_file(filename, name)
    print(f"Employee {name} deleted.")
def main():
    filename = "employees.csv"
    
    while True:
        print("\nMenu:")
        print("1. Add new employee")
        print("2. Display all employees")
        print("3. Update employee information")
        print("4. Delete an employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee(filename)
        elif choice == '2':
            display_all_employees(filename)
        elif choice == '3':
            update_employee(filename)
        elif choice == '4':
            delete_employee(filename)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
