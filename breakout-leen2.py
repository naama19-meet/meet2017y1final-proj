import turtle
import time
turtle.tracer(1,0)

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
SQUARE_SIZE = 20
LENGHT= 6
TIME_STEP = 100

##plat= turtle.clone()
##plat.shape("square")
##plat.color("black")
##plat.penup()
##plat.goto(0,-250)
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

##clones_list = [obj]


##for n in range(LENGHT):
##    last_pos = clones_list[-1].pos()
##    last_x = last_pos[0]
##    new_x = last_x + SQUARE_SIZE
##    obj = turtle.clone()
##    obj.showturtle()
##    obj.shape("square")
##    obj.goto(new_x, last_pos[1])
##    clones_list.append(obj)
    
    

##for i in range(LENGHT):
##    X_POS= plat.pos()[0]
##    Y_POS= plat.pos()[1]
##    X_POS+= SQUARE_SIZE
##    my_pos= (X_POS,Y_POS)
##    plat.goto(X_POS,Y_POS)
##    pos_list.append(my_pos)
##    stamp_ID=plat.stamp()
##    stamp_list.append(stamp_ID)
    
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

# Collision is going to be detected when:
# - y_pos == platform_height+SQUARE_SIZE/2
# - x_pos >= obj.pos()[0] - LENGHT/2*SQUARE_SIZE
# - x_pos <= obj.pos()[0] + LENGHT/2*SQUARE_SIZE


##def move_plat():
##    global clones_list
##    amount = 1
##    if direction==LEFT:
##        print(clones_list)
##        back = clones_list[-1]
##        front = clones_list[0]
##        new_pos = front.pos()
##        back.goto(new_pos[0]-(amount*SQUARE_SIZE),new_pos[1])
##        clones_list = [back] + clones_list[0:-1]
####        for obj in clones_list:
####            old_pos = obj.pos()
####            obj.goto(old_pos[0] - (amount*SQUARE_SIZE), old_pos[1])
##        print("you moved left!")
##        #time.sleep(.1)

##    elif direction==RIGHT:
##        for obj in clones_list:
##            print(obj.pos())
##            old_pos = obj.pos()
##            obj.goto(old_pos[0] + (amount*SQUARE_SIZE), old_pos[1])
##            print(obj.pos())
##        print("you moved right!")
##        #time.sleep(0.1)
    
##    global direction
##    my_pos=plat.pos()
##    X_POS= my_pos[0]
##    Y_POS= my_pos[1]
##
##    if direction==LEFT:
##        left_pos = pos_list[0]
##        plat.goto(left_pos[0] - SQUARE_SIZE, left_pos[1])
##        
##        print("you moved left!")
##
##    elif direction==RIGHT:
##        right_pos = pos_list[-1]
##        plat.goto(right_pos[0] + SQUARE_SIZE, right_pos[1])
##        print("you moved right!")
##
##    # stamp the head
##    head_stamp = plat.stamp()
##    stamp_list.append(head_stamp)
##    pos_list.append(plat.pos())
##
##    # pop the tail
##    stamp_id = stamp_list.pop(0)
##    plat.clearstamp(stamp_id)
##    pos_list.pop(0)
    


##    turtle.ontimer(move_plat,TIME_STEP)
    
    
    

