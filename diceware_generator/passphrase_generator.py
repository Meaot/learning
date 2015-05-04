#
# Diceware Passphrase Generator
# 
# Generates a random passphrase of a specified number
# of words chosen from the Diceware wordlist.
#

import os
import sys
import string

DICT_FILENAME = "diceware_wordlist.txt"

def load_dict():
    """
    returns: a dictionary of the number to word mappings
    in the Diceware words file.
    """
    word_dict = {}
    in_file = open(DICT_FILENAME, 'r', 0)
    for line in in_file:
    	tmp = line.split()
    	key = tmp[0]
    	value = tmp[1]
    	word_dict[key] = value
    return word_dict

def generate_key():
	"""
	returns: a key for a value in the Diceware dictionary.
	"""
	key = ''
	for i in range(0, 5):
		digit = 1 + (ord(os.urandom(1))%6)
		key += str(digit)
	return key

def generate_passphrase():
	"""
	length: desired number of words in the passphrase
	returns: a randomly chosen passphrase
	"""
	word_dict = load_dict()
	flag = False
	while True:
		try:
			if len(sys.argv) == 1 or flag == True:
				length = int(raw_input('Length of desired passphrase: '))
			elif len(sys.argv) > 1:
				length = int(sys.argv[1])
			if length in range(1, 5):
				print 'That\'s pretty insecure... but OK.'
				break
			elif length in range(1, 11):
				break
			else:
				print 'Choose a length <= 10.'
		except ValueError:
			print 'Please enter an integer <= 10.'
			if len(sys.argv) > 1:
				if type(sys.argv[1]) != int:
					flag = True
	passphrase = ''
	for i in range(1, length + 1):
		key = generate_key()
		passphrase += word_dict[key] + ' '
	return passphrase


print 'Passphrase:', generate_passphrase()




		
