import pygame
from checkers.constants import WIDTH,HEIGHT
from checkers.board import Board, BLACK
print(BLACK)
print(WIDTH)
pygame.init()
WIN =pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Checkers')




def main():

    fps = 60
    run = True
    #pygame.init()
    clock = pygame.time.Clock()
    board = Board()
    
    while run:
        clock.tick(fps)

        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw(WIN) 
        pygame.display.update()
    pygame.quit()

main()