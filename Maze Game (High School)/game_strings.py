fire = """                                                                                                            
                                                                                   
"""


welcome_string = """                                                                  
*************************************************************************************
*    ____  _    _ _____ _      _____ _____ _   _  _____       ____    __   ____     *
*   |  _ \| |  | |_   _| |    |  __ \_   _| \ | |/ ____|     |___ \  /_ | |___ \    *
*   | |_) | |  | | | | | |    | |  | || | |  \| | |  __        __) |  | |   __) |   *
*   |  _ <| |  | | | | | |    | |  | || | | . ` | | |_ |      |__ <   | |  |__ <    *
*   | |_) | |__| |_| |_| |____| |__| || |_| |\  | |__| |      ___) |  | |  ___) |   *
*   |____/ \____/|_____|______|_____/_____|_| \_|\_____|     |____/   |_| |____/    *
*                                                                                   *
*                          (2022 Game - By Flynn Costello)                          *                    
*                                                                                   *
*                   ▒▒                  - Escape the building before the            *                  
*               ▓▓                        time runs out and it collapses            *
*               ▓▓▓▓                                                                *
*               ████                    - Enter 'p' to play                         *
*               ░░████                                                              *   
*               ██▓▓██                  - Enter 'i' for the game instructions       *
*       ░░  ████▓▓▓▓    ▒▒                                                          *
*       ▓▓▒▒▓▓██▒▒▓▓  ██░░              - Enter 'k' at any time for the game's      *
*       ▓▓██████▒▒▓▓▒▒████  ▒▒            input keys                                *
*       ██████▒▒▒▒▓▓▒▒██▒▒  ██                                                      *
*       ██▓▓▓▓░░▒▒████▓▓░░▒▒██  ░░      - Enter 'q' at any time to quit the game    *
*       ██▒▒▒▒░░▒▒▓▓██▓▓▓▓████▓▓░░                                                  *
*       ██▒▒▒▒░░▒▒████▓▓██▓▓████░░      - To access the game's leaderboards, enter: *
*       ██▒▒░░░░▒▒▓▓██▒▒██▒▒██▓▓░░         - 'l1' for the game difficulty 1 board   *                                         
*   ░░  ▒▒▒▒░░░░░░▒▒██░░▒▒▒▒▓▓██           - 'l2' for the game difficulty 2 board   *                        
*   ██▓▓▓▓░░  ░░▒▒▒▒░░░░▒▒▓▓▓▓             - 'l3' for the game difficulty 3 board   *                                     
*   ░░██▓▓▒▒░░  ░░░░░░░░░░▓▓░░             - 'l4' for the game difficulty 4 board   *                                     
*       ░░▓▓░░░░        ░░▒▒░░             - 'l5' for the game difficulty 5 board   *                                      
*           ░░▒▒░░      ░░                                                          *
*                                                                                   *
*************************************************************************************
"""


entering_maze_string = """
25th July 2022:
Clouds begin to unfurl themselves across the vivid afternoon sky as shades of crimson red
and tuscan sun yellow mix into a scene of warmth and energy that envelops your small office
cubicle. Working away at the weekly crossword as you realise the 'Long gone cold period' was
the Ice Age, you hear a large bang in a room down the hallway. Peering out of your cubicle
down the lengthy hallway you are suddenly flung backwards by an explosion. Flames erupt from
the room as its walls collapse. Suddenly, as you try to regain youself, a large piece of wood
comes down on your head. Darkness...

Sometime later you awake to the sound of sirens and firealarms. How long has passed? You ask 
youself. Looking around the flames are still approaching. You must escape now before it is too 
late.

(Note: In order to escape you must traverse the building's many corridors and rooms to reach the escape 
(labeled by 'Y'). Be careful of the fires (labeled with 'F') as you will die if you walk into 
them. To avoid this fate, be sure to collect as many water buckets (labelled by 'W') as you can 
as these buckets can be used to extinguish these fires. Finally, your character is represented by the 
letter 'A'. Now Good Luck!)
"""

input_keys = """
Input Keys:
    a - move left
    d - move right
    s - move down
    w - move up 
    q - quit game
    k - keyboard input options
    m - map symbols    
"""

map_symbols = """
Map Symbols:
    * - wall (cannot pass through)
    P - player (your icon)
    X - starting location
    Y - exit
    F - fire (need water bucket to put out - you will die if you don't have enough water buckets)
    W - water bucket (puts out fire)
    1,2 - Teleportation to other number point (i.e., going through 1 teleports you to other number 1 location on the map)
"""

instructions_string = f"""
----------------------------------------------------------------------------------------------------------------------------
Burning Building - Game Instructions:

- The game works by the user (you) traversing a building that is layed out in a similar way to a maze
- You're playable character is marked by the symbol 'A' and must reach 'Y' to win the game (Note: X, marks
where you start)
- To traverse the maze you can utilise the following movement keys:
    {input_keys}

- Additionally, within the map the meanings of each symbol are listed below:
    {map_symbols}

- As you travese the building/maze you will be met with fire icons marked with an 'F'. The only way to move
through these symbols is to have enough water buckets in your inventory (Note: the number of water buckets
you have will repeatedly be printed to you). If you do have enough, you can walk through the flame, thus also
losing one of your water buckets.

- Additionally, squares marked with the numbers of 1 or 2 represent teleporters that, when passed through,
transport you to the other corresponding number (i.e., moving through a cell marked with the number 1 will
teleport you to the other cell in the building marked with the number 1 too)

- Finally, to win the game make sure you get to the exit (Marked by 'Y') within the time limit (This limit
will be printed to you at the start and the amount of time left as you traverse the building will also
be constantly printed too you)

----------------------------------------------------------------------------------------------------------------------------
"""