import pygame
#from checkers_game.constants import PLATUMS,AUGSTUMS
from checkers_game.constants import WIDTH,HEIGHT,COLUMNS,ROWS,SQUARE_SIZE,RED,WHITE,BLUE,BLACK
from checkers_game.SPĒLES_GALDS import SPĒLES_GALDS
from checkers_game.spēle import Spēle
#No sākuma uztaisīsim pygame skatlogu
#tad sākšu taisīt kā vispār spēli varēs spēlēt
pygame.init()
GAME_WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CHECKERS")

def get_row_and_column_from_the_player(position):
    x,y = position
    row = y // SQUARE_SIZE
    column = x // SQUARE_SIZE
    return row,column
#galvenā funkcija kas rūpēsies lai tiktu piefiksēta katra spēlētāju
#izdarība, lai spēli vispār varētu spēlēt, tā atjaunos skatlogu utml.
def main():
    fps = 60
    run = True
    clock = pygame.time.Clock()

    game = Spēle(GAME_WINDOW)
    #kauliņš = Spēles_galds.dabūt_kauliņu(0,1)
    #Spēles_galds.kustēties(kauliņš,3,4)
    #"event loop" īstā funkcija kas strādās
    while run :
        clock.tick(fps)

        for action_of_the_player in pygame.event.get():
            if action_of_the_player.type == pygame.QUIT:
                run = False
            if action_of_the_player.type == pygame.MOUSEBUTTONDOWN:
                #šeit notiks pārbaude tam ko cilvēks ir izdarījis
                #skatīsies vai šamējais ir kko pabīdījis,
                # vai vēl kko izdarījis.
                position = pygame.mouse.get_pos()
                rinda,kolonna = get_row_and_column_from_the_player(position)

        game.update()

        #extra lietas ne no video
        #SKATLOGS.fill(BALTA)
        #pygame.display.flip()

    pygame.quit()
main()