import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SCREEN_WIDTH, 40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 20))

    def update(self):
        pass