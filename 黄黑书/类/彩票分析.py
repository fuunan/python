from random import choice
number=('1','2','3','4','5','6','7','8','9')
a=''
i=0
j=True
print('中奖号码为2567')
while j:
    for m in range(0,4):
        b=choice(number)
        a=a+b
        if a=='2567':
            print(f"循环次数为{i}")
            j=False
        else:
            continue
    a=''
    i+=1