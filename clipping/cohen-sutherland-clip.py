import tkinter as tk

INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000


def calculate_outcode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
        
    return code


def clip_line(canvas, x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    outcode1 = calculate_outcode(x1, y1, xmin, ymin, xmax, ymax)
    outcode2 = calculate_outcode(x2, y2, xmin, ymin, xmax, ymax)
    accept = None

    while True:
        if outcode1 == 0 and outcode2 == 0:
            accept = True
            break
        elif outcode1 & outcode2 != 0:
            break
        else:
            x, y = 0, 0
            outcode = outcode1 if outcode1 != 0 else outcode2
            if outcode & TOP != 0:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif outcode & BOTTOM != 0:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif outcode & RIGHT != 0:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif outcode & LEFT != 0:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if outcode == outcode1:
                x1, y1 = x, y
                outcode1 = calculate_outcode(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                outcode2 = calculate_outcode(x2, y2, xmin, ymin, xmax, ymax)
    if accept:
        print(f"Garis diterima dari x1 = {x1} y1 = {y1} x2 = {x2} y2 = {y2}")
        canvas.create_line(x1, y1, x2, y2, fill="red")


def clip_lines(canvas, lines, xmin, ymin, xmax, ymax):
    canvas.delete("original_line")
    for line in lines:
        x1, y1, x2, y2 = line
        clip_line(canvas, x1, y1, x2, y2, xmin, ymin, xmax, ymax)


def draw_line(event):
    global line_start_x, line_start_y, lines
    if line_start_x is None:
        line_start_x = event.x
        line_start_y = event.y
    else:
        x1 = line_start_x
        y1 = line_start_y
        x2 = event.x
        y2 = event.y
        lines.append((x1, y1, x2, y2))
        canvas.create_line(x1, y1, x2, y2, tags="original_line")
        line_start_x = None
        line_start_y = None


def clip_button_callback():
    clip_lines(canvas, lines, xmin, ymin, xmax, ymax)


line_start_x = None
line_start_y = None
lines = []

window = tk.Tk()
window.title("Line Clipping")
window.geometry("600x600")

canvas = tk.Canvas(window, width=540, height=540, background="white")
canvas.pack()
canvas.bind("<Button-1>", draw_line)

xmin, ymin, xmax, ymax = 100, 100, 440, 440
canvas.create_rectangle(xmin, ymin, xmax, ymax)

clip_button = tk.Button(
    window,
    text="Clip",
    command=clip_button_callback,
)
clip_button.pack()

window.mainloop()
