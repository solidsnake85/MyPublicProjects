# Make two points equal each other
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

firstpoint = Point(25, 50)
secondpoint = Point(25, 50)

print(firstpoint == secondpoint)
print(id(firstpoint))
print(id(secondpoint))