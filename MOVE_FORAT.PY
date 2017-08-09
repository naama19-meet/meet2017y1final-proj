import turtle
UP_EDGE = 300
RIGHT_EDGE = 500
LEFT_EDGE = -500
DOWN_EDGE = -300
TIME_STEP = 100

SIZE_X = 1000
SIZE_Y = 600

turtle.setup(SIZE_X, SIZE_Y)
basket = turle.clone()
turtle.register_shape("basket1.gif")
basket.penup()

def move_basket():
    b_x, b_y = basket.pos()


    turtle.ontimer(move_basket,TIME_STEP)
