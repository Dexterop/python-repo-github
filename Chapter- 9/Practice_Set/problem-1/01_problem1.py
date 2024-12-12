f = open(r"C:\Users\hardi\Desktop\py\Chapter - 9\Practice Set\problem-1\poems.txt", "r")


content = f.read()

if('Twinkle'.lower() in content.lower()):
    print("It contains the word twinkle")
else:
    print("It doesn't contains the word twinkle")

f.close()