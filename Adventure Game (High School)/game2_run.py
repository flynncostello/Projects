"""
Game 2 Idea:

You are the king of a castle and must make decisions to ensure your
kingdom remains the greatest

How successful you are is broken up into 4 areas:
1. Wealth (Gold Storage) 2. Defence (Army) 3. Religon (Church) 4. Happiness (People)
Additionally there will be a citizen hapiness meter from 0-100
If this meter goes below a certain level they will revolt, if
wealth, defence or religion goes below certain level, kingdom
will crumble.
"""
import random
import time
from game2_strings import *
from game2_classes import *
import os
import PIL.Image
from PIL import Image
from convert_image import *
import sys
from playsound import playsound 
#playsound(sound)

folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

wealth_stat = 100 # "w"
defence_stat = 100 # "d"
religion_stat = 100 # "r"
happiness_stat = 100 # "h"

# Events 18, 19 and 20 all lead to one of the 3 endings 
event1 = Event('mixkit-coins-handling-1939.wav', 1, event1_image, event1_intro, event1_yes, event1_no, event1_yes_impacted_fields, event1_yes_impact_numbers, event1_no_impacted_fields, event1_no_impact_numbers)
event2 = Event('mixkit-wild-beast-roar-12.wav', 2, event2_image, event2_intro, event2_yes, event2_no, event2_yes_impacted_fields, event2_yes_impact_numbers, event2_no_impacted_fields, event2_no_impact_numbers)
event3 = Event('mixkit-church-bell-calling-603 (mp3cut.net) (2).wav', 3, event3_image, event3_intro, event3_yes, event3_no, event3_yes_impacted_fields, event3_yes_impact_numbers, event3_no_impacted_fields, event3_no_impact_numbers)
event4 = Event('Dragon Tense - QuickSounds.com (mp3cut.net).mp3', 4, event4_image, event4_intro, event4_yes, event4_no, event4_yes_impacted_fields, event4_yes_impact_numbers, event4_no_impacted_fields, event4_no_impact_numbers)
event5 = Event('earth-rumble-6953 (mp3cut.net).mp3', 5, event5_image, event5_intro, event5_yes, event5_no, event5_yes_impacted_fields, event5_yes_impact_numbers, event5_no_impacted_fields, event5_no_impact_numbers)
event6 = Event('drawing-sword-6234 (mp3cut.net).mp3', 6, event6_image, event6_intro, event6_yes, event6_no, event6_yes_impacted_fields, event6_yes_impact_numbers, event6_no_impacted_fields, event6_no_impact_numbers)
event7 = Event('mixkit-sick-woman-coughing-2218.wav', 7, event7_image, event7_intro, event7_yes, event7_no, event7_yes_impacted_fields, event7_yes_impact_numbers, event7_no_impacted_fields, event7_no_impact_numbers)
event8 = Event('mixkit-demon-monster-ritual-voice-292.wav', 8, event8_image, event8_intro, event8_yes, event8_no, event8_yes_impacted_fields, event8_yes_impact_numbers, event8_no_impacted_fields, event8_no_impact_numbers)
event9 = Event('Crumbing-Paper-1-www.fesliyanstudios.com.mp3', 9, event9_image, event9_intro, event9_yes, event9_no, event9_yes_impacted_fields, event9_yes_impact_numbers, event9_no_impacted_fields, event9_no_impact_numbers)
event10 = Event('22804_acclivity_cathedralofthedowns (mp3cut.net).mp3', 10, event10_image, event10_intro, event10_yes, event10_no, event10_yes_impacted_fields, event10_yes_impact_numbers, event10_no_impacted_fields, event10_no_impact_numbers)
event11 = Event('groanswav-14670 (mp3cut.net).mp3', 11, event11_image, event11_intro, event11_yes, event11_no, event11_yes_impacted_fields, event11_yes_impact_numbers, event11_no_impacted_fields, event11_no_impact_numbers)
event12 = Event('83286130 (mp3cut.net).mp3', 12, event12_image, event12_intro, event12_yes, event12_no, event12_yes_impacted_fields, event12_yes_impact_numbers, event12_no_impacted_fields, event12_no_impact_numbers)
event13 = Event('423119_ogsoundfx_medieval-city-sample (mp3cut.net).wav', 13, event13_image, event13_intro, event13_yes, event13_no, event13_yes_impacted_fields, event13_yes_impact_numbers, event13_no_impacted_fields, event13_no_impact_numbers)
event14 = Event('Hmm-sound-effect.mp3', 14, event14_image, event14_intro, event14_yes, event14_no, event14_yes_impacted_fields, event14_yes_impact_numbers, event14_no_impacted_fields, event14_no_impact_numbers)
event15 = Event('human_crowd_agry_shouting_approx_20_people (mp3cut.net).mp3', 15, event15_image, event15_intro, event15_yes, event15_no, event15_yes_impacted_fields, event15_yes_impact_numbers, event15_no_impacted_fields, event15_no_impact_numbers)
event16 = Event('Melody of death horror-tones6.com (mp3cut.net).mp3', 16, event16_image, event16_intro, event16_yes, event16_no, event16_yes_impacted_fields, event16_yes_impact_numbers, event16_no_impacted_fields, event16_no_impact_numbers)
event17 = Event('Witch Scary Cackle - QuickSounds.com (mp3cut.net).mp3', 17, event17_image, event17_intro, event17_yes, event17_no, event17_yes_impacted_fields, event17_yes_impact_numbers, event17_no_impacted_fields, event17_no_impact_numbers)
event18 = Event('341606_mike-stranks_trickling-stream (mp3cut.net).wav', 18, event18_image, event18_intro, event18_yes, event18_no, event18_yes_impacted_fields, event18_yes_impact_numbers, event18_no_impacted_fields, event18_no_impact_numbers)
event19 = Event('152721__timgormly__spirit-breath1.aiff', 19, event19_image, event19_intro, event19_yes, event19_no, event19_yes_impacted_fields, event19_yes_impact_numbers, event19_no_impacted_fields, event19_no_impact_numbers)
event20 = Event('mixkit-big-army-crowd-marching-461 (mp3cut.net).wav', 20, event20_image, event20_intro, event20_yes, event20_no, event20_yes_impacted_fields, event20_yes_impact_numbers, event20_no_impacted_fields, event20_no_impact_numbers)

events = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12, event13, event14, event15, event16, event17, event18, event19, event20]

run_program = True
current_year = 0

while run_program:
    played_main_menu_sound = False

    while True:
        print(main_menu_string)
        if not(played_main_menu_sound):
            playsound('mixkit-medieval-show-fanfare-announcement-226 (mp3cut.net).wav')
        print("--------------------------------------------------------------------------------")
        print("Enter input below:")
        print("--------------------------------------------------------------------------------")
        choice = input("> ")

        if choice.lower() == "p": # Play game
            break
        elif choice.lower() == "q": # Quit
            print("--------------------------------------------------------------------------------")
            print("\nThanks for playing! Bye. :)\n")
            print("--------------------------------------------------------------------------------")
            quit()

        elif choice.lower() == "i": # Instructions
            print("--------------------------------------------------------------------------------")
            print(instructions_string)
            print("--------------------------------------------------------------------------------")
            continue_game = input("Press enter to continue: ")
            played_main_menu_sound = True

        elif choice.lower() == "l": # Leaderboard
            leaderboard_file = open("leaderboard.txt", "r")
            leaderboard_list = [] # list of [[name, score], ...] etc
            for line in leaderboard_file: # Adding all lines/scores to a new list
                new_entry = line.split(", ")
                score_int = int(new_entry[1])
                new_entry[1] = score_int
                leaderboard_list.append(new_entry)
            leaderboard_file.close()
            leaderboard = create_leaderboard(leaderboard_list)
            print(leaderboard)
            print()
            continue_game = input("Press enter to continue: ")
            played_main_menu_sound = True

        else: # Invalid input
            print("--------------------------------------------------------------------------------")
            print("\nInvalid input\n")
            print("--------------------------------------------------------------------------------")
            time.sleep(2)
            played_main_menu_sound = True

    print("--------------------------------------------------------------------------------")
    if current_year > 0:
        player_name = input("Enter your new King's name: ")
    else:
        player_name = input("Enter your King's name: ")
    print("--------------------------------------------------------------------------------")
    print("\nNow beginning game...\n")
    new_kingdom = KingdomStats()

    game_lost = False
    years_ruling = 0
    events_which_have_occured = [] # List of intgers with events that have occured
    #events_which_have_occured = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    game_start_string = f"""
--------------------------------------------------------------------------------

Welcome King {player_name}!

It's so good to finally meet our new King. You look exactly how everyone 
described you as. I know you're already very busy with running your Kingdom 
and all, so I won't hold you for too long. I just wanted to remind, and warn 
you about the weird events which too often plague our Kingdom. When these events
happen just ensure you make the right decision for the Kingdom. Well, that's
all from me for now. Good Luck!

--------------------------------------------------------------------------------
"""
    print(game_start_string)
    continue_game = input("Press enter to continue: ")
    print("""
--------------------------------------------------------------------------------
Kingdom Timeline:
--------------------------------------------------------------------------------""")
    time.sleep(2)
    while not(game_lost) and years_ruling <= 100:
        # An event has a 25% chance of happening each year
        event_happen_list = (False, False, True)

        event_happend_index = random.randint(0, 2)
        event_happening = event_happen_list[event_happend_index]

        if event_happening and years_ruling != 0:
            print("\n--------------------------------------------------------------------------------\n")
            print(f"{current_year}A.D. - New Event:\n")
            
            new_event_index = pick_event(years_ruling, events_which_have_occured)
            events_which_have_occured.append(new_event_index)
            
            new_event = events[new_event_index]
            print()
            event_result = new_event.run_event(new_kingdom) # This runs the new event
            # If this returns False they have lost, if True then they are still alive

            if event_result == False:
                if new_event_index not in [17, 18, 19]:
                    print(f"\nYou were killed after {years_ruling} years in power")
                game_lost = True
                break

            check_stats = new_kingdom.check_stats() # Checking values are in suitable range
            # If not in range they either need to be decreased to max at 100 or the player has lost if any go below or equal to 0

            if check_stats[0] == False:
                reason = check_stats[1]
                if reason == "w":
                    print("\nYour Kingdom ran out of money! You Lose!")
                if reason == "d":
                    print("\nYour Kingdom ran out of soldiers and was vulnerable to attacks by all creatures and enemies alike! You Lose!")
                if reason == "r":
                    print("\nThe Priests were fed up with how you ruled and made you a matyr for it! You Lose!")
                if reason == "h":
                    print("\nYour citizens overthrew the crown and took the lands for themselves, killing you in the process! You Lose!")
                game_lost = True
            time.sleep(3)
            
            current_stats = f"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Current Kingdom Stats:
- Wealth : {new_kingdom.wealth_stat}
- Defence : {new_kingdom.defence_stat}
- Religion : {new_kingdom.religion_stat}
- Citizen Happiness : {new_kingdom.happiness_stat}

Number of years you have ruled for : {years_ruling} years

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
            if check_stats[0] != False:
                print(current_stats)
                time.sleep(2)
                keep_going = input("Press enter to continue: ")
                print()

        else: # Event not happening this year
            print(current_year, "A.D. - Nothing happened this year")
            playsound('43562827_time-passing-clock-ticking-01 (mp3cut.net).mp3')
            time.sleep(1)

        current_year += 1
        years_ruling += 1
    time.sleep(3)
    if years_ruling >= 100:
        print("After living a long and fulfilling life and ruling for an astonishing 100 years, you pass peacfully in your sleep.")
    if game_lost == True:
        print(loss)
    else:
        print(win) # Only happens if they rule for 100 years

    # Appending info to the leaderboard
    file1 = open("leaderboard.txt", "a")
    string = f"\n{player_name}, {years_ruling}"
    file1.write(string)
    file1.close()

    playing = check_if_wants_to_play()
    if playing == False:
        run_program = False
    
    years_ruling = 0

print("Thanks for playing! Bye. :)\n")
print("--------------------------------------------------------------------------------")    


