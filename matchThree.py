import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame # type: ignore

running = False

windowLength = 800
windowWidth = 600

gridLengthStart = 200
gridLengthEnd = 600

gridWidthStart = 100
gridWidthEnd = 500

cellSize = 40
blockSize = 38

gameRow = 10
gameCol = 10

GREY = (65, 65, 65)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 127, 80)

COLOURS = [GREY, PURPLE, RED, GREEN, YELLOW, BLUE, ORANGE]

BACKGROUND_COLOUR = (173, 216, 230)
GRID_COLOUR = (100, 100, 100)
                
def Draw_Grid():
    screen = pygame.display.set_mode((windowLength, windowWidth))
    pygame.display.set_caption("Match-3 Game")
    screen.fill(BACKGROUND_COLOUR)

    for x in range(gridLengthStart, gridLengthEnd + cellSize, cellSize): 
        pygame.draw.line(screen, GRID_COLOUR, (x, gridWidthStart), (x, gridWidthEnd), 2)
        
    for y in range(gridWidthStart, gridWidthEnd + cellSize, cellSize): 
        pygame.draw.line(screen, GRID_COLOUR, (gridLengthStart, y), (gridLengthEnd, y), 2)

    return screen

def Update_Grid(screen, gameGrid):
    global gameRow, gameCol
    
    for col in range(gameCol):
        for row in range(gameRow):
            realX = gridLengthStart + col * cellSize
            realY = gridWidthStart + row * cellSize
            pygame.draw.rect(screen, COLOURS[gameGrid[col][row]], (realX + 2, realY + 2, blockSize, blockSize))

def Start_Game():
    global running, gameRow, gameCol
    gameGrid = [[0 for i in range(gameRow)] for j in range(gameCol)]
    clickedTiles = []
    
    screen = Draw_Grid()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                col = (mouseX - gridLengthStart) // cellSize
                row = (mouseY - gridWidthStart) // cellSize
                
                if row >= 0 and row < gameRow and col >= 0 and col < gameCol:
                    gameGrid[col][row] = 1
                    Update_Grid(screen, gameGrid)


        pygame.display.update()

def main():
    global running
    running = True

    Start_Game()
    
if __name__ == "__main__":
    main()