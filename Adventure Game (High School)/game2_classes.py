import time
import PIL.Image
from PIL import Image
from convert_image import *
import random
from playsound import playsound
import sys

class Event:
    def __init__(self, event_sound, event_num, event_image, event_intro, event_yes, event_no, event_yes_impacted_fields, event_yes_impact_numbers, event_no_impacted_fields, event_no_impact_numbers):
        self.event_sound = event_sound
        self.event_num = event_num
        self.event_image = event_image
        self.event_intro = event_intro
        self.event_yes = event_yes
        self.event_no = event_no
        self.event_yes_impacted_fields = event_yes_impacted_fields
        self.event_yes_impact_numbers = event_yes_impact_numbers
        self.event_no_impacted_fields = event_no_impacted_fields
        self.event_no_impact_numbers = event_no_impact_numbers
    
    def run_event(self, KingdomStats):
        print(self.event_intro)
        temp_img = self.event_image.copy()
        temp_img.show()
        playsound(self.event_sound)

        time.sleep(3)
        temp_img.close()
        print("\n--------------------------------------------------------------------------------\n")
        while True:
            choice = input("Enter 'y' to accept the choice or 'n' to deny it: ")
            print("\n--------------------------------------------------------------------------------\n")
            
            self.event_image.close()

            if choice.lower() == 'y': # accepted event
                print(self.event_yes)
                fields_impacted, value_impacts = [self.event_yes_impacted_fields, self.event_yes_impact_numbers]
                break
            elif choice.lower() == 'n': # said no to event
                print(self.event_no)
                fields_impacted, value_impacts = [self.event_no_impacted_fields, self.event_no_impact_numbers]
                break
            elif choice.lower() == "q":
                print("Thanks for playing! Bye. :)")
                print("\n--------------------------------------------------------------------------------\n")    
                quit()
            else:
                print("Invalid input")
                print("\n--------------------------------------------------------------------------------\n")
        
        if False in fields_impacted or False in value_impacts: # Player has died during event
            return False

        # Altering stats
        i = 0
        while i < len(fields_impacted):
            cur_field = fields_impacted[i]
            cur_field_impact = value_impacts[i]
            if cur_field == "w":
                KingdomStats.wealth_stat += cur_field_impact
            elif cur_field == "d":
                KingdomStats.defence_stat += cur_field_impact
            elif cur_field == "r":
                KingdomStats.religion_stat += cur_field_impact
            elif cur_field == "h":
                KingdomStats.happiness_stat += cur_field_impact
            else:
                print("Invalid")
                print("--------------------------------------------------------------------------------")
            i += 1
        return True # Event has run --> still may have lost


class KingdomStats: # Each time game is replayed a new KingdomStats class is made
    def __init__(self):
        self.wealth_stat = 100
        self.defence_stat = 100
        self.religion_stat = 100
        self.happiness_stat = 100
    
    def check_stats(self): # Checks if player has lost, return True if he has lost and False if he hasn't lost yet
        field_stats = [self.wealth_stat, self.defence_stat, self.religion_stat, self.happiness_stat] # Making sure all values below or equal to 100
        fields = ['w', 'd', 'r', 'h']
        i = 0
        while i < len(field_stats):
            stat = field_stats[i]
            if stat > 100:
                area = fields[i]
                if area == "w":
                    self.wealth_stat = 100
                if area == "d":
                    self.defence_stat = 100
                if area == "r":
                    self.religion_stat = 100
                if area == "h":
                    self.happiness_stat = 100
            if stat <= 0: # Player has lost by running out of a certain field
                reason = fields[i]
                return [False, reason] # Player lost
            i += 1
        return [True] # Player is fine and still going


def create_leaderboard(leaderboard_list):
    leaderboard_string = """
==========================================
        Kingdom Rule - Leaderboard                                              
    
"""
    # Sorting leaderboard_list - bubble sort
    if len(leaderboard_list) > 1:
        for loop in range(len(leaderboard_list)): # Needs to loop length - 1 times to complete sort
            i = 0
            while i < len(leaderboard_list)-1: # One complete sort (need to do length - 1 sorts)
                temp = leaderboard_list[i]
                if leaderboard_list[i][1] < leaderboard_list[i+1][1]:
                    leaderboard_list[i] = leaderboard_list[i+1]
                    leaderboard_list[i+1] = temp
                i += 1
    
    i = 0
    while i < len(leaderboard_list): # Adding scores to leaderboard string
        king_name = leaderboard_list[i][0]
        score = leaderboard_list[i][1]
        if score == 1:
            new_score_string = f"   {i+1}) {king_name} - {score} year in power\n"
        else:
            new_score_string = f"   {i+1}) {king_name} - {score} years in power\n"
        leaderboard_string += new_score_string
        i += 1

    leaderboard_string += "\n=========================================="

    return leaderboard_string



def pick_event(years_ruling, events_which_have_occured):
    while True:
        new_event_index = random.randint(0, 19)
        if new_event_index in events_which_have_occured:
            continue
        return new_event_index # Returns an index from 0-19 (all possible event options)


def check_if_wants_to_play():
    while True:
        print("--------------------------------------------------------------------------------\n")
        play_again = input("Enter 'y' to play again and 'q' to quit: ")
        print("\n--------------------------------------------------------------------------------\n")
        if play_again.lower() == "q":
            return False
        elif play_again.lower() == "y":
            print("\nTaking you back to the main menu...\n")
            return True
        else:
            print("Invalid input.\n")