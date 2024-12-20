l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     index += 1
#     print(f"The item numeber at index {index} is {item}")

# this can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item numeber at index {index} is {item}")