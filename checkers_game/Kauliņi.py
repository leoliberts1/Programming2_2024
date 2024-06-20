import pygame.draw
from .constants import WHITE, SQUARE_SIZE, GREY, CROWN

class Kauliņš:
    padding = 13
    outline = 2

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.queen = False
        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def crown(self):
        self.queen = True

    def draw_the_piece(self, game_window):
        rādiuss = SQUARE_SIZE // 2 - Kauliņš.padding
        pygame.draw.circle(game_window, GREY, (self.x, self.y), rādiuss + Kauliņš.outline)
        pygame.draw.circle(game_window, self.color, (self.x, self.y), rādiuss)
        if self.queen:
            game_window.blit(CROWN, (self.x - (CROWN.get_width() // 2), self.y - (CROWN.get_height() // 2)))

    def mooving(self, row, column):
        self.row = row
        self.column = column
        self.calculate_position()

    def __repr__(self):
        return str(self.color)
