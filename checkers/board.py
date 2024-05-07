import pygame

import sys
print(sys.path)

from checkers.constants import BLACK, ROWS, RED,Square_size,COLS, WHITE
from checkers.piece import Piece

print(BLACK)

class Board:
    def __init__(self):
        self.board = [[],[]]
        
        self.selected_piece = None

        self.red_left = self.white_left = 12

        self.red_queens = self.white_queens = 0

        self.create_board()

    def draw_squares(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2 ,COLS,2):
                pygame.draw.rect(win,RED,(row*Square_size,col*Square_size,Square_size,Square_size))
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                #selects on which squares the checkers will be drawn
                if col %2 == ((row+1)%2):
                    if row < 3:
                        self.board[row].append(Piece(row,col,WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row,col,RED))
                    else:
                        self.board[row].append(0)
                else: self.board.append(0)
    def draw(self,win):
        self.draw_squares
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)


