import sys,pygame
from settings import *
from level import Level

class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.time = pygame.time.Clock()
        self.lvl = Level()
        self.pause = False
        
    def run(self):
        while True:
            self.pause = self.lvl.pause
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.pause == False:
                self.screen.fill('black')
                self.lvl.run()
                pygame.display.update()
                self.time.tick(FPS)

                