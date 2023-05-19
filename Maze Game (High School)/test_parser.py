from game_parser import parse
import os

folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

filename = "board_simple.txt"

def test_parse(): # FIX!!!
    board_simple = ['**X**\n', '*   *\n', '**Y**\n']
    negative_board_1 = ['**X**\n', '*X  *\n', '**Y**\n']
    negative_board_2 = ['**X*Y\n', '*   *\n', '**Y**\n']
    negative_board_3 = ['**X*1\n', '*   *\n', '**Y**\n']
    negative_board_4 = ['Z*X**\n', '*   *\n', '**Y**\n']

    # Positive case - Parse function under normal circumstances. First four positive test cases 
    # determines if the display attribute of each cell is working as intended.
    assert parse(board_simple)[0][0].display == "*", "FAILED - Positive Test Case 1 - parser"
    print("PASSED - Positive Test Case 1 - parser - Wall diplay attribute works")

    assert parse(board_simple)[0][2].display == "X", "FAILED - Positive Test Case 2 - parser"
    print("PASSED - Positive Test Case 2 - parser - Start diplay attribute works")

    assert parse(board_simple)[1][1].display == " ", "FAILED - Positive Test Case 3 - parser"
    print("PASSED - Positive Test Case 3 - parser - Air diplay attribute works")

    assert parse(board_simple)[2][2].display == "Y", "FAILED - Positive Test Case 4 - parser"
    print("PASSED - Positive Test Case 4 - parser - End diplay attribute works")

    # Negative cases
    # 1) Tests if error handling for more than 1 starting position works
    # 2) Tests if error handling for more than 1 ending position works
    # 3) Tests if error handling for teleport pads works (teleport pad does not have matching pad)
    # 4) Tests if error handling for bad letter in config works
    # (Throughout all of these if the Value error is caught )
    try:
        parse(negative_board_1)
        print("FAILED - Negative Test Case 1 - parser")
    except ValueError as ve1:
        assert str(ve1) == "Expected 1 starting position, got 2.", "FAILED - Negative Test Case 1 - parser"
        print(f"PASSED - Negative Test Case 1 - parser - Handled exception: {ve1}")
    
    try:
        parse(negative_board_2) 
        print("FAILED - Negative Test Case 2 - parser")
    except ValueError as ve2:
        assert str(ve2) == "Expected 1 ending position, got 2.", "FAILED - Negative Test Case 2 - parser"
        print(f"PASSED - Negative Test Case 2 - parser - Handled exception: {ve2}")
    
    try:
        parse(negative_board_3)        
        print("FAILED - Negative Test Case 3 - parser")
    except ValueError as ve3:
        assert str(ve3) == "Teleport pad 1 does not have an exclusively matching pad.", "FAILED - Negative Test Case 3 - parser"
        print(f"PASSED - Negative Test Case 3 - parser - Handled exception: {ve3}")

    try:
        parse(negative_board_4)        
        print("FAILED - Negative Test Case 3 - parser")
    except ValueError as ve4:
        assert str(ve4) == "Bad letter in configuration file: Z.", "FAILED - Negative Test Case 4 - parser"
        print(f"PASSED - Negative Test Case 4 - parser - Handled exception: {ve4}")

    
    # Edge case - Lack of specification surrounding giving empty string.
    try:
        parse("")
    except ValueError as ve5:
        assert str(ve5) == "Expected 1 starting position, got 0.", "FAILED - Edge Test Case 1 - parser"
        print(f"PASSED - Edge Test Case 1 - parser - Handled exception: {ve5}")
    # The reason behind this error being raised is because it is the first 
    # one  the program encounters.


def run_tests():
    test_parse()
