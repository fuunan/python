while True:
    try:
        a=int(input('请输入第一个数'))
        b=int(input('请输入第二个数'))
        answer=a+b
    except ValueError:
        print('请输入数字，而不是文本')
    else:
        print(f"答案是{answer}")
        break