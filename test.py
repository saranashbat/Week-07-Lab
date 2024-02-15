import unittest
from employee_management_system import EmployeeManagementSystem

class Test(unittest.TestCase):
    def setUp(self):
        self.system = EmployeeManagementSystem()

    def testCreateEmployeeMissingInfo(self):
        try:
            self.system.createEmployee("John Doe", 30, 1, None)
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def testRetrieveEmployeeWrongId(self):
        try:
            self.system.retrieveEmployee(-1)
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def testCreateEmployeeStringAge(self):
        try:
            self.system.createEmployee("Jane Smith", "twenty-five", 2, "HR")
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def testCreateEmployeeNegativeAge(self):
        try:
            self.system.createEmployee("Bob Johnson", -40, 3, "Marketing")
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def testCreateEmployeeNegativeId(self):
        try:
            self.system.createEmployee("Alice", 25, -4, "Finance")
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def testEmployeeCreation(self):
        employee = self.system.createEmployee("Test Employee", 30, 1001, "Test Department")

        self.assertEqual(employee.name, "Test Employee")
        self.assertEqual(employee.age, 30)
        self.assertEqual(employee.id, 1001)
        self.assertEqual(employee.department, "Test Department")

    def testRetrieveEmployeeById(self):
        self.system.createEmployee("John Doe", 35, 2001, "HR")

        employee = self.system.retrieveEmployee(2001)

        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.age, 35)
        self.assertEqual(employee.id, 2001)
        self.assertEqual(employee.department, "HR")

if __name__ == "__main__":
    unittest.main()
