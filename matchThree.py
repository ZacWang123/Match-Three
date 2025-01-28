import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame # type: ignore

row = 12
col = 12

def Create_Grid():
    global row, col
    print("row:" , row , "  col:" , col)

def main():
    Create_Grid()
    
if __name__ == "__main__":
    main()