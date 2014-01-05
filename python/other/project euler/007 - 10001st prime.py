from math import sqrt, ceil
n = 5
primes = [2,3] #until i optimize this to do it without the array intially filled, do not post
#check divisibles up to square root of n

while len(primes)<10001:
	for i in range(3,int(ceil(sqrt(n)))+2):
		if not(i%2):
			continue
		else:
			if not(n%i):
				n+=2
				break
			elif (i >= int(ceil(sqrt(n)))):
				primes.append(n)
				n+=2
print len(primes)
print primes[len(primes)-1]
print primes[0:6]
