import pickle, socket, pygame,time, copy
from checkers_game.spēle import Spēle
from checkers_game.constants import WIDTH,HEIGHT,COLUMNS,ROWS,SQUARE_SIZE,RED,WHITE,BLUE,BLACK
from checkers_game.Kauliņi import Kauliņš
server = socket.socket()

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

def main():
    '''The first to connect will also get to make the first move'''
    game = Spēle(":)")
    game_table = game.game_table.game_table
    possible_moves = game.possible_moves
    while True:
        #get two seperate run plans
        #one for each of the players playing
        if game.get_winner() != None:
            print(game.get_winner())
            break
        if game.turn == RED:
            conn1.send(pickle.dumps("Your turn",-1))
            conn2.send(pickle.dumps("Not your turn",-1))
            #both get the clarifying message
            time.sleep(0.05)
            #then both of them recieve the current state of the table
            conn1.send(pickle.dumps(game.game_table.game_table,-1))
            conn2.send(pickle.dumps(game.game_table.game_table, -1))
            finished_turn = False
            time.sleep(0.05)
            #Here is the loop that only works with each player individually
            while finished_turn == False:
                conn1.send(pickle.dumps(game.possible_moves,-1))
                time.sleep(0.05)
                conn1.send(pickle.dumps(game_table,-1))
                row, column = pickle.loads(conn1.recv(1024))
                game.select(row,column)
                if Kauliņš.changes != Kauliņš.old_changes:
                    finished_turn = True
                    conn1.send(pickle.dumps("END",-1))
                    Kauliņš.old_changes +=1
        else :
            conn1.send(pickle.dumps("Not your turn",-1))
            conn2.send(pickle.dumps("Your turn",-1))
            # both get the clarifying message
            #then they both recieve the current state of the table
            conn1.send(pickle.dumps(game.game_table.game_table, -1))
            conn2.send(pickle.dumps(game.game_table.game_table, -1))
            finished_turn = False
            # Here is the loop that only works with each player individually
            while finished_turn == False:
                #conn2.send(pickle.dumps(possible_moves, -1))
                conn2.send(pickle.dumps(game.possible_moves, -1))
                conn2.send(pickle.dumps(game.game_table.game_table, -1))
                row, column = pickle.loads(conn2.recv(1024))
                game.select(row, column)
                if Kauliņš.changes != Kauliņš.old_changes:
                    finished_turn = True
                    conn2.send(pickle.dumps("END", -1))
                    Kauliņš.old_changes += 1
main()
