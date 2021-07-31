import random
def add_pos(a:list,b:list):
    return [a[0]+b[0],a[1]+b[1]]

class Entity:
    """
    キャラクタの基本クラス.キャラクタはsize,name,visualの情報を持つ。
    """
    def __init__(self, size:list, name:str=None, visual=None, skills:list=None, status:list=None, proficiency:list=None):
        """
        Args:
            size:長さ2のリスト
            name:名前
            visual:画像の名前
            skills:動きを決定するオブジェクト[ダメージ補正、発動トリガー(最大３)]
            status:ステータス(長さ3のリスト)["HP","攻撃力","素早さ"]
            proficiency:熟練度(skillsと同じ長さのリスト)
            pos:座標

        """
        self.size = size
        self.name = name
        self.visual = visual
        self.skills = skills
        self.status = status
        self.proficiency = proficiency
        self.pos = [0,0]
    def get_pos(self)->list: #位置情報をリターンする
        return self.pos
    def set_pos(self,p:list):#位置情報をセットする
        self.pos = list(p)
    
class Move_Checker():
    """
    探索パートの移動の制限に関するクラス.
    """
    def __init__(self,map):
        """
        mapの端から端までの幅、高さを引数limitで指定する.
        """  
        self.LEFT_LIMIT = 0
        self.RIGHT_LIMIT = map.col -1
        self.UP_LIMIT = 0
        self.DOWN_LIMIT = map.row -1
        self.map = map
        self.map_deta = map.map
        self.cant_move_area = [] #その他侵入禁止箇所を作る時は、座標をリスト型で、このリストに代入する。

    def set_dont_move_area(self,pos:list):
        """
        移動不可の場所を設定するための関数(処理によって移動不可能な場所を作りたい時に使う.)
        """
        self.cant_move_area.append(pos)

    def move_check(self, pos:list, move_d:list):
        """
        移動しようとする方向に、移動可能かを調べる関数.移動可能ならTrue,不可ならFalseを返す.
        """
        pos_add_sim = add_pos(pos,move_d)
        simulate = self.map_deta[pos_add_sim[1]][pos_add_sim[0]]

        if pos_add_sim[0] < self.LEFT_LIMIT or pos_add_sim[0] > self.RIGHT_LIMIT:
            return False
        elif pos_add_sim[1] < self.UP_LIMIT or pos_add_sim[1] > self.DOWN_LIMIT:
            return False
        elif simulate != 2 and simulate != 3 and simulate != 4:#mapデータが3,4,5(道)のどれでもないとき
            return False
        for i in self.cant_move_area:# その他移動不可のエリア
            if [pos[0]+move_d[0], pos[1]+move_d[1]] == i:
                return False
        return True

class Event_Checker:
    """会話イベントが発生するかどうかを判定するクラス
    """
    def __init__(self):
        """
        event_posに配列で会話イベントが起こるマスを入れておく。
        """
        self.event_pos = [] #会話イベントが発生する座標をここに入れておく.座標は配列の形式で入れてください

    def event_check(self,player_pos):
        """プレイヤーが会話イベントマスにいるとき、Trueを返す
        """
        for area in self.event_pos:
            if player_pos == area:
                return True
        return False

class Player():
    """
    プレイヤーに関するクラス.Entityクラスを使って作成.
    """
    def __init__(self, entity):
        self.entity = entity#キャラクターのパラメータ などを格納
        self.items = {"buttery":0, "doragon_ball":0} #アイテム機能を追加するつもりとのことなので、とりあえず辞書型で置いてます.
    
    def set_pos(self,pos:list):
        """
        自分の位置(座標)をセットする関数
        """
        self.entity.set_pos(pos)
    def get_pos(self):
        return self.entity.get_pos()
    def get_item(self,item_name:str):
        """アイテム入手の処理。
        Args:
            item_name:アイテム名(butteryかdoragon_ball)
        """
        self.items[item_name] += 1
    def use_buttery(self):
        """バッテリー使用の処理。
        HPを回復するが、HP回復の関数がまだ実装されてないみたいなのでとりあえずバッテリー消費だけ。
        """
        if self.items["buttery"] >= 1:
            self.items["buttery"] -= 1


PLAYER_POS = [0,4]#初期位置
class Action_Search:
    """
    探索パートに関するクラス.　プレイヤーの移動や調べるコマンドの処理、メニュー機能の処理を行うクラス.
    """
    def __init__(self,player,_map):
        self.player = player
        self.player.set_pos(PLAYER_POS)
        self.map = _map
        self.move_checker = Move_Checker(self.map)
        self.event_checker = Event_Checker()

    def player_move(self, p:list):
        """
        プレイヤーの移動処理を行う関数
        """
        if (self.move_checker.move_check(self.player.entity.pos, p)):#移動可能かを調べ、移動可能なら移動させる
            pos = add_pos(self.player.entity.pos, p)
            self.player.set_pos(pos)

    def player_search_around(self):
        """周囲を調べる.何を実装するかは未定.アイテムゲットや敵キャラとの遭遇など？
        一旦機能を確認したいので、とりあえず確率でアイテムゲットのprint,それ以外で何も見つからないとする
        ->これが実行されたらGUIが開くようにした。それに結果を表示するようにしてみる.
        """
        set_text = ""
        rand_event = random.random()
        if rand_event > 0.5:
            self.player.get_item("buttery")
            set_text = set_text + " Get Decnhi!"
        else:
            set_text = set_text + " Not Found..."
        return set_text
    
    def player_talk(self):
        set_text = ""
        if self.event_checker.event_check(self.player.get_pos()):
            set_text = "hello!" # 会話イベント発生。ここは仮の処理なので、会話パート結合の際に書き換える.
            #本来は会話イベント移行のための関数を実行する
        else:
            set_text = "Nobody is here..."
        return set_text
    
    def player_use_buttery(self):
        set_text = ""
        #if butteryが１こ以上あるなら
        if self.player.items["buttery"] >= 1:
            #バッテリーを使ったというメッセージをsetし、バッテリーを使う処理を行う
            set_text = "Use Buttery!"
            self.player.use_buttery()
        else:#else (butteryを所持していないなら)
        #バッテリーを持ってないというメッセージをsetする
            set_text = "I don't have buttery..."

        return set_text

class Menu:
    """
    メニューを開いている時の処理を行う.
    """
    INIT_CIRCLE_POS = [425,45]
    NUM_COMMAND = 4
    CIRCLE_MOVE = 20
    LIMIT_CIRCLE_POS_UP = 45
    LIMIT_CIRCLE_POS_UNDER = LIMIT_CIRCLE_POS_UP + CIRCLE_MOVE * (NUM_COMMAND - 1) 
    
    def __init__(self, action):
        self.select_command_pos = self.INIT_CIRCLE_POS
        self.select_command_now = 0 #この数字に対応した処理を行うようにする.
        self.act = action
    
    def select_move_under(self):
        """
        選択ボタンっぽいやつ(円)を下に移動させる関数.
        """
        if self.select_command_pos[1] + self.CIRCLE_MOVE > self.LIMIT_CIRCLE_POS_UNDER:
            self.select_command_pos[1] = 45 #一番下まで行ったら、一番上に戻る。
            self.select_command_now = 0
        else:
            self.select_command_pos[1] += self.CIRCLE_MOVE
            self.select_command_now += 1 
    def select_move_up(self):
        """
        選択ボタンっぽいやつ(円)を上に移動させる関数.
        """
        if self.select_command_pos[1] - self.CIRCLE_MOVE < self.LIMIT_CIRCLE_POS_UP:
            self.select_command_pos[1] = self.LIMIT_CIRCLE_POS_UNDER#一番上まで行ったら、一番下に戻る。
            self.select_command_now = self.NUM_COMMAND - 1
        else:
            self.select_command_pos[1] -= self.CIRCLE_MOVE
            self.select_command_now -= 1
    def select_command(self):
        if self.select_command_now == 0:#Search
            result_text = self.act.player_search_around()
        elif self.select_command_now == 1:#Talk
            result_text = self.act.player_talk()
        elif self.select_command_now == 2:#Use Buttery
            result_text = self.act.player_use_buttery()
        elif self.select_command_now == 3:#doragonball
            result_text = "7ko atsumeruto clear!"
        else:
            result_text = "Er: No Action"
        return result_text