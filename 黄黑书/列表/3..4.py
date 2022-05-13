value=list(range(1,10000001))
print(min(value))
print(max(value))
print(sum(value))
odd=list(range(1,20,2))
for o in odd:
    print(o)
three=list(range(3,31,3))
for t in three:
    print(t)
cube=[]
for c in range(1,11):
    cube.append(c**3)
print(cube)

cube2=list(c**3 for c in range(1,11))
print(cube2)




