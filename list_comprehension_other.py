vec1 = [-4, -2, 0, 2, 4]
print(f'list      {vec1}')
# create a new list with the values doubled
vec = [x*2 for x in vec1]
print(f'list values doubled  {vec}')

# filter the list to exclude negative numbers
vec = [x for x in vec1 if x >= 0]
print(f'list values exclude negative numbers  {vec}')

# apply a function to all the elements
vec = [abs(x) for x in vec1]
print(f'list values ad abs() function  {vec}')

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
strip = [weapon.strip() for weapon in freshfruit]
print(f'list strip space first&last  {strip}')

# create a list of 2-tuples like (number, square)
a=[(x, x**2) for x in range(6)]
print(f'list number square  {a}')

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
b=[num for elem in vec for num in elem]
print(f'list flatten  {b}')

#List comprehensions can contain complex expressions and nested functions:
from math import pi
c=[str(round(pi, i)) for i in range(0, 6)]
print(f'{c}')