# this is a really slow implementation
# figure out a better one 
for a in range(2,500):
	for b in range(2,500):
		if b>a:
			for c in range(2,500):
				if c>b:
					if ((a**2)+(b**2)) == (c**2):
						if (a + b + c) == 1000:
							print a,b,c
							print a*b*c
				else:
					continue
		else:
			continue
