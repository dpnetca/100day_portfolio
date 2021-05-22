#!/user/bin/env python
"""
Simple text based Tic Tac Toe game
Developed by Denis Pointer (https://www.dpnet.ca)
"""
import os

from art import logo
from tictactoe import TicTacToe


def clear_screen():
    """issue clear screen command, "clear" for linux/mac "cls" for windows"""
    os.system("cls" if os.name == "nt" else "clear")


game = TicTacToe()

game_on = True
while game_on:
    while not game.is_winner():
        clear_screen()
        print(logo)
        game.draw_board()
        game.player_selection()

    winner = game.is_winner()

    if winner == "DRAW":
        print("It's a Draw")
    else:
        print(f"The Winner is {winner}")

    valid_input = False
    while not valid_input:
        again = input("play again (y/n): ").lower()
        if again in ["y", "n"]:
            valid_input = True
        else:
            print("Invalid option")

    if again == "n":
        print("Thank you for playing Tic Tac Toe")
        game_on = False
    else:
        game.set_board()
        game.players_turn = winner
