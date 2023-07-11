from tkinter import *
import math

def putPixel(x, y):
    canvas.create_line(x, y, x+1, y, fill="red")

def drawCircle(xc, yc, x, y):
    h = canvas.winfo_height()
    w = canvas.winfo_width()

    putPixel(xc + x + w//2, (h//2) - (yc + y))
    putPixel(xc - x + w//2, (h//2) - (yc + y))
    putPixel(xc + x + w//2, (h//2) - (yc - y))
    putPixel(xc - x + w//2, (h//2) - (yc - y))
    putPixel(xc + y + w//2, (h//2) - (yc + x))
    putPixel(xc - y + w//2, (h//2) - (yc + x))
    putPixel(xc + y + w//2, (h//2) - (yc - x))
    putPixel(xc - y + w//2, (h//2) - (yc - x))

def circleBres(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    while y >= x:
        drawCircle(xc, yc, x, y)
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        drawCircle(xc, yc, x, y)
        canvas.update()
        canvas.after(50)

# Create the tkinter window
window = Tk()
window.title("Bresenham's Circle Drawing Algorithm")
canvas = Canvas(window, width=500, height=500, bg="white")
canvas.pack()

# Draw the axes
h = canvas.winfo_height()
w = canvas.winfo_width()
canvas.create_line(0, h//2, w, h//2)
canvas.create_line(w//2, 0, w//2, h)

circleBres(0, 0, 100)
# circleBres(0, 0, 50)

window.mainloop()
