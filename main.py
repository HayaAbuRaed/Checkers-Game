import pygame
import sys
from checkers.standards import WIDTH, HEIGHT, SQ_SIZE, BLACK, WHITE
from checkers.game import Game
from minimax.algo import minimax

GAME = pygame.display.set_mode ((WIDTH , HEIGHT))
pygame.display.set_caption('Checkers Game')

def main ():
    run = True
    
    clock =  pygame.time.Clock() # to make sure that the game will run at the same speed in all computers, no mater how fast the cpu is
    game = Game(GAME)
    
    def get_position_from_mouse(position):
        x,y = position
        row = y // SQ_SIZE
        col = x // SQ_SIZE
        return row, col
     
    while run:
        clock.tick(60)
        
        if game.winner() != None:
            print('The WINNER is :', game.winner(), '!')
            run = False
        
        if game.turn == BLACK:
            value, new_board = minimax(game.get_board(), 3, BLACK, game)
            game.AI_moves(new_board)
            
        if game.turn == WHITE and game.valid_moves == None:
            game.board.white_checkers = 0
        
        # check for an event 
        for event in pygame.event.get():
            
            # event: pushing quit button 
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            # event: clicking any square in the board
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(position)
                game.select(row,col)
               
        game.update()
               
    #  run = false 
    pygame.quit()
    
main()