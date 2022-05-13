sandwich_orders=['a','b','c','d']
finished_orders=[]
while sandwich_orders:
    finished=sandwich_orders.pop()
    print(f"{finished} is finished")
    finished_orders.append(finished)
print(sandwich_orders)
print(finished_orders)