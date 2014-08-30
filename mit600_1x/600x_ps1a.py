# MIT 6.00.1X
# Problem Set 1, Problem A
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

s = raw_input('Enter a string of letters:\n')
counter = 0
for i in s:
    if i in ('a','e','i','o','u'):
        counter += 1
print 'Number of vowels: ',counter