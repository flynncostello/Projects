from player import Player
import os

folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

"""
In test_player.py there is no need to test if an input is invalid for the move class function
as this has already been done in test_game.py when the game_move function is called
wherein it automatically checks that the input is valid.
"""

def test_game():
    test_player = Player(1, 3)

    # Positive - Normal conditions of player instance including both instances and class methods. 
    assert test_player.row == 1, "FAILED - Positive Test Case 1 - Player"
    print("PASSED - Positive Test Case 1 - Player - Row attribute works")

    assert test_player.col == 3, "FAILED - Positive Test Case 2 - Player"
    print("PASSED - Positive Test Case 2 - Player - Column attribute works")

    test_player.move("s")
    assert test_player.row == 2, "FAILED - Positive Test Case 3 - Player"
    print("PASSED - Positive Test Case 3 - Player - Move method works")


def run_tests():
    test_game()

