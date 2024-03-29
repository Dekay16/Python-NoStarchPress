class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ships settings
        self.ship_speed = 1.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.4
        self.fleet_drop_speed = 10
        self.fleet_direction = 1