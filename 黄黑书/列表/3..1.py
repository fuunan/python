#3=4
names=['y','j','m']
print(f"{names[0]} please come to")
print(f"{names[1]} please come to")
print(f"{names[2]} please come to")
#3-5
print(f"\n{names[1]} can not come")
names[1]='k'
print(f"\n{names[0]} please come to")
print(f"{names[1]} please come to")
print(f"{names[2]} please come to")
#3-6
names.insert(0,"o")
names.insert(2,"l")
names.append("p")
print(names)

delete_people=names.pop(0)
print(f"\nsorry,{delete_people}")
delete_people=names.pop(1)
print(f"\nsorry,{delete_people}")
delete_people=names.pop(2)
print(f"\nsorry,{delete_people}")
del names[0]
del names[1]
del names[2]
print(names)
