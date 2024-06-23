import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    # Update the game display
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    #hidden init used to start or restart the game
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED  # RED starts the game
        self.valid_moves = {}

    # Check if there is a winner
    def winner(self):
        return self.board.winner()

    # Reset the game
    def reset(self):
        self._init()

    # this function checks if the given position a player has selected
    #can be mooved to by a piece if aa piece has been chosen before
    #otherwise the clicked upon piece will be selected
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    # Move the selected piece to a new position
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    # Draw valid moves for the selected piece
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    # Change the turn to the other player
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
