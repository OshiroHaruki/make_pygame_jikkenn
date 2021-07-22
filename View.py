import pygame
from pygame.locals import *

DRAW_LITERAL = 64 #位置を画面サイズ/64で表しているので、描写の際には位置に64をかける必要がある.
class View:
    def __init__(self,screen):
        self.screen = screen
        self.sprites = {}
        self.sprites["player"] = pygame.image.load("./denchu.png")

        """GUIの仮制作用"""
        self.font1 = pygame.font.SysFont(None, 25)
        self.text_command_menu = self.font1.render("Command", False, (255,255,255))
        self.text_status = self.font1.render("Denchu", False, (255,255,255))
        """"""
    
    def getScreenSize(self):
        return self.screen.get_size()
    
    def draw(self, obj):#objは少なくとも、"画像名"と"位置"を持つ
        img = self.sprites[obj.visual]
        draw_pos = [obj.pos[0] * DRAW_LITERAL, obj.pos[1] * DRAW_LITERAL]
        self.screen.blit(img, draw_pos)
    
    def GUI_draw(self):
        pygame.draw.rect(self.screen,(255,255,255), (400,10,200,180))
        pygame.draw.rect(self.screen,(0,0,0), (405,15,190,170))
        pygame.draw.rect(self.screen,(255,255,255), (10,10,150,200))
        pygame.draw.rect(self.screen,(0,0,0), (15,15,140,190))
        self.screen.blit(self.text_command_menu,(460,16))
        self.screen.blit(self.text_status,(55,16))