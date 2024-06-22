import pickle, socket, pygame,time
from checkers_game.spēle import Spēle
from checkers_game.constants import WIDTH,HEIGHT,COLUMNS,ROWS,SQUARE_SIZE,RED,WHITE,BLUE,BLACK
server = socket.socket()

HOST = ""
PORT = 8000

server.bind((HOST,PORT))

server.listen(1)

conn1,addr1 = server.accept()
conn1.send(pickle.dumps("Welcome to the server player 1",-1))
print("player 1 has connected")
conn2,addr2 = server.accept()
conn2.send(pickle.dumps("Welcome to the server player 2",-1))
print("player 2 has connected")


#galvenā funkcija kas rūpēsies lai tiktu piefiksēta katra spēlētāju
#izdarība, lai spēli vispār varētu spēlēt, tā atjaunos skatlogu utml.
def main():
    #fps = 60
    run = True
    #clock = pygame.time.Clock()
    game = Spēle(":)")
    #kauliņš = Spēles_galds.dabūt_kauliņu(0,1)
    #Spēles_galds.kustēties(kauliņš,3,4)
    #"event loop" īstā funkcija kas strādās
    while True :
        if game.get_winner() != None:
            print(game.get_winner())
            break
        #we get the game table that will be sent to both clients
        game_table = game.game_table.game_table
        print(game_table)
        '''[[0, (255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255)],
            [(255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255), 0],
            [0, (255, 255, 255), 0, 0, 0, (255, 255, 255), 0, (255, 255, 255)],
                            [0, 0, (255, 255, 255), 0, 0, 0, 0, 0],
                            [0, 0, 0, (255, 0, 0), 0, 0, 0, 0],
                    [(255, 0, 0), 0, 0, 0, (255, 0, 0), 0, (255, 0, 0), 0],
                [0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0)],
               [(255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0]]
               This is how the table will approximately look'''
        possible_moves = game.possible_moves
        print(possible_moves)
        if game.turn == RED:
            conn1.send(pickle.dumps("Your turn",-1))
            conn1.send(pickle.dumps(game_table,-1))
            time.sleep(0.1)
            conn1.send(pickle.dumps(possible_moves, -1))
            conn2.send(pickle.dumps(game_table, -1))
            made_move = False
            while made_move == False:
                #Here I get the position of whatever the client has selected
                row,column  = pickle.loads(conn1.recv(1024))
                game.select(row,column)
            conn1.send(pickle.dumps("Not your turn",-1))
        else:
            conn2.send(pickle.dumps("Your turn",-1))
            conn1.send(pickle.dumps(game_table, -1))
            conn2.send(pickle.dumps(game_table, -1))


        #game.update()

        #extra lietas ne no video
        #SKATLOGS.fill(BALTA)
        #pygame.display.flip()

    pygame.quit()
main()