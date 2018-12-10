class dog():

    leg = "four"
    def __init__(self, breed, eye, name):

        self.breed = breed
        self.eye = eye
        self.name = name

	def bark(self):
		print ("WHOOF!")

my_dog = dog("lab",	"black", "buddy")
#type(my_dog)
print my_dog.breed
print my_dog.leg
print my_dog.name
print my_dog.eye
print my_dog.bark()
