n = 600851475143
factor = 0

while True:
	for i in range(2,10000): #some arbitrary number to check factors up to (???)
		if not (n%i):
			factor = n
			print i,n
			n = n/i
			continue
	break 
print factor
#results shown to be:
# factor divsor 	factor
# 71 				600851475143
# 839 				8462696833
# 1471 				10086647
# 6857 				6857
#the last set shows that the factor was only divisible by itself (and 1), therefore it is prime
#i don't know how reliable this is
