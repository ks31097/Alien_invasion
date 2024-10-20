import pygame

class Ship():
    """A class for controlling a ship."""
    def __init__(self, ai):
        """Initializes the ship and its starting possition."""
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        """Loads the ship image and gets a rectangle."""
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        """Each new ship appears at the bottom edge of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draws a ship at the current position."""
        self.screen.blit(self.image, self.rect)