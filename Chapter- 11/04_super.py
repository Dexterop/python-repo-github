class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=3

# o = Employee()
# print(o.a, o.b, o.c) #show error cus there are on b and c in employee class

o = Manager()
print(o.a, o.b, o.c) # manager has all the attribute cus of the inheritence