from math import pi

# It is suggested to always do the imports, even is better to move comments lower than imports for convention

def compute_area_square(singVal):
    return singVal**2

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return pi * radius**2

############################################################################
### Stretch 2 and 3 covered but not applied in the program, only defined ###
############################################################################
def compute_area(shape, side1, side2=None):
    #I am using the None at the side2 cause it may be not applicable for some shapes
    shape = shape.lower()
    result = 0
    if side2 == None:
        if shape == "square":
            result = side1**2
        elif shape == "circle":
            result = pi * side1**2
    elif shape == "rectangle":
        result = side1 * side2
    return result

############################################################################
### Stretch 2 and 3 covered but not applied in the program, only defined ###
############################################################################
shape = ""

while shape.lower() != "quit":
    side1 = 0
    side2 = 0
    print("Pick from the options below")
    print("circle")
    print("square")
    print("rectangle")
    shape = input("Which shape you'll calculate area? ")
    shape = shape.lower(
    )  #it is casted into lower before going to if to avoid repetition
    if shape == "circle":
        side1 = float(input(f"Input the radius of the {shape}: "))
        print(
            f"The area of the {shape} with radius {side1:.2f} is equal to {compute_area(shape,side1):.2f}\n"
        )
    elif shape == "rectangle":
        side1 = float(input(f"Input the length of the {shape}: "))
        side2 = float(input(f"Input the width of the {shape}: "))
        print(
            f"The area of the {shape} with length {side1:.2f} and width {side2:.2f} is equal to {compute_area(shape,side1,side2):.2f}\n"
        )
    elif shape == "square":
        side1 = float(input(f"Input the square of the {shape}: "))
        print(
            f"The area of the {shape} with side {side1:.2f} is equal to {compute_area(shape,side1):.2f}\n"
        )
        #In order to complete stretch 1 it can be done as well
        #compute_area_rectangle(side1,side1)
