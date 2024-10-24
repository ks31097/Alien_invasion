import pygame

class Picture:
    def __init__(self, ht):
        self.screen = ht.screen
        self.screen_rect = ht.screen.get_rect()

        self.image = pygame.image.load('/home/kostiantyn/Alien_invasion/ht/picture/out1.PNG')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)