from game_parser import read_lines 
from grid import grid_to_string
from player import Player
import sys

def create_leaderboard(leaderboard_list, difficulty):
    leaderboard_string = f"""
=========================================================================
        Burning Building - Leaderboard (Time to escape building {difficulty})                                                     
    
"""
    # Sorting leaderboard_list - bubble sort
    if len(leaderboard_list) > 1:
        for loop in range(len(leaderboard_list)): # Needs to loop length - 1 times to complete sort
            i = 0
            while i < len(leaderboard_list)-1: # One complete sort (need to do length - 1 sorts)
                temp = leaderboard_list[i]
                if leaderboard_list[i][1] > leaderboard_list[i+1][1]:
                    leaderboard_list[i] = leaderboard_list[i+1]
                    leaderboard_list[i+1] = temp
                i += 1

    i = 0
    while i < len(leaderboard_list): # Adding scores to leaderboard string
        name = leaderboard_list[i][0]
        score = leaderboard_list[i][1]
        if score == 1:
            new_score_string = f"   {i+1}) {name} - {score} seconds\n"
        else:
            new_score_string = f"   {i+1}) {name} - {score} seconds\n"
        leaderboard_string += new_score_string
        i += 1

    leaderboard_string += "\n========================================================================="

    return leaderboard_string




class Game:
    def __init__(self, filename):
        self.list_of_cells = read_lines(filename) # list_of_cells = list of list of cells [[Air, Fire], [...], [...]]
        
        self.positions = [] # [[start pos], [end pos]]
        self.teleport_pos = [] # [["1", 3, 4], ["1", 1, 2]]
        i = 0
        while i < len(self.list_of_cells):
            i2 = 0
            while i2 < len(self.list_of_cells[i]):
                if self.list_of_cells[i][i2].display == "X" or self.list_of_cells[i][i2].display == "Y":
                    self.positions.append([i, i2])
                else:
                    tel_ls = list("123456789")
                    for num in tel_ls:
                        if num == self.list_of_cells[i][i2].display:
                            self.teleport_pos.append([num, i, i2]) # i = row, i2 = col
                i2 += 1
            i += 1
        pos_0_0 = self.positions[0][0]
        pos_0_1 = self.positions[0][1]

        self.player = Player(pos_0_0, pos_0_1) # player starts with acorns original pos

        self.play_again = True # when play_again = False player has reached Y
        self.won = True # If player dies won = False
        self.moves = [] # Only valid moves recorded
        self.old_pos = [] # Used for wall cell to return player to previous cell



    def game_move(self, move):
        self.old_pos.clear()
        self.old_pos.append(self.player.row)
        self.old_pos.append(self.player.col)

        self.player.move(move) # changes players position to new cell

        new_cell = self.list_of_cells[self.player.row][self.player.col] # new cell player is on
        
        step = new_cell.step(self, move) # can use all self instance variables above
        if step[0]:
            return step[1]
        return False

