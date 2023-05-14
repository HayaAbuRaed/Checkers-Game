import pygame
from .board import Board
from .standards import WHITE, BLACK, SQ_SIZE, GREEN

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
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        
    def reset(self):
        self._default()
        
    def select(self, row, col): 
        if self.selected:
            movment = self._move(row, col) 
            if not movment:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row,col)
        if piece !=0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.valid_moves(piece)
            return True
            
        return False
            
    def _move(self, row, col): 
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.switch_turn()
            return True
        
        return False 
    
    def switch_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
           self.turn = WHITE
        else: 
           self.turn = BLACK
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, GREEN, (col * SQ_SIZE + SQ_SIZE//2, row * SQ_SIZE + SQ_SIZE//2), 10)
            
    def winner(self):
        return self.board.winner()
    
    ################## AI ######################
    def get_board (self):
        return self.board
    
    def AI_moves(self, board):
        self.board = board
        self.switch_turn()