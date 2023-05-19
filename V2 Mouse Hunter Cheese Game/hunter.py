'''
Write your solution for the class Hunter here.
This is your answer for Question 8.2.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

import name
import trap

class Hunter:
    def __init__(self, name="Bob", cheese=[["Cheddar", 0], ["Marble", 0], ["Swiss", 0]], gold=125, points=0):
        self.name = name
        self.cheese = cheese
        self.trap = trap.Trap()
        self.gold = gold
        self.points = points
    
    def set_name(self, player_name):
        valid_name = name.is_valid_name(player_name)
        if valid_name:
            self.name = player_name
    
    def set_cheese(self, cheese_quantity_tuple):
        if isinstance(cheese_quantity_tuple, tuple):
            i = 0
            while i < len(cheese_quantity_tuple):
                self.cheese[i][1] = cheese_quantity_tuple[i]
                i += 1
    
    def set_gold(self, new_value_of_gold):
        if isinstance(new_value_of_gold, int):
            self.gold = new_value_of_gold
    
    def set_points(self, new_value_of_points):
        if isinstance(new_value_of_points, int):
            self.points = new_value_of_points
    
    def get_name(self):
        return self.name
    
    def get_cheese(self):
        cheese_string = f"""Cheddar - {self.cheese[0][1]}
Marble - {self.cheese[1][1]}
Swiss - {self.cheese[2][1]}"""
        return cheese_string
    
    def get_gold(self):
        return self.gold
    
    def get_points(self):
        return self.points
    
    def update_cheese(self, new_cheese_values_tuple): # Adds new cheese quantities to hunter's cheese array 
        if isinstance(new_cheese_values_tuple, tuple):
            i = 0
            while i < len(new_cheese_values_tuple):
                self.cheese[i][1] += new_cheese_values_tuple[i]
                i += 1
    
    def consume_cheese(self, type_of_cheese_to_consume):
        cheese = type_of_cheese_to_consume.strip().lower()
        if cheese == "cheddar":
            self.cheese[0][1] -= 1
        elif cheese == "marble":
            self.cheese[1][1] -= 1
        elif cheese == "swiss":
            self.cheese[2][1] -= 1
        else:
            pass
    
    def have_cheese(self, type_of_cheese="Cheddar"):
        # Returns 0 if you don't have any of the type_of_cheese, else it returns how many you have
        if isinstance(type_of_cheese, str):
            i = 0
            while i < len(self.cheese):
                if self.cheese[i][0].lower() == type_of_cheese.lower():
                    return self.cheese[i][1]
                i += 1
            return 0
        else:
            return 0
    
    def display_inventory(self):
        trap_cur_name = self.trap.__str__()
        inventory_string = f"""Gold - {self.gold}
{Hunter.get_cheese(self)}
Trap - {trap_cur_name}"""
        return inventory_string
    
    def arm_trap(self, type_of_cheese_to_arm):
        cheese = type_of_cheese_to_arm
        if cheese == "Cheddar" and Hunter.have_cheese(self, type_of_cheese="Cheddar") > 0:
            self.trap.set_trap_cheese(cheese)
            self.trap.set_arm_status()
        elif cheese == "Marble" and Hunter.have_cheese(self, type_of_cheese="Marble") > 0:
            self.trap.set_trap_cheese(cheese)
            self.trap.set_arm_status()
        elif cheese == "Swiss" and Hunter.have_cheese(self, type_of_cheese="Swiss") > 0:
            self.trap.set_trap_cheese(cheese)
            self.trap.set_arm_status()
        else:
            self.trap.set_trap_cheese(None)
            self.trap.set_arm_status()


    def update_gold(self, added_gold):
        if isinstance(added_gold, int):
            self.gold += added_gold
    
    def update_points(self, added_points):
        if isinstance(added_points, int):
            self.points += added_points

    def __str__(self):
        output_string = f"""Hunter {self.name}
Gold - {self.gold}
Cheddar - {self.cheese[0][1]}
Marble - {self.cheese[1][1]}
Swiss - {self.cheese[2][1]}
Trap - {self.trap.trap_name}"""
        return output_string


"""
a = Hunter()
a.arm_trap("Marble")
a.trap.set_trap_name("Cardboard and Hook Trap")

print(a.trap.trap_name)
print(a.trap.trap_cheese)
print(a.trap.arm_status)
print(a.trap.one_time_enchantment)
"""









