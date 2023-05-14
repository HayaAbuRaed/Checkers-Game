# black pieces direction: down (1)  
# black pieces direction: up   (-1) 

import pygame
from .standards import WHITE, BLACK, SQ_SIZE, CROWN

class Piece:
    def __init__(self, color, row, col):
       self.color = color
       self.row = row
       self.col = col
       self.king = True #is it a king piece?
       False
        
       self.x = 0
       self.y = 0
       self.clac_position()
       
    def clac_position(self): 
        self.x = (SQ_SIZE * self.col) + (SQ_SIZE // 2) 
        self.y = (SQ_SIZE * self.row) + (SQ_SIZE // 2) 
        
    def switch_to_king(self):
        self.king = True
    
    def draw_piece(self, surface):
        pygame.draw.circle(surface, (179, 187, 179), (self.x+2, self.y+1), 35+1 )
        pygame.draw.circle(surface, self.color, (self.x, self.y), 35)
        if self.king:
            surface.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))
        
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.clac_position()