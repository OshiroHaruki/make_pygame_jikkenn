# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
SCR_RECT = Rect(0, 0, 640, 480) #画面サイズ

#マップのクラス
class Map:
    #マップデータ　(サイズ：15×20)
    map = [[0,0,0,0,0,0,0,0,0,9,9,9,0,0,7,7,7,0,0,0,],
           [0,5,5,5,0,0,0,9,9,9,9,9,9,9,9,7,7,7,7,0,],
           [5,5,5,5,5,5,9,9,2,2,2,2,2,9,9,9,9,9,7,7,],
           [3,3,5,5,3,3,2,2,2,2,2,2,2,2,2,2,9,9,9,7,],
           [3,3,3,3,3,3,3,2,2,2,9,9,2,2,2,2,2,2,2,7,],
           [5,5,3,3,3,3,3,3,2,9,9,1,1,1,9,2,2,2,2,7,],
           [0,5,5,5,3,3,3,5,1,1,1,1,1,1,9,9,2,4,4,6,],
           [0,8,8,5,3,3,3,5,5,1,1,1,1,1,1,4,4,4,4,6,],
           [0,0,8,5,5,3,3,3,5,1,1,1,1,1,4,4,4,4,6,6,],
           [0,0,8,8,5,3,3,5,5,5,3,1,4,4,4,4,4,4,6,6,],
           [0,0,0,8,5,3,3,5,5,3,4,4,4,4,4,4,4,4,6,0,],
           [0,8,8,5,5,3,3,3,3,4,4,4,4,4,4,4,4,4,6,0,],
           [0,8,8,5,3,3,3,3,3,3,4,4,4,4,6,4,6,6,6,0,],
           [0,0,8,5,5,5,5,5,5,4,4,6,6,6,6,6,6,6,0,0,],
           [0,0,0,8,8,5,5,0,0,0,0,0,0,6,6,6,0,0,0,0,]]
    row, col = len(map),len(map[0]) #マップの行数、列数を取得
    imgs = [None] * 256             #マップチップ
    msize = 32                     #1マスの大きさ[px]
    #マップの描画
    def draw(self, screen):
        for i in range(self.row):
            for j in range(self.col):
                screen.blit(self.imgs[self.map[i][j]], (j*self.msize,i*self.msize))

#画像の読み込み
def load_img(filename, colorkey=None):
    img = pygame.image.load(filename)
    img = img.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = img.get_at((0,0))
        img.set_colorkey(colorkey, RLEACCEL)
    return img

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    Map.imgs[0] = load_img("WorldMap-A1-011.png")         #海
    Map.imgs[1] = load_img("WorldMap-A1-018.png")         #湖
    Map.imgs[2] = load_img("WorldMap-A2-018.png")         #雪道(移動可能)
    Map.imgs[3] = load_img("BrightForest-A2-001.png")       #森道(移動可能)
    Map.imgs[4] = load_img("WorldMap-A2-020.png")       #岩道(移動可能)
    Map.imgs[5] = load_img("WorldMap-A2-013.png")       #森
    Map.imgs[6] = load_img("WorldMap-A2-024.png")       #岩山
    Map.imgs[7] = load_img("WorldMap-A2-030.png")       #雪山
    Map.imgs[8] = load_img("WorldMap-A2-022.png")       #森山
    Map.imgs[9] = load_img("WorldMap-A2-014.png")       #雪森
    map = Map()
    while (1):
        map.draw(screen)
        pygame.display.update()
        #イベント処理
        for event in pygame.event.get():
            #終了用のイベント処理
            if event.type == QUIT:          #閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       #キーを押したとき   
                if event.key == K_ESCAPE:   #Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()