import pygame
from .constants import WIDTH,HEIGHT


WIN =pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Checkers")

fps = 60


def main():
    
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)
        pass