import pygame
from pygame.locals import *
from map import Map

DRAW_LITERAL_32px = 32 #1マス32pixelなのでその定数

def set_text(font,text):
    return font.render(text,False,(255,255,255))

def draw_frame(screen,x_pos,y_pos,width,height):
    pygame.draw.rect(screen,(255,255,255),(x_pos,y_pos,width,height))
    pygame.draw.rect(screen,(0,0,0),(x_pos+5,y_pos+5,width-10,height-10))

def draw_text(screen,text,x_pos,y_pos):
    screen.blit(text,(x_pos,y_pos))

class View:
    def __init__(self,screen,map):
        self.screen = screen
        self.sprites = {}
        self.load_img = pygame.image.load("./denchu.png")
        self.load_img = pygame.transform.scale(self.load_img,(32,32))
        self.sprites["player"] = self.load_img #denchu.imgを格納

        """GUIの制作用"""
        self.font1 = pygame.font.SysFont(None, 25) #小さめフォント
        self.font2 = pygame.font.SysFont(None, 40) #大きめフォント
        """"""

        """Map用"""
        self.map = map
        self.map.imgs[0] = pygame.image.load("BrightForest-A2-010.png")
        self.map.imgs[1] = pygame.image.load("BrightForest-A2-001.png")
        self.map.imgs[2] = pygame.image.load("BrightForest-A2-003.png")
        """"""
    
    def get_screen_size(self):
        return self.screen.get_size()
    
    def draw_charactor(self, obj):
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
    
    def draw_menu(self):
        """
        メニューのGUIを描写する関数.GUIの枠組みを表示するだけ.
        ->関数で枠やテキストを表示するようにしているので、画面サイズが変更になっても数値をいじるだけで対応可能.
        ->コマンドを増やす時はdraw_text()にいろいろやれば文字を表示できる.
        """
        draw_frame(self.screen,400,10,200,180)
        draw_frame(self.screen,10,10,150,200)
        draw_text(self.screen,set_text(self.font1,"Command"),460,16)
        draw_text(self.screen,set_text(self.font1,"Denchu"),55,16)
        draw_text(self.screen,set_text(self.font1,"Search"),445,35)
        draw_text(self.screen,set_text(self.font1,"Use Buttery"),445,55)

    def draw_search_around(self, text1, text2="", text3="",text4=""):
        """
        「しらべる」実行時にそれを描写する関数.
        引数のtextと枠を描写する.
        textはとりあえず4行までなら設定できます(今後、画面サイズが変更になったらここらへんも変更になる可能性はあります)
        """
        draw_frame(self.screen,120,430,400,200)
        draw_text(self.screen,set_text(self.font2,text1),127,447)
        draw_text(self.screen,set_text(self.font2,text2),127,477)
        draw_text(self.screen,set_text(self.font2,text3),127,507)
        draw_text(self.screen,set_text(self.font2,text4),127,537)

    def draw_circle(self, _x, _y):
        pygame.draw.circle(self.screen,(255,255,255),(_x,_y), 8)