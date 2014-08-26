from datetime import datetime
from math import sqrt

startTime = datetime.now()

def isprime(n):
    for i in xrange(2, n):
        if n%i == 0:
            return False
    return True

def greatest_prime_factor(m):
	prime_factors = []
	for i in xrange(2, int(sqrt(m))):
		if m % i == 0 and isprime(i):
			prime_factors.append(i)
			m //= i
	return prime_factors[-1]
		
print 'Greatest prime factor is: ',greatest_prime_factor(600851475143)

print 'Execution time: ',(datetime.now()-startTime)
			