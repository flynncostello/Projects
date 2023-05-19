'''
Answer for Question 2 - What's ye called?

Name: Flynn Costello
SID: 530488477
unikey: fcos0917
'''

name = input("Larry: What's ye name, Hunter?\n")


is_valid_length = len(name) >= 1 and len(name) <= 9


if len(name) > 0: # Checking if nothing is entered
    is_valid_start = name[0].isalpha() # isalpha checks if the string is a letter in the alphabet
else:
    is_valid_start = False


index = 0
is_one_word = True
# Looping through name string to check if each character is a whitespace or not
while index < len(name):
    if name[index] == " ":
        is_one_word = False
    index += 1


is_valid_name = is_valid_length and is_valid_start and is_one_word


print(f"Larry: Is '{name}' a name I can pronounce?")

print(f"It has a length of {len(name)} which is between 1 to 9 characters? {is_valid_length}!")

print(f"It starts with an alphabet? {is_valid_start}")

print(f"It is a single word? {is_one_word}")

print(f"Larry: I can pronounce this name --- {is_valid_name}")



