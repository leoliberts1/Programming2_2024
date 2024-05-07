import pygame

from .constants import BLACK, ROWS, RED, HEIGHT, WIDTH,Square_size

class Board:
    def __init__(self):
        self.board = [[],[]]
        
        self.selected_piece = None

        self.red_left = self.white_left = 12

        self.red_queens = self.white_queens = 0

    def draw_squares(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2 ,ROWS,2):
                pygame.draw.rect(win,RED,(row*Square_size,col*Square_size,Square_size,Square_size))
                
