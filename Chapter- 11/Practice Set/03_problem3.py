class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        # Calculate the increment based on the new salaryAfterIncrement
        self.increment = ((salary / self.salary) - 1) * 100
    
e = Employee()

# Setting salaryAfterIncrement will update the increment value
e.salaryAfterIncrement = 280  # This will calculate and set the increment
print(e.increment)  # This will print the updated increment value

