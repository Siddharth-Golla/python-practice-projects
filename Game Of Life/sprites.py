import pygame
from settings import *

class Cell:
    """
    Cell class represents a single cell in the grid.
    """
    def __init__(self, x, y):
        """
        Initialize a cell at the given x and y coordinates.
        """
        self.x = x
        self.y = y
        self.alive = False


    def draw(self, screen):
        """
        Draw the cell on the given screen if it is alive.
        """
        if self.alive:
            pygame.draw.rect(screen, CELL_COLOR, (self.x, self.y, TILESIZE, TILESIZE))

    def is_clicked(self, mouse_x, mouse_y):
        return self.x <= mouse_x < (self.x + TILESIZE) and self.y <= mouse_y < (self.y + TILESIZE)

    def __str__(self):
        return f"({self.x},{self.y})"
    



class Grid:
    """
    Grid class represents the game grid.
    """
    def __init__(self):
        """
        Initialize the grid, cells list and add cell objects.
        """
        self.cells = []
        self.create_cells_list()
        
    
    def create_cells_list(self):
        """
        Create a list of cells for the grid.
        """
        for x in range(0, WIDTH, TILESIZE):
            cells_row = []
            for y in range(0, HEIGHT, TILESIZE):
                cells_row.append(Cell(x, y))
            self.cells.append(cells_row)


    def draw_grid(self, screen):
        """
        Draw the grid on the given screen.
        """

        # Draw the cells
        for row in self.cells:
            for cell in row:
                cell.draw(screen)


       # Draw vertical lines
        for row in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (0, row), (WIDTH, row))

       # Draw horizontal lines
        for col in range(0, WIDTH, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (col, 0), (col, HEIGHT))