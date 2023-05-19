import random 
import math
import math_questions # Imports all math question functions
import edu2 # Education game
import adventure # adventure game
import string # Used for checking for whitespaces
import os

folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

while True: # Original welcome text
    print("""
    *****************************
    * Welcome to Horizon Gaming *
    *****************************

    Games:
    Enter 1 for Race Mania
    Enter 2 for Cave Escape

    Leaderboards:
    Enter 3 for Race Mania Leader board

    Enter q to quit
    """)


    menu_choice = input("> ")

    if menu_choice == "1": # edu3
        race_game = edu2.play_race_mania() # race_game = [[race_name, total_points]] x how many goes they did
        
        file0 = open("leaderboard.txt", "a")
        
        string1 = ""
        i = 0
        while i < len(race_game): # String that is appended to leaderboard.txt each time
            string1 += (f"\n1     |     {race_game[i][0]}     |     {race_game[i][1]}")
            i += 1

        file0.write(string1)

        file0.close()

        file1 = open("leaderboard.txt", "r")

        # creating list of contents of txt file without |, each place, name and score will have a different list section
        race_ls = []

        line_num = 0
        while True:
            line = file1.readline()
            if line_num != 0 and not line:
                break
            race_ls.append(line.split("|")) # Putting all scores in lists that are split by |
            line_num += 1
        del race_ls[0]
            

        # Stips all extra spaces before and after each element
        i = 0 
        while i < len(race_ls):
            i2 = 0
            while i2 < len(race_ls[i]):
                race_ls[i][i2] = race_ls[i][i2].strip() # Removing all whitespaces from either side of elements
                i2 += 1
            i += 1

        # Using a function to put the elements in 
        def order(item):
            return float(item[2])

        # new_ls is the sorted (i.e. biggest score to lowers) version of race_ls
        new_ls = sorted(race_ls, key=order, reverse=True)

        file1.close()

        file2 = open("leaderboard.txt", "w")

        i = 0
        while i < len(new_ls): # Adding new string (ordered) to file leaderboard.txt
            place = 1 + i
            string = "\n{}     |     {}     |     {:.1f}".format(place, new_ls[i][1], float(new_ls[i][2]))
            file2.write(string)
            i += 1

        file2.close()

    elif menu_choice == "2":
        adventure.adventure_game() # Adventure Game

    elif menu_choice == "3":

        string1 = """
    * Race Mania Leaderboard *
                
Place          Name          Score
{}""".format("=" * 35) # Printing top part of leaderboard

        print("")
        print(string1)

        file1 = open("leaderboard.txt", "r")

        line = file1.readline() # Reading all lines from leaderboard.txt
        line_no = 0
        while True:
            if not line:
                break
            if line_no == 0:
                line = file1.readline() # line 1 is just a space, doesn't need to be printed
                line_no += 1
                continue 
            print(line) # printing all lines from 2nd line unti lend
            line = file1.readline()
            line_no += 1
        print()
        file1.close()

    elif menu_choice.lower() == "q":
        print("Thanks for playing. Bye!") # Player wants to leave
        print()
        quit()

    else:
        print("Invalid Input") # Input is invalid
        continue