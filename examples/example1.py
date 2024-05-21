"""This is a basic example that just loads a black screen, the escape key or the window X button closes the game"""

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Init Game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Example 1')

running = True
while running:

    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == pygame.K_ESCAPE:
                running = False
            # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == pygame.QUIT:
                running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()