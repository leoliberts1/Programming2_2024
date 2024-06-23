from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN
import pygame

class Piece:
    PADDING = 15  # padding between the piece and the outline of the square
    OUTLINE = 2   # the line around the piece

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False  # Initially, the piece is not a king
        self.x = 0
        self.y = 0
        self.calc_pos()  # Calculate the piece's position

    # Calculate the position of the piece on the board
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # Make the piece a king
    def make_king(self):
        self.king = True

    # Draw the piece on the board
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)  # Draw the outline
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)  # Draw the piece
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))  # Draw the crown if the piece is a king

    # Move the piece to a new position
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()  # Recalculate the position after moving

    # the piece will be represented as it's color
    def __repr__(self):
        return str(self.color)
