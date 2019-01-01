class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi

    def get_circum(self):
        return self.radius * self.pi * 2



d = Circle()
#print d
print(d.radius)
print(d.pi)
print(d.area)
print(d.get_circum())
