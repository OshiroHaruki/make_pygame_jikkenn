from map import Map
from Tansaku_Functions import *

  
class Model:
    def __init__(self,view):
        """
        Attributes:
            view:Viewクラスを格納
            map:マップ情報を格納
            entites:キャラクターの情報をまとめて格納
            denchu_data:探索パートでプレイヤーに情報を与えるために設定
            player:探索パートで動かす物体。
            act_search:探索パートの処理を定義
            is_opened_GUI:メニューGUIが開いているかどうかの状態。
            message:Viewに文字を通知したい時に使うために定義。
            is_opened_message:メッセージが開いているかどうかの状態。
            menu:メニュー機能を定義。
        """
        self.view = view
        self.map = self.view.map #map格納

        self.entites = self.make_entity_book() #戦闘パートで使うらしいので持ってきておく
        self.denchu_data = self.entites[0]
        self.player = Player(self.denchu_data)
        self.act_search = Action_Search(self.player, self.map)

        self.is_opened_GUI = False

        self.message = ""
        self.is_opened_message = False

        self.menu = Menu(self.act_search)

    def move(self,p:list):
        """プレイヤーの移動を行う関数.
        Args:
            p:list[x方向,y方向]で受け取る.
        """
        self.act_search.player_move(p)

    def open_GUI(self):
        """GUIを開く関数.
        """
        self.is_opened_GUI = True

    def close_GUI(self):
        """GUIを閉じる関数.
        """
        self.is_opened_GUI = False
    
    def open_Message(self):
        """メッセージ画面を開く関数.
        """
        self.is_opened_message = True

    def close_Message(self):
        """メッセージ画面を閉じる関数.
        """
        self.is_opened_message = False

    def select_move_under(self):
        """メニュー機能の選択ボタンを下に動かす.
        """
        self.menu.select_move_under()
    def select_move_up(self):
        """メニュー機能の選択ボタンを上に動かす.
        """
        self.menu.select_move_up()
    def select_command(self):
        """メニュー機能の決定ボタンを押した時の処理
        """
        self.message = self.menu.select_command()
        self.open_Message() #今のところは必ずopen_Message()するようにしているが、会話パートの結合次第では条件分岐で、会話パート移行の関数を実行するように処理を変更する。

    def update(self):#ここで描写の更新をViewに通知する
        """viewに結果を通知する関数.
        """
        self.view.draw_map()
        for obj in self.entites[:]:
            self.view.draw_charactor(obj)
        if self.is_opened_GUI:
            self.view.draw_menu(self.player)
            self.view.draw_circle(self.menu.select_command_pos[0],self.menu.select_command_pos[1])
        if self.is_opened_message:
            self.view.draw_search_around(self.message)

    def make_entity_book(self):
        """
        登場人物のステータス等を記載する図鑑
        proficiencyがskillsを参照した長さのリストを持つので、予めskillを定義してからEntityを生成する。
        """
        denchu_skills={"電光石火":[2,0],"10万ボルト":[4,3,1],"雷":[9,2,2,2]}
        robot_skills={"ロケットパンチ":[1,3],"地震":[3,2,2],"目からビーム":[5,1,1,3]}
        
        
        denchu = Entity([32,32],name="denchu",visual = "player",skills = denchu_skills,status=[10,4,2],proficiency=[0]*len(denchu_skills))
        robot = Entity([32,32],name="robot",skills = robot_skills,status=[20,3,1],proficiency=[0]*len(robot_skills))
        entity_book = [denchu,robot]
        
        return entity_book