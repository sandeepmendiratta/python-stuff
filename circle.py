class Circle:
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi
    def get_cirumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(10)
print (my_circle.get_cirumference())
print my_circle.pi
print my_circle.radius
print my_circle.area
