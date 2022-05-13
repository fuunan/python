with open('book') as b:
    v=b.read()
    numebr1=v.lower().count('the')
    number2=v.lower().count(' the ')
    print(numebr1,'\n',number2)

