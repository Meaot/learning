# MIT 6.00.1X
# Problem Set 1, Problem B
# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
# program should print:
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', 
# then your program should print:
# Longest substring in alphabetical order is: abc

s = raw_input('Enter a string of letters:\n')

import string

#currently goes into infinite loop on repeating letters ex aa
def is_in_alpha(chunk):
    def score(i):
        if i == 'a' and chunk.index(i) == 0: #when a is the first letter
            alphScore = 100
        else:
            alphScore = float(string.lowercase.index(i))/26.0
        chunkScore = float(chunk.index(i))/float(len(chunk))
        if chunkScore == 0.0: #avoids issue of dividing by 0 if chunk score is 0
            chunkScore = 0.001
        comboScore = round(alphScore/chunkScore, 5) #avoids floating point issues
        return comboScore 
    for j in chunk:
        while chunk.index(j)+1 < len(chunk)-1: 
            if score(j) >= score(chunk[chunk.index(j)+1]):
                j = chunk[chunk.index(j)+1]
            else:
                return False
        return True
        
print is_in_alpha(s)
    