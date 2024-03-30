"""
CSE212 
(c) BYU-Idaho
05-Teach - Problem 1 

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def unique_letters(text):
    """ 
    Determine if there are any duplicate letters in the text provided
    """

    # Compare all letters to all other letters
    for i in range(len(text)):  
        for j in range(len(text)):
            if i != j:  # Don't want to compare to yourself ... that will 
                        # always result in a match.
                if text[i] == text[j]:
                    return False
    return True
def unique_letters_set(text):
    """ 
    This is my solution for 0(n)
    Determine if there are any duplicate letters in the text provided
    """
    my_set = set(text)
    length_set = len(my_set)
    length_text = len(text)
    # i want to then take the set and check to see that all letters are unique
    if length_set==length_text:
        return True
    else:
        return False

test1 = "abcdefghjiklmnopqrstuvwxyz"  # Expect True because all letters unique
print(unique_letters(test1))

test2 = "abcdefghjiklanopqrstuvwxyz"  # Expect False because 'a' is repeated
print(unique_letters(test2))

test3 = "" 
print(unique_letters(test3))          # Expect True because its an empty string


test1b = "abcdefghjiklmnopqrstuvwxyz"  # Expect True because all letters unique
print(unique_letters_set(test1b))

test2b = "abcdefghjiklanopqrstuvwxyz"  # Expect False because 'a' is repeated
print(unique_letters_set(test2b))

test3b = "" 
print(unique_letters_set(test3b))  