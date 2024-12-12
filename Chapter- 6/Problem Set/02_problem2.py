marks1 = int(input("Enter the marks of subject 1: "))
marks2 = int(input("Enter the marks of subject 2: "))
marks3 = int(input("Enter the marks of subject 3: "))

#check for total percentage
total_percentage = ((marks1+marks2+marks3)/300)*100


if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed: ", total_percentage)

else:
    print("You are failed: ", total_percentage)