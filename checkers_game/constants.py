import pygame
#Spēles dēļa platums un augstums
WIDTH = 800
HEIGHT = 800

#Skaits cik rindas un kolonnas ir uz spēles dēļa
ROWS = 8
COLUMNS = 8

#viena kuba lielums uz spēles dēļa
SQUARE_SIZE = (WIDTH//COLUMNS)

#Krāsas
GREY = (128,128,128)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)


#Importējam kroni karalienēm
CROWN = pygame.transform.scale(pygame.image.load("checkers_game/assets/izzy.png"),(90,50))

