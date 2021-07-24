import random
from map import Map

class Entity:
    """
    キャラクタの基本クラス
    """
    def __init__(self, size:list, name:str=None, visual=None):
        self.pos = [0,0]
        self.size = size
        self.name = name
        self.visual = visual
    def getPos(self)->list: #位置情報をリターンする
        return self.pos
    def setPos(self,p:list):#位置情報をセットする
        self.pos = list(p)
    
class MoveChecker():
    """
    探索パートの移動の制限に関するクラス.
    """
    def __init__(self,limit_x, limit_y):
        """
        マップが変わるごとに移動範囲を手動で入力するのは面倒なので、mapの端から端までを引数limitで指定するように変更した.
        """  
        self.LEFT_LIMIT = 0
        self.RIGHT_LIMIT = limit_x -1
        self.UP_LIMIT = 0
        self.DOWN_LIMIT = limit_y -1
        self.cant_move_area = []
    def set_DontMoveArea(self,pos:list):
        """
        移動不可の場所を設定するための関数
        """
        self.cant_move_area.append(pos)

    def move_check(self, pos:list, move_d:list):
        """
        移動しようとする方向に、移動可能かを調べる関数
        """
        if pos[0] + move_d[0] < self.LEFT_LIMIT or pos[0] + move_d[0] > self.RIGHT_LIMIT:
            return False
        elif pos[1] + move_d[1] < self.UP_LIMIT or pos[1] + move_d[1] > self.DOWN_LIMIT:
            return False
        for i in self.cant_move_area:
            if [pos[0]+move_d[0], pos[1]+move_d[1]] == i:
                return False
        return True

class Player:
    """
    プレイヤーに関するクラス.
    """
    def __init__(self, size:list, name:str=None, visual=None):
        self.entity = Entity([64,64], name = "denchu", visual = "player")
        self.hp = 10 #探索パートではhp使うつもりないけど、とりあえず置いているだけです.
        self.items = {} #アイテム機能を追加するつもりなので、とりあえず辞書型で置いてます.
    def setPos(self,pos:list):
        """
        自分の位置(座標)をセットする関数
        """
        self.entity.setPos(pos)
    def get_item(self):
        """アイテム入手の処理。具体的にはself.items[名前] = 個数　とかにしたい
        
        """
        #print("でんちを みつけた!")
        #pass

PLAYER_POS = [1,19]
class Action_Search_Part:
    """
    探索パートに関するクラス.　プレイヤーの移動や調べるコマンドの処理を行うクラス.
    """
    def __init__(self,player,_map):
        self.player = player
        self.player.setPos(PLAYER_POS)
        self.map = _map
        self.move_checker = MoveChecker(self.map.col,self.map.row)

    def player_move(self, p:list):
        """
        プレイヤーの移動処理を行う関数
        """
        if (self.move_checker.move_check(self.player.entity.pos, p)):
            pos = [self.player.entity.pos[0]+p[0], self.player.entity.pos[1]+p[1]]
            self.player.setPos(pos)

    def player_search_around(self):
        """周囲を調べる.何を実装するかは未定.アイテムゲットや敵キャラとの遭遇など？
        一旦機能を確認したいので、とりあえず確率でアイテムゲットのprint,それ以外で何も見つからないとする
        ->これが実行されたらGUIが開くようにした。それに結果を表示するようにしてみる.
        """
        set_text = ""
        rand_event = random.random()
        if rand_event > 0.5:
            self.player.get_item()
            set_text = set_text + " Get Decnhi!"
        else:
            set_text = set_text + " Not Found..."
        return set_text
        

class Model:
    def __init__(self,view):
        self.view = view
        self.map = self.view.map #map格納
        self.player = Player([64,64],name = "denchu",visual = "player")
        self.act_search_part = Action_Search_Part(self.player, self.map)

        self.entites = [self.player.entity]

        self.isOpenedGUI = False

        self.message = ""
        self.isOpenedMessage = False

    def move(self,p:list):
        """
        プレイヤーの移動を行う関数
        """
        self.act_search_part.player_move(p)

    def search(self):
        """
        プレイヤーの調べるコマンドを行う関数
        """
        self.message = self.act_search_part.player_search_around()
        self.openMessage()

    def openGUI(self):
        """
        GUIを開く関数
        """
        self.isOpenedGUI = True

    def closeGUI(self):
        """
        GUIを閉じる関数
        """
        self.isOpenedGUI = False
    
    def openMessage(self):
        """
        メッセージ画面を開く関数
        """
        self.isOpenedMessage = True

    def closeMessage(self):
        """
        メッセージ画面を閉じる関数
        """
        self.isOpenedMessage = False

    def update(self):#ここで描写の更新を行う
        """
        viewに結果を通知する関数.
        """
        self.view.draw_map()
        for obj in self.entites[:]:
            self.view.draw(obj)
        if self.isOpenedGUI:
            self.view.GUI_draw()
        if self.isOpenedMessage:
            self.view.draw_search_around(self.message)