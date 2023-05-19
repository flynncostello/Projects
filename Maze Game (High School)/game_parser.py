import sys

from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

cells_map = {

    'X':Start,
    'Y':End,
    ' ':Air,
    '*':Wall,
    'F':Fire,
    'W':Water,
}

def read_lines(filename):

    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    try:
        file1 = open(filename, "r")
    except FileNotFoundError:
        print(f"{filename} does not exist!")
        sys.exit()
        

    config_ls = [] # list of strings representing config

    line = file1.readline() # 1st line
    while line:
        config_ls.append(line)
        line = file1.readline() # continues to next line until line == False (no line left)
    
    final_ls = parse(config_ls) # changing list of strings to list of class instances
    return final_ls # list of list of cells



def parse(lines):
    """Transform the input into a grid.

    Input:
        lines -- list of strings representing the grid

    Output:
        list -- contains list of lists of Cells

    Input received is a list of strings. Output should transform each character
    of the string into Cells.
    """
    
    grid = []
    x_count = 0
    y_count = 0
    teleport_count = {}

    for line in lines:
        line = line.strip()
        # line = '*X*'
        cell_line = []
        for char in line:
            # char = 'X'
            
            if char == "X":
                x_count += 1
            if char == "Y":
                y_count += 1

            try:
                int(char)
                # If this passess then the char is a number (teleport pad)
                cell = Teleport(char)

                if char not in teleport_count:
                    teleport_count[char] = 1
                else:
                    teleport_count[char] += 1

            except ValueError:
                if char not in cells_map: # checking for bad letter
                    raise ValueError (f"Bad letter in configuration file: {char}.")
                cell = cells_map[char]() # Adding other type of cell
            
            cell_line.append(cell) # will always append cell
                
        grid.append(cell_line)


    if x_count != 1:
        raise ValueError (f"Expected 1 starting position, got {x_count}.")
    if y_count != 1:
        raise ValueError (f"Expected 1 ending position, got {y_count}.")

    for (key, value) in teleport_count.items():
        if value != 2:
            raise ValueError (f"Teleport pad {key} does not have an exclusively matching pad.")

    return grid


