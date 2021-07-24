import pygame
from pygame.locals import *
from map import Map

DRAW_LITERAL = 64 #位置を画面サイズ/64で表しているので、描写の際には位置に64をかける必要がある.
                  #32か64かは要相談？
                  #したの32pxのほうで開発した方が良さそうだから、一旦そっちで開発する.
DRAW_LITERAL_32px = 32 #mapに合わせた方が後々良さそう

def set_text(font,text):
    return font.render(text,False,(255,255,255))

class View:
    def __init__(self,screen):
        self.screen = screen
        self.sprites = {}
        self.load_img = pygame.image.load("./denchu.png")
        #self.sprites["player"] = pygame.image.load("./denchu.png")
        self.load_img = pygame.transform.scale(self.load_img,(32,32))
        self.sprites["player"] = self.load_img #denchu.imgを格納

        """GUIの制作用"""
        self.font1 = pygame.font.SysFont(None, 25)
        self.font2 = pygame.font.SysFont(None, 40)
        self.text_command_menu = self.font1.render("Command", False, (255,255,255))
        self.text_status = self.font1.render("Denchu", False, (255,255,255))
        self.text_commands = []
        self.text_commands.append(set_text(self.font1, "Search"))
        self.text_commands.append(set_text(self.font1, "Use Buttery"))
        """"""

        """Map用"""
        self.map = Map()
        self.map.imgs[0] = pygame.image.load("BrightForest-A2-010.png")
        self.map.imgs[1] = pygame.image.load("BrightForest-A2-001.png")
        self.map.imgs[2] = pygame.image.load("BrightForest-A2-003.png")
        """"""
    
    def getScreenSize(self):
        return self.screen.get_size()
    
    def draw(self, obj):
        """
        キャラクターを描写する関数.
        objはキャラクタ. objは少なくとも、"画像名(visual)"と"位置(pos)"を持つ
        """
        img = self.sprites[obj.visual]
        draw_pos = [obj.pos[0] * DRAW_LITERAL_32px, obj.pos[1] * DRAW_LITERAL_32px]
        self.screen.blit(img, draw_pos)

    def draw_map(self):
        """
        mapを描写する関数
        """
        self.map.draw(self.screen)
    
    def GUI_draw(self):
        """
        メニューのGUIを描写する関数.GUIの枠組みを表示するだけ.
        """
        pygame.draw.rect(self.screen,(255,255,255), (400,10,200,180))
        pygame.draw.rect(self.screen,(0,0,0), (405,15,190,170))
        pygame.draw.rect(self.screen,(255,255,255), (10,10,150,200))
        pygame.draw.rect(self.screen,(0,0,0), (15,15,140,190))
        self.screen.blit(self.text_command_menu,(460,16))
        self.screen.blit(self.text_status,(55,16))
        self.screen.blit(self.text_commands[0], (445,35))
        self.screen.blit(self.text_commands[1], (445,55))

    def draw_search_around(self, text):
        """
        「しらべる」実行時にそれを描写する関数.
        引数のtextと枠を描写する.
        textは1行しか入力できない
        """
        message = self.font2.render(text, False, (255,255,255))
        pygame.draw.rect(self.screen, (255,255,255),(120,430,400,200))
        pygame.draw.rect(self.screen, (0,0,0),(125,435,390,190))
        self.screen.blit(message,(127,437))

    def draw_circle(self, _x, _y):
        pygame.draw.circle(self.screen,(255,255,255),(_x,_y), 8)