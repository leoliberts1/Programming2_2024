import pygame
from checkers.constants import WIDTH,HEIGHT
from checkers.board import Board
bam = 1
WIN =pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Checkers")

fps = 60


def main():
    
    run = True
    clock = pygame.time.Clock()
    board = Board

    while run:
        clock.tick(fps)

        for event  in pygame.event.get():
            if event.type == pygame.quit:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_squares(WIN)
        pygame.display.update()
    pygame.quit()