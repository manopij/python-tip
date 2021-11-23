# dictionaries are indexed by keys 
# strings and numbers can always be keys
# as a set of key
## immutable type

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel)) #result ['jack', 'guido', 'irv']

print(sorted(tel)) #result ['guido', 'irv', 'jack']

print('guido' in tel) #True
print('jack' not in tel) #False

#The dict() constructor builds dictionaries directly from sequences of key-value pairs
a=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(a)

b=dict(sape=4139, guido=4127, jack=4098)
print(b)

# looping through dictionaries
# the key and corresponding value can be retrieved at the same time using the items() method
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)

#dict comprehensions can be used to create dictionaries from arbitrary key and value expressions
a={x: x**2 for x in (2, 4, 6)}
print(a)

