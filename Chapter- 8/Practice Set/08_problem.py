j = int(input("Enter the Number : "))
def multiplication_table(j):
    for i in range(1,11):
        print(f"{j} x {i} =",i * j )

print(multiplication_table(j))