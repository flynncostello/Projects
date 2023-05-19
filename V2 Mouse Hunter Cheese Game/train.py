'''
Answer for Question 5 - The Training Again from Assignment 1.

Author: Flynn Costello
SID: 530488477
unikey: fcos0917
'''

# you can make more functions or global read-only variables here if you please!
"""
Specifications:
- Inputs for skip (ESC+Enter) are case insensitive and ignore trailing and leading whitespaces
- 

"""

import training_functions

def main():
    '''
    Implement your code here.
    ''' 
    trap, quit_to_main_menu = training_functions.main()
    if quit_to_main_menu:
        return trap

    """Calling main once to include welcome text
    returns trap so that it can be passed to game.py later"""

    continue_game = input("\nPress Enter to continue training and \"no\" to stop training: ").strip().lower()
    amount = training_functions.get_ord(continue_game)
    
    while continue_game != "no" and amount != 27: # will continue until user wants to stop
        setup_trap_quit, trap, cheddar = training_functions.setup_trap()
        if setup_trap_quit:
            return trap
        else:
            sound_horn_quit, horn_input = training_functions.sound_horn()
            if sound_horn_quit:
                return trap
            else:
                hunt_status = training_functions.basic_hunt(cheddar, horn_input)
                training_functions.end(hunt_status)

        continue_game = input("\nPress Enter to continue training and \"no\" to stop training: ").strip().lower()
        amount = training_functions.get_ord(continue_game)


    return trap


if __name__ == '__main__':
    main()
