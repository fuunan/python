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
a=Restaurant('pdd','china food')
a.describe_restayrant()
a.open_restaurant()
a.set_number_served(8)
a.read_number_served()
a.increment_number_served(4)
a.read_number_served()