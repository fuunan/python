class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restayrant(self):
        print(f"This resstaurant cuisine is {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening")
    def set_number_served(self,number):
        self.number_served=number
    def increment_number_served(self,number):
        self.number_served+=number
    def read_number_served(self):
        print(self.number_served)
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        flavors=['apple','banana','orange']
        self.flavors=flavors
        order=[]
        self.order=order
    def order_iceceream(self):
        a = input('what do you need?')
        self.order.append(a)
        active=True
        while active:
            b=input('anthing else?')
            if b=="no":
                active=False
            else:
                self.order.append(b)
        print(f"You have order\n {self.order}")
    def menu_icecream(self):
        print(f"This is menu\n{self.flavors}")
a=IceCreamStand("pdd","icecream")
a.describe_restayrant()
a.open_restaurant()
a.set_number_served(8)
a.read_number_served()
a.menu_icecream()
a.order_iceceream()