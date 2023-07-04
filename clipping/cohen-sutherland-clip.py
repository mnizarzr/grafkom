import tkinter as tk

# define region codes
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
    # Compute the region codes for both endpoints
    outcode1 = calculate_outcode(x1, y1, xmin, ymin, xmax, ymax)
    outcode2 = calculate_outcode(x2, y2, xmin, ymin, xmax, ymax)

    accept = None

    # Clip the line until it is visible or completely outside
    while True:
        if outcode1 == 0 and outcode2 == 0:
            # Both endpoints are inside, draw the line
            accept = True
            break
        elif outcode1 & outcode2 != 0:
            # Both endpoints are outside the same region, discard the line
            break
        else:
            # Compute the intersection point
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

            # Update the coordinates and recalculate the region code
            if outcode == outcode1:
                x1, y1 = x, y
                outcode1 = calculate_outcode(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                outcode2 = calculate_outcode(x2, y2, xmin, ymin, xmax, ymax)

    if accept:
        canvas.delete("original_line")
        canvas.create_line(x1, y1, x2, y)


def main():
    window = tk.Tk()
    window.title("Line Clipping")
    window.geometry("640x480")

    canvas = tk.Canvas(window, width=640, height=480)
    canvas.pack()

    # Window boundaries
    xmin, ymin, xmax, ymax = 100, 100, 500, 400
    canvas.create_rectangle(100, 100, 500, 400)

    # Line endpoints
    x1, y1, x2, y2 = 50, 50, 600, 350

    canvas.create_line(x1, y1, x2, y2, tags="original_line")
    # Button to clip the line
    B = tk.Button(
        window,
        text="Clip",
        command=lambda: clip_line(canvas, x1, y1, x2, y2, xmin, ymin, xmax, ymax),
    )
    B.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
