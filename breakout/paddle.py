from turtle import Turtle

START_POSITION = (0, -250)

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.penup()
        self.setposition(START_POSITION)
        self.shapesize(0.5, 7.0, None)
        self.speed(10)

    
    def paddle_left(self):
        # post listen event to move paddle to the left
        if self.xcor() > -341:
            newx = self.xcor() - 20
            self.goto(newx, self.ycor())

    
    def paddle_right(self):
        # post listen event to move paddle to the right
        if self.xcor() < 340:
            newx = self.xcor() + 20
            self.goto(newx, self.ycor())
    