filename='guest.txt'
with open(filename,'a') as g:
    j=True
    while j:
        name=input('请输入用户名称')
        g.write(f"{name}\n")
        m=input('是否继续添加（y/n）')
        if m=='y':
            continue
        elif m=='n':
            j=False
with open(filename) as g:
    context=g.read()
print(context)