from datetime import datetime
from itertools import product

startTime = datetime.now()

palindromes = []

for a, b in product(range(999, 99, -1), range(999, 99, -1)):
	p = str(a*b)
	first_half = p[:3]
	second_half = ''.join(reversed(p[3:]))
		
	if first_half == second_half:
		palindromes.append(a*b)
	
print 'The largest palindromic number that is the product of two three digit \
numbers is: ',sorted(palindromes)[-1]

print 'Execution time: ',(datetime.now()-startTime)
		