import pygame
from .constants import RED,WHITE,Square_size,GREY

class Piece:

    Padding = 8
    outline = 2

    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.queen = False
        if self.color == RED:
            self.direction = -1
        else:self.direction = 1
        self.x = 0
        self.y = 0
        self.calc_pos()
    

    def calc_pos(self):
        self.x = Square_size*self.col+Square_size//2
        self.y = Square_size*self.col+Square_size//2
    
    def selfqueen(self):
        self.queen = True

    def draw(self,win):
        radius = Square_size//2 - self.Padding
        
        pygame.draw.circle(win,GREY,(self.x,self.y),radius + self.outline)
        pygame.draw.circle(win,self.color,(self.x,self.y),radius)

    def __repr__(self):
        return str(self.color)
        
