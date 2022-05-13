age=input("请输入年龄")
while age != "quit":
    age=int(age)
    if age>=0 and age<=3:
        print("免费")
        break
    elif age<=12:
        print("票价为10美元")
        break
    else:
        print("票价为15美元")
        break
