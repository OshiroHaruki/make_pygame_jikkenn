import unittest
from Tansaku_Functions import *

class Map:
    """テスト用mapクラス.
    """
    map = [[2,3,4],
           [4,5,0],
           [2,2,2],
           [2,2,2],
           [2,2,2]]
    row, col = len(map),len(map[0])

class Test_Move_Checker(unittest.TestCase):
    def test_Move_Checker(self):
        m = Map()
        m_c = Move_Checker(m)
        self.assertEqual(m_c.LEFT_LIMIT,0)
        self.assertEqual(m_c.RIGHT_LIMIT,3-1)
        self.assertEqual(m_c.UP_LIMIT,0)
        self.assertEqual(m_c.DOWN_LIMIT,5-1)

        test_pos = [0,0]
        self.assertTrue(m_c.move_check(test_pos,[1,0]))#マップ情報"3"に移動可能か
        self.assertTrue(m_c.move_check(test_pos,[0,1]))#マップ情報"4"に移動可能か
        test_pos = [1,0]
        self.assertTrue(m_c.move_check(test_pos,[-1,0]))#マップ情報"2"に移動可能か
        self.assertFalse(m_c.move_check(test_pos,[0,1]))#マップ情報"5"に移動可能か
        test_pos = [2,0]
        self.assertFalse(m_c.move_check(test_pos,[0,1]))#マップ情報"0"に移動可能か

        self.assertTrue(m_c.move_check(test_pos,[-1,0]))#マップ情報"3"に移動可能
        NOT_MOVABLE_AREA = [1,0] #その他移動不可座標を設定
        m_c.set_dont_move_area(NOT_MOVABLE_AREA)
        self.assertFalse(m_c.move_check(test_pos,[-1,0]))#設定した座標に移動可能か

class Test_Event_Checker(unittest.TestCase):
    def test_Event_Checker(self):
        e = Event_Checker()
        TEST_EVENT_POS = [0,1]#イベント座標を設定
        e.set_event_pos(TEST_EVENT_POS)
        self.assertEqual(e.event_pos,[TEST_EVENT_POS])#イベント座標が正しく設定されているか

        player_pos = [0,0]
        self.assertFalse(e.event_check(player_pos))#プレイヤー座標とイベント座標が一致しない時
        player_pos = TEST_EVENT_POS
        self.assertTrue(e.event_check(player_pos))#プレイヤー座標とイベント座標が一致する時

class Test_Player(unittest.TestCase):
    def test_Player(self):
        PLAYER_SIZE = [32,32]
        test_entity = Entity(PLAYER_SIZE)
        p = Player(test_entity)
        PLAYER_POS = [0,0]#初期位置
        self.assertEqual(p.get_pos(),PLAYER_POS)

        SET_POS = [3,4]
        p.set_pos(SET_POS)
        self.assertEqual(p.get_pos(),SET_POS)#位置情報をセットできるか

        self.assertEqual(p.items["battery"], 0)#所持数が0であるかどうか
        p.get_item("battery")
        self.assertEqual(p.items["battery"], 1)#所持数１増えているか
        p.use_battery()#batteryを使用
        self.assertEqual(p.items["battery"], 0)#batteryを使う処理が行われているか.

class Test_Action_Search(unittest.TestCase):
    def test_action_search(self):
        PLAYER_SIZE = [32,32]
        test_entity = Entity(PLAYER_SIZE)
        test_player = Player(test_entity)
        test_map = Map()
        act_search = Action_Search(test_player,test_map)

        PLAYER_POS = [0,4]#初期位置
        self.assertEqual(act_search.player.get_pos(), PLAYER_POS) #初期位置が正しい座標にあるか

        MOVE_POS = [1,-1]#移動可能場所に移動する時
        act_search.player_move(MOVE_POS)
        self.assertEqual(act_search.player.get_pos(),[0+1,4-1])#移動しているか
        MOVE_POS2 = [0,-2]#移動不可の場所に移動しようとした時
        act_search.player_move(MOVE_POS2)
        self.assertEqual(act_search.player.get_pos(),[1,3])#先ほどと同じ座標に止まっているか

        message = act_search.player_search_around()
        self.assertIs(type(message),str)#しらべる実行時にstr型で代入されているか.
        i=0
        while i < 100: #アイテムがちゃんと入手できるかをテスト
            message = act_search.player_search_around()
            i += 1
        self.assertGreater(act_search.player.items["battery"], 0)#アイテムが入手できていれば0より大きいはずである.

        message = act_search.player_talk()
        self.assertIs(type(message),str)#実行時にstr型で代入されているか.

        act_search.player.items["battery"] = 1
        message = act_search.player_use_battery()
        self.assertEqual(message,"Use Battery!")#適切に処理がされているか
        message = act_search.player_use_battery()
        self.assertEqual(message,"I don't have battery...")#適切に処理がされているか

class Test_Menu(unittest.TestCase):
    def test_menu(self):
        PLAYER_SIZE = [32,32]
        test_entity = Entity(PLAYER_SIZE)
        test_player = Player(test_entity)
        test_map = Map()
        test_act_search = Action_Search(test_player,test_map)

        menu = Menu(test_act_search)
        self.assertEqual(menu.select_command_now,0)#初期情報
        menu.select_move_under()
        self.assertEqual(menu.select_command_now,1)#1増えているか
        menu.select_move_up()
        self.assertEqual(menu.select_command_now,0)#1減らしているか
        for i in range(menu.NUM_COMMAND):
            menu.select_move_up()
        self.assertEqual(menu.select_command_now,0)#1番上の時にmove_upすると1番下に戻る.なので、コマンドの総数だけ実行すると最初の位置に戻るはず.
        for i in range(menu.NUM_COMMAND):
            menu.select_move_under()
        self.assertEqual(menu.select_command_now,0)#1番下の時にmove_downすると1番上に戻る.なので、コマンドの総数だけ実行すると最初の位置に戻るはず.
        
        for i in range(menu.NUM_COMMAND):
            message = menu.select_command()
            self.assertNotEqual(message,"Er: No Action")#エラーメッセージが表示されていないか
            menu.select_move_under()

if __name__=="__main__":
    unittest.main()
