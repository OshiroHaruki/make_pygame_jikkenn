import pygame
from pygame.locals import *
from map import Map

DRAW_LITERAL_32px = 32 #1マス32pixelなのでその定数
IMG_PIXEL = (32,32)  #1マス32*32pixelの画像サイズ
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
FONT_SIZE_SMALL = 25
FONT_SIZE_BIG = 40

def load_img(filename,colorkey=None):
    """画像読み込みを行う関数。
    Args:
        filename:画像ファイル名
    Return:
        img:画像データ
    """
    img = pygame.image.load(filename)
    img = img.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = img.get_at((0,0))
        img.set_colorkey(colorkey, RLEACCEL)
    return img

def set_text(font,text:str):
    """str型の文字列を画面に写せるように変換する関数.
    Args:
        font:pygame.font.SysFontで定義されるフォントの情報
        text:画面に表示したい文字列
    Return:
        フォントを適用したテキスト
    """
    return font.render(text,False,COLOR_WHITE)

FRAME_DISTANCE = [5,10] #フレームをずらして表示する用の定数.[位置、幅]
def draw_frame(screen,x_pos,y_pos,width,height):
    """画面にGUIの枠を表示する関数.
    Args:
        screen:pygameのscreen
        x_pos:x座標
        y_pos:y座標
        width:幅
        height:高さ
    """
    pygame.draw.rect(screen,COLOR_WHITE,(x_pos,y_pos,width,height))
    pygame.draw.rect(screen,COLOR_BLACK,(x_pos+FRAME_DISTANCE[0],y_pos+FRAME_DISTANCE[0]
                                        ,width-FRAME_DISTANCE[1],height-FRAME_DISTANCE[1]))

def draw_text(screen,text,x_pos,y_pos):
    """画面にtextを表示する関数.
    Args:
        screen:pygameのscreen
        text:表示するテキスト(str型ではなく、上記のset_textで変換されたテキスト)
        x_pos:x座標
        y_pos:y座標
    """
    screen.blit(text,(x_pos,y_pos))

class View:
    def __init__(self,screen,map):
        """
        Args:
            screen:pygameのscreen
            map:Mapクラスの情報
        Attributes:
            screen:pygameのscreen
            load_img:画像を読み込み、一時的に保存する変数.
            sprites:辞書型。画像を格納。{"(呼び出すための)名前":画像のデータ}
            font_small/big: フォント情報を格納
            map:Mapクラスの情報を格納
            Map.imgs[]:マップチップ(画像データ)を格納
        """
        self.screen = screen
        self.sprites = {}
        self.load_img = pygame.image.load("./denchu.png")
        self.load_img = pygame.transform.scale(self.load_img,IMG_PIXEL)#画像サイズを修正
        self.sprites["player"] = self.load_img #denchu.imgを格納

        #GUIの制作用#
        self.font_small = pygame.font.SysFont(None, FONT_SIZE_SMALL) #小さめフォント
        self.font_big = pygame.font.SysFont(None, FONT_SIZE_BIG) #大きめフォント

        #Map用#
        self.map = map
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
    
    def get_screen_size(self):
        return self.screen.get_size()
    
    def draw_charactor(self, obj):
        """
        キャラクターを描写する関数.
        Args
            :obj:entityクラス.entityクラスの"画像名(visual)"と"位置(pos)"を扱う.
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
        メニューのGUIを描写する関数.
        Args:
            player:Playerクラス.Playerクラスのentityのstatusにアクセスする.
        """
        draw_frame(self.screen,400,10,200,180) #右側の枠
        draw_frame(self.screen,10,10,150,100) #左側の枠
        draw_text(self.screen,set_text(self.font_small,"Menu"),460,16)
        draw_text(self.screen,set_text(self.font_small,"Search"),445,35)
        draw_text(self.screen,set_text(self.font_small,"Talk"),445,55)
        draw_text(self.screen,set_text(self.font_small,"Use Battery"),445,75)
        draw_text(self.screen,set_text(self.font_small,"DragOn Ball"),445,95)

        draw_text(self.screen,set_text(self.font_small,"Denchu"),55,16)
        draw_text(self.screen,set_text(self.font_small,"HP:"),35,36)
        draw_text(self.screen,set_text(self.font_small,"ATK:"),35,56)
        draw_text(self.screen,set_text(self.font_small,"SPD:"),35,76)

        if player is not None:
            draw_text(self.screen,set_text(self.font_small,str(player.entity.status[0])),85,36)
            draw_text(self.screen,set_text(self.font_small,str(player.entity.status[1])),85,56)
            draw_text(self.screen,set_text(self.font_small,str(player.entity.status[2])),85,76)
            draw_text(self.screen,set_text(self.font_small,str(player.items["battery"])),575,75)
            draw_text(self.screen,set_text(self.font_small,str(player.items["doragon_ball"])),575,95)

    def draw_search_around(self, text1="", text2="", text3="",text4=""):
        """「Search」コマンド実行時に描写する関数.
        Args:
            text: str型。表示したいメッセージ.４個まで設定できる。
        """
        draw_frame(self.screen,120,250,400,200)
        draw_text(self.screen,set_text(self.font_big,text1),127,267)
        draw_text(self.screen,set_text(self.font_big,text2),127,297)
        draw_text(self.screen,set_text(self.font_big,text3),127,427)
        draw_text(self.screen,set_text(self.font_big,text4),127,457)

    def draw_circle(self, _x, _y):
        """円を表示する関数.
        Args:
            _x:x座標
            _y:y座標
        """
        pygame.draw.circle(self.screen,COLOR_WHITE,(_x,_y), 8)