class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def Area(self):
        return self.length * self.breadth

    def Perimeter(self):
        return (2*(self.length + self.breadth))

    def Check_square(self):
        if(self.length == self.breadth):
            print("It is a square!")
        else:
            print("It is not a square!")

    def Display(self):
        print(f"Length: {self.length}")
        print(f"Breadth: {self.breadth}")
        print(f"Area: {self.Area()}")
        print(f"Perimeter: {self.Perimeter()}")


    @staticmethod
    def Greet():
        print("Hello There!")

a = Rectangle(5,3)
a.Greet()
a.Display()
print(a.Area())
print(a.Perimeter())
a.Check_square()
