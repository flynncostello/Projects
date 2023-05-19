'''
Write your solution for the class Interface here.
This is your answer for Question 8.4.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

import sys

import hunter
import cshop
import mouse

import game
import game_final
import setup
import name
import train
import shop



def hunt(player, gold: int, cheese: list, trap_cheese: str | None, enchant, points: int) -> tuple:
    hunt_again = True
    unsuccessful_hunt_count = 0
    if trap_cheese != None:
        cur_cheese_info = shop.find_cheese_index(trap_cheese.lower())
        cur_cheese_index = cur_cheese_info[1]
        amount_of_trap_cheese_left = cheese[cur_cheese_index][1]
    else:
        amount_of_trap_cheese_left = 0

    while hunt_again:
        #print(player.cheese)
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
                player.consume_cheese(trap_cheese)
                unsuccessful_hunt_count += 1

            else:
                mouse_image = cur_mouse.mouse_image
                print(f"Caught a {mouse_name} mouse!")
                print(mouse_image)
                player.consume_cheese(trap_cheese)
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







class Interface:
    def __init__(self, menu={"1. Exit game": 1, "2. Join the Hunt": 2, "3. The Cheese Shop": 3, "4. Change Cheese": 4}, player=None):
        self.menu = menu
        self.player = hunter.Hunter()

    def set_player(self, cur_player):
        if isinstance(cur_player, hunter.Hunter):
            self.player = cur_player
    
    def get_menu(self):
        menu_string = """1. Exit game
2. Join the Hunt
3. The Cheese Shop
4. Change Cheese"""
        return menu_string

    def change_cheese(self):
        hunter_name = self.player.get_name()
        trap_name = self.player.trap.__str__()
        cheese_list = self.player.cheese
        # Need to make sure when training is done trap.one_time_enchantment is set to true
        e_flag = self.player.trap.one_time_enchantment
        
        cheese_armed, cheese_type_armed = game.change_cheese(hunter_name, trap_name, cheese_list, e_flag)
        if cheese_armed: # cheese_armed will be True if the player 1) enters a valid cheesem, 2) has a valid trap and 3) has at least 1 or more of the cheese type they entered
            #print(cheese_armed)
            #print(cheese_type_armed)

            self.player.arm_trap(cheese_type_armed)
            #self.player.consume_cheese(cheese_type_armed)
            
            #print(self.player.trap.trap_cheese)
            #print(self.player.trap.arm_status)


    def cheese_shop(self):
        cheese_shop = cshop.CheeseShop()
        greeting = cheese_shop.greet()
        #print(greeting)
        #print()
        cheese_shop.move_to(self.player)
    
    def hunt(self):
        #print(self.player.cheese)
        new_gold, new_points = hunt(self.player, self.player.get_gold(), self.player.cheese, self.player.trap.get_trap_cheese(), self.player.trap.one_time_enchantment, self.player.get_points())
        #def hunt(gold: int, cheese: list, trap_cheese: str | None, enchant, points: int) -> tuple:

        # new_gold and new_points are old gold and points + their new value therefore we just set points and gold to these new values
        self.player.trap.set_one_time_enchantment(False)
        self.player.set_gold(new_gold)
        self.player.set_points(new_points)


    def move_to(self, main_menu_choice):
        try:
            main_menu_choice = int(main_menu_choice)
            if main_menu_choice < 1 or main_menu_choice > 4:
                print("Must be within 1 and 4.")
                return "Invalid"
            else:
                if main_menu_choice == 1:
                    return False # Wants to quit the game
                elif main_menu_choice == 2:
                    Interface.hunt(self) # Hunting
                    #print(self.player.cheese)
                    return True
                elif main_menu_choice == 3:
                    print("""Welcome to The Cheese Shop!
Cheddar - 10 gold
Marble - 50 gold
Swiss - 100 gold
""")
                    Interface.cheese_shop(self) # Accessing Cheese shop
                    return True
                else: # main_menu_choice == 4
                    Interface.change_cheese(self) # Changing cheese on trap
                    #print(self.player.trap.get_trap_cheese())
                    return True
        except ValueError:
            print("Invalid input. Try again!")
            return "Invalid" # Needs to get a new input

"""
a = hunter.Hunter()
a.set_name("Pokemon")
a.set_cheese((3, 3, 3))
a.trap.set_trap_name("Hot Tub Trap")
a.trap.one_time_enchantment = True
b = Interface()
b.set_player(a)
#b.move_to("4")
b.cheese_shop()
"""



"""
b = hunter.Hunter()
b.set_cheese((3, 3, 3))
b.trap.set_trap_name("High Strain Steel Trap")
a = Interface()
a.set_player(b)
print(a.get_menu())
a.move_to("back")
"""

"""
while True:
    try:
        choice = int(input(""))
        break
    except ValueError:
        print("Invalid Input")

while choice != "":
    a.move_to(choice)
    while True:
        try:
            choice = int(input("Enter main menu input: "))
            break
        except ValueError:
            print("Invalid Input")

"""




