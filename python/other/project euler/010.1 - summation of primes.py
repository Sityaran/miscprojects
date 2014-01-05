#much faster using sieve
max = 2000000
sum = 0
sieve = range(max)
sieve[0],sieve[1] = False,False
for i in range(2,max):
	if sieve[i]:
		for n in range((2*i),(max),i):
			sieve[n] = False
		sum+=sieve[i]
print sum
