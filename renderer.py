import math

from lighted_sphere import LightedSphere
from vector import Vector


"""
return: brightness_map - a 2d array of brightness values
Different ranges indicates different things
    0 -> 1 : the brightness of the sphere
    -1     : shadow on the wall
    -2     : the wall
    -3     : shadow on the floor 
    -4     : the floor
"""
def render_sphere(sphere: LightedSphere, resulution: int, render_window_size: float, background_distance: float):
    brightness_map = [[0.0 for _ in range(resulution)] for _ in range(resulution)]

    for x_index in range(resulution):
        for y_index in range(resulution):
            x = (2 * (x_index / resulution) - 1) * render_window_size
            y = (2 * (y_index / resulution) - 1) * render_window_size

            z_squared = math.pow(sphere.radius, 2) - math.pow(x, 2) - math.pow(y, 2)
            if z_squared < 0: # Background
                if y <= 0: # Floor
                    z = math.sin(math.pi / 4) * -(sphere.radius + background_distance)
                    pass
                else: # Wall
                    z = -(sphere.radius + background_distance)

                brightness_map[x_index][y_index] = -4
            else: # On sphere
                z = math.sqrt(z_squared)
                pos = Vector(x, y, z)
                bright = pos.dot(sphere.light_pos) / math.pow(sphere.radius, 2)
                brightness_map[x_index][y_index] = (bright + 1) / 2

    return brightness_map
