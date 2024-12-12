class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3

o = Employee()
# print(o.a, o.b, o.c) #show error cus there are on b and c in employee class

o = Manager()
print(o.a, o.b, o.c) # manager has all the attribute cus of the inheritence