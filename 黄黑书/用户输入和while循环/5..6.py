resposes={}
active=True
while active:
    name = input("What's you name?")
    place = input("Where do you want to go?")
    resposes[name]=place
    poll=input("Would you like to let anther person resond?(yes/no)")
    if poll=='yes':
        continue
    elif poll=='no':
        active=False
print(f"\npoll result")
for n,p in resposes.items():
    print(f"The place {n.title()}  want to go is {p}")