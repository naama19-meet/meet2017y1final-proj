
import turtle
import time
turtle.tracer(1,0)

##turtle
turtle.penup()
#turtle.hideturtle()
block_pos = []
block_stamps = []

# the screen
size_x = 1400
size_y = 1000
turtle.setup(size_x , size_y)
turtle.bgcolor("White")
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 910
SQUARE_SIZE = 20
LENGHT= 6
TIME_STEP = 25

UP_EDGE = 270
RIGHT_EDGE = 470
LEFT_EDGE = -470
DOWN_EDGE = -270

edge1=turtle.clone()
edge1.color("Red")
edge1.penup()
##edge1.goto(RIGHT_EDGE,UP_EDGE)
##edge1.pendown()
##edge1.goto(LEFT_EDGE,UP_EDGE)
##edge1.goto(LEFT_EDGE,DOWN_EDGE)
##edge1.goto(RIGHT_EDGE,DOWN_EDGE)
##edge1.goto(RIGHT_EDGE,UP_EDGE)
edge1.goto(470,290)
edge1.pendown()
edge1.goto(-470,290)
edge1.goto(-470,-290)
edge1.goto(470,-290)
edge1.goto(470,290)
turtle.penup()
edge1.hideturtle()
turtle.tracer(1,0)
###the platform





###platform movements
turtle.hideturtle()
turtle.penup()
pos_list=[]
stamp_list=[]

obj = turtle.clone()

obj.showturtle()
obj.shape("square")
obj.resizemode('user')
obj.shapesize(1,LENGHT,1)
platform_height = -SCREEN_HEIGHT/2 + 50
obj.goto(0, platform_height)
obj.color("Black")
    
LEFT_ARROW = 'Left'
RIGHT_ARROW= 'Right'
LEFT_EDGE = -SCREEN_WIDTH/2
RIGHT_EDGE = SCREEN_WIDTH/2


LEFT=0
RIGHT=1
SPEED = 3
direction = LEFT

def left():
    global direction
    direction = LEFT
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
turtle.register_shape("apple (1).gif")
turtle.register_shape("carbs.gif")
turtle.register_shape("meat.gif")
turtle.register_shape("yellowpepel (1).gif")
#shapes = turtle.random("yellowpepel (1).gif" , "meat.gif" , "carbs.gif" , "apple (1).gif")
block.shape("apple (1).gif")
block.penup()

##block.shape("square")
##block.color("White")
##block.pencolor("Blue")


square_size = 20

# make the right turtle object
block_stamper = turtle.clone()
turtle.hideturtle()
block_stamper.shape("apple (1).gif")
block_stamper.penup()
block_stamper.goto(-470, 200)

# lists to keep track of positions and stamps
block_pos = []
block_stamps = []

# loop variables
start_x = -470
end_x = 400
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



    

block.hideturtle()



#the ball \ basket
basket = turtle.clone()
basket.showturtle()
basket.goto(0,-200)
turtle.register_shape("basket (1).gif")
basket.shape("basket (1).gif")

angle = 120

def bounce(angle):
    new_angle = 90-angle
    basket.right(-2*new_angle)
    return(new_angle)

bas_speed = 10
 
basket.left(angle)
def distance(basket_pos,square_pos):
        basket_x,basket_y = basket_pos
        square_x,square_y = square_pos
        d = ((basket_x-square_x)**2 + (basket_y-square_y)**2)**(1/2)
        return d
score = 0
def move_basket():
    global angle , obj_pos , score , bas_speed
    basket.forward(bas_speed)
    

    basket_pos = basket.pos()
    basket_x = basket_pos[0]
    basket_y = basket_pos[-1]
    
    for i in block_pos:
         d = distance(basket.pos(),i)
         if d < 20:
             #print("ddd")
             block_index = block_pos.index(i)
             block_stamper.clearstamp(block_stamps[block_index])
             block_pos.pop(block_index)
             block_stamps.pop(block_index)
             
             angle = bounce(angle)
             score = score +1
             turtle.goto(360,250)
             turtle.color("Red")
             turtle.clear()
             turtle.write("score: " + str(score) , font=("Arial",20, "normal"))
             bas_speed = bas_speed + 0.2

      

    # Hitting the platform
    obj_x= obj.pos()[0]
    obj_y= obj.pos()[1]
    v1= (obj_x + LENGHT/2*SQUARE_SIZE, obj_y)
    v2= (obj_x - LENGHT/2*SQUARE_SIZE, obj_y)
    v3= (obj_x, obj_y + SQUARE_SIZE)
    v4= (obj_x, obj_y - SQUARE_SIZE)

    RIGHT_edge= obj_x + LENGHT/2*SQUARE_SIZE
    LEFT_edge= obj_x - LENGHT/2*SQUARE_SIZE
    UPPER_edge= obj_y + SQUARE_SIZE
    LOWER_edge= obj_y - SQUARE_SIZE
    basket_x= basket.pos()[0]
    basket_y= basket.pos()[1]
    if basket_x <= RIGHT_edge and basket_x >= LEFT_edge and basket_y <= UPPER_edge and basket_y >= LOWER_edge:
        angle = bounce(angle)
    
    if basket_x >= RIGHT_EDGE:
        #basket.goto(RIGHT_EDGE,basket_y)
        angle = bounce(angle)
        #print('hello')
    
    if basket_x <= LEFT_EDGE:
        #basket.goto(LEFT_EDGE,basket_y)
        angle = bounce(angle)

    if basket_y >= UP_EDGE:
        #basket.goto(basket_x,UP_EDGE)
        angle = bounce(angle)

    if obj.pos() == basket_y and basket_x:
        angle = bounce(angle)

    if basket_y <= DOWN_EDGE:
        turtle.goto(-280,-100)
        turtle.color("red")
        turtle.write("GAME OVER!" , font = ("Ariel" , 77 , "normal"))
        time.sleep(2)
        quit()
    
    # check if the basket hit any blocks
    if basket.pos() in block_pos:
        angle = bounce(angle)
        
                
    turtle.ontimer(move_basket,TIME_STEP)

        #score
move_basket()




###eating the food
##obj_x= obj.pos()[0]
##obj_y= obj.pos()[1]
##v1= (obj_x + LENGHT/2*SQUARE_SIZE, obj_y)
##v2= (obj_x - LENGHT/2*SQUARE_SIZE, obj_y)
##v3= (obj_x, obj_y + SQUARE_SIZE)
##v4= (obj_x, obj_y - SQUARE_SIZE)
##
##RIGHT_edge= obj_x + LENGHT/2*SQUARE_SIZE
##LEFT_edge= obj_x - LENGHT/2*SQUARE_SIZE
##UPPER_edge= obj_y + SQUARE_SIZE
##LOWER_edge= obj_y - SQUARE_SIZE

##basket_x= basket.pos()[0]
##basket_y= basket.pos()[1]

##if basket_x <= RIGHT_edge and basket_x >= LEFT_edge and basket_y <= UPPER_edge and basket_y >= LOWER_edge:
##    angle = bounce(angle)
    
#    angle = bounce(angle)
