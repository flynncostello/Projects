### Game 2 Unit Tests ###
import os 
folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)
from game2_classes import *


# check_stats (Function)
test_Kingdom = KingdomStats()

def check_stats_test():
    test1_result = test_Kingdom.check_stats()
    assert test1_result == [True], "Test 1 FAILED - check_stats function doesn't work"
    print("Test 1 PASSED - check_stats function works")

    test_Kingdom.wealth_stat = -1
    test2_result = test_Kingdom.check_stats()
    assert test2_result == [False, 'w'], "Test 2 FAILED - check_stats function doesn't work"
    print("Test 2 PASSED - check_stats function works")


# create_leaderboard (Function)
test_leaderboard_list = [['Flynn', 10], ['Dave', 20], ['Sam', 30]]
expected_output = """
==========================================
        Kingdom Rule - Leaderboard                                              
    
   1) Sam - 30 years in power
   2) Dave - 20 years in power
   3) Flynn - 10 years in power

=========================================="""

def create_leaderboard_test():
    actual_output = create_leaderboard(test_leaderboard_list)
    assert expected_output == actual_output, "Test 3 FAILED - create_leaderboard function doesn't work"
    print("Test 3 PASSED - create_leaderboard function works")


# pick_event (Function)
years_ruling = 10
events_which_have_occured = []
expected_output_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def pick_event_test():
    actual_output1 = pick_event(years_ruling, events_which_have_occured)
    actual_output2 = pick_event(years_ruling, events_which_have_occured)
    actual_output3 = pick_event(years_ruling, events_which_have_occured)
    actual_output4 = pick_event(years_ruling, events_which_have_occured)
    actual_output5 = pick_event(years_ruling, events_which_have_occured)
    assert actual_output1 in expected_output_options, "Test 4 FAILED - pick_event function doesn't work"
    print("Test 4 PASSED - pick_event function works")
    assert actual_output2 in expected_output_options, "Test 5 FAILED - pick_event function doesn't work"
    print("Test 5 PASSED - pick_event function works")
    assert actual_output3 in expected_output_options, "Test 6 FAILED - pick_event function doesn't work"
    print("Test 6 PASSED - pick_event function works")
    assert actual_output4 in expected_output_options, "Test 7 FAILED - pick_event function doesn't work"
    print("Test 7 PASSED - pick_event function works")
    assert actual_output5 in expected_output_options, "Test 8 FAILED - pick_event function doesn't work"
    print("Test 8 PASSED - pick_event function works")


### Running all tests ###
print("\n#########################")
print("## Running unit tests! ##")
print("#########################\n")

print("Check_stats function tests:")
check_stats_test()
print()

print("Create_leaderboard function tests:")
create_leaderboard_test()
print()

print("Pick_event function tests:")
pick_event_test()
print()