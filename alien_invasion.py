import sys
import pygame

class AlienInvasion:
    """A class for managing resources and game behavior."""
    def __init__(self):
        """Initializes the game and creates game resourses."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        """Assigning a background color."""
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starting the main game loop."""
        while True:
            """Tracking keyboard and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            """Each time the loop passes, the screen is redrawn."""
            self.screen.fill(self.bg_color)
            """Display the last drawn screen."""
            pygame.display.flip()

if __name__ == "__main__":
    """Create an instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()