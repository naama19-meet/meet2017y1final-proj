import turtle

turtle_pos = turtle.pos


UP_EDGE = 300
RIGHT_EDGE = 500
LEFT_EDGE = -500
DOWN_EDGE = -300

SIZE_X=1000
SIZE_Y=600


turtle.setup(SIZE_X, SIZE_Y)

if turtle.pos <= DOWN_EDGE:
    turtle.quit()

turtle.goto(0, -310)


