from math import sqrt
tnum = 0
n = 1
div = 1
while div<500:
	tnum += n
	if not(tnum%2):
		div = 0
		for i in range(1,int(sqrt(tnum))+1):
			if not(tnum%i):
				div += 2
		if (int(sqrt(tnum))**2) == tnum:
				div -= 1
	n += 1
print tnum, div
