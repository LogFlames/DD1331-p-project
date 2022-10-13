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
def render_sphere(sphere: LightedSphere, resulution: int, render_window_size: float, background_distance: float, floor_angle: float):
    brightness_map = [[0.0 for _ in range(resulution)] for _ in range(resulution)]

    light_direction = -sphere.light_pos.normalized()

    for x_index in range(resulution):
        for y_index in range(resulution):
            x = (2 * (x_index / resulution) - 1) * render_window_size
            y = (2 * (y_index / resulution) - 1) * render_window_size

            z_squared = math.pow(sphere.radius, 2) - math.pow(x, 2) - math.pow(y, 2)
            if z_squared < 0: # Background
                floor_point_y = -math.cos(floor_angle) * (sphere.radius + background_distance)
                floor_point_z = -math.sin(floor_angle) * (sphere.radius + background_distance)

                z = (y + floor_point_z) / math.tan(floor_angle + math.pi / 2) - floor_point_y

                if z < -background_distance - sphere.radius: 
                    # The point is on the wall
                    z = -background_distance - sphere.radius
                    brightness_map[x_index][y_index] = -2
                else:
                    # The point is on the floor
                    brightness_map[x_index][y_index] = -4

                background_point = Vector(x, y, z)

                # Math from: https://en.wikipedia.org/wiki/Line%E2%80%93sphere_intersection
                delta = (light_direction.dot(background_point)) ** 2 - (background_point.sqr_magnitude() - sphere.radius ** 2)

                if delta >= 0: # There exists one or two intersections between the light line from the background_point with the sphere, so it is covered in shadows
                    brightness_map[x_index][y_index] += 1
            else: # On sphere
                z = math.sqrt(z_squared)
                pos = Vector(x, y, z)
                bright = pos.dot(sphere.light_pos) / math.pow(sphere.radius, 2)
                brightness_map[x_index][y_index] = (bright + 1) / 2

    return brightness_map
