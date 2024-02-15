class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def createEmployee(self, name, age, id, department):
        employee = Employee(name, age, id, department)
        self.employees.append(employee)

    def retrieveEmployee(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None

    def deleteEmployee(self, id):
        for employee in self.employees:
            if employee.id == id:
                self.employees.remove(employee)
                return True
        return False
