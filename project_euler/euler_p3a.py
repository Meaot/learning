#
# Project Euler
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
from datetime import datetime
startTime = datetime.now()

def isprime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

number = (13195)
primeFactors = []
for j in range(2, number):
    if number % j == 0 and isprime(j):
        primeFactors.append(j)

print primeFactors

print 'Execution time: ',(datetime.now()-startTime)