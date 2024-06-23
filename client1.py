import socket, pygame,pickle
from checkers_game.constants import WIDTH,HEIGHT,SQUARE_SIZE
from client_functions import client_functions
question = input("Would you like to play checkers?")
if question.lower() == "yes":
    YES = True
    s = socket.socket()
    HOST = "localhost"
    PORT = 8000
    s.connect((HOST, PORT))
    welcome_message = pickle.loads(s.recv(2048))
    print(welcome_message)
    pygame.init()
    # both of the clients get their "own" display
    GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CHECKERS")
    functions = client_functions()
else:
    YES = False
while YES:
    #question = input("Would you like to play checkers?")
    #Here I get the data from the server about the state of the game table
    message = pickle.loads(s.recv(2048))
    if message == "Your turn":
        print("My turn")
        game_table = pickle.loads(s.recv(2048))
        print(game_table)
        possible_moves = pickle.loads(s.recv(2048))
        print(possible_moves)
        your_turn = True
        functions.draw(GAME_WINDOW,game_table,possible_moves)

    else:
        game_table = message
        your_turn = False
    while your_turn:
        for action_of_the_player in pygame.event.get():
            if action_of_the_player.type == pygame.QUIT:
                YES = False
            if action_of_the_player.type == pygame.MOUSEBUTTONDOWN:
            # šeit notiks pārbaude tam ko cilvēks ir izdarījis
            # skatīsies vai šamējais ir kko pabīdījis,
            # vai vēl kko izdarījis.
                position = pygame.mouse.get_pos()
                #print("šī ir tā nolādētā pozīcija", (position))
                rinda, kolonna = functions.get_row_and_column_from_the_player(position)
                #print(position)
                print(rinda, kolonna,"This is the row and collumn the player has selected")
                #we send the position back to the server
                s.send(pickle.dumps((rinda, kolonna), -1))
                #Now we recieve the new board and the possible moves
                response = pickle.loads(s.recv(16384))
                print(response,"this is the response of the new table after the client has sent the position")
                # "Not your turn this is the response of the new table after the client has sent the position"
                #atbilde?
                game_table = response[0]
                possible_moves = response[1]
                functions.draw(GAME_WINDOW, game_table,possible_moves)

            #game.select(rinda, kolonna)
            #jāaizsūta ko džeks ir izvēlējies



