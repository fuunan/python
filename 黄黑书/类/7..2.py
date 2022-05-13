class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.full_name = self.first_name + self.last_name
    def describe_user(self):
        print(f"The user's full name is {self.full_name}")
    def greet_user(self):
        print(f"Hello,{self.full_name}")
a=User('y','jm')
print(a.first_name)
print(a.last_name)
print(a.full_name)
a.describe_user()
a.greet_user()