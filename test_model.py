import unittest
from Model import *

class View:
    def getScreenSize(self):
        return [300,200]
    def draw(self,screen):
        pass

class ModelTest(unittest.TestCase):
    def test_model(self):
        m = Model(View())
        t_pos = PLAYER_POS

        self.assertEqual(m.player.entity.pos, t_pos)

        m.move([1,0])
        m.update()
        self.assertEqual(m.player.entity.pos, [t_pos[0]+1, t_pos[1]])

if __name__ == "__main__":
    unittest.main()