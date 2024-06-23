# Multiplayer Checkers Game

This is a simple multiplayer Checkers game built using Python and Pygame. The game supports two players who can play on separate clients while connected to a server.

## Project Structure

    checkers_game/
    ├── assets/
    │ ├── crown.png
    │ ├── init.py
    │ ├── board.py
    │ ├── constants.py
    │ ├── game.py
    │ └── piece.py
    ├── client1.py
    ├── client2.py
    ├── client_functions.py
    ├── main.py
    ├── server.py
    ├── README.md
    └── requirements.txt

markdown


## Getting Started

### Prerequisites

•⁠  ⁠Python 3.12
•⁠  ⁠Pygame 2.5.2

### Installation

1.⁠ ⁠Clone the repository:

    ⁠ bash
    git clone https://github.com/yourusername/multiplayer-checkers.git
    cd multiplayer-checkers
     ⁠

2.⁠ ⁠Install the required dependencies:

    ⁠ bash
    pip install -r requirements.txt
     ⁠

### Running the Game

1.⁠ ⁠Start the server:

    ⁠ bash
    python server.py
     ⁠

2.⁠ ⁠Start the first client:

    ⁠ bash
    python client1.py
     ⁠

3.⁠ ⁠Start the second client:

    ⁠ bash
    python client2.py
     ⁠

### How to Play

•⁠  ⁠When both clients are connected, the game will start automatically.
•⁠  ⁠Players take turns to make their moves by clicking on the pieces and moving them to valid positions.
•⁠  ⁠The game follows the standard Checkers rules.

## Acknowledgements

•⁠  ⁠This project uses [Pygame](https://www.pygame.org/), a cross-platform set of Python modules designed for writing video games.
