#-----------------------------------------------------------------------------------
# STEP 1: Just an game loop drawing random rectanges
#-----------------------------------------------------------------------------------

import pygame, sys
import random

pygame.init()

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
FPS = 12
GREY = (29, 29, 29)


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Demo")

clock = pygame.time.Clock()

# Game Loop
while True:

    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                FPS += 2
            elif event.key == pygame.K_s:
                if FPS > 5:
                    FPS -= 2

    # 2. Draw 10 random rectangles
    window.fill(GREY)
    
    for _ in range(10):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.rect(window, color, (random.randint(0, WINDOW_WIDTH-200),
                                         random.randint(0, WINDOW_HEIGHT-200),
                                         random.randint(0, 200),
                                         random.randint(0, 200)))

    pygame.display.update()
    clock.tick(FPS)