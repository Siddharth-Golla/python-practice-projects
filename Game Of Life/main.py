import pygame
from settings import *
from sprites import *

#  Main Game Class Declaration
class Game:
    """
    Game class represents the main game loop and handles the game's logic.
    """
    def __init__(self) -> None:
        """
        Initialize the game. Set up the screen, clock, and grid.
        """

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.grid = Grid()

    def run(self):
        """
        Run the game. This is the main game loop.
        """
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        pass


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


# Game loop initializing
if __name__ == '__main__':
    """
    Main entry point for the game. Creates a Game object and starts the game loop.
    """
    game = Game()
    game.run()