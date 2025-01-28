import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame # type: ignore

running = False

windowLength = 800
windowWidth = 600

row = 10
col = 10

PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 127, 80)

BACKGROUND_COLOUR = (173, 216, 230)
GRID_COLOUR = (100, 100, 100)
                
def Draw_Grid():
    gridLengthStart = 200
    gridLengthEnd = 600

    gridWidthStart = 100
    gridWidthEnd = 500
    
    blockSize = 40
    
    screen = pygame.display.set_mode((windowLength, windowWidth))
    pygame.display.set_caption("Match-3 Game")
    screen.fill(BACKGROUND_COLOUR)
    pygame.draw.rect(screen, GREEN, (240, 140, blockSize, blockSize))

    for x in range(gridLengthStart, gridLengthEnd + blockSize, blockSize): 
        pygame.draw.line(screen, GRID_COLOUR, (x, gridWidthStart), (x, gridWidthEnd), 2)
        
    for y in range(gridWidthStart, gridWidthEnd + blockSize, blockSize): 
        pygame.draw.line(screen, GRID_COLOUR, (gridLengthStart, y), (gridLengthEnd, y), 2)

    return screen

def Start_Game():
    global running, row, col
    
    screen = Draw_Grid()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.update()

def main():
    global running
    running = True

    Start_Game()
    
if __name__ == "__main__":
    main()