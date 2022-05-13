
class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name


class Amd(User):
    def __init__(self,first_name,last_name):
        super(Amd, self).__init__(self,)
a=Amd('yu','l')
print(a.first_name)