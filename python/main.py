class Person:
    def __init__(self , name):
        self.name = name

    def talk(self):
        print(f"Hi , I am {self.name}")

chloe = Person("Chloe Lynn")
chloe.talk()

bob = Person("Bob smith")
bob.talk()
