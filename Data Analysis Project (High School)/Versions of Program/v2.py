"""
Version 2:

- Tried using 'pandas' instead of OpenPYXL however ultimately changed back to OpenPYXL
- Also decided on more functions to include that will be finished later such as filling in blank cells
with a certain input

Note: Most filenames have been changed since this version was created
"""

from pandas import *
file_name = 'novice_data.xlsx'
xlxs = ExcelFile(file_name)
data = xlxs.parse(xlxs.sheet_names[1]) # index is what sheet your using

data_dict = data.to_dict()
"""
This dict is formatted like:
{'column 1 header': {0: row 0 data, 1: row 1 data, ...}, 'column 2 header': {0: row 0 data, 1: row 1 data, ...}}
"""
#print(data_dict)
#print('Origin data structure', data_dict)

subtances = []

for subtance in data_dict:
    subtances.append(subtance)

def get_avg(substance_name, data_dict):
    avg = data_dict[substance_name].mean()
    return avg


print(get_avg(subtances[0], data_dict))



import pandas as pd

### FUNCTIONS ###
def fill_empty_cells(subtance_name, data_file, avg):
    data_file[subtance_name].fillna(avg, inplace = True)

### USER INPUTS ###
action = int(input("""
Available Actions:
- Get Summary statistics for substance (Enter 1)
- Fill in blank data cells for substance (Enter 2)
- Create graphs for substance (Enter 3)
> """))

subtance = f'{input("Enter subtance name: ")}, 1 hour average [ppb]'


### CREATING DATA FILES/DICTS ###
data_file = pd.read_csv('novice_data2.csv')
subtance_headers = data_file.keys()
summary_stats = {} # Dict of summary stats for each subtance

i = 2 # skipping first two columns as they are dates and times
while i < len(subtance_headers):
    cur_data_info = data_file[subtance_headers[i]].describe()
    summary_stats[subtance_headers[i]] = cur_data_info
    i += 1


### ACTIONS ###
if action == 2:
    pass
