from functools import reduce

#Map Example

l = [1, 2, 3, 4, 5]

# square = lambda x: x*x
# sum = lambda a,b,c : a+b+c

# sqList = map(square, l)
# sumList = map(sum , l, l, l)

# print(list(sqList))
# print(list(sumList))

#filter exampke

def even(n):
    if(n%2 == 0 ):
        return True
    return False


onlyEven = filter(even, l)

print(list(onlyEven))

#Reduce FUnction

def sum(a, b):
    return a+b

mul = lambda x,y : x*y
print(reduce(sum, l))
print(reduce(mul, l))