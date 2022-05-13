age=int(input("请输入年龄"))
if age>=0 and age<=2:
        print("这是一个婴儿")
elif age<=4:
    print("这是一个幼儿")
elif age<=13:
    print("这是一个儿童")
elif age<=20:
    print("这是一个青少年")
elif age<=65:
    print("这是一个成年人")
else:
    print("这是一个老年人")