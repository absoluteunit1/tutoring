class Shape:
    
    def __init__(self):
        
        self.boundary = []

    def set_boundary(self, boundary):

        self.boundary = boundary

    def __str__(self):
        str1 = "Boundary: "
        for point in self.boundary:
            str1 += f"{str(point)}, "
        return str1

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"


class Rectangle(Shape):
    pass

class Square(Rectangle):

    def set_side_length(self, length):
        self.set_boundary([Point(0,0), Point(0, length), Point(length, length), Point(length, 0) ])
        
class Triangle(Shape):
    pass



p1 = Point(31, 7)
p2 = Point(40, 5)
p3 = Point(50, 6)
# boundary = [p1, p2, p3] = ["(31,7)", "(40, 5)", "(50, 6)"]


rect = Rectangle()
rect.set_boundary( [ Point(0,0), Point(0,3), Point(5,3), Point(5,0) ] )
print(rect)

square = Square()
square.set_boundary([Point(0, 0), Point(0, 3), Point(3, 3), Point(3, 0)])
print(square)

trgle = Triangle()
trgle.set_boundary([Point(0, 7), Point(3, 3), Point(2, 5)])
print(trgle)

square.set_side_length(5)
print(square)