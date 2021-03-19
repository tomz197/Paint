from tkinter import *


class Color:
    def __init__(self, red, green, blue, column_, row_):
        Button(window, text="",
               width=3, height=1,
               bd=0, bg=rgb((red, green, blue)),
               command=lambda: change_color(red, green, blue)
               ).grid(row=row_, column=column_, padx=2, pady=2, sticky='WSN')


def rgb(value):
    return "#%02x%02x%02x" % value


def clear_canvas():
        canvas.delete('all')


def change_color(r, g, b):
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)
    set_color(1)


def set_color(event):
    color_label.config(bg=rgb(get_rgb()))


def get_rgb():
    r = int(red_slider.get())
    g = int(green_slider.get())
    b = int(blue_slider.get())
    return r, g, b


def draw_line(event):
    global clicked, x, y
    if clicked == 0:
        x = event.x
        y = event.y
        clicked = 1
    else:
        x2 = event.x
        y2 = event.y
        canvas.create_line(x, y, x2, y2,
                           widt=width_slider.get(),
                           fill=rgb(get_rgb()))
        clicked = 0


def paint(event):
    r = int(width_slider.get())
    x1, y1 = (event.x - r), (event.y - r)
    x2, y2 = (event.x + r), (event.y + r)
    canvas.create_oval(x1, y1, x2, y2, fill=rgb(get_rgb()), width=0)


# --------------------------------------------------------------------------------------------------- Main code

# ----------------------------------------------------------------------------- setup
window = Tk()
window.configure(bg=rgb((15, 15, 15)), width=1020, height=800)
window.title("Skicar")
window.grid_columnconfigure(17, weight=1)
canvas = Canvas(window, width=1000, height=700, bg=rgb((30, 30, 30)))

# ----------------------------------------------------------------------------- widgets
# --------------------------------------------------------------- button
clear_button = Button(window, text="Click\nto\nclear\ncanvas",
                      font=('Arial', 10, 'bold'),
                      width=8, height=1, fg=rgb((230, 230, 230)),
                      bd=0, bg=rgb((40, 40, 40)),
                      command=lambda: clear_canvas())
set_bg_button = Button(window, text="Click to change\nbackground",
                       font=('Arial', 9, 'bold'),
                       width=8, height=1, fg=rgb((230, 230, 230)),
                       bd=0, bg=rgb((40, 40, 40)),
                       command=lambda: canvas.configure(bg=rgb(get_rgb())))

Color(255, 0, 0, 6, 0)
Color(255, 160, 0, 7, 0)
Color(255, 255, 0, 8, 0)
Color(0, 200, 0, 9, 0)
Color(0, 0, 255, 10, 0)
Color(0, 170, 255, 11, 0)
Color(255, 0, 255, 12, 0)
Color(120, 70, 20, 13, 0)
Color(0, 0, 0, 14, 0)
Color(85, 85, 85, 15, 0)
Color(170, 170, 170, 16, 0)
Color(255, 255, 255, 17, 0)

Color(255, 125, 125, 6, 1)
Color(255, 160, 125, 7, 1)
Color(255, 255, 125, 8, 1)
Color(125, 200, 125, 9, 1)
Color(125, 125, 255, 10, 1)
Color(125, 170, 255, 11, 1)
Color(255, 125, 255, 12, 1)
Color(150, 100, 50, 13, 1)
Color(0, 0, 0, 14, 1)
Color(85, 85, 85, 15, 1)
Color(170, 170, 170, 16, 1)
Color(255, 255, 255, 17, 1)
# --------------------------------------------------------------- slider
width_slider = Scale(window, width=15, sliderlength=20, length=100, bd=0,
                     font=('Arial', 7, 'bold'),
                     from_=1, to=50, orient=HORIZONTAL)
red_slider = Scale(window, width=15, sliderlength=20, length=150, bd=0,
                   font=('Arial', 7, 'bold'),
                   from_=1, to=255, orient=HORIZONTAL)
green_slider = Scale(window, width=15, sliderlength=20, length=150, bd=0,
                     font=('Arial', 7, 'bold'),
                     from_=1, to=255, orient=HORIZONTAL)
blue_slider = Scale(window, width=15, sliderlength=20, length=150, bd=0,
                    font=('Arial', 7, 'bold'),
                    from_=1, to=255, orient=HORIZONTAL)
# --------------------------------------------------------------- label
rgb_label = Label(window, text="color:\nR\nG\nB",
                  width=8,  height=1, fg=rgb((230, 230, 230)),
                  font=('Arial', 10, 'bold'),
                  bd=0, bg=rgb((40, 40, 40)))
width_label = Label(window, text="width:",
                    width=6,  height=1, fg=rgb((230, 230, 230)),
                    font=('Arial', 10, 'bold'),
                    bd=0, bg=rgb((40, 40, 40)))
color_label = Label(window, text="",
                    width=10,  height=2, fg=rgb((230, 230, 230)),
                    bd=0, bg=rgb(get_rgb()))
none_label = Label(window, text="", width=0, height=0, bd=0, bg=rgb((15, 15, 15)))
# --------------------------------------------------------------- bind
canvas.bind('<Button-3>', draw_line)
canvas.bind("<Button-1>", paint)
canvas.bind("<B1-Motion>", paint)
clicked = 0
red_slider.bind("<B1-Motion>", set_color)
green_slider.bind("<B1-Motion>", set_color)
blue_slider.bind("<B1-Motion>", set_color)

# ----------------------------------------------------------------------------- position

canvas.grid(row=3, column=0, columnspan=18, padx=2, pady=2, sticky='W')
# ------------------------------------- button
set_bg_button.grid(row=2, column=5, padx=2, pady=2, sticky='WSEN')
clear_button.grid(row=0, column=0, rowspan=3, padx=2, pady=2, sticky='WSEN')
# ------------------------------------- label
rgb_label.grid(row=0, column=1, rowspan=3, padx=2, pady=2, sticky='WSEN')
width_label.grid(row=0, column=5, padx=2, pady=2, sticky='WSEN')
color_label.grid(row=0, column=4, rowspan=3, padx=2, pady=2, sticky='WSEN')
none_label.grid(row=0, column=18)
# ------------------------------------- entry
red_slider.grid(row=0, column=2, padx=2, pady=1, sticky='WSEN')
green_slider.grid(row=1, column=2, padx=2, pady=1, sticky='WSEN')
blue_slider.grid(row=2, column=2, padx=2, pady=1, sticky='WSEN')

width_slider.grid(row=1, column=5, padx=2, pady=2, sticky='WSEN')

window.mainloop()
