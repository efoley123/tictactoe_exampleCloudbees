import unittest

import sys
import os
from tictactoegame import TicTacToe

class TestMain(unittest.TestCase):
    def test_tic_tac_toe(self):
        game = TicTacToe()
        assert game.make_move(0) == (True, "Move successful")
        assert game.make_move(0) == (False, "Square already occupied")  # Invalid move, square already taken
        assert game.current_winner is None
        game.make_move(1) # X O
        game.make_move(2) #X O X
        game.make_move(4) # X O X  _ O _
        game.make_move(3) # X O X  X O _
        game.make_move(7) # X O X  X O _   _ O _
        
        assert game.current_winner == 'O'  # X wins

    def test_tic_tac_toe2(self):
        game2 = TicTacToe()
        assert game2.make_move(0) == (True, "Move successful")
        assert game2.make_move(1) == (True, "Move successful")
        game2.make_move(2)
        assert game2.current_winner is None


    """
    def undo_move(self):
            if not self.move_history:
                return False, "No moves to undo!"
            last_move = self.move_history.pop()
            square, player = last_move
            self.board[square] = ' '  # Clear the last move from the board
            self.current_player = player  # Restore the player who made the last move
            self.current_winner = None  # Reset winner in case it was set
            return True, f"Move undone. It's {self.current_player}'s turn again."

    def make_move(self):
        game3 = TicTacToe()
        assert game3.make_move(0) == True

    def new_game():
        game4 = TicTacToe()"""


    

    def test_validate_move(tic_tac_toe):
        game5=TicTacToe()
        assert game5.validate_move(0) == (True, "Valid move")
        assert game5.validate_move(10) == (False, "Move must be between 0 and 8")
        assert game5.validate_move(-1) == (False, "Move must be between 0 and 8")
        assert game5.validate_move(0) == (True, "Valid move")#they haven't made the move yet just checking

    """def test_print_board(capsys, tic_tac_toe):
        tic_tac_toe.print_board()
        captured = capsys.readouterr()
        assert captured.out  # Check if board is printed

    def test_make_move(tic_tac_toe):
        tic_tac_toe.make_move(0)
        assert tic_tac_toe.current_player == 'O'  # Check player switch
        assert tic_tac_toe.board[0] == 'X'  # Check if move is made

    @patch('tictactoe.TicTacToe.check_winner', return_value=True)
    def test_check_winner(mock_check_winner, tic_tac_toe):
        assert tic_tac_toe.check_winner(0) == True

    def test_available_moves(tic_tac_toe):
        tic_tac_toe.board = ['X', 'O', ' ', ' ', 'X', 'O', 'O', 'X', 'O']
        assert tic_tac_toe.available_moves() == [2, 3]

    def test_is_board_full(tic_tac_toe):
        tic_tac_toe.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        assert tic_tac_toe.is_board_full() == True

    def test_reset_game(tic_tac_toe):
        tic_tac_toe.reset_game()
        assert tic_tac_toe.board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def test_print_scores(capsys, tic_tac_toe):
        tic_tac_toe.print_scores()
        captured = capsys.readouterr()
        assert captured.out  # Check if scores are printed"""