import pygame
from .SPĒLES_GALDS import SPĒLES_GALDS
from .constants import RED,WHITE

class Spēle:
    def __init__(self,game_window):
        self.__init()
        self.game_window = game_window
    def update(self):
        self.Game_table.draw(self.game_window)
        pygame.display.update()
    def __init(self):
        self.selected = None
        self.Game_table = SPĒLES_GALDS()
        self.turn = RED
        self.possible_moves = {}
    def reset (self):
        self.__init()
    def select(self,row,column):
        if self.selected:
            result = self.move(row, column)
    def move(self,row,column):

    