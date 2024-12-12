class Demo:
    a = 4

o = Demo()
print(o.a) #prints class atribute cus instance attribute is not present
o.a = 0 # instance attibute is set
print(o.a) #Prints the instance cus instance attribute is present
print(Demo.a) # prints the class attribute