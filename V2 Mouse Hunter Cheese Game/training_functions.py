'''
Name: Flynn Costello
SID: 530488477
unikey: fcos0917
'''

def get_ord(ord_input): # Gets length of ascii input
    # If input isn't a character will return amount = 0
    try: # Some inputs won't be characters like ^[
        amount = ord(ord_input)
    except TypeError:
        amount = 0
    return amount

def intro():
    '''
    Prints the introduction by Larry.
    Only line to print:     "Larry: I'm Larry. I'll be your hunting instructor."
    '''
    print("Larry: I'm Larry. I'll be your hunting instructor.")


def travel_to_camp():
    '''
    Prints the game conversation of travelling and reaching the camp.
    First line to print:    "Larry: Let's go to the Meadow to begin your training!"
    Last line to print:     "Larry: This is your camp. Here you'll set up your mouse trap."
    Input from the user should be taken in once in this function.
    '''
    print("Larry: Let's go to the Meadow to begin your training!")
    travel_to_meadow = input("Press Enter to travel to the Meadow...")
    amount = get_ord(travel_to_meadow)
    #print(amount)
    if amount == 27:
        return True

    print("""Travelling to the Meadow...
Larry: This is your camp. Here you'll set up your mouse trap.""")
    return False

def setup_trap() -> tuple:
    '''
    Prints the game conversation of getting your first trap and setting it.
    First line to print:    "Larry: Let's get your first trap..."
    Last line to print:     Either "Larry places one cheddar on the trap!", or
                            "Larry: Odds are slim with no trap!" depending on if you 
                            chose a trap or not. 
    Input from the user should be taken in twice this function.
    Returns:
        A tuple containing 2 elements:
        1. trap,            str
            - If a trap was chosen, the value is the name of the trap
              e.g. 'High Strain Steel Trap'
            - If no trap was chosen, the value is 'Cardboard and Hook Trap'
              (this will be useful in later questions)
        2. cheddar,         int
            - If a cheese was placed, value is 1
            - If no cheese was placed, value is 0
    '''

    print("Larry: Let's get your first trap...")
    view_traps = input("Press Enter to view traps that Larry is holding...")
    
    amount = get_ord(view_traps)
    if amount == 27:
        return [True, "Cardboard and Hook Trap", 0]

    print("""Larry is holding...
Left: High Strain Steel Trap
Right: Hot Tub Trap""")

    selected_trap = input("Select a trap by typing \"left\" or \"right\": ").strip().lower()
    
    amount = get_ord(selected_trap)
    if amount == 27:
        return [True, "Cardboard and Hook Trap", 0]

    if selected_trap != "right" and selected_trap != "left":
        print("Invalid command! No trap selected.")
        print("Larry: Odds are slim with no trap!")
        trap = "Cardboard and Hook Trap"
        cheddar = 0 # No cheese placed
    else:
        if selected_trap == "right":
            trap = "Hot Tub Trap"
        else: # left
            trap = "High Strain Steel Trap"
        cheddar = 1 # 1 Cheese placed

        print(f"""Larry: Excellent choice.
Your "{trap}" is now set!
Larry: You need cheese to attract a mouse.
Larry places one cheddar on the trap!""")

    return [False, trap, cheddar]


def sound_horn() -> str:
    '''
    Prints the game conversation to sound horn
    First line to print:    "Sound the horn to call for the mouse..."
    Last line to print:     'Sound the horn by typing "yes": '
    Input from the user should be taken in once this function.
    Returns:
        horn input:     str, the input entered by user for sounding horn
        e.g. 'yes'
        e.g. 'asdhasjkhdsa'
    '''
    print("Sound the horn to call for the mouse...")
    horn_input = input("Sound the horn by typing \"yes\": ").strip().lower()

    amount = get_ord(horn_input)
    if amount == 27:
        return [True, horn_input]

    return [False, horn_input]


def basic_hunt(cheddar: int, horn_input: str) -> bool:  
    '''
    Prints the hunt and Larry's feedback of hunt.
    The outcome of hunt is determined by the number of cheddar and horn input.
    First line to print:    Varies depending on the hunt. Could be "Caught a Brown
                            Mouse!" or "Nothing happens."
    Last line to print:     Varies depending on the hunt like above.
    Parameters:
        cheddar:        int, the number of cheddar
        horn_input:     str, the input entered by user for sounding horn
    Returns:
        hunt status:    bool, whether the hunt succeeded or not
    '''

    if horn_input == "yes" and cheddar >= 1: # if cheddar >= 1 then trap is armed
        print("""Caught a Brown mouse!
Congratulations. Ye have completed the training.""")
        hunt_status = True

    elif horn_input == "yes" and cheddar < 1:
        print("""Nothing happens.
To catch a mouse, you need both trap and cheese!""")
        hunt_status = False

    elif horn_input != "yes" and cheddar >= 1:
        print("""Nothing happens.
To catch a mouse, you need both trap and cheese!""")
        hunt_status = False

    else:
        print("""Nothing happens.""")
        hunt_status = False

    return hunt_status


def end(hunt_status: bool):
    '''
    Prints the 'Good luck~' message if hunt was successful
    Parameters:
        hunt_status:    bool, whether the hunt succeeded or not
    '''
    if hunt_status:
        print("Good luck~")
    

def main():
    '''
    Call your functions here.
    Apart from good design, this is so if you import this file in train.py 
    (question 5), it will not run this code. Because this code's __name__ 
    will not be '__main__', but it will instead be 'q4', allowing you to
    import this file to use your functions without running unwanted calling code.
    ''' 
    trap = "Cardboard and Hook Trap"
    intro()

    travel_quit = travel_to_camp()
    if travel_quit:
        return [trap, travel_quit]
    else:
        setup_trap_quit, trap, cheddar = setup_trap() # add argument
        if setup_trap_quit:
            return [trap, setup_trap_quit]
        else:
            sound_horn_quit, horn_input = sound_horn()
            if sound_horn_quit:
                return [trap, sound_horn_quit]
            else:
                hunt_status = basic_hunt(cheddar, horn_input)
                end(hunt_status)
                return [trap, False] # False as they didn't press ESC to quit back to main menu options

'''
This statement is true if you run this script.
This statement is false if this file is to be imported from another script. 
'''
if __name__ == '__main__':
    main()
