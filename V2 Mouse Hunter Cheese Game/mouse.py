'''
Write solutions to 3. New Mouse Release here.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

'''
Keep this line!
'''
import random
import art

TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")

def generate_probabilities(cheese_type, enchant=False):
    cheese = cheese_type.lower()
    if cheese == "cheddar":
        probabilities_tuple = (0.5, 0.1, 0.15, 0.1, 0.1, 0.05)
    
    if cheese == "marble":
        probabilities_tuple = (0.6, 0.05, 0.2, 0.05, 0.02, 0.08)

    if cheese == "swiss" and enchant:
        probabilities_tuple = (0.45, 0.01, 0.05, 0.05, 0.04, 0.4)
    
    if cheese == "swiss" and not(enchant):
        probabilities_tuple = (0.7, 0.01, 0.05, 0.05, 0.04, 0.15)

    return probabilities_tuple # 1x6 (prob NOT generating a mouse, P(mouse 1), ...)

def accumulated_prob(index, probability_tuple):
    i = 0
    total = 0
    while i <= index:
        total += probability_tuple[i]
        i += 1
    return total

#print(accumulated_prob(3, (0.7, 0.01, 0.05, 0.05, 0.04, 0.15)))

def generate_mouse(cheese="Cheddar", enchant=False) -> str | None:
    '''
    Spawn a random mouse during a hunt depending on cheese type
    Hint: You should be using TYPE_OF_MOUSE in this function.
    Returns:
        spawn_mouse: str | None, type of mouse
    '''
    cheese = cheese.lower()
    cheese_probability_tuple = generate_probabilities(cheese, enchant)
    prob = random.random() # probability between 0.0 and 1.0
    # Expect Brown get a Field
    #print(cheese)
    #print(cheese_probability_tuple)
    #print(prob)
    if prob <= accumulated_prob(0, cheese_probability_tuple) and prob >= 0.0:
        spawn_mouse = TYPE_OF_MOUSE[0] # No Mouse

    elif prob <= accumulated_prob(1, cheese_probability_tuple):
        spawn_mouse = TYPE_OF_MOUSE[1] # Brown

    elif prob <= accumulated_prob(2, cheese_probability_tuple):
        spawn_mouse = TYPE_OF_MOUSE[2] # Field

    elif prob <= accumulated_prob(3, cheese_probability_tuple):
        spawn_mouse = TYPE_OF_MOUSE[3] # Grey

    elif prob <= accumulated_prob(4, cheese_probability_tuple):
        spawn_mouse = TYPE_OF_MOUSE[4] # White

    else:
        spawn_mouse = TYPE_OF_MOUSE[5] # Tiny

    return spawn_mouse

#print(generate_mouse("swiss", True))


def generate_coat(mouse_type):
    mouse_name = mouse_type.lower()
    if mouse_name == "brown":
        mouse_image = art.BROWN

    elif mouse_name == "field":
        mouse_image = art.FIELD

    elif mouse_name == "grey":
        mouse_image = art.GREY

    elif mouse_name == "white":
        mouse_image = art.WHITE

    else: # mouse_image == "tiny"
        mouse_image = art.TINY

    return mouse_image




def loot_lut(mouse_type: str | None) -> tuple:
    '''
    Look-up-table for gold and points for different types of mouse
    Parameter:
        mouse_type: str | None, type of mouse
    Returns:
        gold:       int, amount of gold reward for mouse
        points:     int, amount of points given for mouse
    '''
    look_up_table = ((None, 0, 0), ("Brown", 125, 115), ("Field", 200, 200), ("Grey", 125, 90), ("White", 100, 70), ("Tiny", 900, 200))
    i = 0
    while i < len(look_up_table):
        if look_up_table[i][0] == mouse_type:
            gold = look_up_table[i][1]
            points = look_up_table[i][2]
        i += 1
        
    return (gold, points)


class Mouse:
    def __init__(self, cheese="Cheddar", enchant=False):
        self.cheese = cheese
        self.enchant = enchant
        self.name = generate_mouse(self.cheese, self.enchant)
        self.gold, self.points = loot_lut(self.name)
        if self.name != None:
            self.mouse_image = generate_coat(self.name)
    
    def get_final_points_and_gold(self):
        if self.cheese == "Cheddar" and self.name == "Brown" and self.enchant:
            self.points = self.points + 25

        if self.cheese == "Marble" and self.name == "Brown" and self.enchant:
            self.gold = self.gold + 25
        
        return (self.gold, self.points)  

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold
    
    def get_points(self) -> int:
        return self.points
    
    def __str__(self) -> str:
        if self.name == None:
            return "None"
        return self.name





