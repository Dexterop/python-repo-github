def rem(l, word):
    n=[]
    for item in l:
        if not(item ==word):
            n.append(item.strip())
    return n

l = ["hardik", "an", "Rohan","honey"]

print(rem(l, "an"))