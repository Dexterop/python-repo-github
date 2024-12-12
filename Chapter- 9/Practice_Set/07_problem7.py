

with open("log.txt") as f:
    lines = f.readline()

lineno = 1
for line in lines:
    if("python".lower() in lines.lower()):
        print(f"True! line no : {lineno}")
        break
    lineno += 1

else:
    print("False!")