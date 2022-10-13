from lighted_sphere import LightedSphere
from renderer import render_sphere
from visualize import file_visualize, terminal_visualize
from gui import GUI


BACKGROUND_DISTANCE = 5


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
        terminal_visualize(render_sphere(sphere = sphere, resulution = res, render_window_size = rws, background_distance = BACKGROUND_DISTANCE))
    elif render_mode == "file":
        sphere = LightedSphere.create_from_user_input()
        res,rws = get_res_and_rws_from_user()
        file_visualize(render_sphere(sphere = sphere, resulution = res, render_window_size = rws, background_distance = BACKGROUND_DISTANCE))
    elif render_mode == "gui":
        sphere = LightedSphere(radius = 20, x0 = 0.0, y0 = 0.0)
        g = GUI(sphere)
        g.start()


if __name__ == "__main__":
    main()
