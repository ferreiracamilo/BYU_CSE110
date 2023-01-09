from math import pi

#stretch challenge 3 (implementing additional variable to calculate square metes as well updating message to print)
lengthSquare = float(
    input("What is the length of a side of the square? (in centimeters): "))
areaSquare_cm2 = lengthSquare**2
areaSquare_m2 = areaSquare_cm2 / 10000
print(
    f"The area of the square is: {areaSquare_cm2}  cm², or {areaSquare_m2} m²")

lengthRectangle = float(
    input("\nWhat is the length of rectangle? (in centimeters): "))
widthRectangle = float(
    input("What is the width of rectangle? (in centimeters): "))
areaRectangle_cm2 = lengthRectangle * widthRectangle
areaRectangle_m2 = areaRectangle_cm2 / 10000
print(
    f"The area of the rectangle is: {areaRectangle_cm2} cm², or {areaRectangle_m2} m²"
)

radiusCircle = float(
    input("\nWhat is the radius of the circle? (in centimeters): "))
#stretch challenge 1 (importing math > pi for it)
areaCircle_cm2 = pi * radiusCircle**2
areaCircle_m2 = areaCircle_cm2 / 10000
print(
    f"The area of the circle is: {areaCircle_cm2:.2f} cm², or {areaCircle_m2:.4f} m²"
)

#stretch challenge 2
lengthSingleValue = float(
    input(
        "\nInput a single value to calculate upcoming areas (in centimeters): "
    ))

areaSquare2 = lengthSingleValue**2
print(
    f"The area of the square based on single value input is: {areaSquare2:.2f} cm²"
)

areaCircle2 = pi * lengthSingleValue**2
print(
    f"The area of the circle based on single value input is: {areaCircle2:.2f} cm²"
)

cubeVolume = lengthSingleValue**3
print(
    f"The volume of the cube based on single value input is: {cubeVolume:.2f} cm²"
)

sphereVolume = 4 / 3 * pi * lengthSingleValue**3
print(
    f"The volume of the sphere based on single value input is: {sphereVolume:.2f} cm²"
)
