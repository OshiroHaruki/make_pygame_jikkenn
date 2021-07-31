import pygame
from pygame.locals import *
from map import Map

DRAW_LITERAL_32px = 32 #1マス32pixelなのでその定数

def load_img(filename,colorkey=None):
    img = pygame.image.load(filename)
    img = img.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = img.get_at((0,0))
        img.set_colorkey(colorkey, RLEACCEL)
    return img

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
        """使わない
        self.map.imgs[0] = pygame.image.load("BrightForest-A2-010.png")
        self.map.imgs[1] = pygame.image.load("BrightForest-A2-001.png")
        self.map.imgs[2] = pygame.image.load("BrightForest-A2-003.png")
        """
        Map.imgs[0] = load_img("WorldMap-A1-011.png")         #海
        Map.imgs[1] = load_img("WorldMap-A1-018.png")         #湖
        Map.imgs[2] = load_img("WorldMap-A2-018.png")         #雪道
        Map.imgs[3] = load_img("BrightForest-A2-001.png")       #森道
        Map.imgs[4] = load_img("WorldMap-A2-020.png")       #岩道
        Map.imgs[5] = load_img("WorldMap-A2-013.png")       #森
        Map.imgs[6] = load_img("WorldMap-A2-024.png")       #岩山
        Map.imgs[7] = load_img("WorldMap-A2-030.png")       #雪山
        Map.imgs[8] = load_img("WorldMap-A2-022.png")       #森山
        Map.imgs[9] = load_img("WorldMap-A2-014.png")       #雪森
        """"""
    
    def get_screen_size(self):
        return self.screen.get_size()
    
    def draw_charactor(self, obj):
        """
        キャラクターを描写する関数.
        objはキャラクタ. objは少なくとも、"画像名(visual)"と"位置(pos)"を持つ
        """
        if obj.visual is not None:
            img = self.sprites[obj.visual]
            draw_pos = [obj.pos[0] * DRAW_LITERAL_32px, obj.pos[1] * DRAW_LITERAL_32px]
            self.screen.blit(img, draw_pos)

    def draw_map(self):
        """
        mapを描写する関数
        """
        self.map.draw(self.screen)
    
    def draw_menu(self,player=None):
        """
        メニューのGUIを描写する関数.GUIの枠組みを表示するだけ.
        Playerクラスが出来次第、引数にPlayerクラスをとってhpやアイテムの個数をとるように設定する必要があります。
        ->関数で枠やテキストを表示するようにしているので、画面サイズが変更になっても数値をいじるだけで対応可能.
        ->コマンドを増やす時はdraw_text()にいろいろやれば文字を表示できる.

        Args:
            player:ステータスを表示するため。後々「Noneでも大丈夫」な設定は取り払う
        """
        draw_frame(self.screen,400,10,200,180) #右側の枠
        draw_frame(self.screen,10,10,150,100) #左側の枠
        draw_text(self.screen,set_text(self.font1,"Menu"),460,16)
        draw_text(self.screen,set_text(self.font1,"Search"),445,35)
        draw_text(self.screen,set_text(self.font1,"Talk"),445,55)
        draw_text(self.screen,set_text(self.font1,"Use Buttery"),445,75)
        #電池の個数表示機能は、上の"use buttery" の右に、個数を表示すれば良い。
        draw_text(self.screen,set_text(self.font1,"DragOn Ball"),445,95)

        draw_text(self.screen,set_text(self.font1,"Denchu"),55,16)
        draw_text(self.screen,set_text(self.font1,"HP:"),35,36)
        draw_text(self.screen,set_text(self.font1,"ATK:"),35,56)
        draw_text(self.screen,set_text(self.font1,"SPD:"),35,76)

        if player is not None:
            draw_text(self.screen,set_text(self.font1,str(player.entity.status[0])),85,36)
            draw_text(self.screen,set_text(self.font1,str(player.entity.status[1])),85,56)
            draw_text(self.screen,set_text(self.font1,str(player.entity.status[2])),85,76)
            draw_text(self.screen,set_text(self.font1,str(player.items["buttery"])),575,75)
            draw_text(self.screen,set_text(self.font1,str(player.items["doragon_ball"])),575,95)

    def draw_search_around(self, text1="", text2="", text3="",text4=""):
        """
        「しらべる」実行時にそれを描写する関数.
        引数のtextと枠を描写する.
        textはとりあえず4行までなら設定できます(今後、画面サイズが変更になったらここらへんも変更になる可能性はあります)
        """
        draw_frame(self.screen,120,250,400,200)
        draw_text(self.screen,set_text(self.font2,text1),127,267)
        draw_text(self.screen,set_text(self.font2,text2),127,297)
        draw_text(self.screen,set_text(self.font2,text3),127,427)
        draw_text(self.screen,set_text(self.font2,text4),127,457)

    def draw_circle(self, _x, _y):
        pygame.draw.circle(self.screen,(255,255,255),(_x,_y), 8)