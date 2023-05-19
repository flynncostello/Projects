import adv_art

def adventure_game():
    # Invalid Choice
    invalid_choice = """Invalid choice, try again.
    """

    # Original introduction to game, printed only the first time the game is accessed
    print('''
    **************************
    * Welcome to Cave Escape *
    **************************

    Game now beginning...
    =====================


    You wake up in a mine. 
    The air is cold and you are starving.
    You can't remember what had happened to you.

    You see a table behind you with three items
    1) pickaxe 2) gas mask 3) torch
    {}{}{}
    Before you have time to take a breath you see a massive, hairy, grotesque, black spider 
    crawling out from a crack in the walls.
    You only have seconds to spare, which item do you choose?
    (Enter 1, 2 or 3 for corresponding item)
    '''.format(adv_art.pickaxe, adv_art.gas_mask, adv_art.torch))
    print(adv_art.spider)

    # Amount of times the game has been played (used to change intro)
    attempt_no = 0

    # Used to see if player wants to play again at end of code
    contin = True




    # Loop for all paths of game
    while True:

        if attempt_no > 0:
            print('''
    Choose your item:
    1) pickaxe 2) gas mask 3) torch
    ''')

        # First Decision (item)

        item = input("> ")
        print()

        # Checking to see if item is valid. If it not valid it will as for an item again
        if item != "1" and item != "2" and item != "3":
            print("That's not an item, try again.")
            print()
            continue

        # Item is valid player chooses direction to go
        print("""
    Run!
    Quickly which way do you go, 1) right, 2) left or 3) do nothing
    (Enter 1, 2 or 3)""")
        print()


        # Second Decision (direction)

        while True:

            # Direction the player chooses
            choice2 = input("> ")
            print()

            # Direction = Do nothing
            if choice2 == "3":
                print('''
    For some reason doing nothing didn't work. The spider ate you. 
    Game Over!''')
                print()

            # Direction = Left
            elif choice2 == "2":
                print("""
    Dead End. The spider ate you. Game Over!""")
                print()
            
            # Direction == Right
            elif choice2 == "1":
                
                # Next player choose
                print('''
    You escaped from the spider for now.
    Once exiting the original tunnel you are now faced with three choices.

    1) Go into the spider lair 
    2) Try to climb the cliff face 
    3) Get into a mine-cart and ride it down into the unknown 
    (Enter 1, 2 or 3)
    ''')
            







                # Third Decision (within right direction)

                while True:
                    # choice3 = path player wants to take (1,2 or 3)
                    choice3 = input("> ")
                    print()

                    # Spider Lair
                    if choice3 == "1":

                        # If the player originally chose the pickaxe as their item they will escape
                        if item == "1":
                            print('''
    Once entering the lair you find youself 
    faced against more of those disgusting spiders.
    {}
    Luckily you made sure to take that pickaxe.
    After fighting your way through hoards of spider
    you can see a light at the end of the lair. You have found a way out.

    You Win!
            '''.format(adv_art.cobweb))
                        # Player did not choose pickaxe as item
                        else:
                            print('''
    Once entering the cave you were greeted by hundreds 
    of those spiders. You were never seen again.
    {}
    Game Over!              
        '''.format(adv_art.cobweb))

                    # Cliff-face
                    elif choice3 == "2":
                        print('''
    As your arms eventually give out on you, and you begin to fall 
    to your death, you think back to your childhood and remember the 
    rockclimbing lessons you were offered, but didn't take.

    Game Over!         

            ''')

                    # Minecart 
                    elif choice3 == "3":

                        # choice2 = Next area they want to go to
                        print('''
    Luckily the mine-cart took you safely
    down a track to a large opening.
    {}
    Once arriving at the opening you see 3 new possible pathways.

    1) A dark opening, the ending of the tunnel is unknown
    2) A long mine shaft heading for what seemed like the surface.
    3) A closed mineshaft boarded up with wooden planks, you can smell something funny inside.
    (Enter 1, 2 or 3)
            '''.format(adv_art.minecart))        










                        while True:

                            # choice4 = final decision for area
                            choice4 = input("> ")
                            print()
                            
                            # Dark opening
                            if choice4 == "1":
                                
                                # Player chose torch as item
                                if item == "3":
                                    print('''
    After deciding to take the dark opening
    you find youself in complete darkness and fear. Luckily you remembered 
    that you chose the torch as your item... Oh wait there aren't any batteries.

    Suddenly you feel something crawling up your back.
    Finally you find what it is, an enourmous, brown centipede with thousands of small sharp legs and two large
    fangs. You feel yourself slowly weakening as your eyes begin close. Death soon follows.

    Game Over!
                ''')
                                # Player doesn't have torch
                                else:
                                    print('''
    After deciding to take the dark opening
    you find yourself in complete darkenss and fear. Suddenly you feel something crawling up your back.
    Finally you find what it is, an enourmous, brown centipede with thousands of small sharp legs and two large
    fangs. You feel yourself slowly weakening as your eyes begin close. Death soon follows.

    Game Over!                
                ''')
                            # Walk down long mineshaft
                            elif choice4 == "2":
                                print('''
    After deciding to take the tunnel towards the surface
    you begin your long walk to freedom. Some say you made it, others say you
    still haven't finished your walk. Your body is never found.

    Game Over!      
            ''')
                            # Open closed mineshaft (gas)
                            elif choice4 == "3":

                                # Player chose gas mask for item
                                if item == "2":
                                    print('''
    Once taking down the wooden planks
    poisonas gas starts to burst out of the closed mineshaft until it has almost comsumed
    the open area you are standing in. Luckily you chose to take the gas mask, allowing you to breath the air.
    After exploring the new mineshaft for some time you find an exit to the outside world.

    You Win!
        ''')

                                else:
                                    print('''
    Once taking down the wooden planks
    poisonas gas starts to burst out of the closed mineshaft until it has almost comsumed
    the open area you are stading in. As you feel the gas slowly killing you, you try to escape but
    there is no hope.

    Game Over!
        ''')
                            # Invalid choice 4
                            else:
                                print(invalid_choice)
                                continue

                            break

                    # Invalid Choice 3
                    else:
                        print(invalid_choice)
                        continue

                    break
            
            # Invalid choice 2
            else:
                print(invalid_choice)
                continue

            break

        # Asking if player wants to play this game again
        print("Would you like to play again? (y/n)")

        while True:
            play_again = input("> ")
            print()

            # Player wants to play again
            if play_again == "y":

                # Changes the intro
                attempt_no += 1
                break

            elif play_again == "n":

                print("Thanks for playing, returning to home menu.")
                print()
                contin = False
                break

            else:
                
                print("Invalid choice, try again.")
                continue
        
        if contin:
            continue

        return 