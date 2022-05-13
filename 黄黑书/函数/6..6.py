def make_album(name,album,number=None):
    albums={'name':name,'album':album}
    if number:
        albums['number']=number
    return albums
while True:
    n=input('请输入姓名\n如果退出请输入 quit\n')
    if n=="quit":
        break
    a=input('请输入专辑名\n如果退出请输入 quit\n')
    if a=='quit':
        break
    nu=input('输入数量或无或退出（quit）')
    if nu=='无':
        number=False
    elif nu=='quit':
        break
    b=make_album(n,a,nu)
    print(b)
    break
