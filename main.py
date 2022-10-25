from lighted_sphere import LightedSphere
from renderer import render_sphere
from visualize import file_visualize, terminal_visualize
from gui import GUI


BACKGROUND_DISTANCE = 5
FLOOR_ANGLE = 3 
RENDER_WINDOW_SIZE = 50


def get_res_from_user() -> int:
    resulution = None

    while resulution is None:
        resulution_str = input("Render resulution (size of image): ")
        try:
            resulution = int(resulution_str)
        except ValueError:
            print("Please enter a valid integer.")

    return resulution

def info():
    print("This program will render a sphere, lit up by a directional light, against a background.")
    print("It will be rendered either to the terminal, written into a file or shown in a GUI.")
    print("You will decide the radius of the sphere and which point on the sphere the light will hit first.")
    print("The gui provides some extra options of distance between the background and sphere, aswell as the angle of the floor. In the GUI you can also decide on the color-resulution, how many colors it will use to render.")
    print("When rendering to the terminal or a file you can choose the resulution. The render will be twice as many characters wide as it is tall, as each character is twice as high as it is wide.")
    print("See this for a visualization of the scene from the side: https://www.desmos.com/calculator/b5n82epbuy")
    print("")


def main():
    info()

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
