"""Sprites are how we manage objects in the game, if you put it in a Group() or GroupSingle() it makes drawing and updating them very easy"""

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Init Game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Example 2')

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT / 2))

    def update(self):
        # if we want to make it move, we can do that here, here we are adding to the x position to make it go to the right
        # uncomment this line and comment out the pass line
        # self.rect.x += 1
        pass


# We can add it to a GroupSingle if we only want to create one of these squares, or a Group if we want to create multiple
square = pygame.sprite.GroupSingle()
square.add(Square())


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

    # Since we added the sprite to a group we can just call draw() and update() to draw and update the sprite on every frame
    square.draw(screen)
    square.update()

    # Update the display
    pygame.display.flip()

pygame.quit()