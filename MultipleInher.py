class Base1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Base1 class constructor..")
    def display(self):
        print("a:\t",self.a)
        print("b:\t",self.b)

class Base2:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        print("base2 class constructor")

    def display(self):
        print("Base2 display2...")
        print("i:\t",self.i)
        print("j:\t",self.j)

class Child(Base1,Base2):
    def __init__(self,a,b,c,d,i,j):
        #self=1002
        #a=100, b=200, c=300 , d=400
        #Base1.__init__(self,a,b)
        super().__init__(a,b)
        Base2.__init__(self,i,j)
        self.c=c
        self.d=d
        print("Child class constructor..")

    def display(self):
        #self=c1
        #Base1.display(self)
        super().display()
        Base2.display(self)
        print("c:\t",self.c)
        print("d:\t",self.d)
    
    
    
c1=Child(100,200,300,400,500,600)
c1.display() 

