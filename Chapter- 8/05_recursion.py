'''
factprial(1) = 1  
factprial(2) = 2 x 1 
factprial(3) = 3 x 2 x 1
factprial(4) = 4 x 3 x 2 x 1
factprial(5) = 5 x 4 x 3 x 2 x 1

factprial(n) = n x n-1 x........3 x 2 x 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number : "))
print(f"THe factorial of the number is {factorial(n)}")