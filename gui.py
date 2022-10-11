import tkinter as tk
import random
from tkinter import ttk

from lighted_sphere import LightedSphere
from renderer import render_sphere

WIDTH = 512
HEIGHT = 660

CANVAS_SIZE = 512
IMAGE_SIZE = 512

RENDER_WINDOW_SIZE = 40

NUMBER_OF_COLORS = 8


class GUI:
    def __init__(self, sphere: LightedSphere):
        self.sphere = sphere

        self.root = tk.Tk()
        self.root.title("Sphere Renderer")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.resizable(False, False)

        self.frm = ttk.Frame(self.root, width = WIDTH, height = HEIGHT)
        self.frm.pack_propagate(False)
        self.frm.pack(fill = tk.BOTH, expand = tk.YES)

        ttk.Label(self.frm, text = "Test").pack()

        canvas = tk.Canvas(self.frm, bg="#000000", width = CANVAS_SIZE, height = CANVAS_SIZE)
        canvas.pack(side = tk.BOTTOM)

        self.image = tk.PhotoImage(width = IMAGE_SIZE, height = IMAGE_SIZE)
        canvas.create_image((CANVAS_SIZE // 2, CANVAS_SIZE // 2), image = self.image, state = "normal")

        canvas.bind("<Button-1>", self.handle_click)

    def start(self):
        self.render()
        self.root.mainloop()

    def handle_click(self, event):
        cx = (event.x - IMAGE_SIZE / 2) * 2 * RENDER_WINDOW_SIZE / IMAGE_SIZE
        cy = (event.y - IMAGE_SIZE / 2) * 2 * RENDER_WINDOW_SIZE / IMAGE_SIZE

        if self.sphere.try_set_x0_y0(cx, cy):
            self.render()

    def changed_option(self):
        pass

    def render(self):
        brightness_map = render_sphere(self.sphere, IMAGE_SIZE, RENDER_WINDOW_SIZE)

        for i, row in enumerate(brightness_map):
            for j, value in enumerate(row):
                if value == -1:
                    self.image.put("#000000", (i, j))
                    continue

                banded_value = int(NUMBER_OF_COLORS * value) / NUMBER_OF_COLORS
                value_hex = "#{:02x}{:02x}{:02x}".format(int(banded_value * 255), int(banded_value * 255), int(banded_value * 255))

                self.image.put(value_hex, (i, j))


