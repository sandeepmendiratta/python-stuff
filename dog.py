class Dog():
    def __init__(self,name):
        self.name = name


    def speak(self):
        return self.name  + " Says woof"

class Cat():
    def __init__(self,name):
        self.name = name


    def speak(self):
        return self.name  + " Says Meo!"

d = Dog("buddy")
c = Cat ("felix")
# print(d.speak())
# print(c.speak())
def pet_speak(pet):
    print(pet.speak())

pet_speak(d)
pet_speak(c)
