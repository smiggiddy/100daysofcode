from turtle import Turtle
from time import sleep
import turtle

class Bullet(Turtle):
    """Class to manage bullets"""

    def __init__(self, ai_game):
        super().__init__()

        self.ai_game = ai_game
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=.2, stretch_len=.9)
        self.left(90)
        self.hideturtle()
        self.penup()


    def bullet_position(self):
        # gives bullet start position 
        x, y = self.ai_game.ship.pos()
        return x, y        





  




        