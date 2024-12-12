class Employee:
    Company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the Company is {self.Company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")



class Programmer(Employee, Coder):
    Company = "ITC Infotech"
    def showLanguage(self):
         print(f"The name is {self.Company} and he is good with {self.language} language ")


a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()