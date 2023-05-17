
class Parent:
    def __init__(self):
        self.parent = "I'm the parent"
        print("Parent")

    def myMethod(self):
        print("Parent method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child = "I'm the child"
        print("Child")

    def myMethod(self):
        print("Child method")

c = Child()
c.myMethod()
