from math import ceil, sqrt
#this is incredibly slow, there has to be a better way to find primes
sum = 5
for n in range(5,2000000,2):
	for i in range(3,int(ceil(sqrt(n)))+2,2):
		if not(n%i):
			break
		elif i >= (int(ceil(sqrt(n)))):
			sum += n
print sum