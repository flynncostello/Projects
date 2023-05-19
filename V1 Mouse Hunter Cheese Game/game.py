'''
Answer for Question 7 - PIAT: The Hunt

Name: Flynn Costello
SID: 530488477
unikey: fcos0917
'''

'''
Keep this line!
'''
import random

'''
We recommend you import your 'name', 'train' and 'shop' modules to complete this 
question. It will save trouble in needing to copy and paste code from previous 
questions. However if you wish not to, you are free to remove the imports below.
Feel free to import other modules that you have written.
'''
import name
import train
import shop

# you can make more functions here if you please
# or any global variables

title = "Mousehunt"

logo = """
       ____()()
      /      @@
`~~~~~\_;m__m._>o"""

author = 'An INFO1110/COMP9001 Student'

credits = f'''
Inspired by Mousehunt© Hitgrab
Programmer - {author}
Mice art - Joan Stark'''

final_intro_string = f"{title}\n{logo}\n{credits}"



def the_hunt(player_name, gold, cheddar, points):
    hunt_again = True
    unsuccessful_hunt_count = 0
    while hunt_again:
        print("Sound the horn to call for the mouse...")
        sound_horn = input("Sound the horn by typing \"yes\": ")

        if sound_horn == "stop hunt":
            hunt_again = False
            unsuccessful_hunt_count = 0
        elif sound_horn != "yes":
            print("Do nothing.")
            unsuccessful_hunt_count += 1
        elif cheddar < 1:
            print("Nothing happens. You are out of cheese!")
            unsuccessful_hunt_count += 1
        else:
            mouse_odds = random.random() 
            if mouse_odds > 0.5:
                print("Nothing happens.")
                cheddar -= 1
                unsuccessful_hunt_count += 1
            else:
                print("Caught a Brown mouse!")
                cheddar -= 1
                gold += 125
                points += 115
                unsuccessful_hunt_count = 0

        if hunt_again: # This shouldn't print if the user inputted "stop hunt"  
            print(f"My gold: {gold}, My points: {points}\n")
        
        if unsuccessful_hunt_count >= 5 and hunt_again == True:
            continue_hunt = input("Do you want to continue to hunt? ")
            if continue_hunt == "no":
                hunt_again = False
            unsuccessful_hunt_count = 0

    return gold, cheddar, points



def using_shop(gold, cheddar, trap):
    print("""Welcome to The Cheese Shop!
Cheddar - 10 gold""")
    options ="""
How can I help ye?
1. Buy cheese
2. View inventory
3. Leave shop"""

    print(options)
    shop_choice = int(input(""))

    while shop_choice != 3:
        if shop_choice == 2:
            shop.display_inventory(gold, cheddar, trap)
        else: # 1
            gold_spent, quantity = shop.buy_cheese(gold)
            gold -= gold_spent # Removing total money spent at shop from total gold storage
            cheddar += quantity # Adding newely purchased cheese to total cheese storage

        print(options)
        shop_choice = int(input(""))
    
    return gold, cheddar


def action_menu(player_name, trap):
    """
    Runs once the user enters skip or finishes the training

    Inputs:
        player_name - players name
    Outputs:

    """
    gold = 125
    cheddar = 0
    points = 0
    play_game_again = True
    
    while play_game_again:
        print(f"""
What do ye want to do now, Hunter {player_name}?
1. Exit game
2. Join the Hunt
3. The Cheese Shop""")
        game_choice = int(input(""))

        if game_choice == 2:
            gold, cheddar, points = the_hunt(player_name, gold, cheddar, points)
        elif game_choice == 3:
            gold, cheddar = using_shop(gold, cheddar, trap)
        else:
            break



def main():
    print(final_intro_string)

    player_name = input("\nWhat's ye name, Hunter?\n")

    name_is_valid = name.is_valid_name(player_name)

    if name_is_valid:
        print(f"Welcome to the Kingdom, Hunter {player_name}!")
    else:
        player_name = "Bob"
        print(f"Welcome to the Kingdom, Hunter {player_name}!")

    print("Before we begin, let's train you up!")
    start_game_choice = input("Press \"Enter\" to start training or \"skip\" to Start Game: ").lower()

    if start_game_choice != "skip":
        print()
        trap = train.main() # trap is retained from training stage
        #print(trap)
    else:
        trap = "Cardboard and Hook Trap" # If player doesn't complete the tutorial

    # Now starting main game
    action_menu(player_name, trap)




if __name__ == '__main__':
    main()




