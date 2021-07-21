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

        self.assertEqual(m.player.pos, PLAYER_POS)

        m.move([1,0])
        m.update()
        self.assertEqual(m.player.pos, [PLAYER_POS[0]+1, PLAYER_POS[1]])

    
if __name__ == "__main__":
    unittest.main()