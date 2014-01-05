#much faster using sieve
max = 999999999
sieve = range(max)
sieve[0],sieve[1] = False,False
for i in range(2,max):
	if sieve[i]:
		for n in range((2*i),(max),i):
			sieve[n] = False
pandigital = []
for x in sieve:
	if x:
		check = [0]*9
		for s in str(x):
			if int(s):
				check[int(s)-1] += 1
		n = x
		for m in check:
			if m>1:
				n = 0
				break
		if n:
			pandigital.append(n)
print pandigital[len(pandigital)-1]