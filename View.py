import pygame
from pygame.locals import *
from map import Map

DRAW_LITERAL = 64 #位置を画面サイズ/64で表しているので、描写の際には位置に64をかける必要がある.
                  #32か64かは要相談？
                  #したの32pxのほうで開発した方が良さそうだから、一旦そっちで開発する.
DRAW_LITERAL_32px = 32 #mapに合わせた方が後々良さそう
class View:
    def __init__(self,screen):
        self.screen = screen
        self.sprites = {}
        self.load_img = pygame.image.load("./denchu.png")
        #self.sprites["player"] = pygame.image.load("./denchu.png")
        self.load_img = pygame.transform.scale(self.load_img,(32,32))
        self.sprites["player"] = self.load_img #denchu.imgを格納

        """GUIの仮制作用"""
        self.font1 = pygame.font.SysFont(None, 25)
        self.text_command_menu = self.font1.render("Command", False, (255,255,255))
        self.text_status = self.font1.render("Denchu", False, (255,255,255))
        """"""

        """Map用"""
        self.map = Map()
        self.map.imgs[0] = pygame.image.load("BrightForest-A2-010.png")
        self.map.imgs[1] = pygame.image.load("BrightForest-A2-001.png")
        self.map.imgs[2] = pygame.image.load("BrightForest-A2-003.png")
        """"""
    
    def getScreenSize(self):
        return self.screen.get_size()
    
    def draw(self, obj):#objはキャラクタ. objは少なくとも、"画像名(visual)"と"位置(pos)"を持つ
        img = self.sprites[obj.visual]
        draw_pos = [obj.pos[0] * DRAW_LITERAL_32px, obj.pos[1] * DRAW_LITERAL_32px]
        self.screen.blit(img, draw_pos)

    def draw_map(self):
        self.map.draw(self.screen)
    
    def GUI_draw(self):
        pygame.draw.rect(self.screen,(255,255,255), (400,10,200,180))
        pygame.draw.rect(self.screen,(0,0,0), (405,15,190,170))
        pygame.draw.rect(self.screen,(255,255,255), (10,10,150,200))
        pygame.draw.rect(self.screen,(0,0,0), (15,15,140,190))
        self.screen.blit(self.text_command_menu,(460,16))
        self.screen.blit(self.text_status,(55,16))