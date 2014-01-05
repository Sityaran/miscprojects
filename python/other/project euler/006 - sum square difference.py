sum = [0,0,0]
for n in range(1,101):
	sum[0] += n**2
	sum[1] += n
sum[2] = (sum[1]**2) - sum[0]
print sum[2]