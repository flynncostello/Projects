import cells

"""
The only worthwhile test within cells.py is testing the display attribute of each class.
The step function has already been tested within the positive test cases in test_game.py
as each of these cases call the cells step method. Furthermore, within the teleport class
there is little point in testing the allowable input numbers because this is tested within 
the parse function.
"""

def test_game():
    test_start = cells.Start()
    test_end = cells.End()
    test_air = cells.Air()
    test_water = cells.Water()
    test_fire = cells.Fire()
    test_teleport = cells.Teleport('1')

    # Positive - Normal conditions of game instance game_move method
    assert test_start.display == "X", "FAILED - Positive Test Case 1 - Cells"
    print("PASSED - Positive Test Case 1 - Cells - Display works")

    assert test_end.display == "Y", "FAILED - Positive Test Case 2 - Cells"
    print("PASSED - Positive Test Case 2 - Cells - Display works")

    assert test_air.display == " ", "FAILED - Positive Test Case 3 - Cells"
    print("PASSED - Positive Test Case 3 - Cells - Display works")

    assert test_water.display == "W", "FAILED - Positive Test Case 4 - Cells"
    print("PASSED - Positive Test Case 4 - Cells - Display works")

    assert test_fire.display == "F", "FAILED - Positive Test Case 5 - Cells"
    print("PASSED - Positive Test Case 5 - Cells - Display works")

    assert test_teleport.display == "1", "FAILED - Positive Test Case 6 - Cells"
    print("PASSED - Positive Test Case 6 - Cells - Display works")


def run_tests():
    test_game()

