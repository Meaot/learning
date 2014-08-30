# MIT 6.00.1X
# Problem Set 1, Problem B
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.

s = raw_input('Enter a string of letters:\n')

start = 0
end = 3
counter = 0
while end <= len(s):
    if s[start:end] == 'bob':
        counter += 1
    start += 1
    end += 1
    
print 'Number of times bob occurs is: ',counter
