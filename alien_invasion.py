import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """A class for managing resources and game behavior."""
    def __init__(self):
        """Initializes the game and creates game resourses."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        """Assigning a background color."""
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Starting the main game loop."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Tracking keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Each time the loop passes, the screen is redrawn."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        """Display the last drawn screen."""
        pygame.display.flip()

if __name__ == "__main__":
    """Create an instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()