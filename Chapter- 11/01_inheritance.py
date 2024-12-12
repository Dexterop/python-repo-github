class Employee:
    Company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the Salary is {self.Salary}")

    
# class Programmer:
#     Company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the Salary is {self.Salary}")
    
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language ")


class Programmer(Employee):
    Company = "ITC Infotech"
    def showLanguage(self):
         print(f"The name is {self.name} and he is good with {self.language} language ")


a = Employee()
b = Programmer()

print(a.Company, b.Company)