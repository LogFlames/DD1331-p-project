import math


class Vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def normalized(self):
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag, self.z / mag)

    def magnitude(self):
        return math.sqrt(self.sqr_magnitude())

    def sqr_magnitude(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

