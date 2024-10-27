class Settings:
    """Class for storing all settings of the Alien Invasion game."""

    def __init__(self):
        """Initializes game settings."""
        # Screen optins
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 1.5