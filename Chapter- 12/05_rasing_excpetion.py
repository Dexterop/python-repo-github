a = int(input("Hey, Enter 1st number: "))
b = int(input("Hey, Enter 2nd number: "))
if(b==0):
    raise ZeroDivisionError("Hey program not meant to divideby zero")
else:
    print(f"The division of a/b is {a/b}")