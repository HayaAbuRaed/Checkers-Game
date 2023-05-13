import pygame
from .board import Board
from .standards import WHITE, BLACK

class Game:
    def __init__(self, window) : 
        self._default()
        self.window = window
    
    def _default(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE 
        self.valid_moves = {}
            
    def update(self):
        self.board.draw_board(self.window)
        pygame.display.update()
        
    def reset(self):
        self._default()
        
    def select(self, row, col): 
        if self.selected:
            movment = self._move(row, col) 
            if not movment:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row,col)
            if piece !=0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
            
        return False
            
    def _move(self, row, col): 
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.switch_turn()
            return True
        
        return False 
    
    def switch_turn(self):
       if self.turn == BLACK:
            self.turn == WHITE
       else: self.turn = BLACK