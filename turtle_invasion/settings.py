class Settings:
    """Class to store settings for Alien Invasion"""

    def __init__(self):
        """Initialize the static settings for Alien Invasion"""
        self.screen_width = 800
        self.screen_height = 600 
        self.screen_dem = (self.screen_width, self.screen_height)
        self.bgcolor = 'black'
        self.title = 'Turtle Invasion'
        
        # ship settings
        self.ship_color = 'silver'
        self.ship_shape = 'triangle'
        self.ship_start_pos = (0, -270)
        self.max_bullets = 3


        # alien settings
        self.alien_color = 'green'
        self.alien_shape = 'turtle'
        self.fleet_speed = 1
        