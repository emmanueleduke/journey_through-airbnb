class Rectangle:

    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# create an instance of the rectangle class

rec = Rectangle(5, 15, 7)

# access attributes and call method of the object

print("Height:", rec.height)
print("Perimeter:", rec.perimeter())


