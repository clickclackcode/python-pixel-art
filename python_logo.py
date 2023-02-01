import turtle

# colors
black = '#000000'
light_blue = '#55ccff'
med_blue = '#0099ff'
dark_blue = '#0055dd'
light_yellow = '#ffff88'
med_yellow = '#ffee00'
dark_yellow = '#ffcc00'

# create the turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(1)
t.penup()

# directions
north = (0, 1)
south = (0, -1)
east = (1, 0)
west = (-1, 0)
northwest = (-1, 1)
northeast = (1, 1)
southwest = (-1, -1)
southeast = (1, -1)

# function for drawing pixels
def draw_pixels(x, y, num, color, dir, size = 10):
    t.goto(x * size, y * size)
    t.color(color)
    for i in range(num):
        t.begin_fill()
        for j in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()
        t.forward(size * dir[0])
        t.left(90)
        t.forward(size * dir[1])
        t.right(90)

# blue snake outline
draw_pixels(-7, 16, 14, black, east)
draw_pixels(7, 15, 15, black, south)
draw_pixels(6, 1, 16, black, west)
draw_pixels(-9, 0, 7, black, south)
draw_pixels(-10, -7, 6, black, west)
draw_pixels(-16, -6, 14, black, north)
draw_pixels(-15, 8, 16, black, east)
draw_pixels(0, 9, 9, black, west)
draw_pixels(-8, 10, 6, black, north)
draw_pixels(-9, 15, 6, black, south)
draw_pixels(-9, 9, 7, black, west)
draw_pixels(-17, 7, 14, black, south)
draw_pixels(-15, -8, 6, black, east)
draw_pixels(-8, -6, 7, black, north)
draw_pixels(-7, 0, 16, black, east)
draw_pixels(8, 1, 15, black, north)
draw_pixels(6, 17, 14, black, west)

# blue snake eyes
draw_pixels(-5, 13, 2, black, east)
draw_pixels(-4, 12, 2, black, west)

# yellow snake outline
draw_pixels(9, 8, 6, black, east)
draw_pixels(15, 7, 14, black, south)
draw_pixels(14, -7, 16, black, west)
draw_pixels(-1, -8, 9, black, east)
draw_pixels(7, -9, 6, black, south)
draw_pixels(6, -15, 14, black, west)
draw_pixels(-8, -14, 8, black, north)
draw_pixels(-9, -7, 8, black, south)
draw_pixels(-7, -16, 14, black, east)
draw_pixels(8, -14, 7, black, north)
draw_pixels(9, -8, 6, black, east)
draw_pixels(16, -6, 14, black, north)
draw_pixels(14, 9, 6, black, west)

# yellow snake eyes
draw_pixels(3, -11, 2, black, east)
draw_pixels(4, -12, 2, black, west)

# blue snake fill
draw_pixels(-7, 15, 14, light_blue, east)
draw_pixels(-7, 14, 14, light_blue, east)
draw_pixels(-7, 13, 2, med_blue, east)
draw_pixels(-3, 13, 10, med_blue, east)
draw_pixels(-7, 12, 2, med_blue, east)
draw_pixels(-3, 12, 10, med_blue, east)
draw_pixels(-7, 11, 8, dark_blue, east)
draw_pixels(1, 11, 6, med_blue, east)
draw_pixels(-7, 10, 8, dark_blue, east)
draw_pixels(1, 10, 6, med_blue, east)
draw_pixels(1, 9, 6, med_blue, east)
draw_pixels(1, 8, 6, med_blue, east)
draw_pixels(-15, 7, 16, light_blue, east)
draw_pixels(1, 7, 6, med_blue, east)
draw_pixels(-15, 6, 16, light_blue, east)
draw_pixels(1, 6, 6, med_blue, east)
draw_pixels(-15, 5, 22, med_blue, east)
draw_pixels(-15, 4, 22, med_blue, east)
draw_pixels(-15, 3, 6, med_blue, east)
draw_pixels(-9, 3, 16, dark_blue, east)
draw_pixels(-15, 2, 6, med_blue, east)
draw_pixels(-9, 2, 16, dark_blue, east)
draw_pixels(-15, 1, 6, med_blue, east)
draw_pixels(-15, 0, 6, med_blue, east)
draw_pixels(-15, -1, 6, med_blue, east)
draw_pixels(-15, -2, 6, med_blue, east)
draw_pixels(-15, -3, 6, med_blue, east)
draw_pixels(-15, -4, 6, med_blue, east)
draw_pixels(-15, -5, 6, dark_blue, east)
draw_pixels(-15, -6, 6, dark_blue, east)

# yellow snake fill
draw_pixels(9, 7, 6, light_yellow, east)
draw_pixels(9, 6, 6, light_yellow, east)
draw_pixels(9, 5, 6, med_yellow, east)
draw_pixels(9, 4, 6, med_yellow, east)
draw_pixels(9, 3, 6, med_yellow, east)
draw_pixels(9, 2, 6, med_yellow, east)
draw_pixels(9, 1, 6, med_yellow, east)
draw_pixels(9, 0, 6, med_yellow, east)
draw_pixels(-7, -1, 16, light_yellow, east)
draw_pixels(9, -1, 6, med_yellow, east)
draw_pixels(-7, -2, 16, light_yellow, east)
draw_pixels(9, -2, 6, med_yellow, east)
draw_pixels(-7, -3, 22, med_yellow, east)
draw_pixels(-7, -4, 22, med_yellow, east)
draw_pixels(-7, -5, 6, med_yellow, east)
draw_pixels(-1, -5, 16, dark_yellow, east)
draw_pixels(-7, -6, 6, med_yellow, east)
draw_pixels(-1, -6, 16, dark_yellow, east)
draw_pixels(-7, -7, 6, med_yellow, east)
draw_pixels(-7, -8, 6, med_yellow, east)
draw_pixels(-7, -9, 6, med_yellow, east)
draw_pixels(-1, -9, 8, light_yellow, east)
draw_pixels(-7, -10, 6, med_yellow, east)
draw_pixels(-1, -10, 8, light_yellow, east)
draw_pixels(-7, -11, 10, med_yellow, east)
draw_pixels(5, -11, 2, med_yellow, east)
draw_pixels(-7, -12, 10, med_yellow, east)
draw_pixels(5, -12, 2, med_yellow, east)
draw_pixels(-7, -13, 14, dark_yellow, east)
draw_pixels(-7, -14, 14, dark_yellow, east)

turtle.done()