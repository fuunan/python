pet1={'dog':'tom','pig':'jerry','cat':'may'}
pet2={'duck':'yang','horse':'wang','mouse':'zhang'}
pet3={'cat':'liu','mouse':'li','dog':'sun'}
pets=[pet1,pet2,pet3]
for pet in pets:
    for a,n in pet.items():
        print(f"\nThe {n.title()}'s pet is {a}.")