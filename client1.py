import sys
import os
import pygame
import socket
import pickle
import threading

# Import constants and functions
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from client_functions import ClientFunctions

# Server info
HOST = '127.0.0.1'
PORT = 65432

# Initialize pygame
pygame.init()

# get the display going
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Game')

# crate the socket and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# initialize the client
client_functions = ClientFunctions(WIN, client)


# Getting data from the server
def receive_data():
    while True:
        # Receive data
        data = client.recv(4096)
        if data:
            game_state = pickle.loads(data)
            client_functions.set_game_state(game_state)
        pygame.display.update()


# look, we are using threading :D
threading.Thread(target=receive_data, daemon=True).start()


# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        # set the fps
        clock.tick(60)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get the position
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
                #select the piece
                client_functions.select(row, col)

        # Update the client functions and the display
        client_functions.update()
        pygame.display.update()


# Run the main game loop if the script is executed directly
if __name__ == "__main__":
    main()
    pygame.quit()  # Quit pygame
