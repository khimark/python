class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        pass

class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission_rate):
        super().__init__(emp_id, name, weekly_salary)
        self.commission_rate = commission_rate

    def calculate_payroll(self):
        base_salary = super().calculate_payroll()
        return base_salary + (self.commission_rate * base_salary)
    
# Testing the program

# Salary employee
salary_employee = SalaryEmployee(1, "Mickey", 50000)
print(f"Salary employee ({salary_employee.name}) weekly payroll: Ksh{salary_employee.calculate_payroll():.2f}")

# Hourly employee
hourly_employee = HourlyEmployee(2, "Tom", 45, 30)
print(f"Hourly employee ({hourly_employee.name}) weekly payroll: Ksh{hourly_employee.calculate_payroll():.2f}")

# Commission employee
commission_employee = CommissionEmployee(3, "Timothy", 20000, 0.5)
print(f"Commission employee ({commission_employee.name}) weekly payroll: Ksh{commission_employee.calculate_payroll():.2f}")
