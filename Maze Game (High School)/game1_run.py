from game import Game
from game import create_leaderboard
import sys
from grid import grid_to_string
from game_strings import *
import time
import os
from playsound import playsound 


folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

board_simple = "board_simple.txt"
board_medium = "board_medium.txt"
board_hard = "board_hard.txt"
board_supre_hard = "board_super_hard.txt"
board_impossible = "board_impossible.txt"
boards = [board_simple, board_medium, board_hard, board_supre_hard, board_impossible]


# Function used to create "moves" text at end of game
def move_text(moves):
    string = ""
    if len(moves) == 1: # first text (amount of moves)
        string += f"You made {len(moves)} move."
    else:
        string += f"You made {len(moves)} moves."
    string += "\n----------------------------------------------------------------------------------------------------------------------------\n"
    sub_string = ""
    i = 0 # second text (moves made)
    while i < len(moves):
        if i != len(moves) - 1:
            sub_string += moves[i] + ", "
        else:
            sub_string += moves[i]
        i += 1 

    if len(sub_string) == 1:
        string += f"Your move: {sub_string}" # 1 move win
    else:
        string += f"Your moves: {sub_string}"
    
    return string



game_running = True
play_intro_sound = True

while game_running:
    play = False
    cur_maze = 0
    print(welcome_string)
    if play_intro_sound:
        playsound('2019-05-09_-_Escape_Chase_-_David_Fesliyan- (mp3cut.net).mp3')

    print("----------------------------------------------------------------------------------------------------------------------------")
    print("Input choice below:")
    print("----------------------------------------------------------------------------------------------------------------------------")
    play_choice = input("> ")

    if play_choice.lower() == 'q':
        game_running = False
        continue

    elif play_choice.lower() == 'k':
        print(input_keys)
        print()
        continue_game = input("Press enter to continue: ")
        continue

    elif play_choice.lower() == 'p':
        play = True

    elif play_choice == "i":
        print(instructions_string)
        print()
        continue_game = input("Press enter to continue: ")
        play_intro_sound = False
        continue
    try:
        if play_choice.lower()[0] == "l" and len(play_choice) == 2:
            try:
                if play_choice.lower()[1] == '1':
                    leaderboard_file = open("leaderboard1.txt", "r")
                    difficulty = '1'
                elif play_choice.lower()[1] == '2':
                    leaderboard_file = open("leaderboard2.txt", "r")
                    difficulty = '2'
                elif play_choice.lower()[1] == '3':
                    leaderboard_file = open("leaderboard3.txt", "r")
                    difficulty = '3'
                elif play_choice.lower()[1] == '4':
                    leaderboard_file = open("leaderboard4.txt", "r")
                    difficulty = '4'
                elif play_choice.lower()[1] == '5':
                    leaderboard_file = open("leaderboard5.txt", "r")
                    difficulty = '5'
                else:
                    print("\nInvalid input. Try again.\n")
                    play_intro_sound = False
                    continue
            except IndexError:
                print("\nInvalid input. Try again.\n")
                play_intro_sound = False
                continue

            leaderboard_list = [] # list of [[name, score], ...] etc
            for line in leaderboard_file: # Adding all lines/scores to a new list
                new_entry = line.split(", ")
                score_int = float(new_entry[1])
                new_entry[1] = score_int
                leaderboard_list.append(new_entry)
            leaderboard_file.close()
            leaderboard = create_leaderboard(leaderboard_list, difficulty)
            print(leaderboard)
            print()
            continue_game = input("Press enter to continue: ")
            print()
            play_intro_sound = False
            continue
    except IndexError:
        print("\nInvalid input. Try again.\n")
        play_intro_sound = False
        continue

    play_intro_sound = False

    if not(play):
        print("\nInvalid input. Try again.\n")
        continue

    while True:
        try:
            print("----------------------------------------------------------------------------------------------------------------------------")
            player_name = input("Enter your name: ")
            print("----------------------------------------------------------------------------------------------------------------------------")
            board_num = int(input("Enter the game difficulty you would like to play with (1-5) (with 1 as easiest and 5 as hardest): "))
            if board_num not in [1, 2, 3, 4, 5]:
                print("Invalid input. Try again.")
                continue
            cur_maze = board_num
            break
        except ValueError:
            print("\nInvalid input. Try again.\n")

    time_limits_list = (30, 45, 60, 75, 90)
    cur_time_limit = time_limits_list[board_num - 1]

    print("----------------------------------------------------------------------------------------------------------------------------")
    print(f"You have {cur_time_limit} seconds to escape the building before it collapses! (After each move your remaining time will be printed)")
    time.sleep(4)
    board_name = boards[board_num - 1]
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("Game now beginning...")
    print("----------------------------------------------------------------------------------------------------------------------------")
    playsound('341911_sgtpepperarc360_00-game-load (mp3cut.net).wav')
    time.sleep(2)
    print(entering_maze_string)
    time.sleep(3)

    print("----------------------------------------------------------------------------------------------------------------------------\n")
    continue_input = input("Press Enter to continue: ")
    print("----------------------------------------------------------------------------------------------------------------------------\n")

    config = board_name

    game_object = Game(config)
    cells = game_object.list_of_cells
    player = game_object.player

    print("""
====================================
            Building Map            
====================================
""")

    print(grid_to_string(cells, player).strip())
    time_used  = 0 # In seconds
    time.sleep(1)
    playsound('zapsplat_emergency_alarm_slight_distance_reverb_serious_72497 (mp3cut.net).mp3')
    print("""
=========================================

    YOU AWAKE IN THE BURNING BUILDING!  

            ###############   
            #  ESCAPE!!!  #         
            ###############

=========================================
""")
    time.sleep(4)

    # Game playing until user wins, loses or enters 'q'
    while game_object.play_again and time_used < cur_time_limit: # if it is false no more inputs are necessary (i.e. game has ended, can be loss of win)
        time_left = cur_time_limit - time_used
        print(f"\nTime Left before building collapses = {round(time_left, 0)} seconds\n")
        print("----------------------------------------------------------------------------------------------------------------------------")
        start_time = time.time()
        valid_inputs = list("wasdqkm")
        input_move = (input("Input a move: ")).lower()

        
        if len(input_move) == 1 and input_move in valid_inputs:
            text = game_object.game_move(input_move) # Changing players location

            cells = game_object.list_of_cells
            player = game_object.player
            print("""
====================================
            Building Map            
====================================
""")
            print(grid_to_string(cells, player).strip())
            if text == False:
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_used += time_lapsed
                continue
            else:
                print(text)
                print()
        else:
            cells = game_object.list_of_cells
            player = game_object.player
            print("""
====================================
            Building Map            
====================================
""")
            print(grid_to_string(cells, player).strip())
            print("Please enter a valid move (w, a, s, d, q, k, m).\n")
    
        end_time = time.time()
        time_lapsed = end_time - start_time
        time_used += time_lapsed

    if game_object.won and time_used < cur_time_limit: # Player has won
        playsound('mixkit-winning-swoosh-2017.wav')
        print("""
=====================
====== YOU WIN! =====
=====================
""")
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("""\nYou escape from the burning building in the nick of time, looking behind youself the cememnt walls and conrete floors collapse firing dust and small pieces of rock in every direction. You Escaped!\n""")
        time.sleep(5)
        print("----------------------------------------------------------------------------------------------------------------------------")
        moves = game_object.moves
        print(move_text(moves))
        time.sleep(2)
        print("----------------------------------------------------------------------------------------------------------------------------")
        print(f"Your total time was {round(time_used, 1)} seconds!")
        print("----------------------------------------------------------------------------------------------------------------------------")
        time.sleep(2)
        print()
        time.sleep(2)

    else: # Player has lost
        playsound('mixkit-lose-life-falling-2029.wav')
        print("""
=====================
===== YOU LOSE! =====
=====================
""")
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("\nThe building collapses and its flames reduce you to a mere pile of ash. You Died!\n")
        print("----------------------------------------------------------------------------------------------------------------------------")
        time.sleep(5)
        moves = game_object.moves
        print(move_text(moves))
        print("----------------------------------------------------------------------------------------------------------------------------")
        time.sleep(1)
        print()
        time.sleep(2)

    print("\nNow taking you back to the main menu...\n")
    time.sleep(5)
    play_intro_sound = True

    if cur_maze == 1:
        file_name = "leaderboard1.txt"
    if cur_maze == 2:
        file_name = "leaderboard2.txt"
    if cur_maze == 3:
        file_name = "leaderboard3.txt"
    if cur_maze == 4:
        file_name = "leaderboard4.txt"
    if cur_maze == 5:
        file_name = "leaderboard5.txt"

    leaderboard_file = open(file_name, "a")
    string = f"\n{player_name}, {round(time_used, 1)}"
    leaderboard_file.write(string)
    leaderboard_file.close()

print("\nNow exiting game... Thanks for playing!\n")