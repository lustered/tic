#!/usr/bin/env python3
from pandas import DataFrame
from time import sleep

class game:
    def board(self):
        self.board = [['|__|' for _ in range(3)] for x in range(3)]

    def update(self):
        print(DataFrame(self.board))

# TODO:        handle input with previous move 
        # try:
        player_move = str(input('where do you wanna play '))
        #     if 

        # self.moves_log.append(player_move)
        row = player_move[1:]
        col = player_move[:1]
        self.board[int(row)][int(col)] = 'O'


if __name__ == '__main__':
    b = game()
    b.board()
    while True:
        b.update()
