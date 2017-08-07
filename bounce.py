def bounce(angle):
    new_angle = abs(90-angle)
    turtle.right(-2*new_angle)
    return(new_angle)
basket_pos = basket.pos()
basket_x = basket_pos[0]
ba

if basket_x >= RIGHT_EDGE:
    bounce()

if basket_x >= LIFT_EDGE:
    bounce()

if basket_x >= UP_EDGE:
    bounce()

if basket_x >= DOWN_EDGE:
    quit()
