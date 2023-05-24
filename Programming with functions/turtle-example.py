import turtle

def draw_polygon(fred, x, y, size, sides):
    fred.up()
    fred.goto(x, y)
    fred.down()

    for i in range(sides):
        fred.fd(size)
        fred.left(360 / sides)

def draw_star(fred, x, y, size):
    fred.up()
    fred.goto(x, y)
    fred.down()

    for i in range(5):
        fred.fd(size)
        fred.right(180-36)

def draw_us_flag(fred, x, y):
    size = 30
    height = 30
    space = 40
    for row in range(9):
        if row % 2 == 0:
            # 6 stars
            for i in range(6):
                draw_star(fred, x + i * (size + space), y, size)
        else:
            # 5 stars
            for i in range(5):
                draw_star(fred, x + i * (size + space) + size / 2, y, size )
        y -= height

def main():
    turtle.setup(800, 800)
    fred = turtle.Turtle()
    fred.speed(0)

    for i in range(3,4000):
        draw_polygon(fred, 0, 0, 10, i)

    #draw_star(fred, 0, 0, 100)

    #draw_us_flag(fred, -200, 200)

    turtle.done()

main()