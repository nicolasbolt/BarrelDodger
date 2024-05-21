import pygame
from random import randint

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Barrel(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 1:
            width = 40
            height = 20
        if type == 2:
            width = 80
            height = 20
        if type == 3:
            width = 80
            height = 45

        self.image = pygame.Surface((width, height))
        self.image.fill((255,0,255))
        self.rect = self.image.get_rect(midbottom = (SCREEN_WIDTH + randint(100, 400), SCREEN_HEIGHT - 40))

    def update(self):
        self.rect.x -= 10
        self.destroy

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

