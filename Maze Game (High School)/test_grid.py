from grid import grid_to_string

# Extra imports
from player import Player
from game_parser import read_lines

import os

folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

file1 = "board_simple.txt"
file2 = "board_hard.txt"

list_of_list_of_cells1 = read_lines(file1)
list_of_list_of_cells2 = read_lines(file2)

player1 = Player(0, 2)
player2 = Player(0, 1)


def test_grid():
    grid1 = grid_to_string(list_of_list_of_cells1, player1)
    grid2 = grid_to_string(list_of_list_of_cells2, player2)


    # Positive case - Grid_to_string functioning under normal conditions 
    # with valid input of player and list of list of cells - tests that 
    # basic ascpects of function are working as intended
    assert grid1 == """**A****
*X * W*
*     *
* F   *
**Y****



You have 0 water buckets.""", "FAILED - Positive Test Case 1 - Grid_to_string"
    print("PASSED - Positive Test Case 1 - Grid_to_string - functions works with board_simple.txt")
    assert grid2 == """*A**************
*X      2 *W   *
*  *** ** **** *
*  *  W*   1   *
*  ***** ***** *
*   2 *   ****F*
*  ** ***  F   *
*  1********FF *
*************Y**








You have 0 water buckets.""", "FAILED - Positive Test Case 2 - Grid_to_string"
    print("PASSED - Positive Test Case 2 - Grid_to_string - function works with board_hard.txt")

def run_tests():
    test_grid()

