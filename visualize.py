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

    with open("rendered_sphere.txt", "w+") as f:
        f.write(lines)
        print("Sphere renedered to file.")
