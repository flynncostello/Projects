'''
Write your solution for 6. PIAT: Check Setup here.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

import shutil
# shutil.copy(src, dest) - copying src to dest (files)
# for contents in os.walk("/home/"): - loops through contents of the root directory home
#       print contents
# Challenge: Spot the root folder and its files?
# ('/home/', ['demo', 'new'], ['main.py'])
# Challenge: Spot the root folder and its files?
# ('/home/demo', [], ['my_file.txt'])
# Challenge: Spot the root folder and its files?
# ('/home/new', [], ['tip.txt'])
 
import os
import time
import datetime
import sys

"""
    (os.path.isdir(path) - returns true if path is existing directory)

Master Directory:
- Contains files and sample(s) folder as well as config.txt file

Directories (in config.txt):
- /home/user/A1/ - this is valid
- Needs to start and end with /
- Can't contain a .

Files (in config.txt):
- Must always start with ./
- Row before file must be a valid directory

E.g.
VALID config.txt FILE:
/home/files/
./animals.txt  
./history.txt  
./list.txt  
./names.txt
/home/samples/
./count_me.txt


This is what config.txt will look like:
/home/files/
./animals.txt  
./history.txt  
./list.txt  
./names.txt
/home/samples/
./count_me.txt
"""

def point_in_name(string):
    point_in = False
    i = 0
    while i < len(string):
        if string[i] == ".":
            point_in = True
        i += 1
    return point_in

def is_folder_file_or_neither(string):
    """
    Function determines if a given string is a folder, file or neither (i.e., invalid)
    """
    is_folder = False
    is_file = False
    is_neither = False
    dot_in_string = point_in_name(string)

    if string[0] == "/" and string[-1] == "/" and not(dot_in_string):
        is_folder = True
    elif string[:2] == "./" and string[-4:] == ".txt":
        is_file = True
    else:
        is_neither = True
    return (is_folder, is_file, is_neither)


def extract_directory_and_file_paths(master):
    absolute_config_path = f"{master}config.txt"
    try:
        with open(absolute_config_path, "r") as config_file:
            config_lines = config_file.readlines()
    except FileNotFoundError:
        print("Invalid master directory.")
        sys.exit()

    config_directories = []
    config_files = [] # 2 dimensional array with each element being an array of the
    # files that are located within the corresponding element directory in directories folder
    filenames = [] # just file names, e.e.,g history.txt
    """
    E.g.,
    config_directories = ['/home/files/', '/home/samples/']
    config_files = [['/home/files/animals.txt', '/home/files/history.txt', '/home/files/list.txt', '/home/files/na
    mes.txt'], ['/home/samples/count_me.txt']]
    """
    i = 0
    while i < len(config_lines):
        cur_line = config_lines[i].strip() # .strip() is required to get rid of \n character at end of every line read from config.txt
        if cur_line != '':
            is_folder, is_file, is_neither = is_folder_file_or_neither(cur_line)
            if is_folder:
                config_directories.append(cur_line)

            if is_file:
                file_name = cur_line[2:]
                file_absolute_path = f"{config_directories[-1]}{cur_line[2:]}"
                if len(config_files) < len(config_directories):
                    config_files.append([file_absolute_path])
                    filenames.append([file_name])
                else:
                    config_files[-1].append(file_absolute_path)
                    filenames[-1].append(file_name)

        i += 1
    return (config_directories, config_files, filenames)



def installation(master: str, timestamp: str) -> list:
    '''
    Installation copies all required master files into the addresses listed by
    the config file.
    Parameters:
        master:    str,  a string representing the absolute path to the master directory.
        timestamp: str,  a string representing the time to insert into the output.
    Returns:
        output:    list, a list of strings generated from the installation process.
    
    - If file is in config file but not found in master directory program displays message - "Original {file_name} is not found."
    - If installation is unsuccessful program terminates and displays message "Installation error..."
    1) get paths to directories from config file
    2) create new directories
    3) get paths for all files in master directory
    4) create new files
    5) copy files from master directory to new files
    '''
    output_text = []
    """
    Within the folder, "files" there should always be four text files e.g. animals.txt, history.txt, list.txt and names.txt
    Within the folder, "samples" there should be one text file e.g. count_me.txt
    
    Errors:
    - If a file is listed in the configuration file but not found in the master directory,
    the program should display the message "Original {file_name} is not found"
    - os.path.isdir(path) - returns true if path is existing directory

    - If the program is unable to complete installation, the program should terminate
    and display the message "Installation error..."
    """
    output_text.append(f"{timestamp} Start installation process.")

    ### Step 1: ###
    output_text.append(f"{timestamp} Extracting paths in configuration file.")

    config_directories, config_files, filenames = extract_directory_and_file_paths(master)

    total_directories = len(config_directories)
    output_text.append(f"Total directories to create: {total_directories}")

    
    ### Step 2/3 - Check if directories exist - if they do, skip, if they don't create new directory at specified filepath ###
    output_text.append(f"{timestamp} Create new directories.") # in /home
    
    # Checking if directory exists then either say it does or create new directory
    
    index = 0
    while index < len(config_directories):
        cur_directory = config_directories[index]
        if os.path.exists(cur_directory):
            output_text.append(f"{cur_directory} exists. Skip directory creation.")
        else: # Directory doesn't exist
            os.mkdir(cur_directory)
            output_text.append(f"{cur_directory} is created successfully.")
        index += 1

        

    # Step 4 - Needs to find files in the same order that they are listed in the config.txt file
    output_text.append(f"{timestamp} Extracting paths of all files in {master}.")
    all_paths_in_master = sorted(os.listdir(master)) # Lists all paths in master
    dir_num = 0
    while dir_num < len(all_paths_in_master):
        cur_dir = f"{master}{all_paths_in_master[dir_num]}/"
        #print(cur_dir)
        if os.path.isdir(cur_dir):
            all_paths_in_cur_directory = sorted(os.listdir(cur_dir))
            file_num = 0
            #print(all_paths_in_cur_directory)
            while file_num < len(all_paths_in_cur_directory):
                cur_file = f"{cur_dir}{all_paths_in_cur_directory[file_num]}"
                #print(cur_file)
                #print(cur_file)
                output_text.append(f"Found: {cur_file}")
                file_num += 1

        dir_num += 1
    
    
    # Step 5 - Creating new files in /home
    output_text.append(f"{timestamp}  Create new files.")
    
    index1 = 0
    while index1 < len(config_files):
        index2 = 0
        while index2 < len(config_files[index1]):
            cur_file_to_be_added = config_files[index1][index2].strip() # Absolute path to file in terms of /home, not /master 
            create_new_file = open(cur_file_to_be_added, "w")
            output_text.append(f"Creating file: {cur_file_to_be_added}")
            index2 += 1
        index1 += 1

    # Step 6 - Search for file in master, ensure it exists, then copy to /home equivelant place in the new folder and file you created

    output_text.append(f"{timestamp} Copying files.")
    i = 0
    while i < len(config_directories):
        j = 0
        while j < len(config_files[i]):
            try:
                original_path = f"{master}{config_files[i][j][6:]}"
                destination_path = f"{config_files[i][j]}"
                #print(original_path, destination_path)
                output_text.append(f"Locating: {filenames[i][j]}")
                shutil.copy(original_path, destination_path)
                output_text.append(f"Original path: {original_path}")
                output_text.append(f"Destination path: {destination_path}")
            except Exception:
                output_text.append(f"Original path: {original_path} is not found.")
                output_text.append("Installation error...")
                return output_text
            j += 1
        i += 1
    output_text.append(f"{timestamp}  Installation complete.")

    return output_text
    




def logging(logs: list, date: str, time: str) -> None:
    '''
    Logging function uses a list of strings to write previous output into a
    log file.
    Parameters:
        logs: list, output from verification/installation in the form of list of 
                    strings to write to logging file.
        date: str,  a string representing the date to generate the necessary 
                    directory date must be in the format YYYY-MM-DD as seen in 
                    the specs (ex: 2023-Mar-03 for March 3rd, 2023).
        time: str,  a string representing the time to generate the log file
                    time must be in the format HH_MM_SS as seen in the specs
                    (ex: 14_31_27 for 14:31:27).
    '''
    """
    If this command is present with the installation or verification process, 
    in addition to displaying the messages to standard output, the program logs 
    the details into a text file and stores this text file in the folder path 
    /home/logs/{YYYY-MM-DD}. The text file must be created on each run, labelled 
    with the current time of execution in the format HH_MM_SS. The contents of 
    the file is the same as the text output except that the date and time are omitted. 

    If the program is executed on 3rd March 2023 at 14:31:27, the resulting log file 
    should be placed in this folder path: /home/logs/2023-Mar-03 and the name of the 
    file should be 14_31_27.txt. This is an example contents of the file when the program 
    is executed with the given command line arguments:
    

    - Logs details of either installation or verification in a text file and stores this
    at the folder path /home/logs/YYYY-MM-DD
    - Contents of text file as the same as the output from the program except the contents of the
    data and time are omitted - therefore only info text
    - Need to create new folders if its a new day/month/year and a new file every run with name
    hour_min_second.txt
    """

    # new_folder = /home/logs/date
    # date and time are ommited
    folder_name = f"/home/logs/{date}/"
    file_name = f"{time}.txt"
    file_name_absolute_path = f"{folder_name}{file_name}"
    new_logs = logs
    #new_logs = remove_date_and_time(logs)
    # Creating/Checking is logs folder exists
    if not(os.path.isdir("logs")):
        os.mkdir("logs")

    # Checking if folder exists
    if not(os.path.exists(folder_name)): # Folder doesn't already exists
        os.mkdir(folder_name)

    with open(file_name_absolute_path, "w") as new_file:
        i = 0
        while i < len(new_logs):
            new_file.write(f"{new_logs[i]}\n")
            i += 1


def verification(master: str, timestamp: str) -> list:
    '''
    Verification makes sure all files and directories listed in the config file
    are present and match the contents of the master files. 
    Parameters:
        master:    str,  a string representing the absolute path to the master directory.
        timestamp: str,  a string representing the time to insert into the output.
    Returns:
        output:    list, a list of strings generated from the verification process.
    '''
    output_text = []
    output_text.append(f"{timestamp} Start verification process.")
    output_text.append(f"{timestamp} Extracting paths in configuration file.")


    config_directories, config_files, filenames = extract_directory_and_file_paths(master)
    i = 0
    while i < len(config_files):
        config_files[i] = sorted(config_files[i])
        filenames[i] = sorted(filenames[i])
        i += 1

    total_directories = len(config_directories)
    output_text.append(f"Total directories to check: {total_directories}")

    output_text.append(f"{timestamp} Checking if directories exists.")


    # Checking if directories exist in /home
    i = 0
    while i < len(config_directories):
        cur_dir = config_directories[i]
        if os.path.exists(cur_dir):
            output_text.append(f"{cur_dir} is found!")
        else:
            output.append(f"{cur_dir} NOT found!")
            output.append(f"Abnormalities detected...")
            return output_text
        i += 1
    
    # Extracting files in master directory
    files_to_check = []
    output_text.append(f"{timestamp} Extracting files in configuration file.")
    total_files = 0
    dir_num = 0
    #print(config_files)
    while dir_num < len(config_files):
        file_num = 0
        while file_num < len(config_files[dir_num]):
            cur_file = config_files[dir_num][file_num]
            #print(cur_file)
            output_text.append(f"File to check: {cur_file}")
            files_to_check.append(cur_file)
            file_num += 1
            total_files += 1
        dir_num += 1
    output_text.append(f"Total files to check: {total_files}")
    
    # Checking if files exist
    output_text.append(f"{timestamp} Checking if files exists.")
    i = 0
    while i < len(files_to_check):
        if os.path.exists(files_to_check[i]):
            output_text.append(f"{files_to_check[i]} found!")
        else:
            output.append(f"{files_to_check[i]} NOT found!")
            output.append(f"Abnormalities detected...")
            return output_text
        i += 1
    
    # Checking contents of files with master copy
    output_text.append(f"{timestamp} Check contents with master copy.")
    count1 = 0
    #print("XXX", config_files)
    while count1 < len(config_files):
        count2 = 0
        while count2 < len(config_files[count1]):
            # This is now looking at each specific file
            home_file = config_files[count1][count2] # /home/files/history.txt
            master_copy_file = f"{master}{home_file[6:]}" # /home/master/files/history.txt
            try:
                with open(home_file, "r") as home:
                    home_lines = home.readlines()
                with open(master_copy_file, "r") as master_copy:
                    master_copy_lines = master_copy.readlines()
                i = 0
                j = 0
                abnormalies_detected = False
                while i < len(master_copy_lines):
                    try:
                        if master_copy_lines[i] == home_lines[i]:
                            i += 1
                        else:
                            while j <= i:
                                master_error = master_copy_lines[j].strip()
                                home_error = home_lines[j].strip()
                                output_text.append(f"File name: {home_file}, {home_error}, {master_error}")
                                abnormalies_detected = True
                                j += 1
                            i += 1
                    except IndexError:
                        output_text.append("Abnormalities detected...")
                        return output_text

                if abnormalies_detected:
                    output_text.append("Abnormalities detected...")
                    return output_text
                    
                output_text.append(f"{home_file} is same as {master_copy_file}: True") 
                count2 += 1
            except FileNotFoundError:
                output_text.append("Abnormalities detected...")
                return output_text
        count1 += 1
    output_text.append(f"{timestamp}  Verification complete.")
    return output_text



def test_flags(flags):
    """
    if flag is not valid (i.e., not in flags list) or doesn't start with a -
    program termintes, print "Invalid flag. [Source of problem]"
    """
    ### Flag Testing ### - If any are true the program terminates
    if flags == None: # Flags aren't entered, rather left blank (this is still valid input)
        return (None, True)   

    # 1) Flag must start with a '-'
    if flags[0] != '-':
        #raise Exception:
        #print("Invalid flag. Flag must start with '-'.")
        return ("Invalid flag. Flag must start with '-'.", False)
    
    # 2) Log is by itself
    if flags == "-l":
        return ("Invalid flag. Log can only run with install or verify.", False)

    # 3) Includes both verify and install, can only be one or other
    if flags == "-iv" or flags == "-vi":    
        return ("Invalid flag. Choose verify or install process not both.", False)
    
    # 4) Each character must be unique
    characters = []
    characters_all_unique = True
    j = 0
    while j < len(flags):
        k = 0
        while k < len(characters):
            if flags[j] == characters[k]:
                characters_all_unique = False
            k += 1
        characters.append(flags[j])
        j += 1

    if not(characters_all_unique):
        return("Invalid flag. Each character must be unique.", False)

    # 5) Character must be a combo of v, i, l
    index = 1 # Skips the '-'
    while index < len(flags):
        if flags[index] != 'v' and flags[index] != 'i' and flags[index] != 'l':
            return("Invalid flag. Character must be a combination of 'v' or 'i' and 'l'.", False)
        index += 1
    
    return (None, True) # Flags are valid



def print_output_array(output_array):
    i = 0
    while i < len(output_array):
        print(output_array[i])
        i += 1



def main(master: str, flags: str, timestamp: str):
    '''
    Ideally, all your print statements would be in this function. However, this is
    not a requirement --> Need to return strings from other functions and print them here
    Parameters:
        master:    str, a string representing the absolute path to the master directory.
        flags:     str, a string representing the specified flags, if no flag is given
                        through the command line, flags will be an empty string.
        timestamp: str, a string representing the time to insert into the output.
                    in the format: DD MMM YYYY HH:MM:DD , ex: 10 Apr 2023 12:44:17
    '''
    """
    - Includes only text files
Needs:
1) A path to the master folder containing original versions of files
    - Start with / and end with /
    - If invalid directory is passed, message = "Invalid master directory."
2) (Optional) Flag in format -[char] where char can be one of two characters
    - install | verify and log
    - Errors: "Invalid flag. [Source of problem]"
- If more than 2 command line arguments are provided it will use the first two
and disregard the rest
- If not enough are provided at any stage the program wil output "Insufficient arguments."
    (os.path.isdir(path) - returns true if path is existing directory)

Master Directory:
- Contains files and sample(s) folder as well as config.txt file
"""
    cur_date = timestamp[:2]
    month = timestamp[3:6]
    year = timestamp[7:11]
    exact_time = timestamp[12:]

    # YYYY-MM-DD
    date = f"{year}-{month}-{cur_date}"
    # 14_31_27
    time = f"{exact_time.replace(':', '_')}"
    # 03 Mar 2023 00:34:34
    formatted_timestamp = timestamp

    if not(os.path.isdir(master)):
        print("Invalid master directory.", file=sys.stderr)
        sys.exit()

    ### TESTING MASTER PATH ###
    # Doesn't start and end with / / - "Invalid master directory"
    if master[0] != "/" or master[-1] != "/":
        print("Invalid master directory", file=sys.stderr)
        sys.exit()


    ### TESTING FLAGS ###
    flag_message, flag_valid = test_flags(flags)
    if not(flag_valid):
        print(flag_message, file=sys.stderr)
        sys.exit() # Flags aren't valid therefore program terminates

    ### CALLING FUNCTIONS BASED ON FLAGS ###
    #print(flags)
    ### Flag is None as no flag was inputted by user in the command line ###
    if flags == None or flags == '-il' or flags == '-li': # Automatically runs Installation and Logs process (il)
        #print("AAA")
        installation_output_array = installation(master, formatted_timestamp)
        logging(installation_output_array, date, time)
        print_output_array(installation_output_array)

    elif flags == '-i':
        #print("BBB")
        installation_output_array = installation(master, formatted_timestamp)
        print_output_array(installation_output_array)
    
    elif flags == '-v':
        #print("CCC")
        verification_output_array = verification(master, formatted_timestamp)
        #print("XXX")
        print_output_array(verification_output_array)

    elif flags == '-vl' or flags == '-lv':
        #print("DDD")
        verification_output_array = verification(master, formatted_timestamp)
        logging(verification_output_array, date, time)
        print_output_array(verification_output_array)
    
    else:
        return



if __name__ == "__main__":
    # you will need to pass in some arguments here
    # we will leave this empty for you to handle the implementation

    # python3 setup.py /home/master/ -i
    unformatted_timestamp = time.asctime() # string
    day_of_week = unformatted_timestamp[:3]
    month = unformatted_timestamp[4:7]
    day_num = unformatted_timestamp[9:10]
    if len(day_num) == 1:
        day_num = f"0{day_num}"
    cur_time = unformatted_timestamp[11:19]
    year = unformatted_timestamp[20:]
    timestamp = f"{day_num} {month} {year} {cur_time}"

    try:
        master = sys.argv[1]
        try:
            flags = sys.argv[2]
            main(master, flags, timestamp)
        
        except IndexError: # As flags are optional, if they are not given we provide the main function with a flag of None
            main(master, None, timestamp)
    
    except IndexError: # No arguments are given (only 1 is allowed as flags is optional but master is not)
        print("Insufficient arguments.")



"""
User passes path to master directory

Within the master directory is either files or folders which hold more files

We must install or verify these files/folders (v or i) whilst also possibly conducting a log (l)

Once this is done the setup.py is complete



Directories (in config.txt):
- /home/user/A1/ - this is valid
- Needs to start and end with /
- Can't contain a .

Files (in config.txt):
- Must always start with ./
- Row before file must be a valid directory

E.g.
VALID config.txt FILE:
/home/files/
./animals.txt  
./history.txt  
./list.txt  
./names.txt
/home/samples/
./count_me.txt

Flag Options:
- i - Installation process, v - verification process, l - log process
- l cannot happen on its own, it must be conbined with either i or v
    Combinations:
        i
        v
        il
        li
        vl
        lv

Possible Issues:
- Flag needs to start with '-'
- Log cannot run by itself
- Cannot choose both verify and install, one or the other
- Characters cannot repeat
- Cannot include any character that isn't 'v', 'i', or 'l'

    """




