import turtle

turtle.tracer(1,0)

# screen setup
size_x = 800
size_y = 800
turtle.setup(size_x, size_y)
square_size = 20

# make the right turtle object
block_stamper = turtle.clone()
turtle.hideturtle()
block_stamper.shape("square")
block_stamper.color("black")
block_stamper.penup()
block_stamper.goto(-315, 200)


# lists to keep track of positions and stamps
block_pos = []
block_stamps = []

# loop variables
start_x = -315
end_x = 315
start_y = 200

# 30 blocks on one line
# 7 lines of blocks
# move and stamp
for c in range(7):
    for n in range(start_x, end_x - (2*square_size) + 1, square_size):
        pos = block_stamper.pos()
        block_stamper.goto(pos[0] + square_size + 2, pos[1])
        stamp_id = block_stamper.stamp()
        block_pos.append(block_stamper.pos())
        block_stamps.append(stamp_id)
    pos = block_stamper.pos()
    block_stamper.goto(start_x, pos[1] - (square_size + 2))
block_stamper.hideturtle()
    
