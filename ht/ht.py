import sys
import pygame

from ht_settings import HtSettings
from picture import Picture

class BlueSky:
    def __init__(self):
        pygame.init()
        self.settings = HtSettings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue sky")
        self.picture = Picture(self)
        self.bg_color = self.settings.bg_color

    def run_app(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                self.screen.fill(self.bg_color)
                self.picture.blitme()
                pygame.display.flip()

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_app()