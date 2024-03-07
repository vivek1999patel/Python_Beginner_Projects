import random
from player import HumanPlayer, RandomComputerPlayer

class TicTocToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

        @staticmethod
        def make_board():
            board = []
            for _ in range(9):
                board.append[' ']
        
        @staticmethod
        def print_board():
            for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
                print("| " + " | ".join(row)+ " |")

        @staticmethod
        def print_board_nums():
            for row in [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]:
                print("| " + " |".join(row) + " |")