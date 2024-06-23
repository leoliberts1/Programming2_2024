import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import socket
import threading
import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.game import Game
import pickle

HOST = '127.0.0.1'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

clients = []
games = {}

def get_game_state(game):
    return {
        'board': game.board,
        'turn': game.turn,
        'selected': game.selected,
        'valid_moves': game.valid_moves
    }

def handle_client(conn, player):
    game = games[player]
    conn.send(pickle.dumps(get_game_state(game)))
    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break
            game_state = pickle.loads(data)
            game.board = game_state['board']
            game.turn = game_state['turn']
            game.selected = game_state['selected']
            game.valid_moves = game_state['valid_moves']
            for client in clients:
                if client != conn:
                    client.sendall(pickle.dumps(get_game_state(game)))
        except:
            break
    conn.close()

def main():
    print("Server started, waiting for players to connect...")
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(win)
    threading.Thread(target=accept_connections, args=(game,)).start()

def accept_connections(game):
    while True:
        conn, addr = server.accept()
        print(f"Player {len(clients) + 1} has connected")
        clients.append(conn)
        games[len(clients)] = game
        threading.Thread(target=handle_client, args=(conn, len(clients))).start()

if __name__ == "__main__":
    main()
