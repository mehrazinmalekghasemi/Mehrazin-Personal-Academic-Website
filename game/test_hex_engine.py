import unittest
from hex_engine import BLUE, YELLOW, HexGame


class HexEngineTests(unittest.TestCase):
    def test_blue_left_to_right(self):
        g = HexGame(3)
        for i in (0, 1, 3, 2):
            g.board[i] = BLUE
        self.assertEqual(g._find_path(BLUE), [0, 1, 2])

    def test_yellow_top_to_bottom(self):
        g = HexGame(3)
        for i in (0, 3, 6):
            g.board[i] = YELLOW
        self.assertEqual(g._find_path(YELLOW), [0, 3, 6])

    def test_diagonal_hex_neighbors(self):
        g = HexGame(3)
        self.assertIn(4, list(g.neighbors(0)))
        self.assertIn(0, list(g.neighbors(4)))

    def test_orthogonal_only_path_does_not_count_without_hex_diagonal(self):
        g = HexGame(3)
        g.board[0] = BLUE
        g.board[1] = BLUE
        g.board[5] = BLUE
        self.assertIsNone(g._find_path(BLUE))

    def test_game_stops_after_winner(self):
        g = HexGame(3)
        g.board = [BLUE, BLUE, BLUE, 0, 0, 0, 0, 0, 0]
        g.current_player = BLUE
        self.assertTrue(g.play(3))
        self.assertEqual(g.winner, BLUE)
        self.assertFalse(g.play(4))

    def test_no_move_after_winner(self):
        g = HexGame(3)
        g.board = [BLUE, BLUE, 0, 0, 0, 0, 0, 0, 0]
        g.current_player = BLUE
        g.play(2)
        self.assertEqual(g.winner, BLUE)
        self.assertIsNone(g.computer_move())


if __name__ == "__main__":
    unittest.main()
