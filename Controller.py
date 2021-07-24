import pygame
from pygame.locals import *
import sys
from Model import Model
class Controller:
    def __init__(self,model):
        self.model = model
    def keyDown(self,key):
        if self.model.isOpenedGUI == False:# メニューGUIが開いていない時
            if self.model.isOpenedMessage == False:# メッセージが開いている時
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
            else: #メッセージが開いている時
                if key == K_z:
                    self.model.closeMessage()
        else: # GUIが開いているとき
            if key == K_e:
                self.model.closeGUI()