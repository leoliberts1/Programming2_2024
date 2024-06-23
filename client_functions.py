import pickle

import pygame
from checkers.game import Game

class ClientFunctions:
    def __init__(self, win, client):
        self.win = win
        self.client = client
        self.game = None

    def set_game_state(self, game_state):
        if not self.game:
            self.game = Game(self.win)
        self.game.board = game_state['board']
        self.game.turn = game_state['turn']
        self.game.selected = game_state['selected']
        self.game.valid_moves = game_state['valid_moves']
        print("Game object set:", self.game)

    def update(self):
        if self.game:
            self.game.update()
        else:
            print("Game object is not set.")

    def select(self, row, col):
        if self.game:
            self.game.select(row, col)
            self.client.send(pickle.dumps({
                'board': self.game.board,
                'turn': self.game.turn,
                'selected': self.game.selected,
                'valid_moves': self.game.valid_moves
            }))
