c = int(input("Enter the Temp in Celsius : "))

def temp():
    f = (c*9/5) + 32
    return f

print(f"THe temp in Farenhiet is {round(temp(),2)}°F.")