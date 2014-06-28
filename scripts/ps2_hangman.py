# 6.00 Problem Set 2
# kovacs
# Time: Forever (~8 hrs?)
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "ps2_hangman_word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "\nLoading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program

def hangman():

    wordlist = load_words()
    chosen_word = choose_word(wordlist)
    
    obscured_characters = list(len(chosen_word)*'_')
    guessed_portion = ' '.join(obscured_characters)
    available_letters = list(string.lowercase)
    presented_letters = ''.join(available_letters)
    
    def check_input_eligibility(guess):
        """
        Checks if guess is one of the available_letters.
        """
        if presented_letters.find(guess) == -1:
            return False
        else:
            return True
        
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
        if check_input_eligibility(guess) == False:
            print 'Guess a single letter from the available letters please!'
            guess = raw_input('Guess again: ')
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
        print 'Sorry, you lost. The word was: ',chosen_word
        
hangman()
    
    


    
        

