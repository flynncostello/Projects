'''
Write your answer for the full OO version of the game here.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

import sys

import game_final
import train

import trap
import hunter
import cshop
import interface


def main():
    # 1 - Running Game Setup Processes
    tampered_with = game_final.run_setup()
    
    # 2 - Title Page
    print(game_final.title)
    print()

    # 3 - Player Name
    player_name = game_final.personalization(tampered_with)
    
    # 4 - The Training
    print("Before we begin, let's train you up!")
    start_game_choice = input("Press \"Enter\" to start training or \"skip\" to Start Game: ").lower()
    e_flag = False

    if start_game_choice != "skip":
        print()
        trap = train.main() # trap is retained from training stage
        e_flag = True
    else:
        trap = "Cardboard and Hook Trap" # If player doesn't complete the tutorial


    # Creating player object
    player = hunter.Hunter(name=player_name) # Sets players name after it has been checked for profanity
    player.trap.set_trap_name(trap) # Sets players trap name after training
    player.trap.set_one_time_enchantment(e_flag) # Sets enchantment status

    game_interface = interface.Interface()
    game_interface.set_player(player)
    play_again = True
    while play_again:
        print(f"\nWhat do ye want to do now, Hunter {player.get_name()}?")
        print(game_interface.get_menu())
        while True:
            main_menu_choice = input("Enter a number between 1 and 4: ")
            if main_menu_choice == "1":
                sys.exit()
            else:
                print()
                play_again = game_interface.move_to(main_menu_choice)
                #print(play_again)

                if play_again == "Invalid":
                    continue
                if play_again == False:
                    sys.exit()
                if play_again == True:
                    break


        

    #print(player.trap.get_trap_name())
    #print(player.trap.get_one_time_enchantment())
    # Whenever you need to print the trap name use player.trap.__str__() instead



if __name__ == '__main__':
    main()



