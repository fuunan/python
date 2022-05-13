fanorite_place={
    'tom':['beijin','nanjin','lanzhou'],
    'wu':['shanghai','nanchang','xingan'],
    'liu':['gangzhou','beijin','chongqin'],
}
for people,places in fanorite_place.items():
    print(f"\nThe places {people.title()} likes are:")
    for place in places:
        print(place,end="\t")

