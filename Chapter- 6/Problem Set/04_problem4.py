username = input("Enter your username: ")

length_0f_username = len(username)

print(length_0f_username)

if(length_0f_username <10):
    print("Your username contains less than 10 character")
else:
    print("Your username contains more than or equal to 10 character")