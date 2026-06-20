class SalaryNotInRange(Exception):
    def __init__(self, salary):
        self.salary = salary
        self.msg = "Salary is not in range(5000,30000)"
        super().__init__(self.msg)
salary = int(input("Enter salary: "))
if salary<5000 or salary > 30000:
    raise SalaryNotInRange(salary)
else:
    print(salary)