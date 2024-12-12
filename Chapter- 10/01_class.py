class Employee:
    language = "Py" #Class attribute
    salary = 120000

hardik = Employee()
hardik.name = "Hardik" #Instance attribute
print(hardik.name, hardik.language, hardik.salary)

rohan = Employee()
rohan.name = "Rohan Robinson"
print(rohan.name, rohan.language, rohan.salary)

#here name is Instance attribute and salary and language are Class atribute as they directly belong to the class