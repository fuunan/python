places=["beijin","shanghai","guangzhou","chonqin","nanchang"]
print(f"The first three items in the list are")
for p in places[0:3]:
    print(p)
for p in places[1:4]:
    print(p)
for p in places[2:5]:
    print(p)
my_pisas=['pisa1','pisa2','pisa3']
friend_pisas=my_pisas[:]
print(my_pisas)
print(friend_pisas)
my_pisas.append('pisa4')
friend_pisas.append('pisa5')
print(my_pisas)
print(friend_pisas)