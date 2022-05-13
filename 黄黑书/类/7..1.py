class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restayrant(self):
        print(f"This resstaurant cuisine is {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening")
restaurant1=Restaurant('pdd','chinese food')
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restayrant()
restaurant1.open_restaurant()