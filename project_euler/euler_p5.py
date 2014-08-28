from datetime import datetime

startTime = datetime.now()

n = 2520
while not all((n % i) == 0 for i in xrange(2, 21)):
	n += 2

print 'The smallest multiple of 1 through 20 is: ',n	

print 'Execution time: ',(datetime.now()-startTime)

# Necessary approach = Least Common Multiple by prime factorization
 
