a = int(input("Enter you age: "))

if(a>=18):
    print("You are above the age of consent!")
elif(a<0):
    print("Enter a valid age!")
elif(a==0):
    print("0 is a valid age but i am not accepting!")
else:
    print("You are below the age of consent!") 

print("End of the Program!")