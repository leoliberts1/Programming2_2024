import pygame
import socket
import pickle
import threading
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from client_functions import ClientFunctions

HOST = '127.0.0.1'
PORT = 65432

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Game')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client_functions = ClientFunctions(WIN, client)

def receive_data():
    while True:
        data = client.recv(4096)
        if data:
            game = pickle.loads(data)
            client_functions.set_game(game)
        pygame.display.update()

threading.Thread(target=receive_data, daemon=True).start()

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
                client_functions.select(row, col)
        client_functions.update()
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
