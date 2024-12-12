with open("old.txt") as f:
    content = f.read()

with open("renamed.txt", "w") as f:
    content = f.write(content)

