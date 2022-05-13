import random

a=random.choice([0,1,2.,3,4,5,6,7,8,9])
b=random.choice([0,1,2,3,4,5,6,7,8,9])
c=int(input(f"{a}+{b}等于几"))
if c==a+b:
    print("回答正确")
else:
    print("回答错误")
