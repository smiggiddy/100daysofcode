from turtle import Turtle

class Alien(Turtle):
    """Class to manage alien objects"""

    def __init__(self, ai_game):
        super().__init__()

        self.settings = ai_game.settings 

        self.shape(self.settings.alien_shape)
        self.color(self.settings.alien_color)
        self.penup()
        self.left(-90)
        self.goto(-360, 280)


    def _create_fleet(self):
        pass 