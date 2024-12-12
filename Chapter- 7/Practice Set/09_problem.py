# * * *
# *   *       for n = 3
# * * *



n = int(input("Enter the Number : "))

for i in range(1,n+1):
    if(i==1 or i==n): # all stars for 1st and last row
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*")
print("")