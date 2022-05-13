import json
filename='likenumbers.json'
likenumber=input('请输入你喜欢的数')
with open(filename,'w') as f:
    json.dump(likenumber,f)

with open(filename) as f:
    likenumber=json.load(f)
    print(likenumber)