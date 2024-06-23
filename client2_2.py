import socket, pygame, pickle,time
from checkers_game.constants import WIDTH, HEIGHT, SQUARE_SIZE
from client_functions import client_functions

question = input("Would you like to play checkers?")
while question.lower() == "yes":
    s = socket.socket()
    HOST = "localhost"
    PORT = 8080
    s.connect((HOST, PORT))
    welcome_message = pickle.loads(s.recv(2048))
    print(welcome_message, "this is the welcome message")
    pygame.init()
    # both of the clients get their "own" display
    GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CHECKERS_C_2")
    functions = client_functions()
    while True:
        message = pickle.loads(s.recv(2048))
        print(message)
        if message == "Your turn":
            game_board = pickle.loads(s.recv(2048))
            functions.draw(GAME_WINDOW, game_board, {})
            while True:
                possible_moves = pickle.loads(s.recv(2048))
                if possible_moves == "END":
                    break
                game_board = pickle.loads(s.recv(2048))
                print(game_board, possible_moves, "game board and possible moves")
                functions.draw(GAME_WINDOW, game_board, possible_moves)
                Notselected = True
                while Notselected:
                    for action_of_the_player in pygame.event.get():
                        if action_of_the_player.type == pygame.QUIT:
                            YES = False
                        if action_of_the_player.type == pygame.MOUSEBUTTONDOWN:
                            position = pygame.mouse.get_pos()
                            Notselected = False
                rinda, kolonna = functions.get_row_and_column_from_the_player(position)
                time.sleep(0.05)
                print(rinda, kolonna)
                s.send(pickle.dumps((rinda, kolonna), -1))

        else:
            game_board = pickle.loads(s.recv(2048))
            functions.draw(GAME_WINDOW, game_board, {})
            # make code where it displays the thing the server sends and waits again