import tkinter as tk
import math

initial_coordinates = [(100, 150), (300, 150)]
coordinates = [(100, 150), (300, 150)]


def draw_line(canvas):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)


def rotate_line(canvas):
    angle = float(rotation_entry.get()) if float(rotation_entry.get()) else 45
    angle_rad = math.radians(angle)
    start_x, start_y = coordinates[0]
    end_x, end_y = coordinates[1]
    translated_end_x = end_x - start_x
    translated_end_y = end_y - start_y
    rotated_end_x = translated_end_x * math.cos(
        angle_rad
    ) - translated_end_y * math.sin(angle_rad)
    rotated_end_y = translated_end_x * math.sin(
        angle_rad
    ) + translated_end_y * math.cos(angle_rad)
    new_end_x = rotated_end_x + start_x
    new_end_y = rotated_end_y + start_y
    new_coordinates = [(start_x, start_y), (new_end_x, new_end_y)]

    coordinates.clear()
    coordinates.extend(new_coordinates)
    canvas.delete("all")
    draw_line(canvas)


def translate_line(canvas, x, y):
    dx = x - coordinates[0][0]
    dy = y - coordinates[0][1]
    new_coordinates = [(start_x + dx, start_y + dy) for start_x, start_y in coordinates]

    coordinates.clear()
    coordinates.extend(new_coordinates)
    canvas.delete("all")
    draw_line(canvas)


def scale_line(canvas):
    start_x, start_y = coordinates[0]
    end_x, end_y = coordinates[1]
    scale_factor = float(scaling_entry.get()) if float(scaling_entry.get()) else 1.5
    scaled_end_x = start_x + (end_x - start_x) * scale_factor
    scaled_end_y = start_y + (end_y - start_y) * scale_factor
    new_coordinates = [(start_x, start_y), (scaled_end_x, scaled_end_y)]

    coordinates.clear()
    coordinates.extend(new_coordinates)
    canvas.delete("all")
    draw_line(canvas)


def reset_line(canvas):
    coordinates.clear()
    coordinates.extend(initial_coordinates)
    canvas.delete("all")
    draw_line(canvas)


def apply_transformation(event=None):
    selected_transformation = transformation.get()
    if selected_transformation == "rotate":
        rotate_line(canvas)
    elif selected_transformation == "translate":
        translate_line(canvas, event.x, event.y)
    elif selected_transformation == "scale":
        scale_line(canvas)


root = tk.Tk()
root.title("Line Transformation")

canvas = tk.Canvas(root, width=540, height=540, background="white")
canvas.pack()

draw_line(canvas)

transformation = tk.StringVar()
rotate_button = tk.Radiobutton(
    root, text="Rotate", variable=transformation, value="rotate"
)
rotate_button.pack(side=tk.LEFT, padx=10)

translate_button = tk.Radiobutton(
    root, text="Translate", variable=transformation, value="translate"
)
translate_button.pack(side=tk.LEFT, padx=10)

scale_button = tk.Radiobutton(
    root, text="Scale", variable=transformation, value="scale"
)
scale_button.pack(side=tk.LEFT, padx=10)

rotation_label = tk.Label(root, text="Rotation Angle:")
rotation_label.pack(side=tk.LEFT, padx=10)
rotation_entry = tk.Entry(root)
rotation_entry.pack(side=tk.LEFT)

scaling_label = tk.Label(root, text="Scaling Factor:")
scaling_label.pack(side=tk.LEFT, padx=10)
scaling_entry = tk.Entry(root)
scaling_entry.pack(side=tk.LEFT)

canvas.bind("<Button-1>", apply_transformation)

reset_button = tk.Button(root, text="Reset", command=lambda: reset_line(canvas))
reset_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
