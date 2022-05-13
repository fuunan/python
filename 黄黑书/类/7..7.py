class Privileges:
    def __init__(self,privileges):
        privileges=['can add post','can delete post','can ban user ']
        self.privileges=privileges
    def show_privileges(self):
        print(self.privileges)
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


class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.full_name = self.first_name + self.last_name
        self.login_attempts = 0
        self.privileges=
