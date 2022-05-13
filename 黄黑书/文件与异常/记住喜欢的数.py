import json
filename='likenumbers2.json'

'''确定是否已有数字'''
def get_number():
    try:
        with open(filename,) as f:
            likenumber=json.load(f)
    except FileNotFoundError:
        return  None
    else:
        return likenumber

'''添加数字'''
def add_number():
    likenumber=input('你喜欢的数字是多少')
    with open(filename,'w') as f:
        json.dump(likenumber,f)

'''获取数字'''
def print_number():
    likenumber=get_number()
    if likenumber:
        print(f"你最喜欢的数是{likenumber}")
        sure=input('是否正确(y/n)')
        if sure=='n':
            likenumber=add_number()
            print('我们将会记住你喜欢的数')
        else:
            print('好的')
    else:
        likenumber=add_number()
        print('我们将会记住你喜欢的数')

print_number()

