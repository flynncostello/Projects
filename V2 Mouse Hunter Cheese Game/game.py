'''
This file should borrow code from your Assignment 1.
However, it will require some modifications for this assignment.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

'''
Keep this line!
'''
import random

'''
We recommend you import your 'name', 'train' and 'shop' modules to complete this 
question. It will save trouble in needing to copy and paste code from previous 
questions. However if you wish not to, you are free to remove the imports below.
Feel free to import other modules that you have written.
'''
import name
import train
import shop
from intro_string import final_intro_string
import game_final

# you can make more functions or global read-only variables here if you please!

def cheese_shop(gold, cheese, trap):
    print("""Welcome to The Cheese Shop!
Cheddar - 10 gold
Marble - 50 gold
Swiss - 100 gold
""")
    while True:
        print("""How can I help ye?
1. Buy cheese
2. View inventory
3. Leave shop""")
        try:
            main_choice = int(input(""))
            if main_choice < 1 or main_choice > 3:
                print("I did not understand.\n")
                continue
            break
        except ValueError:
            print("I did not understand.\n")


    while main_choice != 3:
        if main_choice == 1: # 1 - Buy cheese
            gold_spent, cheeses_bought_tuple = shop.buy_cheese(gold) # return a tuple, (gold_spent, quantity)
            gold -= gold_spent
            i = 0
            while i < len(cheese):
                cheese[i][1] += cheeses_bought_tuple[i]
                i += 1

        else: # 2 - View inventory
            shop.display_inventory(gold, cheese, trap)

        print("""
How can I help ye?
1. Buy cheese
2. View inventory
3. Leave shop""")
        main_choice = int(input(""))
    
    return (gold, cheese)



def get_game_menu():
    '''
    Returns a string displaying all possible actions at the game menu.
    '''
    main_menu_string = """1. Exit game
2. Join the Hunt
3. The Cheese Shop
4. Change Cheese"""
    return main_menu_string


def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
    '''
    Handles the inputs and ouputs of the change cheese feature.
    Parameters:
        hunter_name: str,        the name of the player.
        trap:        str,        the trap name.
        cheese:      list,       all the cheese and its quantities the player 
                                 currently possesses.
        e_flag:      bool,       if the trap is enchanted, this will be True. 
                                 default value is False.
    Returns:
        trap_status: bool,       True if armed and False otherwise.
        trap_cheese: str | None, the type of cheese in the trap. if player 
                                 exits the function without without arming 
                                 trap succesfully, this value is None.
    '''
    # back - returns to main menu
    # error message --> displays players inventory --> re-promts for cheese
    # All commands are case insensitive and ignore trailing and leading whitespaces in command
    # Ends when either trap is armed successfully or the user opts to leave
    # Returns a tuple (bool (trap status), str (type of cheese in trap))
    # If they leave without arming trap successfully there should be no cheese on trap
    cur_info_text = f"""Hunter {hunter_name}, you currently have:
Cheddar - {cheese[0][1]}
Marble - {cheese[1][1]}
Swiss - {cheese[2][1]}
"""
    print(cur_info_text)
    #cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    cheese_name = input("Type cheese name to arm trap: ").strip().lower()
    while cheese_name != "back":
        cheese_index = shop.find_cheese_index(cheese_name)
        if cheese_index[0] == False: # Invalid cheese name
            print("No such cheese!\n")
        else:
            cheese_i = cheese_index[1]
            amount_in_inventory = cheese[cheese_i][1]
            cheese_type = cheese[cheese_i][0]
            if e_flag:
                enchantment_string = game_final.get_benefit(cheese_type)
                print(f"Your {trap} has a one-time enchantment granting {enchantment_string}.")

            if amount_in_inventory == 0: # None of that certain type of cheese left in inventory
                print("Out of cheese!\n")
            else: # valid cheese and has some of it
                arm_trap = input(f"Do you want to arm your trap with {cheese_type}? ").strip().lower()
                if arm_trap == "back":
                    return (False, None)
                elif arm_trap == "no":
                    print()

                elif arm_trap == "yes":
                    print(f"{trap} is now armed with {cheese_type}!")
                    return (True, cheese_type) # Trap is armed

        print(cur_info_text)
        cheese_name = input("Type cheese name to arm trap: ").strip().lower()
    return (False, None) # Quitting option 4 (change cheese)


#cheese = [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]
#trap = "Cardboard and Hook Trap"
#change_cheese("Dan", trap, cheese, e_flag=False)



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



def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int) -> tuple:
    '''
    Handles the hunt mechanic.
    It includes the inputs and outputs of sounding the horn, the result of 
    the hunt, the gold and points earned, and whether users want to continue 
    after failing consecutively.
    The function will modify the cheese list, if required.
    Parameters:
        gold:        int,        the quantity of gold the player possesses.
        cheese:      list,       all the cheese and quantities the player 
                                 currently posseses.
        trap_cheese: str | None, the type of cheese that the trap is currently 
                                 armed with. if its not armed, value is None.
        points:      int,        the quantity of points that the player 
                                 currently posseses.
    Returns:
        gold:        int,        the updated quantity of gold after the hunt.   
        points:      int,        the updated quantity of points after the hunt.
    '''
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

        #print(amount_of_trap_cheese_left)
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
            mouse_odds = random.random() 
            if mouse_odds > 0.5:
                print("Nothing happens.")
                consume_cheese(trap_cheese, cheese)
                unsuccessful_hunt_count += 1
            else:
                print("Caught a Brown mouse!")
                consume_cheese(trap_cheese, cheese)
                gold += 125
                points += 115
                unsuccessful_hunt_count = 0

        if hunt_again: # This shouldn't print if the user inputted "stop hunt"  
            print(f"My gold: {gold}, My points: {points}\n")
        
        if unsuccessful_hunt_count >= 5 and hunt_again == True:
            continue_hunt = input("Do you want to continue to hunt? ")
            if continue_hunt == "no":
                hunt_again = False
            unsuccessful_hunt_count = 0


    # Updated quantity of gold, updated quantity of points (after hunt)
    return (gold, points)




def action_menu(player_name, trap):
    """
    Runs once the user enters skip or finishes the training

    Inputs:
        player_name - players name
    Outputs:

    """
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    points = 0
    cheese_type_on_trap = None
    play_game_again = True
    
    while play_game_again:
        print(f"\nWhat do ye want to do now, Hunter {player_name}?")
        print(get_game_menu())
        game_choice = int(input(""))

        if game_choice == 2: # Hunt
            gold, points = hunt(gold, cheese, cheese_type_on_trap, points)

        elif game_choice == 3: # Shop
            gold, cheese = cheese_shop(gold, cheese, trap)

        elif game_choice == 4: # Change cheese on trap
            trap_armed, cheese_type_on_trap = change_cheese(player_name, trap, cheese, e_flag=False) # Either True (trap armed) or False (trap not armed)
        
        else:
            break






def main():
    print(final_intro_string)

    player_name = input("\nWhat's ye name, Hunter?\n")

    name_is_valid = name.is_valid_name(player_name)

    if name_is_valid:
        print(f"Welcome to the Kingdom, Hunter {player_name}!")
    else:
        player_name = "Bob"
        print(f"Welcome to the Kingdom, Hunter {player_name}!")

    print("Before we begin, let's train you up!")
    start_game_choice = input("Press \"Enter\" to start training or \"skip\" to Start Game: ").lower()

    if start_game_choice != "skip":
        print()
        trap = train.main() # trap is retained from training stage
        #print(trap)
    else:
        trap = "Cardboard and Hook Trap" # If player doesn't complete the tutorial

    # Now starting main game
    # print(trap)
    
    action_menu(player_name, trap)


if __name__ == '__main__':
    main()
