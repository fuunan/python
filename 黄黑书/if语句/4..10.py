citys={
    'biejin':{
        'country':'china',
        'population':10000000,
        'fact':"It is china's cptial"
    },
    "london":{
        'country':'england',
        'population':9000000,
        'fact':"It is England's captial"
    },
    'newyork':{
        'country':'USA',
        'population':12000000,
        'fact':"It is very big city."
    },
}
for city,informations in citys.items():
    print(f"\nCity_name:{city}")
    for k,v in informations.items():
        print(f"{k}:{v}")