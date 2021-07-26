import pygame
from pygame.locals import *
import sys
from Model import Model
class Controller:
    def __init__(self,model):
        self.model = model
    def keyDown(self,key):
        if self.model.is_opened_GUI == False:# メニューGUIが開いていない時
            if key == K_RIGHT:
                self.model.move([1,0])
            elif key == K_LEFT:
                self.model.move([-1,0])
            elif key == K_UP:
                self.model.move([0,-1])
            elif key == K_DOWN:
                self.model.move([0,1])
            elif key == K_e:
                self.model.open_GUI()
        else: # GUIが開いているとき
            if self.model.is_opened_message == False:# メッセージが開いている時
                if key == K_e:
                    self.model.close_GUI()
                elif key == K_DOWN:
                    self.model.select_move_under()
                elif key == K_UP:
                    self.model.select_move_up()
                elif key == K_z:
                    self.model.select_command()
            else: #メッセージが開いている時
                if key == K_z:
                    self.model.close_Message()