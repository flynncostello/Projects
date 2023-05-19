# step function defines what happens when the player steps onto each cell
import os
folder_directory = os.path.dirname(__file__)
os.chdir(folder_directory)

from playsound import playsound 

class Start:

    def __init__(self):
        self.display = 'X' # Start.display used to call the 'X' icon

    def step(self, game, move):
        game.moves.append(move) 
        return [False]

class End:
    def __init__(self):
        self.display = 'Y'

    def step(self, game, move):
        game.play_again = False
        game.won = True
        game.moves.append(move) 
        return [False]


class Air:
    def __init__(self):
        self.display = ' '

    def step(self, game, move):
        game.moves.append(move)
        playsound('458641_matrixxx_retro-jump-02 (mp3cut.net).wav')
        return [False]


class Wall:
    def __init__(self):
        self.display = '*' # used in parse

    def step(self, game, move):
        game.player.row = game.old_pos[0]
        game.player.col = game.old_pos[1]
        playsound('hit_wall.mp3')
        return [True, "You walked into a wall. Oof!"]



class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self, game, move):
        if game.player.num_water_buckets >= 1:
            game.player.num_water_buckets -= 1
            game.moves.append(move) 
            game.list_of_cells[game.player.row][game.player.col] = Air() # chaning block to air
            playsound('extinguisher-fire_TuX3hhZi.mp3')
            return [True, "With your strong arms, you throw a water bucket at the fire. You walk away through the extinguished flames!"]

        else:
            game.play_again = False
            game.won = False
            game.moves.append(move) 
            playsound('105016__julien-matthey__jm-fx-fireball-01.wav')
            return [True, "\nYou step into a fires and watch your dreams of escape disappear :(. You Die!"]
            

class Water:
    def __init__(self):
        self.display = 'W'

    def step(self, game, move):
        game.player.num_water_buckets += 1
        game.moves.append(move) 
        game.list_of_cells[game.player.row][game.player.col] = Air()
        playsound('527530_jerimee_objective-complete (mp3cut.net).wav')
        return [True, "You've found a bucket of water! (These can be used to extinguise fires labelled by 'F')"]
         


class Teleport:
    def __init__(self, num):
        self.display = num  # teleport number

    def step(self, game, move):
        game.moves.append(move)
        i = 0
        while i < len(game.teleport_pos):
            #print(game.teleport_pos)
            if (game.teleport_pos[i][0] == self.display):
                # checking to see if teleport is the current on the player is stading on
                loc_tel = [game.teleport_pos[i][1], game.teleport_pos[i][2]]
                loc_player = [game.player.row, game.player.col]

                if loc_tel != loc_player: # position of teleporter is not the cell the player is on
                    game.player.row = game.teleport_pos[i][1]
                    game.player.col = game.teleport_pos[i][2]
                    break
                    
            i += 1
        playsound('172206__leszek-szary__teleport.wav')
        return [True, """You've found a teleporter. Whoosh! Suddenly the magical gate breaks 
Physics as we know it and opens a wormhole through space and time teleporting you across the building."""]
    
