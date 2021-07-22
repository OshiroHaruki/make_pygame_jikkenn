import pygame
from pygame.locals import *
import sys
from Model import Model
class Controller:
    def __init__(self,model):
        self.model = model
    def keyDown(self,key):
        if self.model.isOpenedGUI == False:
            if key == K_RIGHT:
                self.model.move([1,0])
            elif key == K_LEFT:
                self.model.move([-1,0])
            elif key == K_UP:
                self.model.move([0,-1])
            elif key == K_DOWN:
                self.model.move([0,1])
            elif key == K_z:
                self.model.search()
            elif key == K_e:
                self.model.openGUI()
        else:
            if key == K_e:
                self.model.closeGUI()