"""We can listen for user input to move a sprite as well"""

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Init Game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Example 3')

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT / 2))

    def update(self):
        # we add the move function here to check for key press on each frame and update the position if there one of the keys are pressed
        self.move()

    def move(self):
        # get_pressed() returns a dictionary of pressed keys, we can check that dictionary for the keys we want
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1


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

    # draw and update sprite group
    square.draw(screen)
    square.update()

    # Update the display
    pygame.display.flip()

pygame.quit()