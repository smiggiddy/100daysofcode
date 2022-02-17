from turtle import Screen
from ball import Ball
from paddle import Paddle
from blocks import Blocks
from time import sleep

def start_game():
    print('game started')
    game_started = True
    game()


# initialize turtle window
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Smiggiddy Out')
screen.tracer(0)

# initialize imports and game components
ball = Ball()
paddle = Paddle()
blocks = Blocks()

game_started = False 


# Setup listening event for left and right
screen.listen()
screen.onkeypress(paddle.paddle_left, "Left")
screen.onkeypress(paddle.paddle_right, "Right")
screen.onkeypress(start_game, "p")


# create blocks for 4 rows 
blocks.create_row()

# print blocks on the screen
StartX, StartY = -380, 200


for blockgroup in blocks.block_groups:
    for block in blockgroup:
        block.goto(StartX, StartY)
        StartX += 30
        
    StartY -= 15
    StartX = -380

def game():

    while True:
        screen.update()
        ball.move()

        

        # keep ball in game boundaries
        if ball.ycor() > 295:
            ball.bounce_y()
        elif ball.xcor() > 395 or ball.xcor() < -395:
            ball.bounce_x()
        elif ball.ycor() < -305:
            sleep(1)
            ball.reset_position()

        # detect collisions with player paddle
        if ball.distance(paddle) < 25 and ball.ycor() > -275:
            ball.bounce_y()

        # detect block collisions
        for block in blocks.blocks:
            if block.distance(ball) < 20:
                block.hideturtle()
                blocks.blocks.remove(block)
                ball.bounce_y()
        
        # sleep(0.05)


screen.exitonclick()