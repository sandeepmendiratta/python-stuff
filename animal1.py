class Animal:
    def __init__(self, name):
        self.name = name

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")



d = Animal("buddy")
#print d
print d.name
print d.whoAmI

