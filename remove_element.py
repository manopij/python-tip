a = [1,2,3,4,5,6,7]
def even(x):
    return x % 2 == 0

a[:] = [x for x in a if not even(x)]

print(*a, sep = ", ") 
