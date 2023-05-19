"""
Version 3:

- Finished some of the basic functions starting with the sorting,
mean and min/max functions
- Created strings for different options and substances that the user will choose alter/analyse
- Began importing the different sheets

Note: Most filenames have been changed since this version was created
"""

def sort_column(column_num, sheet):
    ### Sorts column data in ascending order ###

    # Getting column data in list first
    column_data = []

    column_length = sheet.max_row
    row = 2
    while row < (column_length + 1):
        cell = sheet.cell(row=row, column=column_num).value
        if cell is not None: 
            column_data.append(cell)
        row += 1
    
    # Using bubble sort method to sort column_data list
 
    for pass_num in range(len(column_data) - 1): # Max num passes is length of list - 1
        for i in range(0, (len(column_data) - pass_num - 1)): # Sorted list increases by 1 each time
             if column_data[i] > column_data[i + 1] :
                temp = column_data[i]
                column_data[i] = column_data[i + 1]
                column_data[i + 1] = temp

    return column_data # sorted column data in ascending order as a list


def get_mean(column_num, sheet):
    total_sum = 0

    sorted_col = sort_column(column_num, sheet)
    for num in sorted_col:
        total_sum += num

    mean = total_sum / len(sorted_col)
    return round(mean, 4) # to 4 d.p.


def get_min_max(column_num, sheet):
    sorted_col = sort_column(column_num, sheet)
    minimum = sorted_col[0]
    maximum = sorted_col[-1]
    range_data = round(maximum - minimum, 3)
    return minimum, maximum, range_data


options = """
Enter corresponding number for your choice:
1) Get mean of substance/weather data
2) Get min, max and range of substance/weather data
"""

column_options = """
Enter corresponding number for your choice of subtance/weather condition:
1) CO 1 hour average [ppb]
2) Humidity 1 hour average [%]
3) NEPH 1 hour average [bsp]
4) NO 1 hour average [ppb]
5) NO2 1 hour average [ppb]
6) NOX 1 hour average [ppb]
7) OZONE 1 hour average [ppb]
8) PM10 1 hour average [µg/m≥]
9) SD1 1 hour average [∞]
10) SO2 1 hour average [ppb]
11) Solar 1 hour average [W/m2]
12) Temperature 1 hour average [∞C]
13) Wind Direction 1 hour average [∞]
14) Wind Speed 1 hour average [m/s] 
"""

print("""
----------------------------------------------------------------------------------------------
Data Analysis of Sydney Particle Study Dataset:
----------------------------------------------------------------------------------------------""")

sheet_choice = int(input("""
Would you like to analyse data collected in:
1) Summer
2) Autumn
3) Both Summer and Autumn
(Enter corresponding number)
----------------------------------------------------------------------------------------------
> """))
print("----------------------------------------------------------------------------------------------")

# Sheets for only summer data, only autumn data and both
if sheet_choice == 1:
    original_sheet = summer_sheet
    original_sheet_name = 'original_data_summer'
    sheet_name = 'data_summer'
elif sheet_choice == 2:
    original_sheet = autumn_sheet
    original_sheet_name = 'original_data_autumn'
    sheet_name = 'data_autumn'
elif sheet_choice == 3:
    original_sheet = both_sheet
    original_sheet_name = 'original_data_both'
    sheet_name = 'data_both'
else:
    print("Invalid sheet choice")

headings = get_headings(original_sheet) # list of headings
column_options = create_column_options_string(headings) # string with all column options used throughout program

choice = int(input("""{}
----------------------------------------------------------------------------------------------
> """.format(options)))
print("----------------------------------------------------------------------------------------------")
