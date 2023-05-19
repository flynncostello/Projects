'''
Answer for Question 3 - Function

Name: Flynn Costello
SID: 530488477
unikey: fcos0917
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


def is_valid_name(name):
    test1 = is_valid_length(name)
    test2 = is_valid_start(name)
    test3 = is_one_word(name)
    valid_name = test1 and test2 and test3
    return valid_name




