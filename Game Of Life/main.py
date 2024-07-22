import pygame
import time
from settings import *
from sprites import Grid

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()
        self.grid = Grid()
        self.playing = True
        self.running = False  # Add this attribute to track the running state
        self.generations = 0  # Add this attribute to track the number of generations
        self.last_update_time = time.time()  # Track the last update time

    def run(self):
        """
        Run the game. This is the main game loop.
        """
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        """
        Update the game state. This is where you would update the game logic.
        """
        current_time = time.time()
        if self.running and (current_time - self.last_update_time >= GENERATION_SPEED):  # Only update the grid if the game is running and the interval has passed
            self.grid.update()
            self.generations += 1  # Increment the generation counter
            self.last_update_time = current_time  # Update the last update time

    def draw(self):
        """
        Draw the game state. This is where you would render the game state to the screen.
        """
        self.screen.fill(BGCOLOR)
        self.grid.draw_grid(self.screen)
        pygame.display.flip()

    def events(self):
        """
        Handle game events. This is where you would handle user input and other events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for row in self.grid.cells:
                    for cell in row:
                        if cell.is_clicked(mouse_x, mouse_y):
                            cell.alive = not cell.alive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.running = not self.running  # Toggle the running state
                if event.key == pygame.K_c:
                    self.grid.clear_grid()  # Clear the grid when 'c' is pressed
                    self.generations = 0  # Reset the generation counter

if __name__ == "__main__":
    game = Game()
    game.run()
