import os

folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

from game import Game

file1 = "board_simple.txt"

def test_game():
    test_game = Game(file1)

    # Positive - Normal conditions of game instance game_move method
    assert test_game.game_move("a") != True, "FAILED - Positive Test Case 1 - Game"
    print("PASSED - Positive Test Case 1 - Game - game_move works")

    assert test_game.game_move("d") != True, "FAILED - Positive Test Case 2 - Game"
    print("PASSED - Positive Test Case 2 - Game - game_move works")


    # Negative - Tests the controlling of invalid inputs e.g. inputing a number
    assert test_game.game_move("1") == False, "FAILED - Negative Test Case 1 - Game"
    print("PASSED - Negative Test Case 1 - Game - invalid input handled")

    assert test_game.game_move("abc") == False, "FAILED - Negative Test Case 2 - Game"
    print("PASSED - Negative Test Case 2 - Game - invalid input handled")


    # Edge - Ambiguous result of inputing an empty string / empty list 
    assert test_game.game_move("") == False, "FAILED - Edge Test Case 1 - Game"
    print("PASSED - Edge Test Case 1 - Game - invalid input handled")

    assert test_game.game_move([]) == False, "FAILED - Edge Test Case 2 - Game"
    print("PASSED - Edge Test Case 2 - Game - invalid input handled")


def run_tests():
    test_game()

