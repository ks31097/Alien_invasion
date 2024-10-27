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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # Assigning a background color.
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Starting the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Tracking keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reacts to keystrokes"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Reacts to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Each time the loop passes, the screen is redrawn."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Display the last drawn screen.
        pygame.display.flip()

if __name__ == "__main__":
    """Create an instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()