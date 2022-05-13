a = input("请输入数字: ")
b=len(a)
for i in range (b):
    if(a[i]==a[b-i-1]):
      print('这是一个回文数')
      break
    else:
        print('这不是一个回文数')
        break




