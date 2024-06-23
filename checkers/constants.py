import pygame
import os

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Loading crown image
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
CROWN = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, 'crown.png')), (44, 25))
