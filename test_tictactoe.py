from tictactoegame import TicTacToe

def test_tic_tac_toe():
    game = TicTacToe()
    assert game.make_move(0, 'X') == True
    assert game.make_move(0, 'O') == False  # Invalid move, square already taken
    assert game.current_winner is None
    game.make_move(1, 'X')
    game.make_move(2, 'X')
    assert game.current_winner == 'X'  # X wins

def test_tic_tac_toe2():
    game2 = TicTacToe()
    assert game2.make_move(0, 'X') == True
    assert game2.make_move(1, 'O') == True
    assert game2.current_winner is None

def undo_move(self):
        if not self.move_history:
            return False, "No moves to undo!"
        last_move = self.move_history.pop()
        square, player = last_move
        self.board[square] = ' '  # Clear the last move from the board
        self.current_player = player  # Restore the player who made the last move
        self.current_winner = None  # Reset winner in case it was set
        return True, f"Move undone. It's {self.current_player}'s turn again."

def make_move():
    game3 = TicTacToe()
    assert game3.make_move(0, 'X') == True