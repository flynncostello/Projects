"""
Version 6 (Final Version) of functions file:

- Functions were previously defined in each of of the main program's files
- Includes a range of functions that perform a variety of tasks/actions
"""

import sys

def get_units(headings):
    units = []
    for heading in headings:
        cur_unit = ""
        i = 0
        while i < len(heading):
            letter = heading[i]
            if letter == "[":
                i += 1
                letter = heading[i]
                while letter != ']':
                    cur_unit += letter
                    i += 1
                    letter = heading[i]
                    
            i += 1
        units.append(cur_unit)
    return units


def create_column_options_string(headings):
    """
    Input:
    - headings - list of strings containing headings
    """
    column_options = "\nEnter corresponding number for your choice of subtance/weather condition:\n"
    num = 1
    i = 2 # need to skip first 2 headings as they are date and time
    while i < len(headings):
        heading = headings[i]
        new_string = f"{num}) {heading}\n"
        column_options += new_string
        i += 1
        num += 1

    return column_options


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


def get_mean(column_num, sheet, sorted_col):
    total_sum = 0

    for num in sorted_col:
        total_sum += num

    mean = total_sum / len(sorted_col)
    return round(mean, 4) # to 4 d.p.


def get_min_max(column_num, sheet, sorted_col):
    minimum = sorted_col[0]
    maximum = sorted_col[-1]
    range_data = round(maximum - minimum, 3)
    return minimum, maximum, range_data


def get_modes(column_num, sheet, sorted_col):
    maxcount = 0
    modes = []

    for num in sorted_col:
        occurances = sorted_col.count(num)
        if occurances > maxcount:
            modes.clear()
            modes.append(num)
            maxcount = occurances

        elif occurances == maxcount:
            if num not in modes:
                modes.append(num)
    
    return modes


def get_middle_of_list(data_list): # data list is sorted_col list
    length = len(data_list)
    if length % 2 == 0: # EVEN length
        lower_mid_index = int((length / 2) - 1)
        upper_mid_index = int((length / 2))
        mid = round((data_list[lower_mid_index] + data_list[upper_mid_index]) / 2, 4) # rounded to 4d.p.
    else: # ODD length
        mid_index = int((length - 1) / 2)
        mid = data_list[mid_index]
    
    return mid # return float


def get_quartiles(column_num, sheet, sorted_col):
    ### Gets Q1, median (Q2), Q3 and IQR ###
    # 25% of data below Q1, 25% of data above Q3, median is where 50% of data is both left and right
    length = len(sorted_col)

    median = get_middle_of_list(sorted_col)

    if length % 2 == 0: # EVEN length
        half = int(length / 2)
        q1_list = sorted_col[:half]
        q3_list = sorted_col[half:]
        
    else: # ODD length
        half = int(length // 2)
        q1_list = sorted_col[:half]
        q3_list = sorted_col[half+1:]

    q1 = get_middle_of_list(q1_list)
    q3 = get_middle_of_list(q3_list)

    IQR = round(q3 - q1, 4)

    return q1, median, q3, IQR


def check_for_outliers(column_num, sheet, sorted_col):
    q1, q2, q3, IQR = get_quartiles(column_num, sheet, sorted_col)
    lower_bound = q1 - (1.5 * IQR)
    upper_bound = q3 + (1.5 * IQR)

    outliers = []
    column_data = sorted_col
    for num in column_data:
        if num < lower_bound or num > upper_bound:
            outliers.append(num)
    return outliers # returns a list of floats


def get_outlier_string(original_sheet, headings):
    total_columns = original_sheet.max_column # int
    outliers_string = "" # increased for each column processed in loop below
    cur_column = 3
    while cur_column <= total_columns:
        col_heading = headings[cur_column - 1] # string

        sorted_col = sort_column(cur_column, original_sheet)
        if len(sorted_col) == 0: # Columns that have no data
            outliers_string += f"{col_heading} has no data\n\n"

        else: # Finding outliers
            cur_col_outliers = check_for_outliers(cur_column, original_sheet, sorted_col) # list of floats

            if len(cur_col_outliers) == 0: # Columns that have no outliers
                outliers_string += f"{col_heading} has no outliers\n\n"
            else: # Columns that have outliers - making a string adding all outliers
                total_num_outliers = len(cur_col_outliers)
                cur_col_string = f"{col_heading} has {total_num_outliers} outliers including"
                for outlier in cur_col_outliers:
                    cur_col_string += f", {str(outlier)}"
                
                outliers_string += f"{cur_col_string}\n\n"

        cur_column += 1

    return outliers_string


def get_headings(sheet):
    headings = []
    for cell in sheet[1]:
        headings.append(cell.value)

    return headings


def get_summary_stats(column_num, original_sheet, substance, sorted_col, substance_units):
    mean = get_mean(column_num, original_sheet, sorted_col)
    minimum, maximum, data_range = get_min_max(column_num, original_sheet, sorted_col)
    modes = get_modes(column_num, original_sheet, sorted_col)
    q1, median, q3, IQR = get_quartiles(column_num, original_sheet, sorted_col)
    summary_stats = f"""
    Summary statistics for {substance}:
        * Mean = {round(mean, 3)} {substance_units}
        * Minimum = {round(minimum, 3)} {substance_units}
        * Maximum = {round(maximum, 3)} {substance_units}
        * Range = {round(data_range, 3)} {substance_units}
        * Q1 = {round(q1, 3)} {substance_units}
        * Median (Q2) = {round(median, 3)} {substance_units}
        * Q3 = {round(q3, 3)} {substance_units}
        * IQR = {round(IQR, 3)} {substance_units}
    """
    return summary_stats


def get_variance_and_deviation(column_num, sheet, sorted_col):
    mean = get_mean(column_num, sheet, sorted_col)

    sum_of_squared_deviation = 0
    for i in range(len(sorted_col)):
        sum_of_squared_deviation += (sorted_col[i]- mean)**2

    standard_deviation = ((sum_of_squared_deviation)/len(sorted_col))**0.5
    variance = standard_deviation ** 2
    return variance, standard_deviation


def calc_z_score(value, column_num, original_sheet, sorted_col):
    mean = get_mean(column_num, original_sheet, sorted_col)
    var, standard_deviation = get_variance_and_deviation(column_num, original_sheet, sorted_col)
    z_score = round((value - mean)/standard_deviation, 2)
    return z_score


def determine_values_outside_range(sorted_col, maximum, minimum, headings, column_num, total_rows):
    total_out_of_range = 0
    out_of_range_string = ""
    return_string = ""
    for value in sorted_col:
        if value > float(maximum) or value < float(minimum):
            total_out_of_range += 1
            out_of_range_string += f"{str(value)}, "
    
    if len(out_of_range_string) == 0: # No values that are out of range
        return_string += "All values are in acceptable range"
    else:
        column_name_old = headings[column_num - 1]
        column_name = column_name_old.replace("[", "").replace("]", "") 
        percentage_of_total_values = round((total_out_of_range/(total_rows-1)) * 100, 3) # need to minus one as first row is title
        return_string += f"""{column_name} has {total_out_of_range} values out of acceptable range which is {percentage_of_total_values}% of the total values.
Values which are outside acceptable range include: {out_of_range_string}"""

    return return_string


def create_no_outliers_sheet(sheet_name, workbook, original_sheet, original_sheet_name):
    no_outliers_sheet_name = f'no_outliers_{sheet_name}' # new sheet name
    workbook.create_sheet(no_outliers_sheet_name)
    no_outliers_sheet = workbook[no_outliers_sheet_name] # new sheet

    total_columns = original_sheet.max_column
    total_rows = original_sheet.max_row

    cur_column = 1
    while cur_column <= total_columns:
        cur_row = 1
        if cur_column <= 2: # Adding first two columns of data (only dates and times)
            while cur_row <= total_rows:
                no_outliers_sheet.cell(row=cur_row, column=cur_column).value = original_sheet.cell(row=cur_row, column=cur_column).value
                cur_row += 1
        else: # Summer sheet has no data for first substance column therefore need to skip
            if original_sheet_name == 'original_data_summer' and cur_column == 3:
                no_outliers_sheet.cell(row=1, column=cur_column).value = original_sheet.cell(row=1, column=cur_column).value
                cur_column += 1
                continue
            else: # Adding all cells that are NOT outliers to new sheet
                sorted_col = sort_column(cur_column, original_sheet)
                cur_col_outliers = check_for_outliers(cur_column, original_sheet, sorted_col) # list of outliers as floats
                while cur_row <= total_rows:
                    if original_sheet.cell(row=cur_row, column=cur_column).value not in cur_col_outliers: # not an outlier
                        no_outliers_sheet.cell(row=cur_row, column=cur_column).value = original_sheet.cell(row=cur_row, column=cur_column).value
                    cur_row += 1
        cur_column += 1

    #workbook.save('/Users/42587/Library/CloudStorage/OneDrive-StJosephsCollege/Year 12/SDD/Minor Project/project_data.xlsx')
    workbook.save('project_data.xlsx')

    print(f"Successfully created new sheet called: {no_outliers_sheet_name}\n")

    return no_outliers_sheet_name


def create_no_blanks_sheet(sheet_name, workbook, original_sheet, original_sheet_name, no_outliers_sheet):
    final_altered_sheet_name = f'final_altered_{sheet_name}' # new sheet name
    workbook.create_sheet(final_altered_sheet_name)
    final_altered_sheet = workbook[final_altered_sheet_name] # new sheet
    
    total_columns = original_sheet.max_column
    total_rows = original_sheet.max_row

    while True:
        try:
            fill_in_with = int(input("""What would you like to fill all blank cells with:
1) Mean of data
2) Median of data
(Enter corresponding number) 
--------------------------------------------------------------------------------------------------------       
> """))

            if fill_in_with != 1 and fill_in_with != 2:
                print("Invalid input")
            else:
                break
            print('\n')

        except ValueError:
            print("Invalid input")
            print('--------------------------------------------------------------------------------------------------------')


    cur_column = 1
    while cur_column <= total_columns: 
        if cur_column <= 2: # Adding first two columns that only have dates and times
            cur_row = 1
            while cur_row <= total_rows:
                final_altered_sheet.cell(row=cur_row, column=cur_column).value = no_outliers_sheet.cell(row=cur_row, column=cur_column).value
                cur_row += 1
        else: # Skip summer third column as it has no data
            if original_sheet_name == 'original_data_summer' and cur_column == 3:
                final_altered_sheet.cell(row=1, column=cur_column).value = no_outliers_sheet.cell(row=1, column=cur_column).value # Adding the title only
                cur_column += 1 # Only adding title as there is no data
                continue
            ### MEAN AND MEDIAN ARE CALCULATED USING DATA WITHOUT OUTLIERS IN IT ###

            sorted_col = sort_column(cur_column, original_sheet)

            if fill_in_with == 1: # mean
                fill_in = get_mean(cur_column, no_outliers_sheet, sorted_col)
            elif fill_in_with == 2: # median
                quartiles = get_quartiles(cur_column, no_outliers_sheet, sorted_col)
                fill_in = quartiles[1] 

            cur_row = 1
            while cur_row <= total_rows: # Adding cells from no_outliers_sheet + filled in ones to new sheet
                if no_outliers_sheet.cell(row=cur_row, column=cur_column).value is None:
                    final_altered_sheet.cell(row=cur_row, column=cur_column).value = fill_in
                else: # Cell is filled in first sheet therefore can copy to new one
                    final_altered_sheet.cell(row=cur_row, column=cur_column).value = no_outliers_sheet.cell(row=cur_row, column=cur_column).value
                cur_row += 1

        cur_column += 1
    
    #workbook.save('/Users/42587/Library/CloudStorage/OneDrive-StJosephsCollege/Year 12/SDD/Minor Project/project_data.xlsx')
    workbook.save('project_data.xlsx')

    message = f"Successfully created new sheet called: {final_altered_sheet_name}"
    print('--------------------------------------------------------------------------------------------------------')

    return True, message

