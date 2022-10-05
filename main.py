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


def ascii_gradient(value: float):
    if (value < 0 or value > 1) and value != -1:
        raise Exception("Cannot convert value other than -1 and outside the 0->1 range to an ascii character")

    gradient = [
        (" ", -1),
        (".", 0.3),
        ("-", 0.55),
        ("+", 0.7),
        ("*", 0.85),
        ("M", 1)
    ]

    return next(char for char, bright in gradient if bright >= value)


def terminal_visualize(brightness_map: list[list[float]]):
    lines = ""
    for row in brightness_map:
        lines += "".join(
                map(
                    # Make each 'pixel' two character wide and one high for it to be square
                    # Monospace fonts are twice as high as they are wide
                    lambda value: ascii_gradient(value) * 2, 
                    row)
                )
        lines += "\n"

    print(lines)


def file_visualize(brightness_map: list[list[float]]):
    _ = brightness_map[0]


def get_res_and_rws_from_user() -> tuple[int, float]:
    resulution = None
    render_window_size = None

    while resulution is None:
        resulution_str = input("Render resulution (size of image): ")
        try:
            resulution = int(resulution_str)
        except ValueError:
            print("Please enter a valid integer.")

    while render_window_size is None:
        render_window_size_str = input("Render window size (render from coords (-rws,-rws) to (rws,rws)): ")
        try:
            render_window_size = int(render_window_size_str)
        except ValueError:
            print("Please enter a valid integer.")

    return resulution, render_window_size


def main():
    while (render_mode := input("Render using 'terminal', 'file' or 'GUI'? ").lower().strip()) not in ["terminal", "file", "gui"]:
        print(f"Invalid option '{render_mode}', please enter one of the options above.")

    if render_mode == "terminal":
        sphere = LightedSphere.create_from_user_input()
        res,rws = get_res_and_rws_from_user()
        terminal_visualize(render_sphere(sphere = sphere, resulution = res, render_window_size = rws))
    elif render_mode == "file":
        sphere = LightedSphere.create_from_user_input()
        res,rws = get_res_and_rws_from_user()
        file_visualize(render_sphere(sphere = sphere, resulution = res, render_window_size = rws))
    elif render_mode == "gui":
        sphere = LightedSphere(radius = 20, x0 = 0.0, y0 = 0.0)
        pass


if __name__ == "__main__":
    main()
