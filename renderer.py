import math

from lighted_sphere import LightedSphere


def render_sphere(sphere: LightedSphere, resulution: int, render_window_size: float):
    brightness_map = [[0.0 for _ in range(resulution)] for _ in range(resulution)]

    for x_index in range(resulution):
        for y_index in range(resulution):
            x = (2 * (x_index / resulution) - 1) * render_window_size
            y = (2 * (y_index / resulution) - 1) * render_window_size

            z_squared = math.pow(sphere.radius, 2) - math.pow(x, 2) - math.pow(y, 2)
            if z_squared < 0:
                brightness_map[x_index][y_index] = -1
            else:
                z = math.sqrt(z_squared)
                bright = (x * sphere.x0 + y * sphere.y0 + z * sphere.z0) / math.pow(sphere.radius, 2)
                brightness_map[x_index][y_index] = (bright + 1) / 2

    return brightness_map
