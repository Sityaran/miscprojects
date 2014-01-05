#for all primes under Max, find the greatest power of the prime that exists under Max
#the product of primes raised to their greatest power under max is the smallest multiple
Max = 20
Lcm = 1
for n in range(2,Max+1):
	for i in range(2,n+1): 
		if (not(n%i)) and (n!=2): #to get rid of non primes
			break
		elif (n==2) or (i == n-1):
			x = 0 #exponent
			while True:
				x += 1
				if (n**x) > Max:
					m = n**(x-1)
					break
			Lcm = Lcm*m
			break
print Lcm