class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __sub__(self, num):
        return self.n - num.n

    def __mul__(self, num):
        return self.n * num.n

n = Number(1)
m = Number(2)

print(f"Sum : {n + m}")
print(f"Subtraction : {n - m}")
print(f"Multiplication : {n * m}")