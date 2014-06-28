#
# Project Euler
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of 
# all the multiples of 3 or 5 below 1000.
#
from datetime import datetime
startTime = datetime.now()

n = 2
i = 3
multThree = [i]
while i < 999:
    i = 3*n
    multThree.extend([i])
    n += 1
    
m = 2
k = 5
multFive = [k]
while k < 995:
    k = 5*m
    multFive.extend([k])
    m += 1
    
for k in multFive:
    if k%3 == 0:
        del multFive[multFive.index(k)]
    
sumAll = sum(multThree) + sum(multFive)

print 'The sum of all multiples of 3 and 5 below 1000 is: ',sumAll

print 'Execution time: ',(datetime.now()-startTime)
