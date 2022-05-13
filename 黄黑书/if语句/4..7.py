people1={'tom':0,'tim':1,'jack':2}
people2={'jim':4,'susan':5,'linda':6}
people3={'jerry':7,'linux':8,'python':9}
peoples=[people1,people2,people3]
for people in peoples:
    for p,v in people.items():
        print(p.title())
        print(v)
        