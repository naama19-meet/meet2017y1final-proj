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
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000



###the platform





###platform movements

LENGHT= 4
TIME_STEP = 100
pos_list=[]
stamp_list=[]
obj = turtle.clone()
obj.showturtle()
obj.shape("square")
obj.resizemode('user')
obj.shapesize(1,LENGHT,1)
platform_height = -SCREEN_HEIGHT/2 + 50
obj.goto(0, platform_height)
LEFT_ARROW = 'Left'
RIGHT_ARROW= 'Right'
LEFT_EDGE = -SCREEN_WIDTH/2
RIGHT_EDGE = SCREEN_WIDTH/2


LEFT=0
RIGHT=1
SPEED = 3
direction=LEFT

def left():
    global direction
    direction= LEFT
    if obj.pos()[0]-LENGHT/2*SQUARE_SIZE >= LEFT_EDGE:
        obj.goto(obj.pos()[0]-SPEED*SQUARE_SIZE,obj.pos()[1])
    print("you pressed the left key!")

def right():
    global direction
    direction= RIGHT
    if obj.pos()[0]+LENGHT/2*SQUARE_SIZE <= RIGHT_EDGE:
        obj.goto(obj.pos()[0]+SPEED*SQUARE_SIZE,obj.pos()[1])
    print("you pressed the right key!")

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()





###blocks

block = turtle.clone()
block.shape("square")
block.penup()
block.goto(450,250)
bs = block.stamp()
block.color("White")
block.pencolor("Blue")

gg = 400
for i in range(42):
    
    block.goto(gg , 250)
    bs = block.stamp()
    gg = gg - 20 
bb = 400
for i in range(42):
    block.goto(bb , 225)
    bs = block.stamp()
    bb = bb - 20    
ff = 400
for i in range(42):
    
    block.goto(ff , 200)
    bs = block.stamp()
    ff = ff - 20
xx = 400
for i in range(42):
    
    block.goto(xx , 175)
    bs = block.stamp()
    xx = xx - 20
zz = 400
for i in range(42):
    
    block.goto(zz , 150)
    bs = block.stamp()
    zz = zz - 20


YY = 400
for i in range(42):
    
    block.goto(zz , 125)
    bs = block.stamp()
    YY = YY - 20


LL = 400
for i in range(42):
    
    block.goto(zz , 100)
    bs = block.stamp()
    LL = LL - 20
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

def bounce(angle):
    new_angle = abs(90-angle)
    turtle.right(-2*new_angle)
    return(new_angle)
basket_pos = basket.pos()
basket_x = basket_pos[0]


if basket_x >= RIGHT_EDGE:
    bounce()

if basket_x >= LIFT_EDGE:
    bounce()

if basket_x >= UP_EDGE:
    bounce()

if basket_x >= DOWN_EDGE:
    quit()












