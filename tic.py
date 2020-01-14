#!/usr/bin/env python3
from time import sleep
from pandas import DataFrame
import numpy as np
from termcolor import colored
import os 
import sys


class Game:
    def build_board(self,pref_winner):
        # pref_winner is a default winner that will be passed when building the board
        self.pref_winner = pref_winner
        self.board = [['O' for _ in range(3)] for i in range(3)]
        # fill main diagonal with X and wins
        self.board[0][0], self.board[1][1], self.board[2][2] = pref_winner,pref_winner,pref_winner
        # this pattern makes the game a draw
        # self.board[0][0], self.board[1][1], self.board[2][1],self.board[1][2] = 'X','X','X','X'


    def merge_patterns(self,arr1,arr2,length,optional_arr):
            ret = []
            ret.append(arr1)
            ret.append(arr2)
            if length > 2: ret.append(optional_arr) 

            return ret


    def check_patters(self):
        # horizontals 
        hor1,hor2,hor3 = [],[],[]
        self.horizontals = []
        for i in range(len(self.board)):
            hor1.append(self.board[0][i])
            hor2.append(self.board[1][i])
            hor3.append(self.board[2][i])

        # vericals 
        vert1,vert2,vert3 = [],[],[]
        self.verticals = []
        for i in range(len(self.board)):
            vert1.append(self.board[i][0])
            vert2.append(self.board[i][1])
            vert3.append(self.board[i][2])

        # diagonals
        diag1,diag2 = [],[]
        self.diagonals = []
        for i in range(len(self.board)):
            diag1.append(self.board[i][i])
            diag2.append(self.board[len(self.board)-i-1][i])



        self.all_patterns = []
        self.all_patterns.append(self.merge_patterns(hor1,hor2,3,hor3))
        self.all_patterns.append(self.merge_patterns(diag1,diag2,3,[]))
        self.all_patterns.append(self.merge_patterns(vert1,vert2,3,vert3))


        
    def check_winner(self):
            self.winner = ''
            self.game_on = True

            for i in range(len(self.all_patterns)):
                for j in range(len(self.all_patterns)):
                    if len(set(self.all_patterns[i][j])) < 2 and len(set(self.all_patterns[i][j])) > 0:
                        self.winner = self.all_patterns[i][j][0] 
                        self.game_on = False
                        break
                

    
    def display(self):
        # while the game is still running 
            while self.game_on:
                os.system('clear')
                print(colored(DataFrame(self.board),'yellow'))
                sleep(.1) 


            if not self.game_on:
                print('*' * 16)
                print(colored(DataFrame(self.board),'green'))
                print('*' * 16)
                print(colored('%s WINS!' % (self.winner),'green'))



if __name__ == '__main__':
    game = Game() 
    game.build_board(sys.argv[1])
    game.check_patters()
    game.check_winner()
    game.display()

