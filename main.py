import pygame
import sys
from checkers.standards import WIDTH, HEIGHT, BROWN
from checkers.board import Board

GAME = pygame.display.set_mode ((WIDTH , HEIGHT))
pygame.display.set_caption('Checkers Game')

def main ():
    run = True
    
    clock =  pygame.time.Clock() # to make sure that the game will run at the same speed in all computers, no mater how fast the cpu is
    board = Board()  #crate new Board object
     
    while run:
        clock.tick(60)
        
        # check for an event 
        for event in pygame.event.get():
            
            # event: pushing quit button 
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            # event: clicking any square in the board
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("h")
               
        board.draw_board(GAME)
        pygame.display.update()
               
    #  run = false 
    pygame.quit()
    
main()