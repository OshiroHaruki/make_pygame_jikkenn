import pygame
from pygame.locals import *
import sys
from View import View
from Model import Model
from Controller import Controller
from map import Map

WINDOW_SIZE = (640,640)
WINDOW_TITLE = "RPG_tansaku"

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

        self.map = Map()
        self.view = View(self.screen,self.map)
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
                
                self.model.update()
            pygame.display.update()

if __name__ == "__main__":
    app = App()
    app.event_loop()