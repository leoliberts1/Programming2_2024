import pickle, socket, pygame,time, copy
from checkers_game.spēle import Spēle
from checkers_game.constants import WIDTH,HEIGHT,COLUMNS,ROWS,SQUARE_SIZE,RED,WHITE,BLUE,BLACK
from checkers_game.Kauliņi import Kauliņš
server = socket.socket()

HOST = ""
PORT = 8000
try:
    server.bind((HOST,PORT))
except OSError as e:
    print(e)
    HOST = ""
    PORT = 8080
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
        previous_game_table = copy.deepcopy(game_table)
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
        print("game turn = ", game.turn)
        if game.turn == RED:
            conn1.send(pickle.dumps("Your turn",-1))
            conn1.send(pickle.dumps(game_table,-1))
            time.sleep(0.1)
            conn1.send(pickle.dumps(possible_moves, -1))
            conn2.send(pickle.dumps(game_table, -1))
            made_move = False
            #conn2.send(pickle.dumps("Not your turn", -1))
            while made_move == False:
                #Here I get the position of whatever the client has selected
                row,column  = pickle.loads(conn1.recv(1024))
                print(row,column)
                game.select(row,column)
                print([game.game_table.game_table,game.possible_moves],"This is the game table and the possible moves table before sending it again after something was selected")

                possible_moves = game.possible_moves
                conn1.send(pickle.dumps([game_table,possible_moves],-1))
                print(Kauliņš.old_changes,"old changes count")
                print(Kauliņš.changes,"new count changes")
                if Kauliņš.changes != Kauliņš.old_changes:
                    made_move = True
                    print(conn1,"Has ended their turn")
                    conn1.send(pickle.dumps("Not your move",-1))
                    #conn1.send(pickle.dumps(game.game_table.game_table,-1))
                    Kauliņš.old_changes +=1
        else:
            conn2.send(pickle.dumps("Your turn", -1))
            conn2.send(pickle.dumps(game_table, -1))
            time.sleep(0.1)
            conn2.send(pickle.dumps(possible_moves, -1))
            conn1.send(pickle.dumps(game_table, -1))
            made_move = False
            # conn2.send(pickle.dumps("Not your turn", -1))
            while made_move == False:
                # Here I get the position of whatever the client has selected
                row, column = pickle.loads(conn2.recv(1024))
                print(row, column)
                game.select(row, column)
                print([game.game_table.game_table, game.possible_moves],
                      "This is the game table and the possible moves table before sending it again after something was selected")
                game_table = game.game_table.game_table
                possible_moves = game.possible_moves
                conn2.send(pickle.dumps([game_table, possible_moves], -1))
                if Kauliņš.changes == Kauliņš.old_changes:
                    made_move = True
                    print(conn2, "Has ended their turn")
                    conn2.send(pickle.dumps("Not your move", -1))
                    conn2.send(pickle.dumps(game.game_table.game_table, -1))
                    Kauliņš.old_changes += 1


        #game.update()

        #extra lietas ne no video
        #SKATLOGS.fill(BALTA)
        #pygame.display.flip()

    #pygame.quit()
main()