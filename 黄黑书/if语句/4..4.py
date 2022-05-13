figure={
    'l':1,
    'm':2,
    'k':3,
    'i':4,
    'p':6
}
for name in figure.keys():
    print(name)
for v in figure.values():
    print(v)
figure['j']=12
figure['a']=45
figure['t']=65
figure['e']=78
figure['s']=47
for name in figure.keys():
    print(name)
for v in figure.values():
    print(v)