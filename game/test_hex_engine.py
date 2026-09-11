import unittest
from hex_engine import BLUE, EMPTY, YELLOW, HexGame


class HexEngineTests(unittest.TestCase):
    def test_blue_left_to_right(self):
        g = HexGame(3)
        g.board[0] = BLUE
        g.board[1] = BLUE
        g.board[2] = BLUE
        self.assertEqual(g._find_path(BLUE), [0, 1, 2])

    def test_yellow_top_to_bottom(self):
        g = HexGame(3)
        g.board[0] = YELLOW
        g.board[3] = YELLOW
        g.board[6] = YELLOW
        self.assertEqual(g._find_path(YELLOW), [0, 3, 6])

    def test_hex_diagonal_neighbors(self):
        g = HexGame(3)
        self.assertIn(4, list(g.neighbors(0)))
        self.assertIn(0, list(g.neighbors(4)))

    def test_non_connected_blue_cells_do_not_win(self):
        g = HexGame(3)
        g.board[0] = BLUE
        g.board[2] = BLUE
        self.assertIsNone(g._find_path(BLUE))

    def test_game_stops_after_winner(self):
        g = HexGame(3)
        g.board[0] = BLUE
        g.board[1] = BLUE
        g.current_player = BLUE
        self.assertTrue(g.play(2))
        self.assertEqual(g.winner, BLUE)
        self.assertFalse(g.play(3))

    def test_no_computer_move_after_winner(self):
        g = HexGame(3)
        g.board[0] = BLUE
        g.board[1] = BLUE
        g.current_player = BLUE
        g.play(2)
        self.assertEqual(g.winner, BLUE)
        self.assertIsNone(g.computer_move())

    def test_reset(self):
        g = HexGame(3)
        g.play(0)
        g.reset()
        self.assertEqual(g.board, [EMPTY] * 9)
        self.assertEqual(g.current_player, BLUE)
        self.assertEqual(g.winner, EMPTY)


if __name__ == "__main__":
    unittest.main()
