class Base1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Base1 class constructor..")

    def display1(self):
        print("a:\t",self.a)
        print("a:\t",self.b)

class Base2:
    def display2(self):
        print("Base2 display2...")

class Child(Base1,Base2):
    pass

c1=Child(100,200)
c1.display1()
c1.display2()
