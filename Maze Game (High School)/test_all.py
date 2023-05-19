"""
A simple program that will import my tests and run them all!
"""

#import subprocess
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_cells import run_tests as test_cells
from test_player import run_tests as test_player

print("#########################")
print("## Running unit tests! ##")
print("#########################\n")

print("Game.py tests:")
test_game()
print("\n")

print("Grid.py tests:")
test_grid()
print("\n")

print("Game_parser.py tests:")
test_parser()
print("\n")

print("Cells.py tests:")
test_cells()
print("\n")

print("Player.py tests:")
test_player()
print("\n")