#Old way
squares = []
for x in range(10):
    squares.append(x**2)

print(f'Squares old way {squares}')

#Comprehension A
squares = [x**2 for x in range(10)]
print(f'Squares comprehensionA {squares}')

#Comprehension B
squares = list(map(lambda x: x**2, range(10)))
print(f'Squares comprehensionB {squares}')

