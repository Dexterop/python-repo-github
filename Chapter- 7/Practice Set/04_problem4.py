n = int(input("Enter a number: "))

for i in range(2,n):
    if(n%i)==0:
        print("It is not a Prime number!")
        break
else:
    print("Number is prime")
   
        