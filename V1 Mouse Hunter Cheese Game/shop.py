'''
Answer for Question 6 - PIAT: The Cheese Shop

Name: Flynn Costello
SID: 530488477
unikey: fcos0917
'''

def buy_cheese(gold: int) -> tuple:
    '''
    Feature for players to buy cheddar from shop
    Parameters:
        gold:           int, amount of gold player has
    Returns:
        gold_spent:     int, amount of gold spent
        cheese_bought:  int, amount of cheese bought
    '''
    print(f"You have {gold} gold to spend.")
    purchase_info = input("State [cheese quantity]: ").lower().strip()
    if purchase_info == "back": # wants to leave
        return (0, 0)
    else: # has purchased something
        splitted_purchase_info = purchase_info.split()
        if len(splitted_purchase_info) != 2:
            print("Sorry, did not understand.")
            return (0, 0)

        cheese_type = splitted_purchase_info[0]
        quantity = int(splitted_purchase_info[1])

        if quantity < 0:
            print("Must purchase a positive amount of cheese.")
            return (0, 0)

        if cheese_type != "cheddar":
            print("Sorry, did not understand.")
            return (0, 0)

        gold_spent = 10 * quantity

        if gold_spent > gold:
            print("Insufficient gold.")
            return (0, 0)

        else:
            print(f"Successfully purchase {quantity} cheddar.")
        
        return (gold_spent, quantity)


def display_inventory(gold: int, cheese: int, trap: str) -> None:
    '''
    Prints contents of inventory
    Parameters:
        gold:    int, amount of gold that player has
        cheese:  int, amount of cheese that player has
        trap:    str, name of trap that player has
    '''
    print(f"""Gold - {gold}
Cheddar - {cheese}
Trap - {trap}""")

# you can make more functions here if you please
# or any global variables

def main():
    '''
    Implement your code here.
    '''
    gold = 125
    cheese = 0
    trap = "Cardboard and Hook Trap"
    print("""Welcome to The Cheese Shop!
Cheddar - 10 gold

How can I help ye?
1. Buy cheese
2. View inventory
3. Leave shop""")
    main_choice = int(input(""))
    while main_choice != 3:
        if main_choice == 1: # 1 - Buy cheese
            gold_spend, quantity_purchased = buy_cheese(gold) # return a tuple, (gold_spent, quantity)
            gold -= gold_spend
            cheese += quantity_purchased

        else: # 2 - View inventory
            display_inventory(gold, cheese, trap)

        print("""
How can I help ye?
1. Buy cheese
2. View inventory
3. Leave shop""")
        main_choice = int(input(""))
    
if __name__ == '__main__':
    main()
