from copy import deepcopy
import pygame
from checkers.standards import BLACK, WHITE, BLUE
# RED = (255,0,0)
# WHITE = (255, 255, 255)

# position: the current position that we are in (board object)
# depth: number of levels we're going to scan
def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_checkers_of_color(color):
        valid_moves = board.valid_moves(piece)
        for move, skip in valid_moves.items():
            
            #draw_moves(game, board, piece)
            
            # copies the object not the reference
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board
def draw_moves(game, board, piece):
    valid_moves = board.valid_moves(piece)
    board.draw_board(game.window)
    pygame.draw.circle(game.window, BLUE, (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)
