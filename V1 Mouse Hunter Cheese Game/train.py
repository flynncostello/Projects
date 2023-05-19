'''
Answer for Question 5 - The Training Again

Name: Flynn Costello
SID: 530488477
unikey: fcos0917
'''

'''
We recommend you import your 'q4' module to complete this question. It will save 
trouble in needing to copy and paste code from previous question. However if you 
wish not to, you are free to remove the import below.
'''
import q4

# you can make more functions here if you please
# or any global variables

def main():
    trap = q4.main()
    #print(trap)
    """Calling main once to include welcome text
    returns trap so that it can be passed to game.py later"""

    continue_game = input("\nPress Enter to continue training and \"no\" to stop training: ").strip().lower()
    while continue_game == "": # will continue until user wants to stop
        trap, cheddar = q4.setup_trap()
        horn_input = q4.sound_horn()
        hunt_status = q4.basic_hunt(cheddar, horn_input)
        q4.end(hunt_status)
        continue_game = input("\nPress Enter to continue training and \"no\" to stop training: ").strip().lower()
    return trap
    
if __name__ == '__main__':
    main()
