import pygame
from pygame.locals import *

DRAW_LITERAL = 64 #位置を画面サイズ/64で表しているので、描写の際には位置に64をかける必要がある.
class View:
    def __init__(self,screen):
        self.screen = screen
        self.sprites = {}
        self.sprites["player"] = pygame.image.load("./denchu.png")
    
    def getScreenSize(self):
        return self.screen.get_size()
    
    def draw(self, obj):#objは少なくとも、"画像名"と"位置"を持つ
        img = self.sprites[obj.visual]
        draw_pos = [obj.pos[0] * DRAW_LITERAL, obj.pos[1] * DRAW_LITERAL]
        self.screen.blit(img, draw_pos)