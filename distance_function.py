def distance(basket_pos,square_pos):
    basket_x,basket_y = basket_pos
    square_x,square_y = square_pos
    d = ((basket_x-square_x)**2 + (basket_y-square_y)**2)**(1/2)
    return d
