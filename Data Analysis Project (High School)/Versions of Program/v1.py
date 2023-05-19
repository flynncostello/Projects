"""
Version 1:

- Still playing around with ideas and what I want to do
- Added some functionality and dictionary structures
- Decided on some simple functions (e.g., getting average, 
min, max, mode and median) --> will include code later
"""


# Making data structure dict of lists
data_dict_list = {} # {NO: [1, 2, 3, 4, 5,...], CO: [1, 2, 3, 5,...]} --> numbers are FLOATS

for subtance in data_dict:
    subtance_name = subtance

    column_list = []
    for index_key in data_dict[subtance]:
        cur_row_data = data_dict[subtance][index_key]
        column_list.append(cur_row_data)

    data_dict_list[subtance_name] = column_list

print('New data structure', data_dict_list)

# Functions for getting summary stats
def get_avg(data):
    """
    Inputs:
        data - dict of lists
    Outputs:
        list of avgs
    """
    avg_list = []

    for key in data: # dict
        avg = 0
        total = 0
        total_nums = 0
        cur_data = data[key] # list

        for stat in cur_data: #
            if type(stat) == float:
                total += stat
                total_nums += 1

        avg = total / total_nums
        avg_list.append(round(avg, 3)) # to 3 d.p.

    return avg_list # list of averages as floats to 3 d.p.

print(get_avg(data_dict_list))

def get_max(data):
    maximum = 0

def get_min(data):
    minimum = 0

def get_mode(data):
    mode = 0

def get_median(data):
    median = 0
