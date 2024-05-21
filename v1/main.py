import pygame
from random import choice, randint

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from Player import Player
from Platform import Platform
from Barrel import Barrel

# Init Game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Barrel Dodger')
game_active = False

# Intro Text
font = pygame.font.SysFont('urwbookman', 30)
intro_text_surface =  font.render('Press SPACE to start', False, (255, 255, 255))

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

platform = pygame.sprite.GroupSingle()
platform.add(Platform())

barrel_group = pygame.sprite.Group()

# Set up barrel timer to create new barrels every 800 - 1200 ms
barrel_timer = pygame.USEREVENT + 1
pygame.time.set_timer(barrel_timer, randint(800, 1200))

# function to check for sprite collisons and stop the game if it finds one
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, barrel_group, False):
        barrel_group.empty()
        return False
    else:
        return True

running = True
while running:
    # Set the game to run at 60 frames per second
    clock.tick(FPS)

    # This for loop checks for events, we can check for any key press we want here or any custom event types (our barrel timer)
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == pygame.K_ESCAPE:
                running = False
            # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == pygame.QUIT:
                running = False
        
        if game_active:
            # Whenever the barrel timer goes off, we can use this to handle creating a new barrel
            if event.type == barrel_timer:
                barrel_group.add(Barrel(choice([1, 2, 3])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
        

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Two game states, one for playing the game and one for showing the intro screen
    if game_active:
        player.draw(screen)
        player.update()

        platform.draw(screen)
        platform.update()

        barrel_group.draw(screen)
        barrel_group.update()

        game_active = collision_sprite()
    else:
        # screen.blit() is a way to draw to the screen
        screen.blit(intro_text_surface, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2))
        player.draw(screen)
        platform.draw(screen)
        player.update()

    # Update the display
    pygame.display.flip()

pygame.quit()