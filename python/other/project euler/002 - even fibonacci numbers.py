#problem 2 - even fibonacci numbers
sum = 0
n = 1
previous = 0
current = 1
while n < 4000000:
	n = previous + current
	previous = current
	current = n
	if not (n%2):
		sum += n
print sum