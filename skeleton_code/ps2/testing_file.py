import string

chosen_word = 'aquamarine'
guess = 'a'

def indexes_of_guess_occurrence(guess):
    """
    Loops through the string chosen_word and returns a tuple containing the
    indexes at which a character occurs.
    """
    num_occurrences = chosen_word.count(guess)
    guess_indexes = ()
    begin = 0
    counter = 0
    while counter < num_occurrences:
        guess_indexes += (chosen_word.index(guess,begin,len(chosen_word)), )
        begin = guess_indexes[counter] + 1 
        counter += 1
    return guess_indexes

print indexes_of_guess_occurrence(guess)