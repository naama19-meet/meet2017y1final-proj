def bounce(angle):
    new_angle = abs(90-angle)
    turtle.right(-2*new_angle)
    return(new_angle)
    
