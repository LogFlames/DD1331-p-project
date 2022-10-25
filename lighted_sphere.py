from dataclasses import dataclass
import math

from vector import Vector


@dataclass
class LightedSphere:
    radius: float
    light_pos: Vector

    def __init__(self, radius: float, x0: float, y0: float):
        if radius <= 0:
            raise Exception("Radius must be greater than zero")

        self.radius = radius
        if not self.try_set_x0_y0(x0, y0):
            raise ValueError("Invalid x0 and y0 parameters, they are outside the sphere")

    def try_set_x0_y0(self, x0, y0) -> bool:
        z0_squared = math.pow(self.radius, 2) - math.pow(x0, 2) - math.pow(y0, 2)
        if z0_squared < 0:
            return False

        self.light_pos = Vector(x0, y0, math.sqrt(z0_squared))
        return True

    @staticmethod
    def are_valid_x0_y0(radius: float, x0: float, y0: float) -> bool:
        return math.pow(radius, 2) - math.pow(x0, 2) - math.pow(y0, 2) >= 0

    @staticmethod
    def create_from_user_input():
        radius = None
        x0 = None
        y0 = None

        while radius is None:
            radius_str = input("Radius of the sphere: ")
            try:
                radius = float(radius_str)
            except ValueError:
                print("Please enter a valid float.")
                continue

            if radius <= 0:
                print("Radius must be greater than zero")
                radius = None
                continue

        while x0 is None or y0 is None or not LightedSphere.are_valid_x0_y0(radius, x0, y0):
            x0y0_str = input("Enter x0 and y0 of the point the light shall hit first, separated by a space, the coordinate must lie on the sphere: ")

            try:
                x0_str,y0_str = x0y0_str.split()
            except ValueError:
                print("Please enter two values separated by a space.")
                continue

            try:
                x0,y0 = float(x0_str),-float(y0_str)
            except ValueError:
                print("Please enter float values.")
                continue

            if not LightedSphere.are_valid_x0_y0(radius, x0, y0):
                print("Please enter values that are within the sphere.")
                continue

        return LightedSphere(radius = radius, x0 = x0, y0 = y0)
