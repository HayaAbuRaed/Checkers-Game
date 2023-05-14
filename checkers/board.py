# here is the implementation of th game bord
import pygame
from checkers.standards import BROWN, OFFWHITE, ROWS, COLS, SQ_SIZE, BLACK, WHITE
from .piece import Piece
# Checkers colors: WHITE & BLACK and number: 12 for each player
# Board squares colors: BROWN & OFFWHITE and number: 8*8
class Board:
    def __init__(self):
        self.board = []
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
                    
    
    def move(self, piece, row, col):
        # swap
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        
        if row == ROWS - 1 or row == 0:
            piece.switch_to_king()
            if piece.color == WHITE:
                self.white_kings +=1
            else:
                self.black_kings +=1
                
    def get_piece(self, row, col):
        return self.board[row][col]
    
    def valid_moves(self,checker):
        # moves store every move that the player can do as: (row, col)
        moves = {}
        left = checker.col - 1 
        right = checker.col + 1
        row = checker.row
        
        if checker.color == WHITE or checker.king:
            # start = the row above the current row we are at
            # stop = the num of lines we are looking at [(row-3) indicates that we are seeing only tow steps]
            moves.update(self._move_left(row -1, max(row-3, -1), -1, checker.color, left))
            moves.update(self._move_right(row -1, max(row-3, -1), -1, checker.color, right))
            
        if checker.color == BLACK or checker.king:
            moves.update(self._move_left(row +1, min(row+3, ROWS), 1, checker.color, left))
            moves.update(self._move_right(row +1, min(row+3, ROWS), 1, checker.color, right))
            
        return moves
    # step: indicates direction (up or down)
    # skipped: this will tell us that we killed a checker, and can do another move to kill another one if any
    def _move_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for checker_row in range(start, stop, step):
            # condition: we're looking outside of the board
            if left < 0:
                break
            
            current = self.board[checker_row][left]
            #IF1 - means no checker on the square we're looking at
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(checker_row, left)] = last + skipped
                else:
                    moves[(checker_row, left)] = last
                
                if last:
                    if step == -1:
                        row = max(checker_row - 3, 0)
                    else:
                        row = min(checker_row+3, ROWS)
                    moves.update(self._move_left(checker_row+step, row, step, color, left-1,skipped=last))
                    moves.update(self._move_right(checker_row+step, row, step, color, left+1,skipped=last))
                break
            
            # IF1 - means that we found a checker on the square and it is one of ours (ours = the player that is currently playing)
            elif current.color == color:
                break
            
            #IF1 - means that means that we found a checker on the square we're checking and it is one of the opponent's checkers
            #We put the current value in the last array indicating that it might be followed by an empty square so we can jump into
            else:
                last = [current]

            left -= 1
        
        return moves

    def _move_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for checker_row in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[checker_row][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(checker_row,right)] = last + skipped
                else:
                    moves[(checker_row, right)] = last
                
                if last:
                    if step == -1:
                        row = max(checker_row - 3, 0)
                    else:
                        row = min(checker_row + 3, ROWS)
                    moves.update(self._move_left(checker_row + step, row, step, color, right-1,skipped=last))
                    moves.update(self._move_right(checker_row + step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
    
    
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == WHITE:
                    self.white_checkers -= 1
                else:
                    self.black_checkers -= 1
    
    def winner(self):
        if self.white_checkers <= 0:
            return "BLACK"
        elif self.black_checkers <= 0:
            return "WHITE"
        
        return None
    
    ################## AI ######################
    def evaluate(self):
        return self.black_checkers - self.white_checkers + (self.black_kings * 0.5 - self.white_kings * 0.5)

    def get_checkers_of_color(self, color):
        checkers = []
        for row in self.board:
            for checker in row:
                if checker != 0 and checker.color == color:
                    checkers.append(checker)
        return checkers