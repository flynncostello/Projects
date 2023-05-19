'''
Write your solution for the class CheeseShop here.
This is your answer for Question 8.3.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

import shop
import hunter
import trap

class CheeseShop:
    def __init__(self, cheeses={"Cheddar": 10, "Marble": 50, "Swiss": 100}, menu = {"1. Buy cheese": 1, "2. View inventory": 2, "3. Leave shop": 3}):
        self.cheeses = cheeses
        self.menu = menu
    
    def get_cheeses(self):
        cheese_string = f"""Cheddar - {self.cheeses["Cheddar"]} gold
Marble - {self.cheeses["Marble"]} gold
Swiss - {self.cheeses["Swiss"]} gold"""
        return cheese_string
    
    def get_menu(self):
        menu_string = """1. Buy cheese
2. View inventory
3. Leave shop"""
        return menu_string
    
    def greet(self):
        cheese_shop_welcome_string = f"""Welcome to The Cheese Shop!
{CheeseShop.get_cheeses(self)}"""
        return cheese_shop_welcome_string

    def buy_cheese(self, gold_amount):
        if isinstance(gold_amount, int):
            gold_spent, cheeses_bought_tuple = shop.buy_cheese(gold_amount)
            #print(gold_spent)
            #print(cheeses_bought_tuple)
            gold_left = gold_amount - gold_spent
            return (gold_left, cheeses_bought_tuple)


    
    def move_to(self, hunter):
        """
        1. Buy Cheese
        2. View Inventory
        3. Leave Shop
        """
        #print(CheeseShop.greet(self))
        stay_in_shop = True
        while stay_in_shop:
            print("How can I help ye?")
            print(CheeseShop.get_menu(self))

            cheese_shop_choice = input("")
            if cheese_shop_choice.isdigit():
                cheese_shop_choice = int(cheese_shop_choice)
                if cheese_shop_choice < 1 or cheese_shop_choice > 3:
                    raise ValueError
                else:
                    if cheese_shop_choice == 1:
                        gold_left, cheeses_bought_tuple = CheeseShop.buy_cheese(self, hunter.get_gold())
                        hunter.update_cheese(cheeses_bought_tuple)
                        hunter.gold = gold_left
                        #print(hunter.__str__())
                        print()

                    elif cheese_shop_choice == 2:
                        print(hunter.display_inventory())
                        print()

                    else: # 3
                        stay_in_shop = False # Leaving the shop
                        #print(stay_in_shop)
            else: # Non integer given
                print("I did not understand.")
                print()
            

"""
a = CheeseShop()
b = hunter.Hunter()
a.move_to(b)
"""



