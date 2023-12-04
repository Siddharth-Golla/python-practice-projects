import pygame
from settings import *
from sprites import *

#  Main Game Class Declaration
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        pass

    def draw_grid(self):
        for row in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, row), (WIDTH, row))

        for col in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (col, 0), (col, HEIGHT))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        pygame.display.flip()


    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)


# Game loop initializing
if __name__ == '__main__':
    game = Game()
    game.run()