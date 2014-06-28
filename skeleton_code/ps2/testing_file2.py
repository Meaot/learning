import string

chosen_word = 'aquamarine'

obscured_characters = list(len(chosen_word)*'_')
guessed_portion = ' '.join(obscured_characters)
available_letters = list(string.lowercase)
presented_letters = ''.join(available_letters)

def check_guess(guess):
    """
    Checks to see if the guess is in chosen_word.
    Returns False if it is not in chosen_word and True if it is.
    """
    if chosen_word.find(guess) == -1:
        return False
    else:
        return True

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

def replace_obscured_characters(guess):
    """
    Replaces underscores in obscured_characters with the appropriate letter
    based on indexes provided by indexes_of_guess_occurrence.
    """
    guess_indexes = indexes_of_guess_occurrence(guess)
    counter = 0
    while counter < len(guess_indexes):
        obscured_characters[guess_indexes[counter]] = guess
        counter += 1
    return obscured_characters
    
print '\nWelcome to the game, Hangman!'
print 'I am thinking of a word that is ',len(chosen_word),' letters long.'

guesses = 10

while guesses > 0 and guessed_portion.find('_') != -1:
    print '-'*20
    print 'You have ',guesses,' guesses left.'
    print 'Available letters: ',presented_letters
    guess = raw_input('Please guess a letter: ')
    if check_guess(guess) == True:
        guessed_portion = ' '.join(replace_obscured_characters(guess))
        available_letters.remove(guess)
        presented_letters = ''.join(available_letters)
        print 'Good guess: ',guessed_portion
        
    else:
        guesses -= 1
        available_letters.remove(guess)
        presented_letters = ''.join(available_letters)
        print 'Oops! That letter is not in my word:',guessed_portion
        
if guesses > 0:
    print '-'*20
    print 'Congratulations, you won!'
else:
    print '-'*20
    print 'Sorry, you lost. Game Over.'