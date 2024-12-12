class Employee:
    language = "Py" #Class attribute
    salary = 120000

    def __init__(self, name, salary, language):  # dunder method which is autmatically called
        self.name= name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary} ")
    
    @staticmethod
    def greet():
        print("Good Morning")


hardik = Employee("Hardik" , 1300000, "JavaScript")
#hardik.name = "Hardik"
print(hardik.name, hardik.salary, hardik.language)

# rohan = Employee()