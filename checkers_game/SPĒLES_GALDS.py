import pygame
from .constants import BLACK, ROWS, COLUMNS, RED, SQUARE_SIZE, WHITE, BLUE
from .Kauliņi import Kauliņš

class SPĒLES_GALDS:
    def __init__(self):
        self.game_table = []
        self.red_left = self.white_left = 12
        self.red_queens = self.white_queens = 0
        self.create_the_game_table()

    def draw_the_game_table(self, game_window):
        game_window.fill(BLACK)
        for rinda in range(ROWS):
            for kolonna in range(rinda % 2, COLUMNS, 2):
                pygame.draw.rect(game_window, RED, (SQUARE_SIZE * kolonna, SQUARE_SIZE * rinda, SQUARE_SIZE, SQUARE_SIZE))

    def create_the_game_table(self):
        for rinda in range(ROWS):
            self.game_table.append([])
            for kolonna in range(COLUMNS):
                if kolonna % 2 == (rinda + 1) % 2:
                    if rinda < 3:
                        kauls = Kauliņš(rinda, kolonna, WHITE)
                        self.game_table[rinda].append(kauls)
                    elif rinda > 4:
                        kauls = Kauliņš(rinda, kolonna, RED)
                        self.game_table[rinda].append(kauls)
                    else:
                        self.game_table[rinda].append(0)
                else:
                    self.game_table[rinda].append(0)

    def draw(self, game_window):
        self.draw_the_game_table(game_window)
        for rinda in range(ROWS):
            for kolonna in range(COLUMNS):
                kauliņš = self.game_table[rinda][kolonna]
                if kauliņš != 0:
                    kauliņš.draw_the_piece(game_window)

    def draw_possible_moves(self, moves, game_window):
        for move in moves:
            row, column = move
            pygame.draw.circle(game_window, BLUE, (column * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

    def moove(self, kauliņš, row, column):
        self.game_table[kauliņš.row][kauliņš.column], self.game_table[row][column] = self.game_table[row][column], self.game_table[kauliņš.row][kauliņš.column]
        kauliņš.mooving(row, column)
        if row == ROWS - 1 or row == 0:
            kauliņš.crown()

    def get_piece(self, row, column):
        return self.game_table[row][column]

    def get_possible_moves(self, piece):
        moves = {}
        left = piece.column - 1
        right = piece.column + 1
        row = piece.row
        if piece.color == RED or piece.queen:
            moves.update(self._go_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._go_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.queen:
            moves.update(self._go_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._go_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves

    def _go_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.game_table[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._go_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._go_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _go_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break
            current = self.game_table[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._go_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._go_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves

    def remove(self, pieces):
        for piece in pieces:
            self.game_table[piece.row][piece.column] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
