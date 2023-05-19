'''
Answer for Question 5. Kids' Friendly.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''


# you can make more functions or global read-only variables here if you please!

'''
This part should be your solution from Assignment 1, 3. Functions.
'''
def is_valid_length(name: str) -> bool: # TEST 1
    '''
    Checks if name has length between 1 and 9 (inclusive)
    Parameters:
        name:   str, a name
    Returns:
        Whether the length of the name is valid or not
    '''
    valid_length = len(name) >= 1 and len(name) <= 9
    return valid_length
    

def is_valid_start(name: str) -> bool: # TEST 2
    '''
    Checks if name starts with an alphabet
    Parameters:
        name:   str, a name
    Returns:
        Whether the name starts with an alphabetical character or not
    '''
    if len(name) > 0: # Checking if nothing is entered
        valid_start = name[0].isalpha()
    else:
        valid_start = False
    return valid_start


def is_one_word(name: str) -> bool: # TEST 3
    '''
    Checks if name is a single word
    Parameters:
        name:   str, a name
    Returns:
        Whether the name is one word or not
    '''
    index = 0
    check_if_one_word = True
    # Looping through name string to check if each character is a whitespace or not
    while index < len(name):
        if name[index] == " ":
            check_if_one_word = False
        index += 1
    return check_if_one_word


def is_profanity(word: str, database='/home/files/list.txt', records='/home/files/history.txt') -> bool:
    '''
    Checks if `word` is listed in the blacklist `database`.
    Parameters:
        word:     str,  word to check against database.
        database: str,  absolute directory to file containing list of bad words.
        records:  str,  absolute directory to file to record past offenses by player.
    Returns:
        result:   bool, status of check.
            - True if word is found in database
            - False otherwise
        - If given database is invalid, display "Check directory of database!" 
    For records file:
    - If file exists and has previous offences, add new offence to end
    - If file doesn't exist, create new file at given directory and add the new offence to the file
    '''
    try:
        # Checking database file for word
        database_file_lines = open(database, "r").readlines()
        database_new_lines = []
        index = 0
        while index < len(database_file_lines):
            if database_file_lines[index].strip() != '':
                database_new_lines.append(database_file_lines[index].strip())
            index += 1

        list_index = 0
        while list_index < len(database_new_lines):
            new_word = database_new_lines[list_index]
            if new_word.strip().lower() == word.strip().lower():
                # Regardless if it exists or not either new file will be created or we can end to existing one using "a"
                with open(records, "a") as history_file1:
                    history_file1.write(f"{word}\n")
                
                lines = open(records, "r").readlines()
                new_lines = []
                i = 0
                while i < len(lines):
                    if lines[i].strip() != '':
                        new_lines.append(lines[i].strip())
                    i += 1

                j = 0
                history_file2 = open(records, "w")
                while j < len(new_lines):
                    history_file2.write(f"{new_lines[j]}\n")
                    j += 1
                history_file2.close()
                return True
            list_index += 1

        return False

    except FileNotFoundError:
        print("Check directory of database!")
        return False



def is_valid_name(name):
    test1 = is_valid_length(name)
    test2 = is_valid_start(name)
    test3 = is_one_word(name)
    test4_profanity = is_profanity(name) # If it returns true, it is a word that contains profanity
    valid_name = test1 and test2 and test3 and not(test4_profanity)
    return valid_name


def count_occurrence(word: str, file_records="/home/files/history.txt", start_flag=True) -> int:
    '''
    Count the occurrences of `word` contained in file_records.
    Parameters:
        word:         str,  target word to count number of occurences.
        file_records: str,  absolute directory to file that contains past records.
        start_flag:   bool, set to False to count whole words. True to count words 
                            that start with.
    Returns:
        count:        int, total number of times `word` is found in the file.
    - If start_flag == False, return case insensitive total number of times word appears
    - If start_flag == True, return count of number of times a word in history.txt starts with same letter as word
    - If word is not a string, display
    '''
    #print(file_records)
    if not(isinstance(word, str)):
        print("First argument must be a string object!")
        return 0
    elif word.strip() == "":
        print("Must have at least one character in the string!")
        return 0
    else:
        try:
            history_file = open(file_records, "r")
            #history_file = open("/home/samples/count_me.txt", "r")
            if not(start_flag): # i.e., start_flag = False
                count = 0
                new_word = history_file.readline().strip()
                while new_word != "":
                    if new_word.strip().lower() == word.strip().lower():
                        count += 1
                    new_word = history_file.readline().strip()
                history_file.close()
                return count

            else: # i.e., start_flat = True
                first_letter = word[0].lower()
                letter_occurrences_count = 0
                cur_word = history_file.readline().strip()
                while cur_word != "":
                    cur_word = cur_word.strip().lower()
                    if cur_word[0] == first_letter:
                        letter_occurrences_count += 1
                    cur_word = history_file.readline().strip()
                history_file.close()
                return letter_occurrences_count

        except FileNotFoundError:
            history_file.close()
            print("File records not found!")
            return 0
        



def add_to_file(filename, new_word):
    with open(filename, "a") as f:
        f.write(f"{new_word}\n")

    lines = open(filename, "r").readlines()
    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].strip() != '':
            new_lines.append(lines[i].strip())
        i += 1

    j = 0
    file2 = open(filename, "w")
    while j < len(new_lines):
        file2.write(f"{new_lines[j]}\n")
        j += 1
    file2.close()


def generate_name(word: str, src="/home/files/animals.txt", past="/home/files/names.txt") -> str:
    '''
    Select a word from file `src` in sequence depending on the number of times word occurs.
    Parameters:
        word:     str, word to swap
        src:      str, absolute directory to file that contains safe in-game names
        past:     str, absolute directory to file that contains past names 
                       auto-generated
    Returns:
        new_name: str, the generated name to replace word
    
    - In sequence that it appears in animals.txt unless expection occurs while receiving the arguments word and src
    - If all animal names with same letter have been used up, it will start from top of file again (need to check each valid name as we go to see if it has been used and is in names.txt)
    '''
    if not(isinstance(word, str)):
        print("First argument must be a string object!")
        add_to_file(past, "Bob")
        return "Bob"
    elif word.strip() == "":
        print("Must have at least one character in the string!")
        add_to_file(past, "Bob")
        return "Bob"
    else:
        first_character = word[0].lower()
        try:
            ### SRC ###
            animals_list = open(src, "r").readlines()
            correct_animals_list = [] # FINAL LIST OF ANIMAL NAMES
            
            # Making animals list nice
            i1 = 0
            while i1 < len(animals_list):
                if animals_list[i1].strip() != '':
                    correct_animals_list.append(animals_list[i1].strip())
                i1 += 1
        
            # Creating new animals         
            all_animals_same_char_from_src = []
            j1 = 0
            while j1 < len(correct_animals_list):
                cur_animal = correct_animals_list[j1]
                if cur_animal[0].lower() == first_character:
                    all_animals_same_char_from_src.append(cur_animal)
                j1 += 1
            

            try:
                ### PAST ###
                past_list = open(past, "r").readlines()
                correct_past_list = []

                i2 = 0
                while i2 < len(past_list):
                    if past_list[i2].strip() != '':
                        correct_past_list.append(past_list[i2].strip())
                    i2 += 1

                all_words_same_char_from_past = []

                j2 = 0
                while j2 < len(correct_past_list):
                    cur_word = correct_past_list[j2]
                    if cur_word[0].lower() == first_character:
                        all_words_same_char_from_past.append(cur_word)
                    j2 += 1
                

                ### NOW GOING THROUGH EACH WORD IN PAST'S LIST ###
                if len(all_words_same_char_from_past) == 0: # Choose first animal with same first char
                    new_name = all_animals_same_char_from_src[0]
                else:
                    last_word = all_words_same_char_from_past[-1]
                    if last_word == all_animals_same_char_from_src[-1]: # i.e., they're both the last word/animal in the file
                        # Then we pick the first animal name in the list
                        new_name = all_animals_same_char_from_src[0]
                    else:
                        # aniamls = [bunny, banjo, boom]
                        # past = [bunny, banjo]
                        # Finding current index
                        word_we_are_looking_for = all_words_same_char_from_past[-1]
                        k = 0
                        required_index = 0
                        while k < len(all_animals_same_char_from_src):
                            if all_animals_same_char_from_src[k] == word_we_are_looking_for:
                                required_index = k
                            k += 1

                        new_name = all_animals_same_char_from_src[required_index+1]
                
                add_to_file(past, new_name)
                return new_name

            except FileNotFoundError:
                # None of the names have been generated before - creating new file to store names
                first_animal = all_animals_same_char_from_src[0]
                new_storage_file = open(past, "w")
                new_storage_file.write(first_animal)
                new_storage_file.close()
                return first_animal 


        except FileNotFoundError:
            print("Source file is not found!")
            add_to_file(past, "Bob")
            return "Bob"
        





def main():
    # If name doesn't pass what's ye called AND has profanity, an animal name must be genereated from the given text file
    name = input("Check name: ").strip()
    while name.lower() != "s":
        is_valid = is_valid_name(name)
        if is_valid:
            print(f"{name} is a valid name!") # Working
        else:
            new_name = generate_name(name) # Not Working
            print(f"Your new name is: {new_name}")

        name = input("Check name: ").strip()            




if __name__ == "__main__":
    main()






