'''
Answer for Question 7 - PIAT: Improved Full Game.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

import shutil
import os
import time
import datetime
import sys

import setup
import name
import game
import train
import shop
import mouse


title = """Mousehunt

       ____()()
      /      @@
`~~~~~\_;m__m._>o

Inspired by Mousehunt© Hitgrab
Programmer - An INFO1110/COMP9001 Student
Mice art - Joan Stark and Hayley Jane Wakenshaw"""


def has_cheese(to_check, my_cheese):
    i = 0
    while i < len(my_cheese):
        if my_cheese[i][0] == to_check:
            quantity = my_cheese[i][1]
            if quantity > 0:
                return quantity
            else:
                return 0
        i += 1

def consume_cheese(to_eat: str, cheese: list) -> None:
    '''
    Handles the consumption of cheese.
    Will modify the cheese list, if required.
    Parameters:
        to_eat:    str,        the type of cheese to consume during the hunt.
        cheese:    list,       all the cheeses and quantities the player 
                               currently posseses.
    '''
    cheese_info = shop.find_cheese_index(to_eat.lower())
    cheese_index = cheese_info[1]
    #print("XXX", cheese_index, "XXX")
    cur_value = cheese[cheese_index][1]
    
    # Value should never be negative
    cheese[cheese_index][1] -= 1
    if cheese[cheese_index][1] < 0:
        cheese[cheese_index][1] = 0


def hunt(gold: int, cheese: list, trap_cheese: str | None, enchant, points: int) -> tuple:
    hunt_again = True
    unsuccessful_hunt_count = 0
    if trap_cheese != None:
        cur_cheese_info = shop.find_cheese_index(trap_cheese.lower())
        cur_cheese_index = cur_cheese_info[1]
        amount_of_trap_cheese_left = cheese[cur_cheese_index][1]
    else:
        amount_of_trap_cheese_left = 0

    while hunt_again:
        if trap_cheese != None:
            cur_cheese_info = shop.find_cheese_index(trap_cheese.lower())
            cur_cheese_index = cur_cheese_info[1]
            amount_of_trap_cheese_left = cheese[cur_cheese_index][1]
        else:
            amount_of_trap_cheese_left = 0

        print("Sound the horn to call for the mouse...")
        sound_horn = input("Sound the horn by typing \"yes\": ")
        
        if sound_horn == "stop hunt":
            hunt_again = False
            unsuccessful_hunt_count = 0
        elif sound_horn != "yes":
            print("Do nothing.")
            unsuccessful_hunt_count += 1
        elif amount_of_trap_cheese_left <= 0: # No cheese on the trap
            print("Nothing happens. You are out of cheese!")
            unsuccessful_hunt_count += 1
        else:
            # Creating mouse class
            #print(trap_cheese)
            cur_mouse = mouse.Mouse(trap_cheese, enchant)
            mouse_name = cur_mouse.name
            #print(mouse_name)

            if mouse_name == None:
                print("Nothing happens.")
                consume_cheese(trap_cheese, cheese)
                unsuccessful_hunt_count += 1

            else:
                mouse_image = cur_mouse.mouse_image
                print(f"Caught a {mouse_name} mouse!")
                print(mouse_image)
                consume_cheese(trap_cheese, cheese)
                added_gold, added_points = cur_mouse.get_final_points_and_gold()
                gold += added_gold
                points += added_points
                unsuccessful_hunt_count = 0

        enchant = False

        if hunt_again: # This shouldn't print if the user inputted "stop hunt"  
            print(f"My gold: {gold}, My points: {points}\n")
        
        if unsuccessful_hunt_count >= 5 and hunt_again == True:
            continue_hunt = input("Do you want to continue to hunt? ")
            if continue_hunt == "no":
                hunt_again = False
                enchant = False
            unsuccessful_hunt_count = 0


    # Updated quantity of gold, updated quantity of points (after hunt)
    return (gold, points)






def run_setup():
    """
    - Game first verifys if all required files are correctly present - using -v
    - If abnormalities are found the game will prompt users to repair the game by entering, YES or yes
    - If they choose to repair, the game runs installation again, i.e., -i
    - If anything else than YES and yes are entered the game warns the user, asks for confirmation again
    - Return True is files are tampered, else return False
    """
    unformatted_timestamp = time.asctime() # string
    day_of_week = unformatted_timestamp[:3]
    month = unformatted_timestamp[4:7]
    day_num = unformatted_timestamp[9:10]
    if len(day_num) == 1:
        day_num = f"0{day_num}"
    cur_time = unformatted_timestamp[11:19]
    year = unformatted_timestamp[20:]
    timestamp = f"{day_num} {month} {year} {cur_time}"
    master = '/home/game_master/'

    # First check
    verification_output_list = setup.verification(master, timestamp)
    verification_result = verification_output_list[-1]
    v_pass_string = f"{timestamp}  Verification complete."
    v_fail_string = "Abnormalities detected..."
    
    tampered_with = False

    if verification_result == v_fail_string: # I.e., game files are tampered and need repairing
        # First Warning
        repair_game = input("Do you want to repair the game? ").strip().lower()
        if repair_game == "yes":
            setup.installation(master, timestamp)
        else:
            # Second Warning
            print("Game may malfunction and personalization will be locked.")
            proceed = input("Are you sure you want to proceed? ").strip().lower()
            if proceed == "yes":
                print("You have been warned!!!")
                tampered_with = True
            else:
                sys.exit()
    print("""Launching game...
.
.
.""")
    return tampered_with


def personalization(temper_flag):
    if temper_flag:
        user_name = "Bob"
        print(f"Welcome to the Kingdom, Hunter {user_name}!")
        return user_name
    else:
        strike = 1
        user_name = input("What's ye name, Hunter? ").strip().lower()
        name_is_valid = name.is_valid_name(user_name)
        if not(name_is_valid): # Invalid Name
            print("""That's not nice!
I'll give ye 3 attempts to get it right or I'll name ye!
Let's try again...""")

            while strike <= 3:
                user_name = input("What's ye name, Hunter? ").strip().lower()
                name_is_valid = name.is_valid_name(user_name)
                if not(name_is_valid):
                    print(f"Nice try. Strike {strike}!")
                else:
                    print(f"Welcome to the Kingdom, Hunter {user_name}!")
                    return user_name
                strike += 1

            automatic_name = name.generate_name(user_name)
            print(f"""I told ye to be nice!!!
Welcome to the Kingdom, Hunter {automatic_name}!""")
            return automatic_name

        else:
            print(f"Welcome to the Kingdom, Hunter {user_name}!")
            return user_name

"""
def the_training():
    Enchantment effects:
    - Only first hunt after the training
    - Only applicable to a trap given by Larry, i.e., player needs to pick left or right
    - Swiss + Tiny mouse, +0.25 attraction rate
    - Marble + Brown mouse, +25 gold
    - Cheddar + Brown mouse, +25 points
    - Enchantment can only wear off after hunting once (regardless of outcome of hunt, i.e., not arming and failing still wears enchantment off)
"""

def get_benefit(cheese): # Is only printed in change_cheese if player has completed training and have_enchantment = True 
    benefit_string = ""
    if cheese.lower() == "cheddar":
        benefit_string = "+25 points drop by next Brown mouse"
    if cheese.lower() == "marble":
        benefit_string = "+25 gold drop by next Brown mouse"
    if cheese.lower() == "swiss":
        benefit_string = "+0.25 attraction to Tiny mouse"

    return benefit_string # String object representing the benefit of the enchanted trap


def new_action_menu(player_name, trap, have_enchantment):
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    points = 0
    cheese_type_on_trap = None
    play_game_again = True

    if have_enchantment:
        trap = f"One-time Enchanted {trap}"
    
    
    while play_game_again:
        print(f"\nWhat do ye want to do now, Hunter {player_name}?")
        print(game.get_game_menu())

        while True:
            try:
                game_choice = int(input("Enter a number between 1 and 4: "))
                if game_choice < 1 or game_choice > 4:
                    print("Must be between 1 and 4.")
                    continue
                else:
                    if game_choice != 1 and game_choice != 2:
                        print()
                
                break
            except ValueError:
                print("Invalid input.")

        """
        Enchantment:
        - Wears of after 1 round of hunting
        """
        if game_choice == 2: # Hunt
            gold, points = hunt(gold, cheese, cheese_type_on_trap, have_enchantment, points)
            if have_enchantment:
                # Changing enchanted version of trap back to its normal state
                trap = trap[19:] # Removing extra text which was included when it was enchanted
            have_enchantment = False
            

        elif game_choice == 3: # Shop
            gold, cheese = game.cheese_shop(gold, cheese, trap)

        elif game_choice == 4: # Change cheese on trap
            trap_armed, cheese_type_on_trap = game.change_cheese(player_name, trap, cheese, e_flag=have_enchantment) # Either True (trap armed) or False (trap not armed)
        
        else:
            quit()



def main():
    # 1 - Running Game Setup Processes
    tampered_with = run_setup()
    
    # 2 - Title Page
    print(title)
    print()

    # 3 - Player Name
    player_name = personalization(tampered_with)
    
    # 4 - The Training
    have_enchantment = False
    print("Before we begin, let's train you up!")
    start_game_choice = input("Press \"Enter\" to start training or \"skip\" to Start Game: ").lower()

    if start_game_choice != "skip":
        print()
        trap = train.main() # trap is retained from training stage
        if trap != "Cardboard and Hook Trap":
            have_enchantment = True

    else:
        trap = "Cardboard and Hook Trap" # If player doesn't complete the tutorial


    # 5 - New Game Features
    running_game = new_action_menu(player_name, trap, have_enchantment)



if __name__ == '__main__':
    main()




