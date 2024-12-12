#entering a num
n = int(input("Enter a num : "))


for i in range(1, n+1): #the range is for rows
    print(" "* (n-i), end="")#this is for the space(for first row - 3 - i => 3-1=2, so 2 blank spaces and so on...) and end does not give new line
    print("*"* (2*i-1), end="")#this line prints the '*' 2*i-1 is the series for odd num and end does not give new line
    print("") # this line gives new line