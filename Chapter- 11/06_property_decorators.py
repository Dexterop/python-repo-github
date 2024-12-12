class Employee:
    a = 2

    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

    @property
    def name(self):
        return "{self.fname} {self.lname}"

    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45
print(e.a)

f = Employee()
print(f.a)

e.name= "Hardik Yadav"
print(e.fname, e.lname)

e.show()