import socket, pygame,pickle
from checkers_game.constants import WIDTH,HEIGHT,SQUARE_SIZE
from client_functions import client_functions
question = input("Would you like to play checkers?")
if question.lower() == "yes":
    YES = True
    s = socket.socket()
    HOST = "localhost"
    PORT = 8000
    '''tr00
        s.connect((HOST, PORT))
    except ConnectionRefusedError as e:
        print(e)
        PORT = 8080
        s.connect((HOST, PORT))'''
    s.connect((HOST, PORT))
    welcome_message = pickle.loads(s.recv(2048))
    print(welcome_message, "this is the welcome message")
    pygame.init()
    # both of the clients get their "own" display
    GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CHECKERS_C_1")
    functions = client_functions()
else:
    YES = False
while YES:
    #question = input("Would you like to play checkers?")
    #Here I get the data from the server about the state of the game table
    print("tiekam pie jaunā game_table")
    game_table = pickle.loads(s.recv(2048))
    print(game_table)
    if game_table == "Your turn":
        print("In the 'your turn' if statment")
        #print("My turn")
        game_table = pickle.loads(s.recv(2048))
        #print(game_table)
        possible_moves = pickle.loads(s.recv(2048))
        #print(possible_moves)
        your_turn = True
        functions.draw(GAME_WINDOW,game_table,possible_moves)
        index = 0
    else:
        game_table = game_table
        if len(game_table) == 2:
            game_table = game_table[0]
        your_turn = False
        possible_moves = {}
        print("Not this clients move statment")
        functions.draw(GAME_WINDOW,game_table,possible_moves)
    while your_turn:
        for action_of_the_player in pygame.event.get():
            if action_of_the_player.type == pygame.QUIT:
                YES = False
            if action_of_the_player.type == pygame.MOUSEBUTTONDOWN:
                # šeit notiks pārbaude tam ko cilvēks ir izdarījis
                # skatīsies vai šamējais ir kko pabīdījis,
                # vai vēl kko izdarījis.
                '''Šeit dabūnam to kur cilvēks uzspiež un sūtam serverim
                pēctam iegūstam kāds ir jaunais spēles galds un tad atsākam
                gaidīt ko cilvēks izdarīs'''
                position = pygame.mouse.get_pos()
                #print("šī ir tā nolādētā pozīcija", (position))
                rinda, kolonna = functions.get_row_and_column_from_the_player(position)
                #print(position)
                print(rinda, kolonna,"This is the row and collumn the player has selected")
                #we send the position back to the server
                s.send(pickle.dumps((rinda, kolonna), -1))
                #Now we recieve the new board and the possible moves
                #After the first round here we recieve the new board
                response = pickle.loads(s.recv(16384))
                print(response,"this is the response of the new table after the client has sent the position")
                # "Not your turn this is the response of the new table after the client has sent the position"
                '''if response == "Not your move":
                    your_turn = False
                    I don't know why but this refused to work'''
                #atbilde?
                if len(response) ==2:
                    game_table = response[0]
                    possible_moves = response[1]
                else:
                    game_table = response
                    possible_moves = {}
                print(game_table, "šeit tlt vajadzētu būt problēmām ar iespējamajiem gājieniem")
                print(possible_moves,"Šeit vajadzētu būt problēmān ar iespējamajiem gājieniem")

                #print(possible_moves)
                if game_table == "N":
                    print("esam game_table = N vietā")
                    your_turn = False
                    #game_table = pickle.loads(s.recv(16384))
                    print(game_table,"this is the game table after recieving it, still in the client")
                    '''[[[0, (255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255)],
                     [(255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255), 0],
                      [0, (255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255), 0, (255, 255, 255)],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                         [(255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0],
                          [0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0)],
                           [(255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0]
                           ], {(4, 1): [], (4, 3): []}]'''
                    #game_table = game_table[0]
                    #print(game_table,"again the game table still in the client")
                    #possible_moves = {}
                    print("tagad jābeidzas")
                    #functions.draw(GAME_WINDOW, game_table, possible_moves)

                else:functions.draw(GAME_WINDOW, game_table,possible_moves)
    #šeit jāsaraksta ko darīs spēlētājs kamēr nav viņa gājiens
    #No sākuma vienkārši jādabūn laukums un tad jāgaida kamēr otrs paiet

            #game.select(rinda, kolonna)
            #jāaizsūta ko džeks ir izvēlējies



