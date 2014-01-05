sum = 0

for n in range(1000):
	if (not (n%3)) or (not (n%5)):
		sum += n
	elif not ((n%3) + (n%5)):
		sum -= n

print sum

	
