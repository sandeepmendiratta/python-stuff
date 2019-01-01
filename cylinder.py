class Cylinder():
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.radius = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius * self.radius * self.radius

    def surface_area(self):
        return ((2*self.pi*self.radius) * self.radius) + ((self.pi*self.radius**2)*2)
c = Cylinder(4,5)
print(c.volume())
print(c.surface_area())
