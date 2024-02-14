import math

def cylinder_volume(radius, height):
    """
    Calculate the volume of a cylinder.

    :param radius: The radius of the base of the cylinder.
    :param height: The height of the cylinder.
    :return: The volume of the cylinder.
    """
    return math.pi * (radius ** 2) * height

if __name__ == "__main__":
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    volume = cylinder_volume(radius, height)
    print(f"The volume of the cylinder is: {volume}")