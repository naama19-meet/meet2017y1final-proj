import turtle

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
SQUARE_SIZE = 20
LENGHT= 10
TIME_STEP = 100

plat= turtle.clone()
plat.shape("square")
plat.color("black")
plat.penup()
plat.goto(0,-250)
turtle.hideturtle()
pos_list=[]
stamp_list=[]

for i in range(LENGHT):
    X_POS= plat.pos()[0]
    Y_POS= plat.pos()[1]
    X_POS+= SQUARE_SIZE
    my_pos= (X_POS,Y_POS)
    plat.goto(X_POS,Y_POS)
    pos_list.append(my_pos)
    stamp_ID=plat.stamp()
    stamp_list.append(stamp_ID)
    
LEFT_ARROW = 'Left'
RIGHT_ARROW= 'Right'



LEFT=0
RIGHT=1

direction=LEFT

def left():
    global direction
    direction= LEFT
    print("you pressed the left key!")

def right():
    global direction
    direction= RIGHT
    print("you pressed the right key!")

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def move_plat():
    global direction
    my_pos=plat.pos()
    X_POS= my_pos[0]
    Y_POS= my_pos[1]

    if direction==LEFT:
        plat.goto(X_POS - SQUARE_SIZE, Y_POS)
        print("you moved left!")

    elif direction==RIGHT:
        plat.goto(X_POS + SQUARE_SIZE, Y_POS)
        print("you moved right!") 

    turtle.ontimer(move_plat,TIME_STEP)
    
move_plat()
    
    
    
    

