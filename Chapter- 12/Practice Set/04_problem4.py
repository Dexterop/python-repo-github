a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError 
    print("Infinite")
else:
    print(f"The Division of {a} / {b} is {a/b} ")