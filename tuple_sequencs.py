#A tuple consists of a number of values separated by commas, for instance:
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
#t[0] = 88888 #Error

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

#also more efficiency than list 