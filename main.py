from lighted_sphere import LightedSphere
from renderer import render_sphere
from visualize import file_visualize, terminal_visualize
from gui import GUI


BACKGROUND_DISTANCE = 5
FLOOR_ANGLE = 3 
RENDER_WINDOW_SIZE = 40


def get_res_from_user() -> int:
    resulution = None

    while resulution is None:
        resulution_str = input("Render resulution (size of image): ")
        try:
            resulution = int(resulution_str)
        except ValueError:
            print("Please enter a valid integer.")

    return resulution


def main():
    while (render_mode := input("Render using 'terminal', 'file' or 'GUI'? ").lower().strip()) not in ["terminal", "file", "gui"]:
        print(f"Invalid option '{render_mode}', please enter one of the options above.")

    if render_mode == "terminal":
        sphere = LightedSphere.create_from_user_input()
        res = get_res_from_user()
        terminal_visualize(render_sphere(sphere = sphere, resulution = res, render_window_size = RENDER_WINDOW_SIZE, background_distance = BACKGROUND_DISTANCE, floor_angle = FLOOR_ANGLE))
    elif render_mode == "file":
        sphere = LightedSphere.create_from_user_input()
        res = get_res_from_user()
        file_visualize(render_sphere(sphere = sphere, resulution = res, render_window_size = RENDER_WINDOW_SIZE, background_distance = BACKGROUND_DISTANCE, floor_angle = FLOOR_ANGLE))
    elif render_mode == "gui":
        sphere = LightedSphere(radius = 20, x0 = 0.0, y0 = 0.0)
        g = GUI(sphere)
        g.start()


if __name__ == "__main__":
    main()
