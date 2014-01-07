x=13
chains=[0,0]
while x<1000000:
	n = x
	chain = 1
	while n>1:
		if not(n%2):
			n = n/2
		else:
			n = 3*n + 1
		chain+=1
	if chain>chains[0]:
		chains=chain,x
	x+=2 #odd numbers will produce longer chains ?
print chains
