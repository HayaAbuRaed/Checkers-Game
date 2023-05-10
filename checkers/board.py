# here is the implementation of th game bord
import pygame
from checkers.standards import BROWN, OFFWHITE, ROWS, COLS, SQ_SIZE, BLACK, WHITE
from .piece import Piece
# Checkers colors: WHITE & BLACK and number: 12 for each player
# Board squares colors: BROWN & OFFWHITE and number: 8*8
class Board:
    def __init__(self):
        self.board = []
        self.selectd_square = None
        self.black_checkers = self.white_checkers = 12 
        self.black_kings = self.white_kings = 0
        self.create_board()
        
    def draw_squares(self,game):
        #fill all the boad in brown, thennnn
        game.fill(BROWN)
        
        #customize (add) the offwhite squares
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(game, OFFWHITE, (row*SQ_SIZE, col*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
        
    def create_board(self): 
        for row in range (ROWS):
            self.board.append([])
            for col in range (COLS):
                if col % 2 == ((row + 1) % 2):#(col % 2 == 0 & row % 2 != 0) | (col % 2 != 0 & row % 2 == 0):
                    if row < 3 :
                        self.board[row].append(Piece(BLACK, row, col))
                    elif row > 4:
                        self.board[row].append(Piece(WHITE, row, col))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
                    
    def draw_board(self, game):
        self.draw_squares(game)
        for row in range (ROWS):
            for col in range (COLS):
                checker = self.board[row][col]
                if checker != 0:
                    checker.draw_piece(game)
