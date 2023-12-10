import pygame
from settings import *

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False


    # Draw the cell if it is alive
    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, WHITE, (self.x, self.y, TILESIZE, TILESIZE))


    def __str__(self):
        return f"({self.x},{self.y})"
    



class Grid:
    def __init__(self):
        self.cells = []
        self.create_cells_list()
        
    
    def create_cells_list(self):
        for x in range(0, WIDTH, TILESIZE):
            cells_row = []
            for y in range(0, HEIGHT, TILESIZE):
                cells_row.append(Cell(x, y))
            self.cells.append(cells_row)


    def draw_grid(self, screen):
        for row in self.cells:
            for cell in row:
                cell.draw(screen)


        for row in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (0, row), (WIDTH, row))

        for col in range(0, WIDTH, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (col, 0), (col, HEIGHT))