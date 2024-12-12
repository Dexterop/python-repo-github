class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin_code):
        self.name = name
        self.salary = salary
        self.pin_code = pin_code


p = Programmer("Hardik", 120000, 201308)
print(p.name, p.salary, p.pin_code, p.company)
r = Programmer("Rohan", 150000, 201306)
print(r.name, r.salary, r.pin_code, r.company)