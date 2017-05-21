import unittest

from movement import Knight

class MovementTestCase(unittest.TestCase):
	board=[["  ","  ","  ","  ","  "],
			["  ","  ","  ","  ","  "],
			["  ","  ","  ","  ","  "],
			["  ","  ","  ","  ","  "],
			["  ","  ","  ","  ","  "]]
    def Knight_Can_Move_When_Valid(self):
    	board = self.board
    	board[2][2] = "Wn"
        self.assertTrue(Knight())

if __name__ == '__main__':
    unittest.main()