fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


print('\033c') # clear screen

#Count
a=fruits.count('apple')
print(f"Count apple have {a}")

#Index
a=fruits.index('banana')
print(f"Banana index is {a}")

a = fruits.index('banana', 4)  # Find next banana starting a position 4
print(f"Banana next index is {a}")

#Reverse
fruits.reverse()
print(fruits)

#Index after reverse
a=fruits.index('banana')
print(f"Banana reverse index is {a}")

#Append
fruits.append('grape')
print(f"Fruits are {fruits}")

#Sort
fruits.sort()
print(f"Sorting fruits are {fruits}")

#Pop
a=fruits.pop()
print(f"Pop fruits are '{a}'")
print(f"Fruits are {fruits}")




