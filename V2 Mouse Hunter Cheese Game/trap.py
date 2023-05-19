'''
Write your solution for the class Trap here.
This is your answer for Question 8.1.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

import mouse
import game_final

class Trap:
    def __init__(self, trap_name="", trap_cheese=None, arm_status=False, one_time_enchantment=False):
        self.trap_name = trap_name
        self.trap_cheese = trap_cheese # If not None and cheese is in inventory
        self.arm_status = arm_status # If is True (True of False)
        """
        If a trap is armed with a trap_cheese that is not None and players
        have the cheese in their inventory, players will have a chance to
        successfully attract a mouse when they sound the horn 
        """
        self.one_time_enchantment = one_time_enchantment

    def set_trap_name(self, name):
        valid_traps = ["Cardboard and Hook Trap", "High Strain Steel Trap", "Hot Tub Trap"]
        i = 0
        name_is_valid = False
        while i < len(valid_traps):
            if valid_traps[i] == name:
                name_is_valid = True
            i += 1

        if name_is_valid:
            self.trap_name = name

    def set_trap_cheese(self, cheese):
        if cheese == "Cheddar":
            self.trap_cheese = "Cheddar"
        elif cheese == "Marble":
            self.trap_cheese = "Marble"
        elif cheese == "Swiss":
            self.trap_cheese = "Swiss"
        else:
            self.trap_cheese = None
    

    def set_arm_status(self):
        cheese = self.trap_cheese
        trap = self.trap_name
        if cheese == "Cheddar" or cheese == "Marble" or cheese == "Swiss":
            if trap == "Cardboard and Hook Trap" or trap == "High Strain Steel Trap" or trap == "Hot Tub Trap":
                self.arm_status = True
            else:
                self.arm_status = False
        else:
            self.arm_status = False
    
    def set_one_time_enchantment(self, e_flag):
        if self.trap_name != "Cardboard and Hook Trap" and e_flag:
            self.one_time_enchantment = True
        else:
            self.one_time_enchantment = False

    def get_trap_name(self):
        return self.trap_name
    
    def get_trap_cheese(self):
        return self.trap_cheese
    
    def get_arm_status(self):
        return self.arm_status
    
    def get_one_time_enchantment(self):
        return self.one_time_enchantment
    
    def get_benefit(cheese):
        benefit_string = game_final.get_benefit(cheese)
        return benefit_string
    
    def __str__(self): # Prints the traps name
        if self.one_time_enchantment:
            trap_name_string = f"One-time Enchanted {self.trap_name}"
        else:
            trap_name_string = self.trap_name
        return trap_name_string


"""
trap1 = Trap()
trap1.set_trap_cheese("Marble")
trap1.set_trap_name("Cardboard and Hook Trap")
trap1.set_arm_status()
print(trap1.get_trap_cheese())
print(trap1.get_arm_status())
"""












