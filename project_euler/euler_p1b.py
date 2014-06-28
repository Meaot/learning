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

def sumthis(this):
    endsum = 0
    for i in this:
        endsum += i
    return endsum

i = 3
multThree = []
while i < 1000:
    if i%3 == 0:
        multThree.append(i)
        i += 1
    else:
        i += 1

j = 5
multFive = []
while j < 1000:
    if j%5 == 0:
        multFive.append(j)
        j += 1
    else:
        j += 1
        
for k in multFive:
    if k%3 == 0:
        del multFive[multFive.index(k)]
        
sumAll = sumthis(multThree) + sumthis(multFive)

print 'The sum of all multiples of 3 and 5 below 1000 is: ',sumAll

print 'Execution time: ',(datetime.now()-startTime)
