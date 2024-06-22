import pygame
from .SPĒLES_GALDS import SPĒLES_GALDS
from .constants import RED, WHITE

class Spēle:
    def __init__(self, game_window):
        self.__init()
        self.game_window = game_window

    def update(self):
        self.game_table.draw(self.game_window)
        self.game_table.draw_possible_moves(self.possible_moves, self.game_window)

        pygame.display.update()

    def __init(self):
        self.selected = None
        self.game_table = SPĒLES_GALDS()
        self.turn = RED
        self.possible_moves = {}

    def reset(self):
        self.__init()

    def select(self, row, column):
        #If a piece has already been chosen
        #it gets moved
        if self.selected:
            result = self._move(row, column)
            if not result:
                self.selected = None
                self.select(row, column)
        piece = self.game_table.get_piece(row, column)
        #else the piece becomes the selected one
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.possible_moves = self.game_table.get_possible_moves(piece)
            return True
        return False

    def _move(self, row, column):
        piece = self.game_table.get_piece(row, column)
        if self.selected and (row, column) in self.possible_moves:
            self.game_table.moove(self.selected, row, column)
            skipped = self.possible_moves[(row, column)]
            if skipped:
                self.game_table.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        self.possible_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_winner(self):
        if self.game_table.red_left <= 0:
            return "WHITE"
        elif self.game_table.white_left <= 0:
            return "RED"
        return None
