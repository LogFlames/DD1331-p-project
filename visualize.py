def ascii_gradient(value: float):
    if (value < 0 or value > 1) and value not in [-1, -2, -3, -4]:
        raise Exception("Cannot convert value other than -1 and outside the 0->1 range to an ascii character")

    gradient = [
        (".", -4), # Floor
        ("S", -3), # Floor Shadow
        (" ", -2), # Wall
        ("S", -1), # Wall Shadow
        (",", 0.3),
        ("-", 0.55),
        ("+", 0.7),
        ("*", 0.85),
        ("M", 1)
    ]

    return next(char for char, bright in gradient if bright >= value)


def terminal_visualize(brightness_map: list[list[float]]):
    lines = ["" for _ in range(len(brightness_map))]
    for row in brightness_map:
        for i, char in enumerate(row):
            # Make each 'pixel' two character wide and one high for it to be square
            # Monospace fonts are twice as high as they are wide
            lines[i] += ascii_gradient(char) * 2

    print("\n".join(lines))


def file_visualize(brightness_map: list[list[float]]):
    lines = ["" for _ in range(len(brightness_map))]
    for row in brightness_map:
        for i, char in enumerate(row):
            # Make each 'pixel' two character wide and one high for it to be square
            # Monospace fonts are twice as high as they are wide
            lines[i] += ascii_gradient(char) * 2

    print("\n".join(lines))

    with open("rendered_sphere.txt", "w+") as f:
        f.write("\n".join(lines))
        print("Sphere renedered to 'rendered_sphere.txt'.")
