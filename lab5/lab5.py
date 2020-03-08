# Creating the parent class
class Shape:

    # __init__ is the contructor method. It initializes the class with no initialized variables
    # self is the reference/pointer to the instance of the class ( think this: class is a blueprint, the instance your townhouse that you've built)

    def __init__(self):

        # creating an empty list. self points to the boundary list of your instance

        self.boundary = []

    # Created a method (function inside the class). This method takes an arguement, which is a list of boudaries (points)

    def set_boundary(self, anything):

        # This points the parameter boudary to the boundary variable of your instance
        # the parameter can literally by any name you want. 

        # Note: Change anything to boundary just in case for assignment!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.boundary = anything


    def __str__(self):
        str1 = "Boundary: "
        for point in self.boundary:  # The shape can ahve various points (square 4, triangle 3, etc) so we have to use a for loop to know how many boundaries we have. 
            str1 += f"{str(point)}," # for each boundary, convert the onbject to string and add to our str1 to create the string with all the boundaries
        return str1[0:len(str1) - 1] # this returns the string, excluding the last item ( the comma)

class Point():

    # Seperate class (not a child class). Not inheriting any attributes
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})" # using the f string formatting to return a string with our x and y points

# Creating a subclass. This this the child class ( the class inside the brackets is the parent, from which we inherit methods and variables from)
class Rectangle(Shape):
    pass
    # since the rectable class is inheriting the attributes of the parent class Shape so it doesnt require initializing or changing anything. 


class Square(Rectangle):

    # Since a square has all same sides, knowing the length of one side, you can get the points of all the points
    # length is the paramete the specifies the length of the square

    # Use the method from the parent class shape (set_boundary) to specify the points of the square!

    def set_side_length(self, length):
        self.set_boundary([Point(0,0), Point(0, length), Point(length, length), Point(length, 0) ])
        
class Triangle(Shape):
    pass


# Creating a instance of the Point class. 
p1 = Point(31, 7)
p2 = Point(40, 5)
p3 = Point(50, 6)

# creating an instance of the Rectangle class
# keep in mind, you are able to create many instance of any class. 
# ex: rect1 = Rectangle()
#     rect2 = Rectangle()

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
