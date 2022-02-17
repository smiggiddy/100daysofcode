from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("gray")
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.x_move = 2
        self.y_move = 2

    def move(self):
        """Makes the ball move diag to the right"""
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        self.goto(newx, newy)

    
    def bounce_y(self):
        """Makes the ball go in the opposite direction"""
        self.y_move *= -1
    
    def bounce_x(self):
        """Makes ball bounce with paddle colission"""
        self.x_move *= -1 

    def reset_position(self):
        self.goto(0, -220)
        self.bounce_y()   