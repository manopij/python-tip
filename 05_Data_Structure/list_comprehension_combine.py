#Old
#combs = []
#for x in [1,2,3]:
#    for y in [3,1,4]:
#        if x != y:
#             combs.append((x, y))

combine = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(f'Combine comprehensionA {combine}')

combine = [(x, y) for x in [1,2,3] for y in [3,1,4]]
print(f'Combine comprehensionB {combine}')