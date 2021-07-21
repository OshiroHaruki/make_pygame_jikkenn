import pygame
from pygame.locals import *
import sys
from View import View
from Model import Model
from Controller import Controller

WINDOW_SIZE_HEIGHT = 640
WINDOW_SIZE_WIDTH = 640
WINDOW_TITLE = "RPG_tansaku"

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE_WIDTH,WINDOW_SIZE_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.view = View(self.screen)
        self.model = Model(self.view)
        self.controller = Controller(self.model)

        self.isTansaku = True
    def event_loop(self):
        while True:
            if self.isTansaku:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        self.controller.keyDown(event.key)
                self.screen.fill((0,255,0))
                self.model.update()
            pygame.display.update()

if __name__ == "__main__":
    app = App()
    app.event_loop()