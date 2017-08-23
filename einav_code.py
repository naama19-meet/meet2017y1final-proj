import turtle
import random

turtle.tracer(1,0)

SIZE_X=1000
SIZE_Y=600
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup
SQUARE_SIZE=22
START_LENGTH=6
turtle.color("#red")
turtle.bgcolor("#yellow")

#initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
turtle.penup()
snake = turtle.clone()
snake.shape("square")

#upload the photos (blocks and basket)
turtle.register_shape("block.gif")
turtle.register_shape("block1.gif")
turtle.register_shape("block2.gif")
turtle.register_shape("block3.gif")
turtle.register_shape("basket.gif")

food= turtle.clone()


turtle.hideturtle()
