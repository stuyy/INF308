# Anson Foong INF 308 Test

# The purpose of this program is to calculate the areas of the Circle, Square, Trapozoid, Triangle, and Rectangle that are drawn in the graph. We need to calculate each area, sum up their areas to get the total area, and then get the average of the area.

# I think we did go over functions because in one of the assignments, we were required to write a function to generate a random number. So I hope it's okay to define these functions as is

grid_square = .25 # Each square of the grid is .25 x .25, aka 1/4 x 1/4
PI = 3.14159265359 # PI CONSTANT DEFINED BY OURSELVES

# Declare a function to get the area of the rectangle
# The rectangle is 5 squares.

def area_of_rect():
    length = grid_square * 5
    width = grid_square
    return length * width

# Function to get the area of circle
def area_of_circle():
    radius = grid_square # Since each square has a length of .25 and the circle has a diameter of .50, the radius is half of that.
    return PI * radius * radius

# Function to get area of square
def area_of_square():
    side = grid_square * 2 # Since each square of the grid is .25, the side of a square is twice of that on the graph
    return side * side

# The triangle is a right triangle, so we define the function as follows
def area_of_right_triangle():
    legOne = grid_square * 2 # Get the leg of the triangle
    legTwo = grid_square * 2 # Get the leg of the triangle

    return (legOne*legTwo)/2

#Function to get area of trapezoid
def area_of_trapezoid():
    a = grid_square * 2 # Need to get a
    base = grid_square * 4 # Need to get base, multiply by 4 because the base of the trapezoid in the grid is made up of four squares.
    height = grid_square * 3 # Get the height, multiply by 3 because the height is made up of 3 squares.

    return ((a+base)*height)/2

# Function to get the total area
def total_area():
    return area_of_rect() + area_of_circle() + area_of_square() + area_of_trapezoid() + area_of_right_triangle()

# Function to get the average area
def average_area():
    return (area_of_rect() + area_of_circle() + area_of_square() + area_of_trapezoid() + area_of_right_triangle())/5

# Print output of each shape's area, their total area, and the average.
print("Area of rectangle: " + str(area_of_rect()))
print("Area of circle: " + str(area_of_circle()))
print("Area of Square: " + str(area_of_square()))
print("Area of right triangle: " + str(area_of_right_triangle()))
print("Area of trapezoid: " + str(area_of_trapezoid()))
print("Total Area: " + str(total_area()))
print("Average Area: " + str(average_area()))
