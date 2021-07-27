""" In this project, I created a calculator that can compute the are of circles and triangles """

import math

print("Welcome to the Area Calculator! Using this calculator, you can calculate the areas of "
      "circles or triangles.\n\n")


def circle_area_calculator():
    """ This function prompts the user to input a radius and uses it to calculate the area of
    a circle."""

    flag = False
    # asks for the radius until the value entered is valid
    while not flag:
        try:
            radius = float(input("Please enter the radius of the circle: "))
            flag = True
            # calculate the area of the circle using the formula
            area = str(math.pi * radius ** 2)

            print("The area of your circle is " + area)

        except ValueError:
            print("\nInvalid input. Please enter at least one digit and do not enter letters.\n")


def triangle_area_calculator():
    """ This function prompts the user to input a base and a height and uses it to calculate
    the area of a triangle."""

    baseFlag = False
    # asks for the base until the value entered is valid
    while not baseFlag:
        try:
            base = float(input("Please enter the base of the triangle: "))
            baseFlag = True

        except ValueError:
            print("\nInvalid input. Please enter at lease one digit and enter numbers only.\n")

    heightFlag = False
    # asks for the height until the value entered is valid
    while not heightFlag:
        try:
            height = float(input("Please enter the height of the triangle: "))
            heightFlag = True

        except ValueError:
            print("\nInvalid input. Please enter at lease one digit and enter numbers only.\n")

    # calculate the area of a triangle using the formula
    area = str(0.5 * base * height)

    print("The area of your triangle is " + area)

# prompt user to select a shape until a valid shape is selected and call the appropriate function to calculate area
valid = False

while not valid:
    option = input("Enter c for circle and t for triangle: ")
    if option.lower() == "c" or option.lower() == "circle":
        valid = True
        circle_area_calculator()
    elif option.lower() == "t" or option.lower() == "triangle":
        valid = True
        triangle_area_calculator()
    else:
        print("\nInvalid input. Please enter c for circle and t for triangle.\n")

print("\n\nThank you for using the Area Calculator!")
