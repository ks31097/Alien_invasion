import pygame

class Ship():
    """A class for controlling a ship."""
    def __init__(self, ai):
        # Initializes the ship and its starting possition.
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.settings = ai.settings

        # Loads the ship image and gets a rectangle.
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()

        # Each new ship appears at the bottom edge of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Preservation of the real coordinate of the ship's center.
        self.x = float(self.rect.x)

        # Move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position based on the flag."""
        # The x attribute is updated, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect attribute based on self.x
        self.rect.x = self.x

    def blitme(self):
        """Draws a ship at the current position."""
        self.screen.blit(self.image, self.rect)