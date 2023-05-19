'''
Write your solution to 1. Upgraded Cheese Shop here.
It should borrow code from Assignment 1.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))

# you can make more functions or global read-only variables here if you please!

def calculate_cost(cheese_index, quantity):
    # finding cheese index in CHEESE_MENU
    cost = CHEESE_MENU[cheese_index][1] * quantity
    return cost

def find_cheese_index(cheese_name):
    i = 0
    # Checking if cheese entered is valid
    while i < len(CHEESE_MENU):
        if cheese_name == CHEESE_MENU[i][0].lower():
            return (True, i)
        i += 1
    return (False, i)




def buy_cheese(gold: int) -> tuple:
    '''
    Feature for players to buy cheese from shop.
    Parameters:
        gold:           int,    amount of gold that player has
    Returns:
        gold_spent:     int,    amount of gold spent
        cheese_bought:  tuple,  amount of each type of cheese bought
    '''
    # first error message is only error message
    # Cheese errors take priority (i.e., If both, cheese error first)
    # Even if invalid input is given keep being promted to buy more cheese
    # Only way to leave cheese shop is by entering "back" command
    # Commands are case insensitive (i.e., use .lower())
    # Cheese are single words
    cur_gold = gold
    gold_spent = 0 # Initially no gold spent
    cheeses_bought_list = [0, 0, 0] # Initially no cheese bought

    print(f"You have {cur_gold} gold to spend.")

    shop_input = input("State [cheese quantity]: ") # 2 items
    while shop_input.lower() != "back":
        split_shop_input = shop_input.split()
        if shop_input == "":
            cheese = ""
            valid_cheese = False
        else:
            cheese = split_shop_input[0].lower()
            valid_cheese, cheese_index = find_cheese_index(cheese)

        if not(valid_cheese): # Invalid cheese
            print(f"We don't sell {cheese}!")
        else: # Valid Cheese
            # Valid cheese missing quantity
            if len(split_shop_input) < 2:
                print("Missing quantity.")
            else:
                quantity = split_shop_input[1]
                try:
                    quantity_int = int(quantity)
                    if quantity_int <= 0:
                        # Valid cheese, invalid quantity (<= 0)
                        print("Must purchase positive amount of cheese.")
                    else:
                        cost = calculate_cost(cheese_index, quantity_int)
                        new_gold = cur_gold - cost
                        if new_gold < 0:
                            print("Insufficient gold.")
                        else:
                            gold_spent += cost
                            cheeses_bought_list[cheese_index] += quantity_int
                            cur_gold -= cost
                            print(f"Successfully purchase {quantity} {cheese}.")

                except ValueError:
                    # Valid cheese invalid quantity
                    print("Invalid quantity.")

        # New order        
        print(f"You have {cur_gold} gold to spend.")
        shop_input = input("State [cheese quantity]: ")

    cheeses_bought_tuple = tuple(cheeses_bought_list)
    #print(gold_spent, cheeses_bought_tuple)
    return (gold_spent, cheeses_bought_tuple)

#buy_cheese(125)


def display_inventory(gold: int, cheese: list, trap: str) -> None:
    '''
    Displays contents of inventory.
    Parameters:
        gold:   int,  amount of gold that player has
        cheese: list, amount of each type of cheese that player has
        trap:   str,  name of trap that player that player has
    '''
    inventory_string = f"""Gold - {gold}
Cheddar - {cheese[0][1]}
Marble - {cheese[1][1]}
Swiss - {cheese[2][1]}
Trap - {trap}"""
    print(inventory_string)


def main():
    gold = 125
    cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
    trap = 'Cardboard and Hook Trap'
    # TODO: Add code here

    print("""Welcome to The Cheese Shop!
Cheddar - 10 gold
Marble - 50 gold
Swiss - 100 gold

How can I help ye?
1. Buy cheese
2. View inventory
3. Leave shop""")
    main_choice = int(input(""))
    while main_choice != 3:
        if main_choice == 1: # 1 - Buy cheese
            gold_spent, cheeses_bought_tuple = buy_cheese(gold) # return a tuple, (gold_spent, quantity)
            #print(gold_spent, cheeses_bought_tuple)
            gold -= gold_spent
            i = 0
            while i < len(cheese):
                cheese[i][1] += cheeses_bought_tuple[i]
                i += 1

        else: # 2 - View inventory
            display_inventory(gold, cheese, trap)

        print("""
How can I help ye?
1. Buy cheese
2. View inventory
3. Leave shop""")
        main_choice = int(input(""))


if __name__ == "__main__":
    main()
