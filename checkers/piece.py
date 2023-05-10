# black pieces direction: down (1)  
# black pieces direction: up   (-1) 

import pygame
from .standards import WHITE, BLACK, SQ_SIZE

class Piece:
    def __init__(self, color, row, col):
       self.color = color
       self.row = row
       self.col = col
       self.king = False #is it a king piece?
       
       if self.color == WHITE :
           self.direction = -1 #up
       else:
           self.direction = 1 #down
        
       self.x = 0
       self.y = 0
       self.clac_position()
       
    def clac_position(self): 
        self.x = (SQ_SIZE * self.col) + (SQ_SIZE // 2) 
        self.y = (SQ_SIZE * self.row) + (SQ_SIZE // 2) 
        
    def switch_to_king(self):
        self.king = True
    
    ########### COME BACK #############
    def draw_piece(self, surface):
        pygame.draw.circle(surface, (179, 187, 179), (self.x+2, self.y+1), 35+1 )
        pygame.draw.circle(surface, self.color, (self.x, self.y), 35)
        
    # def __repr__(self):
    #     return str(self.color)       
       
    