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

    def count_alive_neighbors(self, cell):
        """
        Counts the number of alive neighboring cells around a given cell.
        Args:
            cell (Cell): The cell for which to count alive neighbors.
        Returns:
            int: The number of alive neighboring cells.
        """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        alive_neighbors = 0
        for direction in directions:
            neighbor_x = cell.x + direction[0] * TILESIZE
            neighbor_y = cell.y + direction[1] * TILESIZE
            if 0 <= neighbor_x < WIDTH and 0 <= neighbor_y < HEIGHT:
                neighbor_cell = self.cells[neighbor_x // TILESIZE][neighbor_y // TILESIZE]
                if neighbor_cell.alive:
                    alive_neighbors += 1
        return alive_neighbors

    def update(self):
        """
        Update the state of the cells in the grid based on the rules of Conway's Game of Life.
        """
        # Create a new state grid initialized with the current state of each cell
        new_state = [[cell.alive for cell in row] for row in self.cells]

        # Iterate over each cell to determine its new state
        for row in self.cells:
            for cell in row:
                alive_neighbors = self.count_alive_neighbors(cell)
                if cell.alive:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_state[cell.x // TILESIZE][cell.y // TILESIZE] = False
                else:
                    if alive_neighbors == 3:
                        new_state[cell.x // TILESIZE][cell.y // TILESIZE] = True

        # Apply the new state to each cell
        for row in self.cells:
            for cell in row:
                cell.alive = new_state[cell.x // TILESIZE][cell.y // TILESIZE]

    def draw_grid(self, screen):
        """
        Draw the grid on the given screen.
        """
        # Draw the cells
        for row in self.cells:
            for cell in row:
                cell.draw(screen)

        # Draw horizontal lines
        for row in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (0, row), (WIDTH, row))

        # Draw vertical lines
        for col in range(0, WIDTH, TILESIZE):
            pygame.draw.line(screen, LIGHTGREY, (col, 0), (col, HEIGHT))

    def clear_grid(self):
        """
        Clear the grid by setting all cells to dead.
        """
        for row in self.cells:
            for cell in row:
                cell.alive = False
