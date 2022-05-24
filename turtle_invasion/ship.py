from turtle import Turtle 

class Ship(Turtle):
    """Class for user controlled ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings 

        self.shape(self.settings.ship_shape)
        self.color(self.settings.ship_color)
        self.penup() 
        self.goto(self.settings.ship_start_pos)
        self.tilt(90)


    def move_left(self):
        """Moves ship to left"""

        if self.xcor() > -360:
            newx = self.xcor() - 30
            self.goto(newx, self.ycor())


    def move_right(self):
        """Moves ship to the right"""

        if self.xcor() < 360:
            newx = self.xcor() + 30 
            self.goto(newx, self.ycor())






