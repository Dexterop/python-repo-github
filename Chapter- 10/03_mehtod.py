class Employee:
    language = "Py" #Class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary} ")
    
    @staticmethod
    def greet():
        print("Good Morning")

hardik = Employee()

hardik.greet()
hardik.getInfo()
#Employee.getInfo(hardik)