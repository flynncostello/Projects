import sys
from game_strings import *

class Player:
    def __init__(self, row, col):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = row
        self.col = col

    def move(self, move):

        if move == "w":
            self.row -= 1
            
        elif move == "s":
            self.row += 1

        elif move == "a":
            self.col -= 1
        
        elif move == "d":
            self.col += 1
    
        elif move == "k":
            print("----------------------------------------------------------------------------------------------------------------------------")
            print(input_keys) 
        
        elif move == "m":
            print("----------------------------------------------------------------------------------------------------------------------------")
            print(map_symbols)

        elif move == "q":
            print("----------------------------------------------------------------------------------------------------------------------------")
            print("\nNow exiting game... Thanks for playing!\n")
            sys.exit(1)
