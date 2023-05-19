def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Inputs:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Output:
        string: A string representation of the grid and player.

    The whole grid should be represented in a single string.
    """
    
    string = ""
    # ['a', 'b'] -> [(0, 'a'), (1, 'b')]

    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if i == player.row and j == player.col:
                string += player.display
            else:
                string += cell.display
        string += "\n"

    if player.num_water_buckets == 1:
        string += f"\nYou have {player.num_water_buckets} water bucket."
    else:
        string += f"\nYou have {player.num_water_buckets} water buckets."

    return string

    
