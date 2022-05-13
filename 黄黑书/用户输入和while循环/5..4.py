age=""
active= True
while active:
    age = input("请输入年龄")
    if age =='quit':
        active=False
    else:
        age=int(age)
        if age>=0 and age<=3:
            print('免费')
        elif age<=12:
            print('票价为10美元')
        else:
            print('票价为15美元')