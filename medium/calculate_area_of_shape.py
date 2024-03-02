"""
Find Area of Circle: Calculate the area of a circle given radius.
Find Area of Square: Calculate the area of a square given length of side.
Find Area of Rectangle: Calculate the area of a rectangle given length and breadth.
Find Area of Triangle: Calculate the area of a triangle given base and height.
Find Area of Cube: Calculate the area of a cube given length of side.
Find Area of Cuboid: Calculate the area of a cuboid given length, breadth and height.
Find Area of Sphere : Calculate the area of a sphere given radius.
"""

import math


def area_of_shape(shape_name, *args):
    shape_name = shape_name.lower()
    area = 0
    if shape_name == "circle":
        area = math.pi * (args[0] ** 2)

    elif shape_name == "square":
        area = args[0] ** 2

    elif shape_name == "rectangle":
        area = args[0] * args[1]

    elif shape_name == "triangle":
        area = 0.5 * args[0] * args[1]

    elif shape_name == "cube":
        area = 6 * (args[0] ** 2)

    elif shape_name == "cuboid":
        area = 2*(args[0]*args[1] + args[0]*args[2] + args[1]*args[2])

    elif shape_name == "sphere":
        area = 4 * math.pi * (args[0] ** 2)

    return round(area, 2)


def get_dimensions(shape):
    if shape == "circle" or shape == "sphere":
        radius = float(input(f"Enter radius for {shape}:"))
        return [radius]
    elif shape == "square" or shape == "cube":
        side = float(input(f"Enter side for {shape}:"))
        return [side]
    elif shape == "rectangle":
        length = float(input(f"Enter length for {shape}:"))
        breadth = float(input(f"Enter breadth for {shape}:"))
        return length, breadth
    elif shape == "triangle":
        base = float(input(f"Enter base of {shape}:"))
        height = float(input(f"Enter height of {shape}:"))
        return base, height
    elif shape == "cuboid":
        length = float(input(f"Enter length for {shape}:"))
        breadth = float(input(f"Enter breadth for {shape}:"))
        height = float(input(f"Enter height of {shape}:"))
        return length, breadth, height
    else:
        print("Invalid shape name. Please confirm if there is not any typo.")


def main():
    shape = input("Enter shape name : ")
    dimensions = get_dimensions(shape)
    area = area_of_shape(shape, *dimensions)
    print(f"Area of {shape} = {area} sq.units")


if __name__ == "__main__":
    main()
