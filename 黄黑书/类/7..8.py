from random import randint
class Die:
    def __int__(self):
        self.sides=6
    def change_siides(self,number):
        self.sides=number
    def roll_die(self):
        i=1
        if self.sides==6:
            while i<=10:
                a=randint(1,6)
                print(a)
                i+=1
        elif self.sides==10:
            while i<=10:
                a=randint(1,10)
                print(a)
                i+=1
        elif self.sides==20:
            while i<=10:
                a=randint(1,20)
                print(a)
                i+=1
b=Die()
b.change_siides(20)
b.roll_die()

