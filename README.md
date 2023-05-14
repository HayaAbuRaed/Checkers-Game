# Checkers Game with Minimax Algorithm
This is a Checkers game programmed in Python, with the implementation of the Minimax Algorithm. The game is built with Pygame library to provide a graphical user interface (GUI) that enhances the user experience.
<br/><br/>

<p align="center">
  <img src="https://github.com/HayaAbuRaed/Checkers-Game/assets/123592435/a1c3da71-b563-4f3a-826f-484f8d0369e2" alt="example image" width="500">
</p>
<br/><br/>

## ⚡ About the Game
Checkers, also known as Draughts, is a two-player board game played on a standard 8x8 checkered game board. The objective of the game is to capture all of your opponent's pieces or to block them so they cannot make any more moves.

Each player starts the game with 12 pieces, which are placed on the dark squares of the first three rows on opposite sides of the board. The pieces move diagonally forward, one square at a time, unless a capturing move is available.

In Checkers, there are two types of moves: non-capturing moves and capturing moves. A non-capturing move is simply moving a piece one square diagonally forward to an adjacent empty square. A capturing move involves jumping over an opponent's piece to capture it. A player must make a capturing move if one is available.

  ### Valid moves:

• Non-capturing move: A piece moves one square diagonally forward to an adjacent empty square.

• Capturing move: A piece jumps over an opponent's piece to capture it and lands on an empty square. The jump can be in any diagonal direction as long as there is an opponent's piece to be captured and an empty square to land on after the capture.

• Double capture move: If a capturing move results in the player's piece landing in a position to make another capture, then the player must continue to make capturing moves until they can no longer do so.

• Kinging: If a piece reaches the last row of the opponent's side of the board, it is promoted to a king. A king can move diagonally forward or backward and can make capturing moves in both directions.

• Forced capturing move: If a player has multiple capturing moves available, they must choose the move that captures the most pieces.
<br/><br/>

## 📄 Installation
To install the game on your system, follow these steps:

Clone the repository to your local machine using git clone https://github.com/HayaAbuRaed/Checkers-Game.git
Navigate to the cloned repository using the command cd checkers-minimax
Install the dependencies required for the project using the command pip install (pip install pygame)
<br/><br/>

## 🚀 Usage
To start the game, navigate to the cloned repository on your local machine and run the main.py file using the command python main.py. You can play the game against the computer and enjoy the optimized gameplay experience with Pygame graphics.
<br/><br/>

## 🎮 Gameplay
The game is played according to standard Checkers rules. The player can move their pieces diagonally and capture the opponent's pieces by jumping over them. The game continues until one player has no pieces left on the board or is unable to make a move. The Minimax Algorithm is used to provide an optimized gameplay experience, which makes the game challenging and fun to play.
<br/><br/>
