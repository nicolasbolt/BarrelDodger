import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(midbottom = (80, 580))
        self.gravity = 0
        self.jump_counter = 0

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 560:
            self.rect.bottom = 560

    def update(self):
        self.apply_gravity()
        self.player_input()

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump()

        if self.rect.bottom >= 560:
            self.jump_counter = 0

    def jump(self):
        if self.jump_counter < 2:
            self.gravity = -20
            self.jump_counter += 1
    