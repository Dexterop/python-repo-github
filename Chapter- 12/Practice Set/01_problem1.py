try:
    with open("1.txt", "r") as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f2:
        print(f2.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f3:
        print(f3.read())
except Exception as e:
    print(e)


print("Thank You!")