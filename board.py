#!/usr/bin/env python3
from pandas import DataFrame
from time import sleep
class game:
    def board(self):
        self.board = [['+']*3] * 3

    def update(self):
        winner = '' 
        print(DataFrame(self.board))
        player_move = str(input('where do you wanna play '))


if __name__ == '__main__':
    while True:
        b = game()
        b.board()
        b.update()
