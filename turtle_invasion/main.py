from aliens import Alien
from bullet import Bullet
from settings import Settings 
from random import randint
from ship import Ship
from turtle import Screen, bgcolor, Turtle


class AlienInvasion: 
    """Main clase for game"""

    def __init__(self) -> None:
        """initialize alien invasion game"""

        self.settings = Settings()
        self.screen = Screen()
        self.screen.bgcolor(self.settings.bgcolor)
        self.screen.title('Alien Invasion')
        self.screen.setup(self.settings.screen_width, self.settings.screen_height)
        self.screen.tracer(0)



        # initialize ship
        self.ship = Ship(self)

        # list of objects
        self.alien_fleet = []
        self._bullets = []
        self._move_bullet = False 
            

        # Main loop window
        self.game_on = False 

        # Welcome message 
        self.text = Turtle()
        self.text.color('white')
        self.text.write('Press P to Begin')
        self._check_events()
        self.screen.mainloop()


    
    def start_game(self):
        """Listens for P press and then starts game"""
        self.game_on = True 
        self.text.clear()
        self.text.hideturtle()
        self.run_game()





    def run_game(self):
        """Runs the main game"""
        self._create_alien_fleet()

        while self.game_on:
            self._check_events()
            self.screen.update()


            if self._move_bullet == True:
                self._fire_bullet()

            self._check_bullet_collision()
            self._check_turtle_collision()
            self._check_turtle_ship_collission()


            if randint(0,8) == 1:
                self._move_fleet(self.settings.fleet_speed)


        self.screen.mainloop()



    def _check_events(self):
        """Respond to keypress events"""
        self.screen.listen()
        self.screen.onkeypress(self.ship.move_left, "Left")
        self.screen.onkeypress(self.ship.move_right, "Right")
        self.screen.onkeypress(self._create_bullet, "space")
        self.screen.onkey(self.start_game, "p")

    
    def _create_alien_fleet(self):
        """Creates An Alien Object and fleet"""
        _sub = 0

        for row in range(6):
        # Creates a row of turtles 
            for x  in range(0, 750, 30):
                self.alien = Alien(self)
                self.alien.goto(-360 + x, 280 - _sub)
                self.alien_fleet.append(self.alien)

            _sub += 30

    
    def _move_fleet(self, speed):
        """Moves fleet forward every few rounds"""

        for turt in self.alien_fleet:
            turt.forward(speed)


    def _create_bullet(self):
        # Function creates bullet objects 
        if len(self._bullets) < 4:
            bullet = Bullet(self)
            x, y = bullet.bullet_position()
            bullet.goto(x, y)
            bullet.showturtle()
            self._bullets.append(bullet)
            self._move_bullet = True


    def _fire_bullet(self):
        """Function moves bullets forward"""
        for b in self._bullets:
            if b.ycor() <    380:
                b.forward(10)
            else:
                b.hideturtle()
                self._bullets.remove(b)


    def _check_bullet_collision(self):
        """Function checks if bullet hit a turtle"""

        for turt in self.alien_fleet:
            for b in self._bullets:
                if turt.distance(b) < 15:
                    self.alien_fleet.remove(turt)
                    self._bullets.remove(b)
                    b.hideturtle()
                    turt.hideturtle()


    def _check_turtle_collision(self):
        """Function checks if turtle collides with wall"""

        for turt in self.alien_fleet:
            if turt.ycor() < -265:
                self.game_on = False 

    
    def _check_turtle_ship_collission(self):
        """Check if turtle hits ship"""

        for turt in self.alien_fleet:
            if turt.distance(self.ship) < 15:
                self.game_on = False 
        


        


if __name__ == "__main__":
    game = AlienInvasion()
