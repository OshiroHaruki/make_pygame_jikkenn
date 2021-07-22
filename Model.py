import random

class Entity:
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
    def __init__(self):      
        self.LEFT_LIMIT = 0
        self.RIGHT_LIMIT = 9
        self.UP_LIMIT = 0
        self.DOWN_LIMIT = 9
        self.cant_move_area = []
    def set_DontMoveArea(self,pos:list):
        self.cant_move_area.append(pos)

    def move_check(self, pos:list, move_d:list):
        if pos[0] + move_d[0] < self.LEFT_LIMIT or pos[0] + move_d[0] > self.RIGHT_LIMIT:
            return False
        elif pos[1] + move_d[1] < self.UP_LIMIT or pos[1] + move_d[1] > self.DOWN_LIMIT:
            return False
        for i in self.cant_move_area:
            if [pos[0]+move_d[0], pos[1]+move_d[1]] == i:
                return False
        return True

class Player:
    def __init__(self, size:list, name:str=None, visual=None):
        self.entity = Entity([64,64], name = "denchu", visual = "player")
        self.hp = 10 #探索パートではhp使うつもりないけど、とりあえず置いているだけです.
        self.items = {} #アイテム機能を追加するつもりなので、とりあえず辞書型で置いてます.
    def setPos(self,pos:list):
        self.entity.setPos(pos)
    def get_item(self):
        """アイテム入手の処理。具体的にはself.items[名前] = 個数　とかにしたい
        
        """
        print("でんちを みつけた!")
        #pass

PLAYER_POS = [0,0]
class Action_Search:
    def __init__(self,player):
        self.player = player
        self.player.setPos(PLAYER_POS)
        self.move_checker = MoveChecker()

    def player_move(self, p:list):
        if (self.move_checker.move_check(self.player.entity.pos, p)):
            pos = [self.player.entity.pos[0]+p[0], self.player.entity.pos[1]+p[1]]
            self.player.setPos(pos)

    def player_search_around(self):
        """周囲を調べる.何を実装するかは未定.アイテムゲットや敵キャラとの遭遇など？
        一旦機能を確認したいので、とりあえず確率でアイテムゲットのprint,それ以外で何も見つからないとする
        """
        print("しらべチュウ...")
        rand_event = random.random()
        if rand_event > 0.5:
            self.player.get_item()
        else:
            print("なにも みつからなかった...")

class Model:
    def __init__(self,view):
        self.view = view
        self.player = Player([64,64],name = "denchu",visual = "player")
        self.act_search = Action_Search(self.player)

        self.entites = [self.player.entity]

        self.isOpenedGUI = False

    def move(self,p:list):
        self.act_search.player_move(p)

    def search(self):
        self.act_search.player_search_around()

    def openGUI(self):
        self.isOpenedGUI = True

    def closeGUI(self):
        self.isOpenedGUI = False

    def update(self):#ここで描写の更新を行う
        for obj in self.entites[:]:
            self.view.draw(obj)
        if self.isOpenedGUI:
            self.view.GUI_draw()