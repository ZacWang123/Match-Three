import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame # type: ignore

running = False

windowLength = 800
windowWidth = 600

gridLengthStart = 200
gridLengthEnd = 600
gridLengthInterval = 40

gridWidthStart = 100
gridWidthEnd = 500
gridWidthInterval = 40


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
                
def Draw_Grid(screen):
    screen.fill(BACKGROUND_COLOUR)
    pygame.draw.rect(screen, GREEN, (240, 140, gridLengthInterval, gridWidthInterval))

    for x in range(gridLengthStart, gridLengthEnd + gridLengthInterval, gridLengthInterval): 
        pygame.draw.line(screen, GRID_COLOUR, (x, gridWidthStart), (x, gridWidthEnd), 2)
        
    for y in range(gridWidthStart, gridWidthEnd + gridWidthInterval, gridWidthInterval): 
        pygame.draw.line(screen, GRID_COLOUR, (gridLengthStart, y), (gridLengthEnd, y), 2)

def Start_Game():
    global running
    
    screen = pygame.display.set_mode((windowLength, windowWidth))
    pygame.display.set_caption("Match-3 Game")
    Draw_Grid(screen)

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