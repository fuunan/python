class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.full_name = self.first_name + self.last_name
        self.login_attempts=0
    def describe_user(self):
        print(f"The user's full name is {self.full_name}")
    def greet_user(self):
        print(f"Hello,{self.full_name}")
    def increment_login_attempts(self,number):
        self.login_attempts+=number
    def reset_login_attempts(self):
        self.login_attempts=0
    def read_login_attenmos(self):
        print(self.login_attempts)
a=User('SON','yuhao')
a.describe_user()
a.greet_user()
for i in range(0,6):
    a.increment_login_attempts(1)
a.read_login_attenmos()
a.reset_login_attempts()
a.read_login_attenmos()