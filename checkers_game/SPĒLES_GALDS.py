import pygame
from .constants import BLACK,ROWS,COLUMNS,RED,SQUARE_SIZE,WHITE
from .Kauliņi import Kauliņš
#fails kurā tiks radīts spēles laukums
class SPĒLES_GALDS:
    def __init__(self):
        self.game_table = []
        self.turn = 0
        self.red_left = self.white_left = 12
        self.red_queens = self.white_queens = 0
        self.create_the_game_table()
    def draw_the_game_table(self,game_window):
        game_window.fill(BLACK)
        for rinda in range(ROWS):
            for kolonna in range(rinda%2, COLUMNS,2):
                #pirmās divas vietas iekavās nosaka pozīciju kur kubs tiks krāsots
                pygame.draw.rect(game_window,RED,(SQUARE_SIZE*rinda,SQUARE_SIZE*kolonna,SQUARE_SIZE,SQUARE_SIZE))
    def create_the_game_table(self):
        for rinda in range(ROWS):
            self.game_table.append([])
            for kolonna in range(COLUMNS):
                # ja pašreizējā kolonna kur esam
                #ir vienāda ar (rinda+1) %2
                if kolonna % 2 == ((rinda+1)%2):
                    if rinda <3:
                        kauls = Kauliņš(rinda,kolonna,WHITE)
                        self.game_table[rinda].append(kauls)
                        kauls.calculate_position()
                    elif rinda > 4 :
                        kauls = Kauliņš(rinda,kolonna,RED)
                        self.game_table[rinda].append(kauls)
                        kauls.calculate_position()
                    else: self.game_table[rinda].append(0)
                else: self.game_table[rinda].append(0)
    def draw(self,game_window):
        self.draw_the_game_table(game_window)
        for rinda in range(ROWS):
            for kolonna in range(COLUMNS):
                kauliņš = self.game_table[rinda][kolonna]
                if kauliņš != 0:
                    #kauliņš.aprēķināt_pozīciju()
                    kauliņš.draw_the_piece(game_window)
    def moove(self,kauliņš,row,column):
        #vecais ir tas kas pārvietojas uz jaunā vietu
        vecais = self.game_table[kauliņš.row][kauliņš.column]
        jaunais = self.game_table[row][column]

        self.game_table[row][column] = vecais
        self.game_table[kauliņš.row][kauliņš.column] = jaunais
        kauliņš.mooving(row,column)
        #Šī komanda darbosies tikai uz kauliņiem kas iekustēsies uz pēdējām rindām
        #derētu vēlāk pataisīt drošāku, lai kauliņi kaujot uz atpakaļu nevar iekaut savā teritorijā un kļūt par karalienēm
        if row == ROWS or row == 0:
            if kauliņš.krāsa == WHITE:
                self.white_queens +=1
            else:
                self.red_queens +=1
    def get_piece(self,row,column):
        return self.game_table[row][column]





