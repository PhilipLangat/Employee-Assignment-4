# Base class for employees
class Employee:
    def __init__(self, name, employee_id, base_salary):
        """
        Initializes a new employee with name, employee ID, and base salary.
        """
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def __str__(self):
        """
        Returns a string representation of the employee.
        """
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Base Salary: Ksh.{self.base_salary}"

    def calculate_salary(self):
        """
        Returns the base salary. Can be overridden by subclasses.
        """
        return self.base_salary


# Full-time employee class inheriting from Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, benefits):
        """
        Initializes a new full-time employee with name, employee ID, base salary, and benefits.
        """
        super().__init__(name, employee_id, base_salary)
        self.benefits = benefits

    def __str__(self):
        """
        Returns a string representation of the full-time employee, including benefits.
        """
        return f"Full-Time Employee: {super().__str__()}, Benefits: Ksh.{self.benefits}"

    def calculate_salary(self):
        """
        Returns the total salary including benefits.
        """
        return self.base_salary + self.benefits


# Part-time employee class inheriting from Employee
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        """
        Initializes a new part-time employee with name, employee ID, hourly rate, and hours worked.
        """
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        # The base salary for part-time is calculated by multiplying hourly rate with hours worked
        base_salary = hourly_rate * hours_worked
        super().__init__(name, employee_id, base_salary)

    def __str__(self):
        """
        Returns a string representation of the part-time employee, including hourly rate and hours worked.
        """
        return (f"Part-Time Employee: {super().__str__()}, Hourly Rate: Ksh.{self.hourly_rate}, "
                f"Hours Worked: {self.hours_worked}")

    def calculate_salary(self):
        """
        Returns the total salary based on the hourly rate and hours worked.
        """
        return self.hourly_rate * self.hours_worked


# Company class to manage employees
class Company:
    def __init__(self):
        """
        Initializes the company with an empty list of employees.
        """
        self.employees = []

    def add_employee(self, employee):
        """
        Adds a new employee to the company.
        """
        self.employees.append(employee)

    def display_employees(self):
        """
        Displays the details of all employees in the company.
        """
        print("Company Employees:")
        for employee in self.employees:
            print(employee)
        print()  # Blank line for better readability

    def calculate_total_salary(self):
        """
        Calculates and returns the total salary expense of the company.
        """
        total_salary = sum(employee.calculate_salary() for employee in self.employees)
        return total_salary


# Example usage of the system
if __name__ == "__main__":
    # Creating a company
    company = Company()

    # Adding employees to the company
    emp1 = FullTimeEmployee("Alice", "E001", 50000, 10000)
    emp2 = PartTimeEmployee("Bob", "E002", 20, 100)
    company.add_employee(emp1)
    company.add_employee(emp2)

    # Displaying employees
    company.display_employees()

    # Calculating total salary expense
    total_salary = company.calculate_total_salary()
    print(f"Total Salary Expense: Ksh.{total_salary}")
