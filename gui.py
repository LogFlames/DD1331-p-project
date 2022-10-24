import math
import itertools

import time

import tkinter as tk
from tkinter import ttk

from lighted_sphere import LightedSphere
from renderer import render_sphere, PixelEnum


WIDTH = 512
HEIGHT = 1024

CANVAS_SIZE = 512
IMAGE_SIZE = CANVAS_SIZE

RENDER_WINDOW_SIZE = 40


class GUI:
    def __init__(self, sphere: LightedSphere):
        self.sphere = sphere
        self.number_of_colors = 8
        self.background_distance = 5
        self.background_angle = 75

        self.root = tk.Tk()
        self.root.title("Sphere Renderer")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.resizable(False, False)

        self.frm = ttk.Frame(self.root, width = WIDTH, height = HEIGHT)
        self.frm.pack(fill = tk.BOTH, expand = tk.YES)

        self.radius_scale = tk.Scale(
                self.frm, 
                label = "Radius",
                from_ = 1, 
                to = RENDER_WINDOW_SIZE, 
                orient = tk.HORIZONTAL, 
                length = WIDTH // 2, 
                resolution = -1)
        self.radius_scale.set(self.sphere.radius)
        self.radius_scale.pack()

        self.number_of_colors_label = ttk.Label(self.frm, text = str(self.number_of_colors))
        self.number_of_colors_label.pack()

        self.number_of_colors_scale = tk.Scale(
                self.frm, 
                label = "Number of Colors",
                from_ = 1, 
                to = 8, 
                orient = tk.HORIZONTAL, 
                length = WIDTH // 2, 
                resolution = 1, 
                showvalue = False, 
                command = lambda new_noc: self.number_of_colors_label.config(text = str(2 ** int(new_noc))))
        self.number_of_colors_scale.set(math.log2(self.number_of_colors))
        self.number_of_colors_scale.pack()

        self.background_distance_scale = tk.Scale(
                self.frm, 
                label = "Background Distance",
                from_ = 0, 
                to = 100, 
                orient = tk.HORIZONTAL, 
                length = WIDTH // 2, 
                resolution = -1)
        self.background_distance_scale.set(self.background_distance)
        self.background_distance_scale.pack()

        self.background_angle_scale = tk.Scale(
                self.frm, 
                label = "Background Angle",
                from_ = 1, 
                to = 90, 
                orient = tk.HORIZONTAL, 
                length = WIDTH // 2, 
                resolution = 1)
        self.background_angle_scale.set(self.background_angle)
        self.background_angle_scale.pack()

        ttk.Button(self.frm, text = "Update", command = self.parameter_changed).pack()

        self.canvas = tk.Canvas(self.frm, bg="#000000", width = CANVAS_SIZE, height = CANVAS_SIZE)
        self.canvas.pack(side = tk.BOTTOM)

        self.image = tk.PhotoImage(width = IMAGE_SIZE, height = IMAGE_SIZE)
        self.canvas.create_image((CANVAS_SIZE // 2, CANVAS_SIZE // 2), image = self.image, state = "normal")

        self.canvas.bind("<Button-1>", self.handle_click)

    def start(self):
        self.render()
        self.root.mainloop()

    def handle_click(self, event):
        cx = (event.x - IMAGE_SIZE / 2) * 2 * RENDER_WINDOW_SIZE / IMAGE_SIZE
        cy = (event.y - IMAGE_SIZE / 2) * 2 * RENDER_WINDOW_SIZE / IMAGE_SIZE

        if self.sphere.try_set_x0_y0(cx, cy):
            self.render()

    def parameter_changed(self):
        new_radius = self.radius_scale.get()
        new_number_of_colors = 2 ** int(self.number_of_colors_scale.get())
        new_background_distance = self.background_distance_scale.get()
        new_background_angle = self.background_angle_scale.get()

        radius_change_factor = new_radius / self.sphere.radius
        self.sphere.radius = new_radius
        self.sphere.try_set_x0_y0(self.sphere.light_pos.x * radius_change_factor, self.sphere.light_pos.y * radius_change_factor)

        self.number_of_colors = new_number_of_colors
        self.background_distance = new_background_distance
        self.background_angle = new_background_angle

        self.render()

    def render(self):
        brightness_map = render_sphere(self.sphere, IMAGE_SIZE, RENDER_WINDOW_SIZE, self.background_distance, (self.background_angle + 90) / 90 * math.pi / 2)

        for i, row in enumerate(brightness_map):
            for j, pixel in enumerate(row):
                if pixel == PixelEnum.FLOOR:
                    self.image.put("#990000", (i, j))
                elif pixel == PixelEnum.FLOOR_SHADOW:
                    self.image.put("#440000", (i, j))
                elif pixel == PixelEnum.WALL:
                    self.image.put("#009900", (i, j))
                elif pixel == PixelEnum.WALL_SHADOW:
                    self.image.put("#004400", (i, j))
                else:
                    banded_value = int(self.number_of_colors * pixel) / self.number_of_colors
                    value_hex = "#{:02x}{:02x}{:02x}".format(int(banded_value * 255), int(banded_value * 255), int(banded_value * 255))
                    self.image.put(value_hex, (i, j))


