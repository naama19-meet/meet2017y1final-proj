import turtle
basket = turtle.clone()





UP_EDGE = 300
RIGHT_EDGE = 500
LEFT_EDGE = -500
DOWN_EDGE = -300

SIZE_X=1000
SIZE_Y=600


basket.goto(0, -500)

basket_pos = basket.pos()

print(basket_pos[1])

turtle.setup(SIZE_X, SIZE_Y)

if basket_pos[1] <= DOWN_EDGE:
    print("yo")
    quit()


turtle.listen()

quit()

def move_basket():
    my_pos=basket.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    TIME_STEP=100
    turtle.ontimer(move_basket,TIME_STEP)



