#problem 4.1 - this is faster

palindrome = 0,0

for x in range(100,1000):
    for y in range(100,1000):
        z = str(x*y)
        if not(len(z)%2):
            half = (len(z)/2)
        else:
            half = (len(z)/2)-1

        half1 = z[half:]
        half2 = (z[:half])[::-1]

        if (half1 == half2) and (x*y > palindrome[0]):
            palindrome = (x*y), (x,y)
        

print palindrome #palindrome[0] is the actual palindrome
