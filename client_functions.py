import pygame
from checkers_game.constants import WIDTH,HEIGHT,COLUMNS,ROWS,SQUARE_SIZE,RED,WHITE,BLUE,BLACK,GREY

class client_functions():
    padding = 13
    outline = 2
    def __init__(self):
        self.name = ("functions that do the same thing as the functions"
                     "in the other files in respect to drawing the checkers table")

    def draw_the_game_table(self, game_window):
        game_window.fill(BLACK)
        for rinda in range(ROWS):
            for kolonna in range(rinda % 2, COLUMNS, 2):
                pygame.draw.rect(game_window, RED, (SQUARE_SIZE * kolonna, SQUARE_SIZE * rinda, SQUARE_SIZE, SQUARE_SIZE))
    def draw_the_piece(self,kauliņš,position,game_window):
        '''    def draw_the_piece(self, game_window):
        rādiuss = SQUARE_SIZE // 2 - Kauliņš.padding
        pygame.draw.circle(game_window, GREY, (self.x, self.y), rādiuss + Kauliņš.outline)
        pygame.draw.circle(game_window, self.color, (self.x, self.y), rādiuss)
        if self.queen:
            game_window.blit(CROWN, (self.x - (CROWN.get_width() // 2), self.y - (CROWN.get_height() // 2)))'''
        print(kauliņš)
        rādiuss = SQUARE_SIZE //2 - self.padding
        krāsa = (255,255,255)
        #if kauliņš == krāsa:

        pygame.draw.circle(game_window, GREY, (kauliņš.x, kauliņš.y), rādiuss + self.outline)
        pygame.draw.circle(game_window, kauliņš.color, (kauliņš.x,kauliņš.y), rādiuss)
    def draw_possible_moves(self, moves, game_window):
        for move in moves:
            row, column = move
            pygame.draw.circle(game_window, BLUE, (column * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
    def draw(self, game_window,game_table,possible_moves):
        print(game_table)
        self.draw_the_game_table(game_window)
        for rinda in range(ROWS):
            for kolonna in range(COLUMNS):
                kauliņš = game_table[rinda][kolonna]
                if kauliņš != 0:
                    #kauliņš.draw_the_piece(game_window)
                    print(type(kauliņš))
                    self.draw_the_piece(kauliņš,[rinda,kolonna],game_window)
        self.draw_possible_moves(possible_moves,game_window)
        pygame.display.update()
        print("success?")

    def get_row_and_column_from_the_player(position):
        x, y = position
        row = y // SQUARE_SIZE
        column = x // SQUARE_SIZE
        return row, column
    def __repr__(self):
        return self.name