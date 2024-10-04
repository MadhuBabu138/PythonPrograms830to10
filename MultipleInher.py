class Base1:
    def __init__(self):
        print("Base1 class constructor..")
class Base2:
    def display(self):
        print("Base display...")

class Child(Base1,Base2):
    pass

c1=Child()
c1.display()
