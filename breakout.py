import turtle
##turtle
turtle.penup()
#turtle.hideturtle()
block_pos = []
block_stamps = []

# the screen
size_x = 1000
size_y = 600
turtle.setup(size_x , size_y)
turtle.bgcolor("Black")




###the platform
plat = turtle.clone()
plat.shape("square")
plat.color("White")
plat.penup()
plat.goto(0 , -250)
plat.pendown()





###platform movements






###blocks

block = turtle.clone()
block.shape("square")
block.penup()
block.goto(450,250)
bs = block.stamp()
block.color("White")

gg = 400
for i in range(17):
    
    block.goto(gg , 250)
    bs = block.stamp()
    gg = gg - 50 
bb = 400
for i in range(17):
    block.goto(bb , 200)
    bs = block.stamp()
    bb = bb - 50    
ff = 400
for i in range(17):
    
    block.goto(ff , 150)
    bs = block.stamp()
    ff = ff - 50
xx = 400
for i in range(17):
    
    block.goto(xx , 100)
    bs = block.stamp()
    xx = xx - 50
zz = 400
for i in range(17):
    
    block.goto(zz , 50)
    bs = block.stamp()
    zz = zz - 50
block.hideturtle()

###eating the food
def eat_food():
    if basket.pos() in block_pos:
         block_ind = block_pos.index(basket.pos())
         block.clearstamp(block_stamps[block_ind])
         block_pos.pop(block_ind)
         block_stamps.pop(block_ind)
         print("You have eaten the food!")




#the ball \ basket
basket = turtle.clone()
basket.goto(plat.pos())
basket.shape("circle")
basket.color("Blue")
#while basket not in block_stamps:
#    basket.forward(8543)











###ball balance from walls














