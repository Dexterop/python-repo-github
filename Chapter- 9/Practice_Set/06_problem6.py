with open("log.txt") as f:
    content = f.read()

if("python".lower() in content.lower()):
    print("True!")
else:
    print("False!")