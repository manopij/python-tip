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
