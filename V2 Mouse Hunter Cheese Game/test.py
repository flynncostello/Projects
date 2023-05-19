'''
Write solutions to 4. New Mouse Release here.

Author: Flynn Costello
SID: 530488477
Unikey: fcos0917
'''

# Need to show that Mouse class is successful
# At spawning random mouse with approximate probability
# to the given specifications

# Creating lots Mice
from mouse import Mouse

TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")

def get_mouse_index(mouse_name):
    index = 0
    while index < len(TYPE_OF_MOUSE):
        if TYPE_OF_MOUSE[index] == mouse_name:
            return index
        index += 1
    
def calc_percentage(amount, total):
    percentage = round(amount/total, 2) # Rounds percentage to 2d.p.
    return percentage

mouse_occurances = [0, 0, 0, 0, 0, 0] # Each index stores the amount of a certain type of mouse generated
total = 100000
i = 0
while i < total: # Creating 100000 mice
    new_mouse = Mouse()
    mouse_index = get_mouse_index(new_mouse.get_name())
    mouse_occurances[mouse_index] += 1
    i += 1
#print(mouse_occurances)
# Getting approx percentage of each type of mouse in mouse_list
percentage_none = calc_percentage(mouse_occurances[0], total)
percentage_brown = calc_percentage(mouse_occurances[1], total)
percentage_field = calc_percentage(mouse_occurances[2], total)
percentage_grey = calc_percentage(mouse_occurances[3], total)
percentage_white = calc_percentage(mouse_occurances[4], total)
percentage_tiny = calc_percentage(mouse_occurances[5], total)


def test01(percentage_none):
    actual = percentage_none
    expected = 0.50 # The probability of getting none 
    assert actual == expected, "Test 1 FAILED - None Type Mouse, Result is Invalid"
    print("Test 1 PASSED - None Type Valid Result")

def test02(percentage_brown):
    actual = percentage_brown
    expected = 0.10
    assert actual == expected, "Test 2 FAILED - Brown Mouse, Result is Invalid"
    print("Test 2 PASSED - Brown Mouse, Result is Valid")

def test03(percentage_field):
    actual = percentage_field
    expected = 0.15
    assert actual == expected, "Test 3 FAILED - Field Mouse, Result is Invalid"
    print("Test 3 PASSED - Field Mouse, Result is Valid")

def test04(percentage_grey):
    actual = percentage_grey
    expected = 0.10
    assert actual == expected, "Test 4 FAILED - Grey Mouse, Result is Invalid"
    print("Test 4 PASSED - Grey Mouse, Result is Valid")

def test05(percentage_white):
    actual = percentage_white
    expected = 0.10 
    assert actual == expected, "Test 5 FAILED - White Mouse, Result is Invalid"
    print("Test 5 PASSED - White Mouse, Result is Valid")

def test06(percentage_tiny):
    actual = percentage_tiny
    expected = 0.05 
    assert actual == expected, "Test 6 FAILED - Tiny Mouse, Result is Invalid"
    print("Test 6 PASSED - Tiny Mouse, Result is Valid")


def run_all_tests():
    test01(percentage_none)
    test02(percentage_brown)
    test03(percentage_field)
    test04(percentage_grey)
    test05(percentage_white)
    test06(percentage_tiny)


if __name__ == "__main__":
    run_all_tests()






