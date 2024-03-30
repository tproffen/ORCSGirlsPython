#-----------------------------------------------------------------------------------
# STEP 2: Using the grod class
#-----------------------------------------------------------------------------------

from grid import Grid
import pygame, sys

pygame.init()

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 20
FPS = 12
GREY = (29, 29, 29)


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Demo")

grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
clock = pygame.time.Clock()

# Simulation Loop
while True:

    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            grid.toggle_cell(row, column)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                FPS += 2
            elif event.key == pygame.K_s:
                if FPS > 5:
                    FPS -= 2
            elif event.key == pygame.K_r:
                grid.fill_random()
            elif event.key == pygame.K_c:
                grid.clear()
            elif event.key == pygame.K_i:
                grid.fill_image('image.png')

    # 2. Draw 10 random rectangles
    window.fill(GREY)
    grid.draw(window)    
 
    pygame.display.update()
    clock.tick(FPS)